import time    #importing stuff
import board
import digitalio
import pwmio 
from adafruit_motor import servo

led1 = digitalio.DigitalInOut(board.GP13)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP18)
led2.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP16)  #what stuff is going in vs out and where it's at
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
pwm_servo = pwmio.PWMOut(board.GP5, duty_cycle=2 ** 15, frequency=50)  #setting up servo
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

while True: 
     if button.value == False:    #so when we aren't pressing it anymore
          for x in reversed(range(11)):
               led1.value = True
               time.sleep(0.5)     #rest a sec between counts
               print(x)
               led1.value = False
               time.sleep(0.5)
          while True:
               print("liftoff!")     #say liftoff
               led2.value = True
               servo1.angle = 180     #turn180
               time.sleep(0.5)