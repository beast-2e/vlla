from fractions import Fraction
import math, time

WIDTH = 60
HEIGHT = 32

class Color:
    """Represents a color for the VLLA, using one byte for RGB.

    Note that the maximum for any channel is 0xfe (though it is not
    recommended to go even close to that high).
    """

    def __init__(self, r=0, g=0, b=0):
        """Initializes the color to (rgb), maxing out at 0xfe"""
        self.rgb = [0, 0, 0]
        self.r = r
        self.g = g
        self.b = b

    @property
    def r(self):
        return self[0]

    @r.setter
    def r(self, new):
        self[0] = new

    @property
    def g(self):
        return self[1]

    @g.setter
    def g(self, new):
        self[1] = new

    @property
    def b(self):
        return self[2]

    @b.setter
    def b(self, new):
        self[2] = new

    def __getitem__(self, key):
        return self.rgb[key]

    def __setitem__(self, key, value):
        self.rgb[key] = max(0, min(value, 0xfe))

    def __iter__(self):
        return iter(self.rgb)

    def __str__(self):
        return '#{:>02x}{:>02x}{:>02x}'.format(self.r, self.g, self.b)

    def __repr__(self):
        return 'Color({:#x}, {:#x}, {:#x})'.format(self.r, self.g, self.b)

BLACK = Color()

class Canvas:
    """Represents a drawing canvas for the VLLA."""

    def __init__(self, background=BLACK, top='/dev/ttyACM0', bottom='/dev/ttyACM1'):
        """Initializes a 60x32 canvas using background as the default color.

        The files to output to are given by top and bottom, which can either
        be str objects with the filename, or RawIo objects
        """

        self.canvas = [
            chan for chan in background for i in range(0, WIDTH*HEIGHT)
        ]

        if type(top) is str:
            self.top = open(top, 'wb')
        else:
            self.top = top

        if type(bottom) is str:
            self.bottom = open(bottom, 'wb')
        else:
            self.bottom = bottom

    def set_pixel(self, row, col, color):
        """Sets the pixel at (row, col) to color."""
        assert 0 <= row < HEIGHT, "row is out of range"
        assert 0 <= col < WIDTH, "column is out of range"

        for i in range(0, 3):
            self.canvas[(row * WIDTH + col) * 3 + i] = color[i]

    def clear(self, background=BLACK):
        """Clears the canvas to the given background color."""
        for i in range(0, len(self.canvas)):
            self.canvas[i] = background[i % 3]

    def flush(self):
        """Sends the canvas data to the VLLA."""
        half = WIDTH*HEIGHT*3//2
        self.top.write(bytearray([0xff] + self.canvas[:half]))
        self.top.flush()
        self.bottom.write(bytearray([0xff] + self.canvas[half:]))
        self.bottom.flush()

    def __getitem__(self, i):
        """Returns the pixel at (x,y)."""
        row, col = i
        r = self.canvas[(row * WIDTH + col) * 3]
        g = self.canvas[(row * WIDTH + col) * 3 + 1]
        b = self.canvas[(row * WIDTH + col) * 3 + 2]
        return Color(r, g, b)

class DrawingCanvas(Canvas):
    """Represents a Canvas that has methods for drawing common geometric shapes.

    These currently include rectangles, circles, and lines.
    """

    def draw_line(self, start, end, color):
        """Draws a one pixel thick line from start to end

        start and end are both provided as (x, y). Currently diagonal lines will
        appear jagged.
        """
        x1, y1 = start
        x2, y2 = end
        width = x1 - x2
        height = y1 - y2

        if abs(width) > abs(height):
            dx = 1
            count = abs(width)

            if x1 < x2:
                x = x1
                y = y1
                dy = Fraction(y2 - y1, abs(width))
            else:
                x = x2
                y = y2
                dy = Fraction(y1 - y2, abs(width))
        else:
            dy = 1
            count = abs(height)

            if y1 < y2:
                y = y1
                x = x1
                dx = Fraction(x2 - x1, abs(height))
            else:
                y = y2
                x = x2
                dx = Fraction(x1 - x2, abs(height))

        for i in range(count):
            self.set_pixel(col=math.floor(x), row=math.floor(y), color=color)
            x += dx
            y += dy

    def draw_rectangle(self, start, end, border, fill_color=True):
        """Draws a rectangle with one corner at start, the other at end.

        start and end are of the form (x, y). fill_color should be a color,
        True, or None. If None is given, the rectangle will not be filled, but
        if True is given, the rectangle will be filled with fill_color.
        """
        x1, y1 = start
        x2, y2 = end

        if x1 > x2:
            temp = x1
            x1 = x2
            x2 = temp
        if y1 > y2:
            temp = y1
            y1 = y2
            y2 = temp

        for x in range(x1, x2+1):
            self.set_pixel(row=y1, col=x, color=border)
            self.set_pixel(row=y2, col=x, color=border)
        for y in range(y1, y2+1):
            self.set_pixel(row=y, col=x1, color=border)
            self.set_pixel(row=y, col=x2, color=border)

        if fill_color is not None:
            if fill_color is True:
                fill_color = border

            for x in range(x1+1, x2):
                for y in range(y1+1, y2):
                    self.set_pixel(row=y, col=x, color=fill_color)

    def draw_circle(self, center, radius, border, fill_color=None):
        """Draws a circle with the given center and radius.

        center is of the form (x, y). fill_color should be either a color or
        None. If None is given, the circle will not be filled.
        """
        cx, cy = center

        def draw_outside():
            for deg in range(0, 360, 5):
                x = cx + radius * math.cos(math.pi * deg / 180)
                y = cy + radius * math.sin(math.pi * deg / 180)

                self.set_pixel(
                    row=round(y),
                    col=round(x),
                    color=border
                )

        def draw_inside():
            pass

        draw_outside()

if __name__ == '__main__':
    white = Color(0x7f, 0x7f, 0x7f)
    red = Color(0x7f, 0, 0)
    blue = Color(0, 0, 0x7f)
    c = DrawingCanvas()

    while True:
        c.clear()
        c.draw_line((0, 0), (59, 31), white)
        c.draw_line((59, 0), (0, 31), white)
        c.draw_line((30, 0), (30, 31), white)
        c.draw_line((0, 16), (59, 16), white)
        c.flush()
        time.sleep(2)

        c.clear()
        c.draw_rectangle((30, 10), (40, 20), red)
        c.draw_rectangle((20, 31), (10, 21), blue, fill_color=red)
        c.flush()
        time.sleep(2)

        c.clear()
        c.draw_circle((30, 16), 10, white)
        c.flush()
        time.sleep(2)
