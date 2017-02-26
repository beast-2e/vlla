# Usage:
# python high_frame_rate_socket.py
# while vlla-socket is running

import time
import random
import base64
import websocket

ws = websocket.WebSocket()
ws.connect("ws://127.0.0.1:8080", subprotocols=["echo-protocol"])

while True:
    for fps in [30, 60, 120, 240]:
        for i in range(3*fps):
            ws.send(base64.b64encode([255] + bytearray(map(lambda x: (fps-10 if ((x%60)+240*i/(fps))%20 < 10 else 0), range(60 * 16)))))
            time.sleep(1.0/fps)
    for fps in [30, 60, 120, 240]:
        for i in range(3*fps):
            ws.send(base64.b64encode([255] + bytearray(map(lambda x: (fps-10 if i%2==0 else 0), range(60 * 16)))))
            time.sleep(1.0/fps)
    for fps in [30, 60, 120, 240]:
        for i in range(3*fps):
            ws.send(base64.b64encode([255] + bytearray(map(lambda x: random.randrange(0, 255), range(60 * 16)))))
            time.sleep(1.0/fps)
