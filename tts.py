# -*- coding:utf-8 -*-

import sys
import websocket
import time

ws = websocket.WebSocket()
ws.connect("ws://192.168.73.249:8766", max_size = 10752000)

ws.send("Hello world test")
'''
audio = ws.recv_frame()
print(audio)
'''
with open('./test.mp3', 'wb') as f:
    while (True):
        audio = ws.recv_frame()
        if len(audio.data) == 2 and audio.data == b'\x03\xe8':
            print('exit')
            break
        print(type(audio.data), len(audio.data))
        print('-------------------------------')
        f.write(audio.data)


ws.close()
