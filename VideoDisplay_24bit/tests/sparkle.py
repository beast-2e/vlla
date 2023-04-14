"""Code to make the display "sparkle"."""

from random import randrange
import time
from vlla import *

def sparkle(c, display, until=None):
    """Runs the display function, making the vlla "sparkle" each time.

    Args:
        canvas (vlla.Canvas): Canvas to draw on
        display (fn(vlla.Canvas)): Display function to call
        until (float or None): Time to run until.
    """

    while until is None or time.time() < until:
        display(c)
        count = randrange(1, 19)
        white = Color(0x7f, 0x7f, 0x7f)

        to_set = [(randrange(0, 32), randrange(0, 60)) for i in range(0, count)]

        for i in range(0, 5):
            for row, col in to_set:
                color = c[row, col]
                color.r += 20
                color.g += 20
                color.b += 20
                c.set_pixel(row, col, color)

            c.flush()
            time.sleep(0.1)

        for i in range(0, 5):
            for row, col in to_set:
                color = c[row, col]
                color.r -= 20
                color.g -= 20
                color.b -= 20
                c.set_pixel(row, col, color)

            c.flush()
            time.sleep(0.1)
