from vlla import *

pink = Color(25, 3, 19)
green = Color(1, 24, 7)
blue = Color(3, 6, 12)

c = DrawingCanvas()

c.draw_rectangle((0, 0), (59, 10), pink, pink)
c.draw_rectangle((0, 11), (59, 20), green, green)
c.draw_rectangle((0, 21), (59, 31), blue, blue)
c.flush()
