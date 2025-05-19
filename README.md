# MouseAndKeyboardVisualizer

## Requirements
### Version
- Python 3 (3.11.9 is what was used for this)
### Packages
- pynput
- screeninfo
- matplotlib
- numpy
- seaborn
### OS
- must be on windows (uses winsound)

## Usage
- run Python main.py <Resolution width> <resolution height> or no arguments (only do this if your desktop resolution is the same as in game)
- Running main will start a countdown. While this countdown is running, tab into whatever game is being played. Once the countain is done, a beep will sound. This is when the data starts being collected
- after time is up (which is default to 180 seconds and can be changed by changing MAXRUNNINGTIME in main) or when the end key is pressed, graphs relating the mouse movement and keyboard input will be made automatically
