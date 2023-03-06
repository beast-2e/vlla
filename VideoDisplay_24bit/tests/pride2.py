#!/usr/bin/python3

import vlla

c = vlla.Canvas()

for i in range(0, 6):
    for j in range(0, 60):
        c.set_pixel(i, j, vlla.Color(24, 0, 0))
for i in range(6, 11):
    for j in range(0, 60):
        c.set_pixel(i, j, vlla.Color(24, 12, 0))
for i in range(11, 16):
    for j in range(0, 60):
        c.set_pixel(i, j, vlla.Color(24, 24, 0))

for i in range(16, 21):
    for j in range(0, 60):
        c.set_pixel(i, j, vlla.Color(0, 24, 0))
for i in range(21, 26):
    for j in range(0, 60):
        c.set_pixel(i, j, vlla.Color(0, 0, 24))
for i in range(26, 32):
    for j in range(0, 60):
        c.set_pixel(i, j, vlla.Color(24, 0, 24))

c.flush()
