from vlla import *

magenta = Color(21, 0, 11)
lavender = Color(16, 8, 15)
blue = Color(0, 6, 17)

c = DrawingCanvas()

c.draw_rectangle((0, 0), (59, 10), magenta, magenta)
c.draw_rectangle((0, 11), (59, 20), lavender, lavender)
c.draw_rectangle((0, 21), (59, 31), blue, blue)
c.flush()
