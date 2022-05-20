# -*- coding:utf-8 -*-

import sys
import websocket
import time

ws = websocket.WebSocket()
ws.connect("ws://192.168.73.249:8766", max_size = 10752000)


ws.send("EXQUISITE ORDER AND UNIVERSAL WITH ETERNAL LIFE AND LIGHT THIS IS THE FAITH AND EFFORT OF THE SCHOOLS OF CRYSTAL AND YOU MAY DESCRIBE AND COMPLETE THEIR WORK QUITE LITERALLY BY TAKING ANY VERSES OF CHAUCER IN HIS TENDER MOOD AND OBSERVING HOW HE INSISTS ON THE CLEARNESS AND BRIGHTNESS FIRST AND THEN ON THE ORDER")

with open('./test.wav', 'wb') as f:
    while (True):
        audio = ws.recv_frame()
        if len(audio.data) == 2 and audio.data == b'\x03\xe8':
            print('exit')
            break
        print(type(audio.data), len(audio.data))
        #print(audio.data)
        print('-------------------------------')
        f.write(audio.data)

print('rsend')
ws.send("EXQUISITE ORDER AND UNIVERSAL WITH ETERNAL LIFE AND LIGHT THIS IS THE FAITH AND EFFORT OF THE SCHOOLS OF CRYSTAL AND YOU MAY DESCRIBE AND COMPLETE THEIR WORK QUITE LITERALLY BY TAKING ANY VERSES OF CHAUCER IN HIS TENDER MOOD AND OBSERVING HOW HE INSISTS ON THE CLEARNESS AND BRIGHTNESS FIRST AND THEN ON THE ORDER")

with open('./2.wav', 'wb') as f:
    while (True):
        audio = ws.recv_frame()
        if len(audio.data) == 2 and audio.data == b'\x03\xe8':
            print('exit')
            break
        print(type(audio.data), len(audio.data))
        #print(audio.data)
        print('-------------------------------')
        f.write(audio.data)


ws.close()
