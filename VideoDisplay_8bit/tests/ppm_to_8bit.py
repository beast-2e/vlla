# Usage:
# python ppm_to_8bit.py > /dev/ttyACM1

import fileinput

linecount = 0
maxcolor = 256
currentbyte = 0
allbytes = []

for line in fileinput.input():
    if line[0] == "#":
        continue
    elif linecount < 2:
        pass
        #print line,linecount
    elif linecount == 2:
        maxcolor = int(line)
    elif (linecount % 3 == 0): # Red
        #print "red"
        #print line, linecount
        currentbyte = 0
        currentbyte |= int(8*int(line)/maxcolor) << 5
    elif (linecount % 3 == 1): # Green
        #print "green"
        currentbyte |= int(8*int(line)/maxcolor) << 2 
    elif (linecount % 3 == 2): # Blue
        #print "blue"
        currentbyte |= int(4*int(line)/maxcolor)
        #print currentbyte
        allbytes.append(currentbyte)
    linecount += 1

print bytearray(allbytes)
