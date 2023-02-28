from vlla import *

purple = Color(18, 6, 22)
white = Color(26, 26, 26)
green = Color(7, 13, 4)

c = DrawingCanvas()

c.draw_rectangle((0, 0), (59, 10), purple, purple)
c.draw_rectangle((0, 11), (59, 20), white, white)
c.draw_rectangle((0, 21), (59, 31), green, green)
c.flush()
