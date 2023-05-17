import time
from vlla import *

def read_file(name, multicolor=False):
    contents = open('ec/' + name + '.txt', 'r').read()
    contents = ''.join(contents.split('\n'))

    if multicolor:
        contents = ['M' if c == 'R' else ' ' for c in contents]

    return contents

c = Canvas()
ec = read_file('ec', multicolor=True)
man = read_file('burning_man')

suits = [ec, man]

i = 0

make_colors = [
    lambda i: Color(i, 0, 0),
    lambda i: Color(0, i, 0),
    lambda i: Color(0, 0, i),
    lambda i: Color(i, i, 0),
    lambda i: Color(i, 0, i),
    lambda i: Color(0, i, i),
    lambda i: Color(i, i // 2 - 1, 0),
]

color_index = 0

def set_pixel(row, col, color, intensity):
    intensity *= 2
    intensity = intensity if intensity != 10 else 11

    if color == 'O':
        color = Color(intensity, intensity // 2 - 1, 0)
    elif color == 'R':
        color = Color(intensity, 0, 0)
    elif color == 'M':
        color = make_colors[int(color_index)](intensity)
    else:
        color = BLACK

    c.set_pixel(row, col, color)

def display(intensity):
    for row in range(0, HEIGHT):
            for col in range(0, WIDTH):
                set_pixel(row, col, suits[i][row * WIDTH + col], intensity)

    c.flush()

while True:
    for intensity in range(1, 11):
        display(intensity)
        time.sleep(0.04)

    time.sleep(0.1)

    for intensity in range(1, 9):
        display(10-intensity)
        time.sleep(0.04)

    i = (i+1) % len(suits)
    color_index = (color_index + 0.5) % len(make_colors)
