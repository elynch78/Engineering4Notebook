import time #imports stuff
import board
import adafruit_mpu6050
import busio

sda_pin = board.GP14  #sets up i2c
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)  #sets up accelerometer
mpu = adafruit_mpu6050.MPU6050(i2c)
led1 = digitalio.DigitalInOut(board.GP13)  #sets up led
led1.direction = digitalio.Direction.OUTPUT

while True:
    if mpu.acceleration[0]:
        led.value = True
    if mpu.acceleration[1]:
        led.value = True

        