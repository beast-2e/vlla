from vlla import *

white = Color(0x7f, 0x7f, 0x7f)
c = DrawingCanvas()
c.draw_circle((10, 15), 5, white)
c.draw_line((15, 15), (30, 15), white)
c.draw_line((30, 15), (40, 10), white)
c.draw_line((30, 15), (40, 20), white)
c.draw_line((20, 15), (15, 20), white)
c.draw_line((20, 15), (15, 10), white)
c.flush()
