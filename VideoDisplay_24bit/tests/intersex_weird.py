from vlla import *

yellow = Color(30, 22, 0)
purple = Color(10, 0, 10)

c = DrawingCanvas()
c.draw_rectangle((0, 0), (59, 31), yellow, yellow)
c.draw_circle((30, 16), 8, purple)
c.draw_circle((30, 16), 7, purple)
c.flush()
