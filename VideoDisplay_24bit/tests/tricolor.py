#!/usr/bin/python3

import sys

output = b'\xff'

for i in range(0, 16):
    for j in range(0, 20):
        output += b'\x40\x00\x00'
    for j in range(0, 20):
        output += b'\x40\x40\x40'
    for j in range(0, 20):
        output += b'\x00\x00\x40'

sys.stdout.buffer.write(output)
