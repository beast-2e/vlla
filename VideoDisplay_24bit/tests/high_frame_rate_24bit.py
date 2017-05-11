# Usage:
# python high_frame_rate_8bit.py > /dev/ttyACM1

import time
import random

fpscolor = [
    [255, 250, 0],
    [255, 150, 0],
    [255, 0, 150],
    [150, 0, 255]
]
while True:
    for f, fps in enumerate([30, 60, 120, 240]):
        for i in range(3*fps):
            print bytearray([255]+map(lambda x: (fpscolor[f][x%3] if (((x/3)%60)+240*i/(fps))%20 < 10 else 0), range(60 * 16 * 3)))
            time.sleep(1.0/fps)
    for f, fps in enumerate([30, 60, 120, 240]):
        for i in range(3*fps):
            print bytearray([255]+map(lambda x: (fpscolor[f][x%3] if i%2==0 else 0), range(60 * 16 * 3)))
            time.sleep(1.0/fps)
    for f, fps in enumerate([30, 60, 120, 240]):
        for i in range(3*fps):
            print bytearray([255]+map(lambda x: (fpscolor[f][x%3] if (1.0*x/3/16/60) < 1.0*i/(3*fps) else 0), range(60 * 16 * 3)))
            time.sleep(1.0/fps)

#    for fps in [30, 60, 120, 240]:
#        for i in range(3*fps):
#            print bytearray([255]+map(lambda x: random.randrange(0, 255), range(60 * 16 * 3)))
#            time.sleep(1.0/fps)
