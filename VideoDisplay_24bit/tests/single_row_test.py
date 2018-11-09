# Usage:
# python high_frame_rate_8bit.py > /dev/ttyACM1
print bytearray([255]+sum([([200,0,0] if pixel%120==0 else [100,50,0] if pixel%120<59 else [0,200,0] if pixel%120==59 else [0,200,200] if pixel%120==60 else [0,0,100] if pixel%120<119 else [200,0,200]) for pixel in range(0,32*60)],[]))
