"""Version Pump Automation

- update pyproject.toml
- clean build mkdocs
- deploy mkdocs
- create new github commit, tag and release

Examples:
    - dry run
    ./pump.py patch

    - update pyproject.toml and local git tag
    ./pump.py patch --tag

    - update everything and publish new version
    ./pump.py patch --tag --publish
"""

import toml
from click import argument, Choice, option, command, secho
from subprocess import getstatusoutput
from functools import reduce

CHOICES = ["major", "minor", "patch"]


# === uti ===
def abort(msg: str = "") -> None:
    secho(msg or "Aborted.", fg="red")
    exit(1)


def run(cmd: str) -> None:
    """run shell command"""
    secho(cmd)
    if getstatusoutput(cmd)[0]:
        abort()


# === main ===


@command()
@argument("section", type=Choice(CHOICES))
@option("--tag/--no-tag", help="tag local commit with new version", default=False)
@option(
    "--publish/--no-publish",
    help="publish to pypi and update github release",
    default=False,
)
@option("--msg", help="git commit message", default="chore: version pump")
def main(section, tag, publish, msg):
    """Version Pump Automation CLI"""

    # parse toml
    data = toml.load("pyproject.toml")
    old_version = data["tool"]["poetry"]["version"]
    new_version = upgrade_version(section, old_version)
    data["tool"]["poetry"]["version"] = new_version

    print(old_version, "->", new_version)

    if tag:
        with open("pyproject.toml", "w") as f:
            toml.dump(data, f)
            print(f"pyproject.toml pumped to {new_version}")

        run(f"git tag {new_version}")

        # publish to pypi, update github release, commit changelog
        if publish:
            cmds = [
                "mkdocs build -c",  # clean build
                "mkdocs gh-deploy",  # deploy docs
                "git push --tag",
                f'git add . && git cm -am "{msg}" && git push',
            ]

            for cmd in cmds:
                run(cmd)


def upgrade_version(section: str, old_version: str) -> str:
    """upgrade new version from old version

    Tests:
        >>> upgrade_version('major', '0.1.1')
        '1.0.0'

        >>> upgrade_version('minor', '0.1.1')
        '0.2.0'

        >>> upgrade_version('patch', '0.1.1')
        '0.1.2'
    """
    ver_dict = {k: int(v) for k, v in zip(CHOICES, old_version.split("."))}

    # pump version
    ver_dict[section] += 1

    # reset sub-version num
    match section:
        case "minor":
            ver_dict["patch"] = 0
        case "major":
            ver_dict["patch"] = 0
            ver_dict["minor"] = 0

    new_version = reduce("{}.{}".format, ver_dict.values())
    return new_version
