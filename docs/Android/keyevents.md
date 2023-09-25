## Key events
### Explanation 
Every keyboard button has self key event number. Using key events allow us to take an action like a tap on requested button.
### How use that - Command Prompt
```
adb shell input keyevent <key event number>
```
### How use that - Python
In the beginning import library 'os':
```
import os
```
Execute Command Prompt order over python script using function 'system'
```
os.system("adb shell input keyevent <key event number>")
```
### How use that - Appium Python
On defined driver use built-in function press_keycode():
```
self.driver.press_keycode(key_event)
```
### Most useful key events
```
0 --> "KEYCODE_UNKNOWN"
1 --> "KEYCODE_MENU"
2 --> "KEYCODE_SOFT_RIGHT"
3 --> "KEYCODE_HOME"
4 --> "KEYCODE_BACK"
5 --> "KEYCODE_CALL"
6 --> "KEYCODE_ENDCALL"
19 --> "KEYCODE_DPAD_UP"
20 --> "KEYCODE_DPAD_DOWN"
21 --> "KEYCODE_DPAD_LEFT"
22 --> "KEYCODE_DPAD_RIGHT"
23 --> "KEYCODE_DPAD_CENTER"
24 --> "KEYCODE_VOLUME_UP"
25 --> "KEYCODE_VOLUME_DOWN"
58 --> "KEYCODE_ALT_RIGHT"
59 --> "KEYCODE_SHIFT_LEFT"
60 --> "KEYCODE_SHIFT_RIGHT"
61 --> "KEYCODE_TAB"
62 --> "KEYCODE_SPACE"
66 --> "KEYCODE_ENTER"
67 --> "KEYCODE_DEL"
```
Link to all key events:
```
https://gist.github.com/arjunv/2bbcca9a1a1c127749f8dcb6d36fb0bc
```