import RPi.GPIO as GPIO
import time

def is_turn_on_led(*args, **kwargs) -> None:
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.output(17, GPIO.HIGH)
        print("Led ON")
        time.sleep(2)
        GPIO.output(17, GPIO.LOW)
        time.sleep(2)
    except KeyboardInterrupt:
        GPIO.output(17, GPIO.LOW)
        print("Led OFF switch manual")
        GPIO.cleanup()
    finally:
        print("Led OFF")
        time.sleep(1)
        GPIO.cleanup()
    