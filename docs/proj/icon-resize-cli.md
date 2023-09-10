# Icon Resize CLI

[![pypi-badge]][pypi-url] ![py-badge] [![black-badge]][black-url] ![mit]

![screenshot](https://i.imgur.com/K00hCxN.png)

> CLI to create lossless icons in multiple sizes

🔗 [source code]

[mit]: https://img.shields.io/github/license/hoishing/icon-resize
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black
[py-badge]: https://img.shields.io/badge/python-3.10%20%7C%203.11-blue
[source code]: https://github.com/hoishing/icon-resize-cli/

## Features

- resize icon file(png/jpg) to multiple sizes
- lossless compression for png files
- maintain aspect ratio and transparency

## Prerequisite

- macOS or Linux (Windows not tested)
- python3.10+
- [Image Magick][magick] `brew install imagemagick`

## Installation

`pip install icon-resize`

## Usage

```shell
# default resize to 256, 128, 64
icon-resize mic-512

# specify resize to 128, 64
icon-resize mic-512 --sizes "128,64"

# save to 'mic' folder with default sizes
icon-resize mic-512 --out-folder mic/

# enable autocomplete in current session
eval "$(_ICON_RESIZE_COMPLETE=zsh_source icon_resize)"
```

## Technical Details

- use [Typer][typer] for CLI and help docs generation
- use [Image Magick][magick] for both resize and compress images

## Questions?

Open a [github issue] or ping me on [Twitter ![twitter-icon]][Twitter]

[github issue]: https://github.com/hoishing/icon-resize-cli/issues
[Twitter]: https://twitter.com/intent/tweet?text=https://github.com/hoishing/icon-resize-cli/%20%0D@hoishing
[twitter-icon]: https://api.iconify.design/logos/twitter.svg?width=20
[typer]: https://typer.tiangolo.com
[magick]: https://imagemagick.org
[pypi-badge]: https://img.shields.io/pypi/v/icon-resize
[pypi-url]: https://pypi.org/project/icon-resize/
