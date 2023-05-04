#pins_v1.py

# Initialize 4 pins as outputs: a0, a1, a2, a3
# Change the values of these pins and observe with a DVM

import board
import digitalio

print("Running pins.py")
print("tests pins")
print()

# set led ON to indicate program is running
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

print("this code tests pins A0, A1, A2, A3")

pin_a0 = digitalio.DigitalInOut(board.A0)
pin_a0.direction = digitalio.Direction.OUTPUT

pin_a1 = digitalio.DigitalInOut(board.A1)
pin_a1.direction = digitalio.Direction.OUTPUT

pin_a2 = digitalio.DigitalInOut(board.A2)
pin_a2.direction = digitalio.Direction.OUTPUT

pin_a3 = digitalio.DigitalInOut(board.A3)
pin_a3.direction = digitalio.Direction.OUTPUT

test_value = True

while True:
    pin_a0.value = test_value
    pin_a1.value = test_value
    pin_a2.value = test_value
    pin_a3.value = test_value






