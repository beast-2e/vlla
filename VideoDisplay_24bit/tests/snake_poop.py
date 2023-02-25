#!/usr/bin/python3

import math
import time

#white = [50, 65, 65]
red = [127, 0, 0]
green = [0, 127, 0]
blue = [0, 0, 127]
orange = [127, 63, 0]
cycle = [red, green, blue, orange]
black = [0, 0, 0]

color = 0

while True:
    canvas = [[black for i in range(0, 60)] for i in range(0, 32)]

    # make top of T
    for y in range(10, 14):
        for x in range(24, 36):
            canvas[y][x] = cycle[color]

    # make bottom of T
    for y in range(14, 22):
        for x in range(28, 32):
            canvas[y][x] = cycle[color]

    # make circle
    for i in range(0, 40):
        angle = i * math.pi / 20
        for radius in range(11, 14):
            x = round(math.cos(angle) * radius + 30)
            y = round(math.sin(angle) * radius + 15)
            canvas[y][x] = cycle[color]

    pixels = [
        canvas[y][x][chan]
            for chan in range(0, 3)
            for x in range(0, 60)
            for y in range(0, 32)
    ]

    top = open('/dev/ttyACM0', 'wb')
    top.write(bytearray([255] + pixels[:2880]))
    top.close()

    bottom = open('/dev/ttyACM1', 'wb')
    bottom.write(bytearray([255] + pixels[2880:]))
    top.close()

    time.sleep(1)
    color = (color + 1) % len(cycle)
