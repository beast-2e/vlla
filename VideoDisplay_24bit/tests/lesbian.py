from vlla import *

def lesbian(c):
    color = Color(21, 14, 0)
    c.draw_rectangle((0, 0), (59, 4), color, color)
    color = Color(24, 12, 3)
    c.draw_rectangle((0, 5), (59, 9), color, color)
    color = Color(26, 16, 7)
    c.draw_rectangle((0, 10), (59, 13), color, color)
    color = Color(26, 26, 26)
    c.draw_rectangle((0, 14), (59, 17), color, color)
    color = Color(24, 11, 20)
    c.draw_rectangle((0, 18), (59, 21), color, color)
    color = Color(15, 4, 11)
    c.draw_rectangle((0, 22), (59, 26), color, color)
    color = Color(18, 0, 11)
    c.draw_rectangle((0, 27), (59, 31), color, color)
    c.flush()

if __name__ == '__main__':
    import time
    from random import randrange

    c = DrawingCanvas()

    while True:
        lesbian(c)
        count = randrange(1, 19)
        white = Color(0x7f, 0x7f, 0x7f)

        to_set = [(randrange(0, 32), randrange(0, 60)) for i in range(0, count)]

        for i in range(0, 5):
            for row, col in to_set:
                color = c[row, col]
                color.r += 20
                color.g += 20
                color.b += 20
                c.set_pixel(row, col, color)

            c.flush()
            time.sleep(0.1)

        for i in range(0, 5):
            for row, col in to_set:
                color = c[row, col]
                color.r -= 20
                color.g -= 20
                color.b -= 20
                c.set_pixel(row, col, color)

            c.flush()
            time.sleep(0.1)
else:
    lesbian(DrawingCanvas())
