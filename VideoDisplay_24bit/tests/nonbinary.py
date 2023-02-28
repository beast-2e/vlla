from vlla import *

yellow = Color(25, 24, 5)
white = Color(25, 25, 25)
purple = Color(16, 7, 21)

c = DrawingCanvas()
c.draw_rectangle((0, 0), (59, 7), yellow, yellow)
c.draw_rectangle((0, 8), (59, 15), white, white)
c.draw_rectangle((0, 16), (59, 23), purple, purple)
c.draw_rectangle((0, 24), (59, 31), BLACK, BLACK)
c.flush()
