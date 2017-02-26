# Usage:
# python high_frame_rate_8bit.py > /dev/ttyACM1

import time
import random

while True:
    for fps in [30, 60, 120, 240]:
        for i in range(3*fps):
            print bytearray(map(lambda x: (fps-10 if ((x%60)+240*i/(fps))%20 < 10 else 0), range(60 * 16)))
            time.sleep(1.0/fps)
    for fps in [30, 60, 120, 240]:
        for i in range(3*fps):
            print bytearray(map(lambda x: (fps-10 if i%2==0 else 0), range(60 * 16)))
            time.sleep(1.0/fps)
    for fps in [30, 60, 120, 240]:
        for i in range(3*fps):
            print bytearray(map(lambda x: random.randrange(0, 255), range(60 * 16)))
            time.sleep(1.0/fps)
