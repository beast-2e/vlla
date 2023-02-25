#!/usr/bin/python3

line = input()
words = []

try:
    while line is not None:
        line = line.split(sep='#')[0].strip()
        words += line.split()
        line = input()
except EOFError:
    pass

words = iter(words)

if next(words) != 'P3':
    raise RuntimeError('file is not PPM')

width = int(next(words))
height = int(next(words))
max = int(next(words))

if width != 60 and height != 32:
    raise NotImplementedError('sizes not equal to 160x32 not supported')

def read_half():
    buffer = [255]
    buffer += [int(int(next(words)) / max * 255) for i in range(0, 60 * 16 * 3)]
    return bytearray(buffer)

top = open('/dev/ttyACM0', 'wb')
top.write(read_half())
bottom = open('/dev/ttyACM1', 'wb')
bottom.write(read_half())
