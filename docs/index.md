# 👋 Hi~ Kelvin's Speaking

While wandering in a bookstore one day, I stumbled upon a book recommended by Taiwan's IT Minister, [Audrey Tang], which advocated for a work method known as [work out loud].

After reading a few pages, I was immediately captivated and inspired. As a result, I took the time to organize my past works and toy projects, open-sourced them on [Github], and documented the motivations and technical stacks that I utilized.

The outcome of this effort can be seen on this website, showcasing my work and interests, their rationale, and the logic behind the technical decisions I made while solving various problems. I hope you find them intriguing 😉

## Mobile Apps

- see all recent published iOS / macOS app [here][iOS apps]

| app                |   lang   | platform    | category      |           repo           |
|:------------------ |:--------:| ----------- | ------------- |:------------------------:|
| [ZERO]             | ![swift] | iOS + macOS | strategy game | [![git-logo]][zero-game] |
| [Video Compressor] | ![swift] | iOS         | utility       |                          |
| [Easy Dictionary]  | ![swift] | iOS + macOS | education     |                          |
| [英漢字典]         | ![swift] | iOS         | education     |                          |
| [同音字典]         | ![swift] | iOS + macOS | education     |                          |

## Web Apps

| app                  |           tech stack           | description                                                          |            repo            |
|:-------------------- |:------------------------------:|:-------------------------------------------------------------------- |:--------------------------:|
| [Speech Recognition] | [PWA] + [Alpine.js] + [UnoCSS] | quick and easy speech synthesis PWA powered by Google Web Speech API | [![git-logo]][voice-recog] |

## Chrome Extensions

| extension                      | lang  | description                                                                    |                    repo                     |
|:------------------------------ |:-----:|:------------------------------------------------------------------------------ |:-------------------------------------------:|
| [Mini Authenticator]           | ![ts] | minimal 2FA authenticator that never store your secret keys                    |          [![git-logo]][mini-auth]           |
| [Multilingual Voice Search]    | ![js] | Google voice search in languages different from your OS and location settings  |       [![git-logo]][voice-search-crx]       |

## Python Packages

- well documented and tested python packages published to PyPi

| package           | lang  | description                                    |              repo              |
|:----------------- |:-----:|:---------------------------------------------- |:------------------------------:|
| [Pipable]         | ![py] | pipe operation in python                       |   [![git-logo]][pipable-git]   |
| [kTemplate]       | ![py] | a minimalist python html template              |  [![git-logo]][ktemplate-git]  |
| [Icon Resize CLI] | ![py] | CLI to create lossless icons in multiple sizes | [![git-logo]][icon-resize-git] |

## NPM Packages

| packages         | lang  | description                            |           repo           |
|:---------------- |:-----:|:-------------------------------------- |:------------------------:|
| [TOTP Generator] | ![ts] | time-based one-time-password generator | [![git-logo]][totp-auth] |

## Utilities

| app                       |           lang / run           | description                                                          |
|:------------------------- |:------------------------------:|:-------------------------------------------------------------------- |
| [doc2txt]                 | [![colab-logo]][doc2txt-colab] | extract text from epub, pdf and docx                                 |
| [Personalize CangJie IME] |   [![binder]][cangjie-ipynb]   | generate custom char set for 倉頡 IME in Windows                     |
| [Selenium Crawler]        |  [![binder]][selenium-ipynb]   | web crawler by [Selenium], captcha resolved by [Tesseract OCR]       |
| [Raycast Scripts]         |            ![bash]             | quickly open current Finder directory in specific app with [Raycast] |

## Legacy Projects

| project                           |                lang                 | description                                                          |
|:--------------------------------- |:-----------------------------------:|:-------------------------------------------------------------------- |
| [Atom Cell Navigation]            |          ![coffee-script]           | Atom editor extension for fast navigating between jupyter cells      |
| [Markdown to Dash Docset]         |                ![py]                | convert md to HTML files that can be used for generating Dash docset |
| [GData iOS Static lib]            |                obj-c                | iOS static library of Google Data APIs                               |
| [認識佛教 iOS app][buddhism-objc] |                obj-c                | 認識佛教 audio book player for iOS < v10                             |

## More

- [ping me on twitter ![twitter]][tw-shing]
- [my portfolio ![profile-icon]][profile]
- [open source projects ![git-logo]][github]

