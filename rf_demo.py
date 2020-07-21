import time
from machine import Pin

def rfSwitch(channels='A', sysCode='', on=True, pinNb=17):
    frame = [0 for _ in range(0, 128)]
    frame[128-32] = 1

    txPin = Pin(pinNb, Pin.OUT)
    sendframe = ''

    for i in range(1,6):
        if str(i) in sysCode:
            sendframe += '0'
        else:
            sendframe += 'F'
            
    for i in range(6,10):
        if chr(i + 59) in channels.upper():
            sendframe += '0'
        else:
            sendframe += 'F'

    sendframe += 'F'
            
    if on:
        sendframe += '0F'
    else:
        sendframe += 'F0'

    print(sendframe)

    for i, b in enumerate(sendframe):
        idx = i * 8
        if b == '0':
            for j, n in enumerate([1,0,0,0,1,0,0,0]):
                frame[idx + j] = n
            
        elif b == 'F':
            for j, n in enumerate([1,0,0,0,1,1,1,0]):
                frame[idx + j] = n

    for _ in range(0,6):
        for i, s in enumerate(frame):
            start = time.ticks_us()
            now = 0
            while now < 370:
                now = time.ticks_diff(time.ticks_us(), start)
            if s:
                txPin.on()
                
            else:
                txPin.off()
            start = time.ticks_us()


