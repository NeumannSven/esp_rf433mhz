
import time
import utime
from machine import Pin

i = 0
now = 0
start = time.ticks_us()

def irqhandler(pin):
    global i, frame, now, start
    
    now = time.ticks_diff(time.ticks_us(), start)
    start = time.ticks_us()

    if i > 400:
        i = 0
    i += 1
    frame[i] = pin.value()


frame = [0 for _ in range(0,300)]
rxPin = Pin(16, Pin.PULL_DOWN)
rxPin.irq(irqhandler, Pin.IRQ_FALLING)




def finddata():
    for i, p in enumerate(frame):
        if p and not any(frame[i+1:i+32]):
            print("sync", i)
            if i > 95:
                for j in range(i-96,i,8):
                    print(frame[j:j+8])

#for _ in range(20):
#    for i in range(0,300):
        #start = time.ticks_us()
        #now = 0
        #while now < 370:
        #    now = time.ticks_diff(time.ticks_us(), start)
        #    start = time.ticks_us()
#        utime.sleep_us(360)
#        if rxPin.value():
#            frame[i] = 1
#        else:
#            frame[i] = 0


#    finddata()

while True:
    if now >= 400*31:
        print("sync signal")
        print(frame)
