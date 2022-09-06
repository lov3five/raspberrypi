import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
INPUT_PIN = 4
GPIO.setup(INPUT_PIN, GPIO.IN)

try: 
    while True:
        if GPIO.input(4):
            print("I'm reading TRUE on GPIO {INPUT_PIN}")
        else:
            print("I'm reading FALSE on GPIO {INPUT_PIN}")
        time.sleep(1)
finally:
    print("Cleaning up...")
    GPIO.cleanup()
