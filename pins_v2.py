#pins_v2.py

# Connect 4 output pins to 4 input pins. Verify that output values are
# read correctly on the inputs.
#   A0 -> D4
#   A1 -> D6
#   A2 -> D24
#   A3 -> D25

import board
import digitalio

print("Running pins.py")
print("tests pins")
print()

# set led ON to indicate program is running
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

print("this code tests output pins driving input pins")
print("A0 -> D4")
print("A1 -> D6")
print("A2 -> D24")
print("A3 -> D25")
print()

# set up output pins pin_a0, pin_a1, pin_a2, pin_a3

pin_a0 = digitalio.DigitalInOut(board.A0)
pin_a0.direction = digitalio.Direction.OUTPUT

pin_a1 = digitalio.DigitalInOut(board.A1)
pin_a1.direction = digitalio.Direction.OUTPUT

pin_a2 = digitalio.DigitalInOut(board.A2)
pin_a2.direction = digitalio.Direction.OUTPUT

pin_a3 = digitalio.DigitalInOut(board.A3)
pin_a3.direction = digitalio.Direction.OUTPUT

# set up input pins pin_d4

pin_d4 = digitalio.DigitalInOut(board.D4)
pin_d4.direction = digitalio.Direction.INPUT

pin_d6 = digitalio.DigitalInOut(board.D6)
pin_d6.direction = digitalio.Direction.INPUT

pin_d24 = digitalio.DigitalInOut(board.D24)
pin_d24.direction = digitalio.Direction.INPUT

pin_d25 = digitalio.DigitalInOut(board.D25)
pin_d25.direction = digitalio.Direction.INPUT


print("Setting oupt test_value to 0111\n")

pin_a0.value = 0
pin_a1.value = 1
pin_a2.value = 1
pin_a3.value = 1

d4_in = pin_d4.value
d6_in = pin_d6.value
d24_in = pin_d24.value
d25_in = pin_d25.value

print("input pin values")
print("pin_d4 ",d4_in)
print("pin_d6 ",d6_in)
print("pin_d24 ",d24_in)
print("pin_d25 ",d25_in)

"""
# print output nibble, then input nibble
print("output = ", pin_a3.value, pin_a2.value, pin_a1.value, pin_a0.value)
print("input = ", d25_in, d24_in, d6_in, d4_in)
"""

while True:
    pass


