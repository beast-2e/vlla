#!/bin/env python3
import snake, pride_flags, time, vlla

while True:
    c = vlla.DrawingCanvas()
    pride_flags.shuffle(c, period=1200)
    snake.loop(c, until=time.time() + 1200)
