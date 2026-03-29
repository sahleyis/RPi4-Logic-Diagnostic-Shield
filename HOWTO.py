import RPi.GPIO as GPIO
import time

# Pin definitions from the shield schematic
# These are the BCM pin numbers for the 4 LEDs
led_pins = [17, 27, 22, 23]

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW) # Start with all LEDs off

try:
    while True:
        # Scan Forward: LED 1 -> 2 -> 3 -> 4
        for pin in led_pins:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.1) # Change this number to speed up or slow down
            GPIO.output(pin, GPIO.LOW)
            
        # Scan Backward: LED 3 -> 2 (skip 4 and 1 to prevent double-blink at ends)
        for pin in reversed(led_pins[1:3]):
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(pin, GPIO.LOW)

except KeyboardInterrupt:
    # Cleanup pins on exit
    GPIO.cleanup()


# run the command python HOWTO.py in the terminal to run it
