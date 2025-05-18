from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Key
import os, logging, csv, time
import statsVisual, utility
import winsound
from screeninfo import get_monitors
monitor = get_monitors()[0]
screen_width = monitor.width
screen_height = monitor.height
CENTERWIDTH = screen_width // 2
CENTERHEIGHT = screen_height // 2

pressedKeys = set()
timesPressed = dict()

prevMouseX, prevMouseY = 0, 0
lastTime = time.time()
startTime = time.time()
MOUSECAPTURETIMEDIF = 0.1
MAXRUNNINGTIME = 180 # this number is in seconds
running = True
keyboardStatsFile = 'keyStats.csv'
mouseStatsFile = 'mouseStats.txt'

if os.path.exists(mouseStatsFile):
    print("deleting mouseStats.txt")
    os.remove(mouseStatsFile)
if os.path.exists(keyboardStatsFile):
    print("deleting keyStats.csv")
    os.remove(keyboardStatsFile)

logging.basicConfig(filename=(mouseStatsFile), level=logging.DEBUG, format='')

def stopRunning():
    mouse_listener.stop()
    keyboard_listener.stop()
    global running
    running = False

def on_press(key):
    if key == Key.end:
        stopRunning()

    if key not in pressedKeys:
        pressedKeys.add(key)
        key = str(key).replace("'", "")
        if key in timesPressed:
            timesPressed[key] += 1
        else:
            timesPressed[key] = 1
        print(f"Key pressed: {key}")

def on_release(key):
    if key in pressedKeys:
        pressedKeys.remove(key)

def on_move(x, y):
    global prevMouseX, prevMouseY, lastTime
    if utility.checkForCenter(x,y): #idk if this is really needed
        x = CENTERWIDTH
        y = CENTERHEIGHT 
    if prevMouseX != x and prevMouseY != y: # filters out duplicate data if any slips through
        logging.info(str(x) + ' ' + str(y))
        lastTime = time.time()
    prevMouseX, prevMouseY = x, y

if __name__ == "__main__":
        for i in range(0,4):
            time.sleep(1)
            print('starting in ' + str(3-i) + ' seconds')
        mouse_listener = MouseListener(on_move= on_move)
        keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)
        winsound.Beep(300, 500)
        mouse_listener.start()
        keyboard_listener.start()

        while running:
            time.sleep(.001) # this is to prevent the script from using too many resources (i love python :D)
            if (time.time() - startTime) > MAXRUNNINGTIME:
                print("timeout, stopping script")
                stopRunning()

        with open(keyboardStatsFile, 'w', newline = '') as file:
            writer = csv.writer(file)
            for key, times in timesPressed.items():
                writer.writerow([key, times])
        
        statsVisual.plotMouse()
        statsVisual.visualizeKeyboard()

