# MouseAndKeyboardVisualizer

## Requirements
### Version
- Python 3 (3.11.9 is what was used for this)
### Packages
- pynput
- screeninfo
- matplotlib
- seaborn
### OS
- must be on windows (uses winsound)

## Usage
- Ensure that the resolution used in game is the same as on the desktop (ie if your ingame resolution is 1280*960, set the desktop resolution to that too)
- Running main will start a countdown. While this countdown is running, tab into whatever game is being played. Once the countain is done, a beep will sound. This is when the data starts being collected
- after time is up (which is default to 180 seconds and can be changed by changing MAXRUNNINGTIME in main) or when the end key is pressed, graphs relating the mouse movement and keyboard input will be made automatically
