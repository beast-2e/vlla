#!/usr/bin/python3

import math
import time

white = [50, 65, 65]
red = [90, 0, 0]
green = [0, 127, 0]
blue = [0, 0, 127]
orange = [127, 55, 0]
cycle = [red, orange, green, blue]
black = [0, 0, 0]

index = 0
step = 0
top = open('/dev/ttyACM0', 'wb')
bottom = open('/dev/ttyACM1', 'wb')

steps = 30

def blend(c, step):
    theta = step / steps * math.pi
    factor1 = (math.cos(theta) + 1) / 2
    factor2 = 1 - factor1
    first = cycle[c]
    second = cycle[(c + 1) % len(cycle)]
    map = lambda i: int(first[i] * factor1 + second[i] * factor2)
    return [map(i) for i in range(0, 3)]

while True:
    color = blend(index, step)
    canvas = [[black for i in range(0, 60)] for i in range(0, 32)]

    # make top of T
    for y in range(12, 14):
        for x in range(24, 36):
            canvas[y][x] = color

    # make bottom of T
    for y in range(14, 24):
        for x in range(29, 31):
            canvas[y][x] = color

    # make circle
    for i in range(0, 40):
        angle = i * math.pi / 20
        for radius in range(12, 14):
            x = round(math.cos(angle) * radius + 30)
            y = round(math.sin(angle) * radius + 16.5)
            canvas[y][x] = color

    pixels = [
        canvas[y][x][chan]
            for y in range(0, 32)
            for x in range(0, 60)
            for chan in range(0, 3)
    ]

    top.write(bytearray([255] + pixels[:2880]))
    top.flush()

    bottom.write(bytearray([255] + pixels[2880:]))
    bottom.flush()

    time.sleep(1 / 20)

    step += 1

    if step >= steps:
        step = 0
        index = (index + 1) % len(cycle)
