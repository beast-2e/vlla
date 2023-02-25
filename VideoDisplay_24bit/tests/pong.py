#!/usr/bin/python3

from enum import Enum
import queue, termios, sys, tty, time, threading
import vlla

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

Key = Enum('Key', ['LEFT_UP', 'RIGHT_UP', 'LEFT_DOWN', 'RIGHT_DOWN', "INT"])

def getkey():
    ch = getch().lower()

    if ch == '\x1b':
        if getch() == '[':
            ch = getch()

            if ch == 'A':
                return Key.RIGHT_UP
            elif ch == 'B':
                return Key.RIGHT_DOWN
    elif ch == '\x03':
        raise KeyboardInterrupt
    elif ch == 'w':
        return Key.LEFT_UP
    elif ch == 's':
        return Key.LEFT_DOWN

    return None

key_queue = queue.SimpleQueue()

def key_reader():
    while True:
        try:
            key_queue.put(getkey())
        except KeyboardInterrupt:
            key_queue.put(Key.INT)
            return

lpaddle = 0
rpaddle = 0
ball_row = 16
ball_col = 30
dt = 0.1
theta = 0
v = 1

color = vlla.Color(g=0x7f)
canvas = vlla.Canvas()

def draw():
    for i in range(0, 8):
        canvas.set_pixel(lpaddle + i, 1, color)
        canvas.set_pixel(rpaddle + i, vlla.WIDTH - 2, color)

    canvas.set_pixel(ball_row, ball_col, color)
    canvas.flush()
    canvas.clear()

draw()
reader = threading.Thread(target=key_reader)
reader.start()

prev = time.time()

while True:
    start = time.time()

    try:
        remaining = max(dt - (time.time() - prev), 0)
        key = key_queue.get(timeout=remaining)
    except queue.Empty:
        pass

    if time.time() - prev >= dt:
        ball_col = (ball_col + v) % vlla.WIDTH
        prev = time.time()
        draw()
        continue

    if key == Key.LEFT_UP:
       lpaddle = max(lpaddle - 1, 0)
    elif key == Key.RIGHT_UP:
        rpaddle = max(rpaddle - 1, 0)
    elif key == Key.LEFT_DOWN:
        lpaddle = min(lpaddle + 1, vlla.HEIGHT - 8)
    elif key == Key.RIGHT_DOWN:
        rpaddle = min(rpaddle + 1, vlla.HEIGHT - 8)
    elif key == Key.INT:
        raise KeyboardInterrupt
    draw()

