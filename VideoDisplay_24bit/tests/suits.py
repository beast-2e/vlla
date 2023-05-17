import time
from vlla import *

def read_file(name, color):
    contents = open('suits/' + name + '.txt', 'r').read()
    contents = ''.join(contents.split('\n'))
    return [color if c == '#' else ' ' for c in contents]

c = Canvas()
spade = read_file('spade', 'B')
club = read_file('club', 'B')
heart = read_file('heart', 'R')
diamond = read_file('diamond', 'R')

suits = [spade, heart, club, diamond]

i = 0

def set_pixel(row, col, color, intensity):
    intensity *= 2
    intensity = intensity if intensity != 10 else 11

    if color == 'B':
        color = Color(0, 0, intensity)
    elif color == 'R':
        color = Color(intensity, 0, 0)
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
        time.sleep(0.025)

    time.sleep(0.1)

    for intensity in range(1, 9):
        display(10-intensity)
        time.sleep(0.025)

    i = (i+1) % len(suits)
