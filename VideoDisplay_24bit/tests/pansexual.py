from vlla import *

blue = Color(3, 18, 26)
yellow = Color(26, 22, 0)
pink = Color(26, 3, 14)

c = DrawingCanvas()

c.draw_rectangle((0, 0), (59, 10), pink, pink)
c.draw_rectangle((0, 11), (59, 20), yellow, yellow)
c.draw_rectangle((0, 21), (59, 31), blue, blue)

c.flush()
