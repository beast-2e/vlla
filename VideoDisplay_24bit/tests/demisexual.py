from vlla import *

white = Color(26, 26, 26)
purple = Color(11, 0, 11)
gray = Color(8, 8, 8)

c = DrawingCanvas()
c.draw_rectangle((0, 0), (59, 11), white, white)
c.draw_rectangle((0, 12), (59, 18), purple, purple)
c.draw_rectangle((0, 19), (59, 31), gray, gray)

c.draw_line((59, 0), (59, 31), BLACK)

# draw triangle
for i in range(15):
    c.draw_line((i, i), (i, 31 - i), BLACK)

c.flush()
