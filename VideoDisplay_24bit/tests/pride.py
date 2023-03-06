#!/usr/bin/python3

output = [255]

for i in range(0, 6):
    for j in range(0, 60):
        output += [24, 0, 0]
for i in range(0, 5):
    for j in range(0, 60):
        output += [24, 12, 0]
for i in range(0, 5):
    for j in range(0, 60):
        output += [24, 24, 0]

top_half = open('/dev/ttyACM0', 'wb')
top_half.write(bytes(output))
top_half.flush()

output = [255]

for i in range(0, 5):
    for j in range(0, 60):
        output += [0, 24, 0]
for i in range(0, 5):
    for j in range(0, 60):
        output += [0, 0, 24]
for i in range(0, 6):
    for j in range(0, 60):
        output += [24, 0, 24]

bottom_half = open('/dev/ttyACM1', 'wb')
bottom_half.write(bytes(output))
bottom_half.flush()