[github]: https://github.com/hoishing
[py]: https://api.iconify.design/logos/python.svg?width=20
[js]: https://api.iconify.design/logos/javascript.svg?width=20
[ts]: https://api.iconify.design/logos/typescript-icon.svg?width=20
[bash]: https://api.iconify.design/logos/bash-icon.svg?width=20
[swift]: https://api.iconify.design/logos/swift.svg?width=20
[coffee-script]: https://api.iconify.design/cib/coffeescript.svg?color=%235999FF&width=20
[twitter]: https://api.iconify.design/logos/twitter.svg?width=20
[profile-icon]: https://api.iconify.design/carbon/user-profile.svg?color=%23EF476F&width=20
[binder]: https://mybinder.org/badge_logo.svg
[Video Compressor]: https://apps.apple.com/hk/app/video-compressor/id482465886
[Easy Dictionary]: https://apps.apple.com/hk/app/%E8%8B%B1%E6%BC%A2%E5%AD%97%E5%85%B8-easy-dictionary/id684273271
[英漢字典]: https://apps.apple.com/hk/app/%E8%8B%B1%E6%BC%A2%E5%AD%97%E5%85%B8-ec-dict/id371152394
[同音字典]: https://apps.apple.com/hk/app/%E5%90%8C%E9%9F%B3%E5%AD%97%E5%85%B8/id956045098
[ZERO]: https://apps.apple.com/hk/app/zero-tbs/id1399856976
[iOS apps]: https://apps.apple.com/hk/developer/fbm/id371152397
[cangjie-ipynb]: https://mybinder.org/v2/gh/hoishing/cangjie/HEAD?labpath=create_code.ipynb
[Personalize CangJie IME]: https://github.com/hoishing/cangjie
[Markdown to Dash Docset]: https://github.com/hoishing/markdown-to-dash-docset
[mini-auth]: https://github.com/hoishing/mini-authenticator
[Atom Cell Navigation]: https://github.com/hoishing/cell-navigation
[totp-auth]: https://github.com/hoishing/totp-auth
[TOTP Generator]: https://www.npmjs.com/package/totp-auth
[GData iOS Static lib]: https://github.com/hoishing/GData-iOS-Static-Library-1.12
[tw-shing]: https://twitter.com/hoishing
[profile]: https://hoishing.github.io/
[voice-recog]: https://github.com/hoishing/voice-recog
[zero-game]: https://github.com/hoishing/zero-game
[buddhism-objc]: https://github.com/hoishing/buddhism-objc
[Icon Resize CLI]: https://pypi.org/project/icon-resize
[icon-resize-git]: https://github.com/hoishing/icon-resize-cli
[unocss]: https://github.com/unocss/unocss
[alpine.js]: https://alpinejs.dev
[pwa]: https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps
[Speech Recognition]: https://hoishing.github.io/speech-recog
[git-logo]: https://api.iconify.design/bi/github.svg?color=%236FD886&width=20
[Tesseract OCR]: https://github.com/madmaze/pytesseract
[selenium]: https://selenium-python.readthedocs.io
[Selenium Crawler]: https://github.com/hoishing/selenium-crawler
[voice-search-crx]: https://github.com/hoishing/multilingual-voice-search
[Multilingual Voice Search]: https://chrome.google.com/webstore/detail/multilingual-voice-search/ecfkiahgkikgihfhkmpggilephnaaidm
[Mini Authenticator]: https://chrome.google.com/webstore/detail/mini-authenticator/nmhjblhloefhbhgbfkdgdpjabaocnhha
[Raycast Scripts]: https://github.com/hoishing/raycast-scripts
[raycast]: https://www.raycast.com
[Audrey Tang]: https://zh.wikipedia.org/zh-tw/%E5%94%90%E9%B3%B3
[work out loud]: https://youtu.be/XpjNl3Z10uc
[kTemplate]: https://pypi.org/project/ktemplate/
[kTemplate-git]: https://github.com/hoishing/kTemplate
[pipable]: https://pypi.org/project/pipable
[pipable-git]: https://github.com/hoishing/pipable
[selenium-ipynb]: https://mybinder.org/v2/gh/hoishing/selenium-crawler/HEAD?labpath=selenium-crawler.ipynb
[colab-logo]: https://colab.research.google.com/assets/colab-badge.svg
[doc2txt-colab]: https://colab.research.google.com/github/hoishing/doc2txt/blob/main/doc2txt.ipynb
[doc2txt]: https://github.com/hoishing/doc2txt
