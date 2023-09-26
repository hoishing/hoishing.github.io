---
title: AVSpeechSynthesisVoice Fall Back Mechanism
published: true
description: how to handle missing languages in target devices
tags: iOS, swift, AVSpeechSynthesisVoice
---
###### date: 2023-09-26

I recently received complaints from my users stating that some (but not all) devices couldn't perform TTS in my [dictionary app].

At first, I was quite confused because all the devices I had on hand worked fine, as did all the simulators.

Eventually, I realized that the issue might be caused by missing target voices on the user's device.

This can be resolved by implementing a fallback mechanism if the user hasn't installed the required voice package.

```swift
// specific target voice
let targetVoiceID = "com.apple.voice.compact.zh-TW.Meijia"

// fallback language
let fallbackLang = "zh-TW"

// fallback if the user doesn't have the target voice
let voice = AVSpeechSynthesisVoice(identifier: targetVoiceID) ?? AVSpeechSynthesisVoice(language: fallbackLang)
```

One notable feature of `AVSpeechSynthesisVoice(language:)` is that it will further fallback to the system's default voice if the target language is not available. In contrast, `AVSpeechSynthesisVoice(identifier:)` will simply return `nil`.

On reflection, I probably should invite users who are experiencing issues to become beta testers, even though we've only connected online and have never met in person. 😜

[dictionary app]: https://apps.apple.com/hk/app/id371152394
