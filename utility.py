from screeninfo import get_monitors
monitor = get_monitors()[0]
screen_width = monitor.width
screen_height = monitor.height

CENTERWIDTH = screen_width // 2
CENTERHEIGHT = screen_height // 2

def checkForCenter(x,y):
    return x in range(CENTERWIDTH-1, CENTERWIDTH+1) and y in range(CENTERHEIGHT-1, CENTERHEIGHT+1)