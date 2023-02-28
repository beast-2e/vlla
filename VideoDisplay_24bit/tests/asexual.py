from vlla import *

gray = Color(9, 9, 9)
white = Color(26, 26, 26)
purple = Color(13, 0, 13)

c = DrawingCanvas()

c.draw_rectangle((0, 0), (59, 7), BLACK, BLACK)
c.draw_rectangle((0, 8), (59, 15), gray, gray)
c.draw_rectangle((0, 16), (59, 23), white, white)
c.draw_rectangle((0, 24), (59, 31), purple, purple)

c.flush()
