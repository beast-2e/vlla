#!/usr/bin/python3

from vlla import *

c = Canvas()

blue = Color(8, 21, 25)
pink = Color(25, 17, 18)
white = Color(26, 26, 26)

for row in range(0, 7):
    for col in range(0, 60):
        c.set_pixel(row, col, blue)

for row in range(7, 13):
    for col in range(0, 60):
        c.set_pixel(row, col, pink)

for row in range(13, 19):
    for col in range(0, 60):
        c.set_pixel(row, col, white)

for row in range(19, 25):
    for col in range(0, 60):
        c.set_pixel(row, col, pink)

for row in range(25, 32):
    for col in range(0, 60):
        c.set_pixel(row, col, blue)

c.flush()
