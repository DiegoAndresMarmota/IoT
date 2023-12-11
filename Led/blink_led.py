import RPi.GPIO as GPIO
import time

# The code snippet is setting up a loop that will repeatedly turn on and off a GPIO pin on a Raspberry
# Pi.
def is_turn_on_led(*args, **kwargs) -> None:
try:
    while true:
        GPIO.output(18, GPIO.HIGH)
        time.sleep(2)
        print("Led ON")
        GPIO.output(18, GPIO.LOW)
        time.sleep(2)
except KeyboardInterrupt:
    print("Led OFF switch manual")
    GPIO.cleanup()
finally:
    time.sleep(1)
    GPIO.output(18, GPIO.LOW)
    print("Led OFF")
    GPIO.cleanup()