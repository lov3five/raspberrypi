""" 
    *Update*
    sudo apt-get update
    sudo apt-get install build-essential python-dev

    * clone the Adafruit library *
    git clone https://github.com/adafruit/Adafruit_Python_DHT.git
    cd Adafruit_Python_DHT

    *  install the library for Python 2 and Python 3 *
    sudo python setup.py install
    sudo python3 setup.py install
"""
import RPi.GPIO as GPIO
import Adafruit_DHT

GPIO.setmode(GPIO.BCM)

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4 #GPIO4
while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C    Humidity={1:0.1f}%".format(temperature,humidity))
    else:
        print("Error!!! WARNING DATA FROM SENSOR")
