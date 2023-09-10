# Selenium Crawler

[![binder-badge]][launch] ![py-badge] ![mit] [![black-badge]][black-url]

> a web crawler written in python, powered by [Selenium] and [Tesseract] OCR

🔗 [source code](https://github.com/hoishing/selenium-crawler)

[mit]: https://img.shields.io/github/license/hoishing/selenium-crawler
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black
[py-badge]: https://img.shields.io/badge/python-3.10%20%7C%203.11-blue

## Motivation

In a project I need to collect the name and address of all dental laboratories in Taiwan. Unfortunately the [Ministry of Health and Welfare] doesn't provide a structured format(csv, json...etc) for download. The data only available as website tables having just 10 records each page, and there are about 1000 pages... so I got to crawl it without having other faster and simpler options(or maybe I should contact the government officials, which is faster?? 🤔...).

### Choosing Web Crawler

I struggled quite some time for which web crawling library should be used. Besides Selenium, other candidates included [Scrapy], [Playwright] and [Puppeteer].

Scrapy is a highly structured framework. I need to follow its structure to write python classes and middle-wares if using it. Then use CLI to run the crawling. The well structured format does provide clear separation of concerns. Its good for creating serious crawler, especially when working with a team that each member responsible for a specific part of a project. However, its a bit overkill for an one-man simple crawling project like this one, so maybe next time.

Playwright, as a pytest plugin in python, its more test oriented and depend on [pytest] with CLI. This added an other layer of complication, also not well suited in jupyter's exploratory programming style. Therefore 🙅‍♀️

Puppeteer is the closest competitor. I like its flexible and elegant API on selecting elements. The main reason for not choosing it is that exploratory programming style for javascript is not that "out-of-box" comparing with python. Yes, I can do exploratory programming with js, such as using [Quokka] in VSCode, installing [iJavascript] kernel for jupyter, or using [RunKit] online... etc. The DX of these toolings are just not as smooth and mature as jupyter + python.

Another essential benefit of using jupyter is that, I can easily "deploy" the program online using [Binder], so the users can test it immediately by simply pressing [![binder-badge]][launch], and tell me if it fit their needs. This fast feedback loop significantly accelerates the development cycle 👍

So, the final stack for this simple crawler is: python + selenium + jupyter -> Binder 🎉

## Usage

- run online with [![binder-badge]][launch]
- or install and run locally
    - clone repo
    - install dependencies `poetry install`
    - run `selenium-crawler.ipynb` in VSCode

## tech stack

- [Jupyter]: exploratory programming in python
    - effectively try out any CSS selector / XPath combinations
- [Selenium]
    - First use normal mode to have visual feedback while exploring XPaths
    - then use headless mode in production
- [Tesseract]: Google's OCR library for recognizing captcha
- [pil]: create image object from the captcha binary retrieved by Selenium

## Questions?

Open a [github issue] or ping me on [Twitter ![twitter-icon]][Twitter]

[github issue]: https://github.com/hoishing/selenium-crawler/issues
[Twitter]: https://twitter.com/intent/tweet?text=https://github.com/hoishing/selenium-crawler/%20%0D@hoishing
[twitter-icon]: https://api.iconify.design/logos/twitter.svg?width=20
[jupyter]: https://docs.jupyter.org/
[Ministry of Health and Welfare]: https://mohw.gov.tw/
[Tesseract]: https://github.com/madmaze/pytesseract
[pil]: https://pillow.readthedocs.io
[selenium]: https://selenium-python.readthedocs.io
[scrapy]: https://scrapy.org
[playwright]: https://github.com/microsoft/playwright
[puppeteer]: https://github.com/puppeteer/puppeteer
[pytest]: https://github.com/pytest-dev/pytest
[runkit]: https://runkit.com
[quokka]: https://quokkajs.com
[iJavascript]: https://github.com/n-riesco/ijavascript
[binder]: https://mybinder.org
[launch]: https://mybinder.org/v2/gh/hoishing/selenium-crawler/HEAD?labpath=selenium-crawler.ipynb
[binder-badge]: https://mybinder.org/badge_logo.svg
