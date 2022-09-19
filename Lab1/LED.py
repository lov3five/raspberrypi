from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
RED_LED_PIN = 17 #GPIO = 11 BOARD
GREEN_LED_PIN = 27 #GPIO = 13 BOARD
YELLOW_LED_PIN = 22 #GPIO = 15 BOARD

GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# Hàm lighWithTime(LED_PIN, time) dùng để phát sáng đèn trong thời gian time (s) => LED_PIN chân đèn, time tính bằng giây
def lightWithTime(LED_PIN, time):
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(time)
    GPIO.output(LED_PIN, GPIO.LOW)

while True:
    lightWithTime(RED_LED_PIN, 5)
    print("RED turn on")
    lightWithTime(YELLOW_LED_PIN, 3)
    print("YELLOW turn on")
    lightWithTime(GREEN_LED_PIN, 8)
    print("GREEN turn on")