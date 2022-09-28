import board  #import shit
import adafruit_mpu6050
import busio 
import time
import digitalio 
import terminalio
import displayio

displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x68, reset=board.GP28)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
from adafruit_display_text import label
import adafruit_displayio_ssd1306
led_red = digitalio.DigitalInOut(board.GP18)   #led setup
led_red.direction = digitalio.Direction.OUTPUT
sda_pin = board.GP14   #setup pico
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x3d) #screen


while True:
    print(mpu.acceleration)   #say the values
    time.sleep(.5)

    if mpu.acceleration[0] < -9 or mpu.acceleration[0] > 9:
        led_red.value = True  #at 90 degrees led is on

    else:
        led_red.value = False  #if not led is off