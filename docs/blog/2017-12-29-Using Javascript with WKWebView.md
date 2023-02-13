---
title: Using Javascript with WKWebView
subtitle: Harnessing The Power of Both Languages in Your Apps
gh-repo: hoishing/TestJS_WKWebView
tags: 
  - js
  - iOS
  - swift
---
###### date: 2017-12-29

WebKit allows us to use javascript along side with the native swift code. On one hand, we could call the javascript statements in swift. On the other hand, javascript from web view could be able to trigger a delegate method defined in swift code. This gives us a two way communication between the native swift code and javascript used by a web view.

## Basic Setup

Here we have a window with a WKWebView showing some text. It has 2 buttons inside. One for showing the text and triggering a swift handler, the other for hiding the text. Also, we have a native button that triggers a javascript function to hide the text.

<img src='https://i.imgur.com/lt6RyEb.png' width='400'/>

## Triggering Javascript Functions from Swift

The IB outlet and action of the app as follow. Note that we simply use `evaluateJavaScript(_:completionHandler:)` to trigger some javascript in the web view, `hideText()` is a custom method we defined inside javascript.

```swift
@IBOutlet var webV: WKWebView!

@IBAction func showJSAlert(_ sender: Any) {
   let js = "hideText();"
   webV.evaluateJavaScript(js, completionHandler: nil)
}
```

## Receiving Javascript Messages

To receive message from the javascript, we need to provide a message name for javascript to call upon. We just name it "jsHandler". After that we load the html and javascript into the web view.

```swift
 override func viewDidLoad() {
   super.viewDidLoad()
   webV.configuration.userContentController.add(self, name: "jsHandler")
   let bundleURL = Bundle.main.resourceURL!.absoluteURL
   let html = bundleURL.appendingPathComponent("try.html")
   webV.loadFileURL(html, allowingReadAccessTo:bundleURL)
}
```

We also need to adopt the `WKScriptMessageHandler` protocol in our view controller, and implement the `userContentController(_:didReceive:)` method. For simplicity, we just print out the message received from the javascript.

```swift
func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
   if message.name == "jsHandler" {
       print(message.body)
   }
}
```

The HTML and javascript we loaded as follow. Note that in the `showText()` method, the `window.webkit.messageHandlers.jsHandler.postMessage()` is the method we use to trigger the delegate method implemented in our view controller.

```html
<!DOCTYPE html>
<html>
  <head>
    <script>
      function hideText() {
        document.getElementById('demo').style.display = 'none';
      }

      function showText() {
        document.getElementById('demo').style.display = 'block';
        window.webkit.messageHandlers.jsHandler.postMessage('trigger from JS');
      }
    </script>
  </head>
  <body>
    <p id="demo">Hello World.</p>
    <input
      type="button"
      onclick="showText()"
      value="Show Text and Trigger Handler"
    />
    <input type="button" onclick="hideText()" value="Hide Text" />
  </body>
</html>
```

[Download Sample Project](https://github.com/hoishing/TestJS_WKWebView)
