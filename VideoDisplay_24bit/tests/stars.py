#!/usr/bin/python3

import itertools
import random
import sys

row = 1
col = 1

canvas = [[[0,0,0] for i in range(0, 60)] for i in range(0, 16)]

while row < 15:
    while col < 59:
        if random.random() < 0.1:
            canvas[row][col] = [0x7f, 0x7f, 0x7f]
            col += 1
        col += 1
    row += 1

bytes = [canvas[row][col][chan] for chan in range(0, 3) for col in range(0, 60) for row in range(0, 16)]
bytes = [0xff] + bytes
sys.stdout.buffer.write(bytearray(bytes))
