import RPi.GPIO as GPIO
import Adafruit_DHT #library of sensor DHT

GPIO.setmode(GPIO.BCM)
RED_LED_PIN = 17 #GPIO = 11 BOARD
GREEN_LED_PIN = 27 #GPIO = 13 BOARD
YELLOW_LED_PIN = 22 #GPIO = 15 BOARD

GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4 #GPIO = 7 BOARD
while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if temperature > 27:
        GPIO.output(GREEN_LED_PIN, GPIO.LOW)
        GPIO.output(YELLOW_LED_PIN, GPIO.LOW)
        GPIO.output(RED_LED_PIN, GPIO.HIGH)
        print("Temp={0:0.1f}*C =>> RED turn on")
    elif temperature <= 27 and temperature >= 20:
        GPIO.output(GREEN_LED_PIN, GPIO.LOW)
        GPIO.output(RED_LED_PIN, GPIO.LOW)
        GPIO.output(YELLOW_LED_PIN, GPIO.HIGH)
        print("Temp={0:0.1f}*C =>> YELLOW turn on")
    elif temperature < 20:
        GPIO.output(RED_LED_PIN, GPIO.LOW)
        GPIO.output(YELLOW_LED_PIN, GPIO.LOW)
        GPIO.output(GREEN_LED_PIN, GPIO.HIGH)
        print("Temp={0:0.1f}*C =>> GREEN turn on")
