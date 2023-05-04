import board
import digitalio
import time

print("Running blink2.py")
print("blinks A0 and A1 pins")

# make an object with the pin

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

pulse1 = digitalio.DigitalInOut(board.A0)
pulse1.direction = digitalio.Direction.OUTPUT

pulse2 = digitalio.DigitalInOut(board.A1)
pulse2.direction = digitalio.Direction.OUTPUT

pause = 0.2  #seconds

while True:
    led.value = True
    pulse1.value = True

    time.sleep(pause)
    pulse2.value = False
    #time.sleep(0.005)

    led.value = False
    pulse1.value = False
    time.sleep(pause)
    pulse2.value = True


