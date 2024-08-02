from pathlib import Path
import subprocess

base = Path.home() / 'gh'

for f in Path("docs/proj").iterdir():
    if f.suffix == ".md":
        legacy = "" if (base / f.stem).exists() else "legacy" 
        folder = base / legacy / f.stem
        readme = folder / "README.md"

        # print(readme, "-", readme.exists())
        cmd = ["ln", "-f", readme, f,]
        # print(cmd)
        subprocess.run(cmd, check=True)
