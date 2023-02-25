import time
import vlla

canvas = vlla.Canvas()
green = vlla.Color(g=0x7f)

#while True:
for row in range(0, vlla.HEIGHT):
    for col in range(0, vlla.WIDTH):
        start = time.time()
        canvas.set_pixel(row, col, green)
        canvas.flush()
        canvas.clear()
        end = time.time()
        time.sleep(0.05 - (end - start))
