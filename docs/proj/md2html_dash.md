# Markdown to Dash Docset

[![GitHub](https://img.shields.io/github/license/hoishing/markdown-to-dash-docset)](https://opensource.org/licenses/MIT)

[Dash](https://kapeli.com/dash) was my favorite documentation app on macOS. Besides reading tech docs, I also use it for reading tech books due to its handy search functionalities.

This python utils was created for converting ebook written in markdown to HTML files, that are suitable for generating Dash docset later on. It's written in jupyter format for easy debugging and exploratory coding. So you have to run with VSCode instead of running directly with python.

## Tech Details

🔗 [source code](https://github.com/hoishing/markdown-to-dash-docset)

- [Jupyter in VSCode](https://code.visualstudio.com/docs/python/jupyter-support-py) for exploratory programming
- [YAML](https://pyyaml.org/) for configuration
- [Pygments](https://pygments.org/) as syntax highlighter
- [less css](https://lesscss.org/) as css preprocessor
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for manipulating HTML elements (insert, append...etc)

After creating the HTML files, generate Dash docset with [dashing](https://github.com/technosophos/dashing) CLI.

### Python Packages

```js
bs4 = "^0.0.1"
pyyaml = "^6.0"
markdown2 = "^2.4.6"
jupyter = "^1.0.0"
lesscpy = "^0.15.1"
```

## Usage

- put markdown files in `src` folder
- edit config.yaml to suit your package
- replace icon.png
- run all cells in md2html.py in VSCode
- in terminal
  - cd output
  - run `dashing build <package_name>`

## Need Help?

Open a [github issue](https://github.com/hoishing/markdown-to-dash-docset/issues) or ping me on [Twitter](https://twitter.com/hoishing) ![](https://api.iconify.design/logos/twitter.svg?width=20)
