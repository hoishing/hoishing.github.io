# Google Playbook Annotations to Markdown

[![binder]][binder-ipynb] ![py-badge] ![mit] [![black-badge]][black-url]

- convert ebook annotations(highlights and custom notes) of Google Playbook to markdown files
- one markdown file per book

🔗 [source code]

[mit]: https://img.shields.io/github/license/hoishing/selenium-crawler
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black
[py-badge]: https://img.shields.io/badge/python-3.10%20%7C%203.11-blue
[source code]: https://github.com/hoishing/playbook2md

## Motivation

I am a heavy Google Playbooks user. Why?

- compare to Amazon, it has much more Chinese titles
- compare to Taiwan ebook stores, it has much more English titles 😂

In short, it has the largest ebook collection for my reading languages. If I want to use just one provider to centralize my ebooks and annotations, store them online so that I can access them anytime in multiple devices(phone, tablet, laptop...) Playbook is a good choice. Not to mention the price in Playbook often a little lower then others.

After using [Zettelkasten] with [Obsidian] as my personal knowledge management system, I think its good to integrate the learning/insights from my previous reading into Obsidian. So I want to extract the annotations from Playbook. Playbook does store them on google docs though, in a format not easy to re-use 🤷‍♀️... So I decided to extract them directly from Google Takeout.

[zettelkasten]: https://en.wikipedia.org/wiki/Zettelkasten
[obsidian]: https://obsidian.md/

## Usage

### Download Your Ebook Annotations

- export ebook annotations for Google Playbook through [Google Takeout](https://takeout.google.com)
- select json format
- download the exported annotations as a zip file

### Prepare Your Runtime Environment

- run online with [![binder]][binder-ipynb]
- or locally with python >= 3.10 + ipykernel in VSCode

### Extract Annotations to Markdown

- set the following in the "params" section of `playbook.ipynb`:
    - `vault`: folder path of exported markdown files
    - `takeout_zip`: path of the zip file downloaded from Google Takeout

- run all cells of `playbook.ipynb`
- markdown files should be generated inside the vault folder

## Questions?

Open a [github issue] or ping me on [Twitter ![twitter-icon]][Twitter]

[github issue]: https://github.com/hoishing/playbook2md/issues
[Twitter]: https://twitter.com/intent/tweet?text=https://github.com/hoishing/playbook2md/%20%0D@hoishing
[twitter-icon]: https://api.iconify.design/logos/twitter.svg?width=20
[binder]: https://mybinder.org/badge_logo.svg
[binder-ipynb]: https://mybinder.org/v2/gh/hoishing/playbook2md/HEAD?labpath=playbook.ipynb
