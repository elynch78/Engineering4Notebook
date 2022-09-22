import time #imports stuff
import board
import adafruit_mpu6050
import busio

sda_pin = board.GP14  #sets up i2c
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)  #sets up accelerometer
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))  #things serial monitor needs to read
    print("Temperature: %.2f C" % mpu.temperature)
    print("")
    time.sleep(1)