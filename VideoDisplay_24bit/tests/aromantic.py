from vlla import *

dark = Color(8, 22, 12)
light = Color(16, 26, 16)
white = Color(26, 26, 26)
gray = Color(12, 12, 12)

c = DrawingCanvas()

c.draw_rectangle((0, 0), (59, 6), dark, dark)
c.draw_rectangle((0, 7), (59, 12), light, light)
c.draw_rectangle((0, 13), (59, 18), white, white)
c.draw_rectangle((0, 19), (59, 25), gray, gray)
c.draw_rectangle((0, 26), (59, 31), BLACK, BLACK)
c.flush()
