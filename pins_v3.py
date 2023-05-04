#pins_v3.py

# Configure A0 = input with pullup.
# Configure D4 = output.

# Connect external switch.1 to A0 input. Switch.2 is grounded.
# Route D4 input (inside the RP2040) to A0 output.
# Observe A0 output: switch open = 3.3V, switch closed = 0V.

import board
import digitalio
import time

print("Running pins_v3.py")
print("switch is input to D4 input and read at A0 output")
print()

# set led ON to indicate program is running
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

# set up pin_d4 as input, with pullup
pin_d4 = digitalio.DigitalInOut(board.D4)
pin_d4.direction = digitalio.Direction.INPUT
pin_d4.pull = digitalio.Pull.UP

# set up pin_a0 as output
pin_a0 = digitalio.DigitalInOut(board.A0)
pin_a0.direction = digitalio.Direction.OUTPUT

input_value = pin_d4.value
print("pin_d4 =", input_value)

pin_a0.value = input_value

while True:
    
    input_value = pin_d4.value
    time.sleep(0.01)  #debounce input
    pin_a0.value = input_value
        
    





