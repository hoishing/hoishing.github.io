---
title: Create Menu Bar Apps On macOS
tags: 
  - macOS
  - swift
---
###### date: 2017-10-10

![menu bar apps](https://imgur.com/NsSPohe.png)

Menu bar apps refer to apps that sit on the menu bar (a.k.a. status bar) of macOS. It provide instant access of the key functionalities, as well as being accessible all time during a login session.

## Creating the Status Bar Item

We use `NSStatusBar.system().statusItem(withLength: -1)` to request a status bar item from the system. Note that it may be failed (return nil) if the status bar is already full packed with many other status bar items.

Upon successfully got an status bar item, you got a NSButton as the UI element to put on the menu bar. You need to configure it by providing an image, as well as setting the target and action of the button.

All these should be done during the app launching period, so in the app delegate, we have:

```swift
//strong reference to retain the status bar item object
var statusItem: NSStatusItem?

func applicationDidFinishLaunching(_ aNotification: Notification) {
   statusItem = NSStatusBar.system().statusItem(withLength: -1)  
   
   guard let button = statusItem?.button else {
       print("status bar item failed. Try removing some menu bar item.")
       NSApp.terminate(nil)
       return
   }
   
   button.image = NSImage(named: "MenuBarButton")
   button.target = self
   button.action = #selector(displayMenu)
}
```

Note that a strong reference must be used to retain the status bar item object returned by the system. Otherwise it will be released afterwards, and nothing will be shown on the menu bar.

## Displaying the Menu

To display the menu, you need to provide a reference point for placing the menu object, in this case, the status bar button. We then create a mouse event, and use `popUpContextMenu(_:with:for:)` to bring up the menu.

```swift
@IBOutlet weak var appMenu: NSMenu!

@objc func displayMenu() {
    guard let button = statusItem?.button else { return }
    let x = button.frame.origin.x
    let y = button.frame.origin.y - 5
    let location = button.superview!.convert(NSMakePoint(x, y), to: nil)
    let w = button.window!
    let event = NSEvent.mouseEvent(with: .leftMouseUp,
                                  location: location,
                                  modifierFlags: NSEvent.ModifierFlags(rawValue: 0),
                                  timestamp: 0,
                                  windowNumber: w.windowNumber,
                                  context: w.graphicsContext,
                                  eventNumber: 0,
                                  clickCount: 1,
                                  pressure: 0)!
    NSMenu.popUpContextMenu(appMenu, with: event, for: button)
}
```

## Info.plist Setting

If your app is menu bar **ONLY**, similar to the Dropbox macOS client, you need to set `Application is agent = YES` in your Info.plist in order to omit the Dock's app icon and the app menu on the upper left corner.

[Download Sample Project](https://github.com/hoishing/TestMenuBar)
