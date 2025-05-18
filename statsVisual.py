import csv
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import logging

logging.getLogger('matplotlib').setLevel(logging.WARNING)

layout = [
    ['Key.esc', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Key.backspace'],
    ['Key.tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
    ['Key.caps_lock', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'', 'Key.enter'],
    ['Key.shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'Key.shift'],
    ['Key.ctrl_l', 'Key.cmd', 'Key.alt_l', 'fn', 'Key.space', 'fn', 'Key.alt_gr', 'Key.menu', 'Key.ctrl_r']
]

def plotMouse():
    xValues = []
    yValues = []
    f = open('mouseStats.txt', 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        line = line.strip()
        if line == '':
            continue
        x, y = line.split(' ')
        x = int(x)
        y = int(y)
        xValues.append(x)
        yValues.append(y)
    plt.plot(xValues, yValues)
    plt.title('mouse movement')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('mouseStats.png')
    plt.show()


def visualizeKeyboard():
    with open('keyStats.csv', 'r') as file:
        reader = csv.reader(file)
        data = {k: int(v) for k, v in reader}

    max_len = max(len(row) for row in layout)
    keys = list(data.keys())
    values = list(data.values())

    matrix = []
    for row in layout:
        row_vals = []
        for key in row:
            val = data.get(key, 0)
            row_vals.append(val)
        row_vals += [0] * (max_len - len(row_vals))
        matrix.append(row_vals)
    annotations = [row + [''] * (max_len - len(row)) for row in layout]

    plt.figure(figsize=(16, 6))
    sns.heatmap(matrix, annot=annotations, fmt="", cmap="YlOrBr", linewidths=1, cbar=True)
    plt.title("Keyboard Input Heatmap")
    plt.axis('off')
    plt.savefig('keyboardStats.png')
    plt.show()



if __name__ == '__main__':
    plotMouse()
    visualizeKeyboard()