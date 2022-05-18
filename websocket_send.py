# -*- coding:utf-8 -*-

import sys
import websocket
import time

ws = websocket.WebSocket()
ws.connect("ws://localhost:8766", max_size = 10752000)

# asr result
#ws.send("Hello world test")
##txtAnswer = ws.recv_frame()
#time.sleep(2)
#
#with open(sys.argv[1], 'rb') as f:
#    while True:
#        content = f.read(3200)
#        if not content:
#            break
#        ws.send_binary(content)
#
#ws.send(' ')
#
#print("receive....")
#txtAnswer = ws.recv_frame()
#print( websocket.ABNF.OPCODE_MAP[txtAnswer.opcode])
##tmp = unicode(txtAnswer.data,'utf-8').encode('gbk')
#print(txtAnswer.data.decode("utf-8"))


# tts result
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
    #print( websocket.ABNF.OPCODE_MAP[audio.opcode])
#tmp = str(audio.data,'utf-8')
#print(tmp)
        print(type(audio.data), len(audio.data))
        print('-------------------------------')
        f.write(audio.data)


ws.close()
