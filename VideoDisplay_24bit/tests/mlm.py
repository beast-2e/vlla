from vlla import *

c = DrawingCanvas()
color = Color(1, 12, 6)
c.draw_rectangle((0, 0), (59, 4), color, color)
color = Color(4, 20, 12)
c.draw_rectangle((0, 5), (59, 9), color, color)
color = Color(15, 24, 14)
c.draw_rectangle((0, 10), (59, 13), color, color)
color = Color(26, 26, 26)
c.draw_rectangle((0, 14), (59, 17), color, color)
color = Color(12, 17, 23)
c.draw_rectangle((0, 18), (59, 21), color, color)
color = Color(8, 7, 21)
c.draw_rectangle((0, 22), (59, 26), color, color)
color = Color(6, 3, 12)
c.draw_rectangle((0, 27), (59, 31), color, color)
c.flush()