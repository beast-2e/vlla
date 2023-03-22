"""Contains the various pride flags (hope I got most of them)"""

from vlla import *

def agender(c):
    """Draws the agender flag on the DrawingCanvas c"""
    gray = Color(8, 8, 8)
    mint = Color(13, 24, 0)
    white = Color(31, 31, 31)

    c.draw_rectangle((0, 0), (59, 4), BLACK, BLACK)
    c.draw_rectangle((0, 5), (59, 9), gray, gray)
    c.draw_rectangle((0, 10), (59, 13), white, white)
    c.draw_rectangle((0, 14), (59, 17), mint, mint)
    c.draw_rectangle((0, 18), (59, 21), white, white)
    c.draw_rectangle((0, 22), (59, 26), gray, gray)
    c.draw_rectangle((0, 27), (59, 31), BLACK, BLACK)
    c.flush()

def aromantic(c):
    """Draws the aromantic flag on the DrawingCanvas c"""
    dark = Color(8, 22, 12)
    light = Color(16, 26, 16)
    white = Color(26, 26, 26)
    gray = Color(12, 12, 12)

    c.draw_rectangle((0, 0), (59, 6), dark, dark)
    c.draw_rectangle((0, 7), (59, 12), light, light)
    c.draw_rectangle((0, 13), (59, 18), white, white)
    c.draw_rectangle((0, 19), (59, 25), gray, gray)
    c.draw_rectangle((0, 26), (59, 31), BLACK, BLACK)
    c.flush()

def asexual(c):
    """Draws the asexual flag on the DrawingCanvas c"""
    gray = Color(8, 8, 8)
    white = Color(26, 26, 26)
    purple = Color(13, 0, 13)

    c.draw_rectangle((0, 0), (59, 7), BLACK, BLACK)
    c.draw_rectangle((0, 8), (59, 15), gray, gray)
    c.draw_rectangle((0, 16), (59, 23), white, white)
    c.draw_rectangle((0, 24), (59, 31), purple, purple)

    c.flush()

def bisexual(c):
    """Draws the bisexual flag on the DrawingCanvas c"""
    magenta = Color(21, 0, 11)
    lavender = Color(16, 8, 15)
    blue = Color(0, 6, 17)

    c.draw_rectangle((0, 0), (59, 10), magenta, magenta)
    c.draw_rectangle((0, 11), (59, 20), lavender, lavender)
    c.draw_rectangle((0, 21), (59, 31), blue, blue)
    c.flush()

def demisexual(c):
    """Draws the demisexual flag on the DrawingCanvas c"""
    white = Color(26, 26, 26)
    purple = Color(11, 0, 11)
    gray = Color(8, 8, 8)

    c.draw_rectangle((0, 0), (59, 11), white, white)
    c.draw_rectangle((0, 12), (59, 18), purple, purple)
    c.draw_rectangle((0, 19), (59, 31), gray, gray)

    c.draw_line((59, 0), (59, 31), BLACK)

    # draw triangle
    for i in range(15):
        c.draw_line((i, i), (i, 31 - i), BLACK)

        c.flush()

def genderfluid(c):
    """Draws the genderfluid flag on the DrawingCanvas c"""
    pink = Color(26, 12, 16)
    white = Color(25, 25, 25)
    purple = Color(19, 2, 21)
    blue = Color(5, 6, 19)

    c.draw_rectangle((0, 0), (59, 6), pink, pink)
    c.draw_rectangle((0, 7), (59, 12), white, white)
    c.draw_rectangle((0, 13), (59, 18), purple, purple)
    c.draw_rectangle((0, 19), (59, 25), BLACK, BLACK)
    c.draw_rectangle((0, 26), (59, 31), blue, blue)
    c.flush()

def genderqueer(c):
    """Draws the genderqueer flag on the DrawingCanvas c"""
    purple = Color(18, 6, 22)
    white = Color(26, 26, 26)
    green = Color(7, 13, 4)

    c.draw_rectangle((0, 0), (59, 10), purple, purple)
    c.draw_rectangle((0, 11), (59, 20), white, white)
    c.draw_rectangle((0, 21), (59, 31), green, green)
    c.flush()

def intersex(c):
    """Draws the intersex flag on the DrawingCanvas c"""
    yellow = Color(30, 22, 0)
    purple = Color(8, 0, 8)

    c.draw_rectangle((0, 0), (59, 31), yellow, yellow)
    c.draw_circle((30, 16), 9, purple)
    c.draw_circle((30, 16), 8, purple)
    c.draw_circle((30, 16), 7, purple)
    c.draw_circle((30, 16), 6, purple)
    c.flush()

def lesbian(c):
    """Draws the lesbian flag on the DrawingCanvas c"""
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

