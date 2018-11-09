# Usage:
# python high_frame_rate_8bit.py > /dev/ttyACM1

print bytearray([255]+map(lambda x: 0, range(60 * 16 * 3)))
