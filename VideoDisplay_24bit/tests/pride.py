#!/usr/bin/python3

output = [255]

for i in range(0, 6):
    for j in range(0, 60):
        output += [64, 0, 0]
for i in range(0, 5):
    for j in range(0, 60):
        output += [64, 32, 0]
for i in range(0, 5):
    for j in range(0, 60):
        output += [64, 64, 0]

top_half = open('/dev/ttyACM0', 'wb')
top_half.write(bytes(output))

output = [255]

for i in range(0, 5):
    for j in range(0, 60):
        output += [0, 64, 0]
for i in range(0, 5):
    for j in range(0, 60):
        output += [0, 0, 64]
for i in range(0, 6):
    for j in range(0, 60):
        output += [64, 0, 64]

bottom_half = open('/dev/ttyACM1', 'wb')
bottom_half.write(bytes(output))