def mlm(c):
    """Draws the men-loving-men flag on the DrawingCanvas c"""
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

def nonbinary(c):
    """Draws the nonbinary flag on the DrawingCanvas c"""
    yellow = Color(25, 24, 5)
    white = Color(25, 25, 25)
    purple = Color(16, 7, 21)

    c.draw_rectangle((0, 0), (59, 7), yellow, yellow)
    c.draw_rectangle((0, 8), (59, 15), white, white)
    c.draw_rectangle((0, 16), (59, 23), purple, purple)
    c.draw_rectangle((0, 24), (59, 31), BLACK, BLACK)
    c.flush()

def pansexual(c):
    """Draws the pansexual flag on the DrawingCanvas c"""
    blue = Color(3, 18, 26)
    yellow = Color(26, 22, 0)
    pink = Color(26, 3, 14)

    c.draw_rectangle((0, 0), (59, 10), pink, pink)
    c.draw_rectangle((0, 11), (59, 20), yellow, yellow)
    c.draw_rectangle((0, 21), (59, 31), blue, blue)

    c.flush()

def polyamory(c):
    """Draws the polyamory flag on the DrawingCanvas c"""
    pink = Color(25, 3, 19)
    green = Color(1, 24, 7)
    blue = Color(3, 6, 12)

    c.draw_rectangle((0, 0), (59, 10), pink, pink)
    c.draw_rectangle((0, 11), (59, 20), green, green)
    c.draw_rectangle((0, 21), (59, 31), blue, blue)
    c.flush()

def pride(c):
    """Draws the rainbow pride flag on the DrawingCanvas c"""
    c.draw_rectangle((0, 0), (59, 5), Color(24, 0, 0))
    c.draw_rectangle((0, 6), (59, 10), Color(24, 12, 0))
    c.draw_rectangle((0, 11), (59, 15), Color(24, 24, 0))
    c.draw_rectangle((0, 16), (59, 20), Color(0, 24, 0))
    c.draw_rectangle((0, 21), (59, 25), Color(0, 0, 24))
    c.draw_rectangle((0, 26), (59, 31), Color(24, 0, 24))
    c.flush()

def transgender(c):
    """Draws the transgender flag on the DrawingCanvas c"""
    blue = Color(8, 21, 25)
    pink = Color(25, 17, 18)
    white = Color(26, 26, 26)

    c.draw_rectangle((0, 0), (59, 6), blue)
    c.draw_rectangle((0, 7), (59, 12), pink)
    c.draw_rectangle((0, 13), (59, 18), white)
    c.draw_rectangle((0, 19), (59, 24), pink)
    c.draw_rectangle((0, 25), (59, 31), blue)
    c.flush()

def shuffle(c, period=1200, prev_last=None):
    """Shuffles through all the pride flags, displaying them on DrawingCanvas c.

    Each flag will be displayed for period seconds, and the function will only
    return after displaying them all. The last flag to be displayed will be
    returned.

    The order of the flags is randomized, but if prev_last is given, that flag
    will not be displayed first.
    """
    import random

    flags = [
        agender,
        aromantic,
        asexual,
        bisexual,
        demisexual,
        genderfluid,
        genderqueer,
        intersex,
        lesbian,
        mlm,
        nonbinary,
        pansexual,
        polyamory,
        pride,
        transgender,
    ]

    random.shuffle(flags)

    if flags[0] == prev_last:
        i = random.randrange(1, len(flags))
        temp = flags[i]
        flags[i] = flags[0]
        flags[0] = temp

    prev_last = flags[-1]

    for flag in flags:
        flag(c)
        time.sleep(period)

    return prev_last

if __name__ == '__main__':
    import sys, random, time

    c = DrawingCanvas()

    if len(sys.argv) < 2 or sys.argv[1].lower() == 'shuffle':
        period = int(sys.argv[2]) if len(sys.argv) >= 3 else 1200
        last = None

        while True:
            last = shuffle(c, period, last)
    else:
        flag = sys.argv[1].lower()

        flags = {
            'agender': agender,
            'aromantic': aromantic,
            'asexual': asexual,
            'bisexual': bisexual,
            'demisexual': demisexual,
            'genderfluid': genderfluid,
            'genderqueer': genderqueer,
            'intersex': intersex,
            'lesbian': lesbian,
            'mlm': mlm,
            'nonbinary': nonbinary,
            'pansexual': pansexual,
            'polyamory': polyamory,
            'pride': pride,
            'transgender': transgender,
        }

        try:
            flag = flags[flag]
        except KeyError:
            print(f'{flag} is not a valid command')
            print('Usage: {} [command]'.format(sys.argv[0]))
            print('Allowed commands:')
            print('shuffle')

            for flag in flags:
                print(flag)
        else:
            flag(c)
