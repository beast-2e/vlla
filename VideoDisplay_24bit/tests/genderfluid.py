from vlla import *

pink = Color(26, 12, 16)
white = Color(25, 25, 25)
purple = Color(19, 2, 21)
blue = Color(5, 6, 19)

c = DrawingCanvas()

c.draw_rectangle((0, 0), (59, 6), pink, pink)
c.draw_rectangle((0, 7), (59, 12), white, white)
c.draw_rectangle((0, 13), (59, 18), purple, purple)
c.draw_rectangle((0, 19), (59, 25), BLACK, BLACK)
c.draw_rectangle((0, 26), (59, 31), blue, blue)
c.flush()
