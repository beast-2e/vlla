from vlla import *

gray = Color(8, 8, 8)
mint = Color(13, 24, 0)
white = Color(31, 31, 31)

c = DrawingCanvas()
c.draw_rectangle((0, 0), (59, 4), BLACK, BLACK)
c.draw_rectangle((0, 5), (59, 9), gray, gray)
c.draw_rectangle((0, 10), (59, 13), white, white)
c.draw_rectangle((0, 14), (59, 17), mint, mint)
c.draw_rectangle((0, 18), (59, 21), white, white)
c.draw_rectangle((0, 22), (59, 26), gray, gray)
c.draw_rectangle((0, 27), (59, 31), BLACK, BLACK)
c.flush()
