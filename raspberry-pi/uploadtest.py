import time
import board
import digitalio

led1 = digitalio.DigitalInOut(board.GP13)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP18)
led2.direction = digitalio.Direction.OUTPUT

for x in reversed(range(11)):
    led1.value = True
    time.sleep(0.5)
    print(x)
    led1.value = False
    time.sleep(0.5)
while True:
    print("liftoff!")
    led2.value = True
    time.sleep(0.5)