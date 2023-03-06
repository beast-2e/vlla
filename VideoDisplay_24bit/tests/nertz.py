from vlla import *

white = Color(0x20, 0x20, 0x20)

def draw_N(c, pos):
    x = pos * 12 + 1
    y = 10

    c.draw_line((x, y), (x, y + 9), white)
    c.draw_line((x, y), (x + 9, y + 9), white)
    c.draw_line((x + 9, y), (x + 9, y + 9), white)

def draw_E(c, pos):
    x = pos * 12 + 1
    y = 10

    c.draw_line((x, y), (x + 9, y), white)
    c.draw_line((x, y), (x, y + 9), white)
    c.draw_line((x, y + 4), (x + 7, y + 4), white)
    c.draw_line((x, y + 9), (x + 7, y + 9), white)

def draw_R(c, pos):
    x = pos * 12 + 1
    y = 10

    c.draw_line((x, y), (x, y + 9), white)
    c.draw_line((x, y), (x + 9, y + 3), white)
    c.draw_line((x + 9, y + 3), (x, y + 6), white)
    c.draw_line((x, y + 6), (x + 9, y + 9), white)

def draw_T(c, pos):
    x = pos * 12 + 1
    y = 10

    c.draw_line((x, y), (x + 9, y), white)
    c.draw_line((x + 4, y), (x + 4, y + 9), white)

def draw_Z(c, pos):
    x = pos * 12 + 1
    y = 10

    c.draw_line((x, y), (x + 9, y), white)
    c.draw_line((x + 9, y), (x, y + 9), white)
    c.draw_line((x, y + 9), (x + 9, y + 9), white)

c = DrawingCanvas()
draw_N(c, 0)
draw_E(c, 1)
draw_R(c, 2)
draw_T(c, 3)
draw_Z(c, 4)
c.flush()
