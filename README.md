# Engineering_4_Notebook


## Table of Contents
* [Pico Intro](#Pico_Intro)
* [Launchpad 1-Countdown](#Launchpad_1-Countdown)
* [Launchpad 2-LED](#Launchpad_2-LED)
* [Launchpad 3-Button](#Launchpad_3-Button)
* [Launchpad 4-Servo](#Launchpad_4-Servo)
* [Crash Avoidance P1](#Crash_Avoidance_P1)
* [Crash Avoidance P2](#Crash_Avoidance_P2)
* [Crash Avoidance P3](#Crash_Avoidance_P3)
* [Landing Area P1](#Landing_Area_P1)

## Pico_Intro

### Assignment Description

I had to get my pico to blink it's led. 

### Evidence 

![Link to proof](images/IMG-4190.MOV)

### Code

``` python
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)

```

### Reflection

This was really easy because I did it after doing all the harder assignments . 

## Launchpad_1-Countdown

### Assignment Description

I worked with Gaby to code a 10 second countdown on Python that tells you to launch when the count ends. This will be useful for our final project. 

### Evidence 

![Link to proof](images/Untitled.mp4)

### Code

``` python
import time
for x in range (10,0,-1):  #counting range for timer
    print(x)
    time.sleep (1)  #rest 1 sec between each number
print("LAUNCHY")   #say dis

```

### Reflection

This was a relatively simple assignment, we learned how to use range through [this](https://www.w3schools.com/python/gloss_python_for_range.asp) which makes the countdown work. The time.sleep makes it so there is space between the countdown of numbers. 


## Launchpad_2-LED

### Assignment Description

Today Gaby and I created code to make a red light flash as the serial monitor counts down from ten and then flashes a red light when the word 'launch' is printed. This will be useful later in the year if we need LEDs for our project or something that functions similarly either through code or practice. 


### Evidence

![Link to proof](images/ledgif.mp4)


### Wiring

<img src="images/L2LED.jpg" alt="" width="200" height="200" />


### Code

``` python

import time #Imports variables
import board
import digitalio 

led1 = digitalio.DigitalInOut(board.GP13) #where the stuff is at
led1.direction = digitalio.Direction.OUTPUT #gives direcction
led2 = digitalio.DigitalInOut(board.GP18) 
led2.direction = digitalio.Direction.OUTPUT 

for x in reversed(range(11)): 
    led1.value = True #turns light on
    time.sleep(0.5) #wait time
    print(x) #tells it what to say
    led1.value = False #turns led off
    time.sleep(0.5) 
while True:
    print("liftoff!") #what to say
    led2.value = True #turns red light on
    time.sleep(0.5) #hits snooze
 
 ```

### Reflection

I had trouble figuring out the positioning of the code because one led has to be later on becasue it depends on the countdown being finished vs happening at the same time. Originally our red led was not working and we thought it was the code, but the problem was actually that we had misidentified our leds so it's important to label things because it makes things more organized and easier to use or understand later on. 



## Launchpad_3-Button

### Assignment Description

Today Gaby and I created code so that our countdown and leds will start at the press of a button. (To mimic a more realistic countdown sequence)


### Evidence

![Link to proof](images/buttongif.mp4)

### Wiring

<img src="images/L3BUTTON.jpeg" alt="" width="250" height="250" />


### Code

``` python

import time #imports
import board
import digitalio

led1 = digitalio.DigitalInOut(board.GP13) #pins 
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP18)
led2.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP16) #adds in the button
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP #incorperates the button into the circuit

while True: #if the button is pressed this will happen
     if button.value == False:
          for x in reversed(range(11)):
               led1.value = True #light bright
               time.sleep(0.5) #light snooze
               print(x)
               led1.value = False #light off
               time.sleep(0.5)
          while True:
               print("liftoff!") #says dis
               led2.value = True
               time.sleep(0.5)
 
 ```

### Reflection

Alright, so as someone with very limited experience and liking for coding, this took a lot of questions and thinking. I was still just adding on to my previous code, but I have never used a button, much less coded for it so that was new. First off, I didn't know where to put the new code (again). I had to add "if button.value == False:" and then tab everything over a bunch under it. This makes it so that once you press the button everything else follows. 



## Launchpad_4-Servo

### Assignment Description

Today Gaby and I had to add on to our countdown code again so that a servo will turn 180 degrees at the end of the ciruit and mimic the liftoff. 

### Evidence

![Link to proof](images/IMG-4190.MOV)

### Wiring

<img src="images/servo.jpeg" alt="" width="250" height="250" />

### Code

``` python
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

servo1.angle = 0


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
              
```

### Reflection

The servo code was given in the assignment, and you just had to add it on to the end of the While True so the assigment went pretty smoothly. We were in the wrong pin because Gaby thought that the 7th pin down was GP7, but it was actually GP5 so once we had that figured out the servo worked and we were done. 

## Crash_Avoidance_P1

### Assignment Description

I had to get an accelerometer working and print acceleration, gyro, and temperature values in the terminal. 

### Evidence 

![](images/P1.gif)

### Code

``` python
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
```

### Reflection

This was fairly simple, once we had the right libraries moved into our circuitpy, we used the code from the assignment we were basically there.  


## Crash_Avoidance_P2

### Assignment Description

I had to get an accelerometer working so that when it was 90 degrees an led would turn on.  

### Evidence 

![](images/CA2.gif)

### Code

``` python
import board  #import stuff
import adafruit_mpu6050
import busio 
import time
import digitalio 

led_1 = digitalio.DigitalInOut(board.GP18)   #led setup
led_1.direction = digitalio.Direction.OUTPUT
sda_pin = board.GP14   #setup pico
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)


while True:
    print(mpu.acceleration)   #say the values
    time.sleep(.5)

    if mpu.acceleration[0] < -9 or mpu.acceleration[0] > 9:
        led_1.value = True  #at 90 degrees led is on

    else:
        led_1.value = False  #if not led is off
```

### Reflection

The code was confusing for this but Max helped us so it was fine. I had the wrong setup for 90 degree acceleration values but after that was fixed the thing worked smoothly. 


## Crash_Avoidance_P3

### Assignment Description

I had to get my led to blink at 90 degrees and print gyro xyz values onto a screen as well. 

### Evidence 

![](images/CA3.gif)

### Code

``` python
import board  #import shit
import adafruit_mpu6050
import busio 
import time
import digitalio 
import terminalio
import displayio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

displayio.release_displays()
sda_pin = board.GP14   #setup pico
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP28)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
led_red = digitalio.DigitalInOut(board.GP18)   #led setup
led_red.direction = digitalio.Direction.OUTPUT

mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68) #accelerometer


while True:
    print(mpu.acceleration)   #say the values
    time.sleep(.5)
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
    splash = displayio.Group()  #create the display group

    title = "ANGULAR VELOCITY" #add title block to display group
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
    splash.append(text_area) 

    title = f"x: {mpu.gyro[0]}" 
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=15)
    splash.append(text_area)  
    
    title = f"y: {mpu.gyro[0]}" 
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=30)
    splash.append(text_area) 

    title = f"z: {mpu.gyro[0]}" 
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=45)
    splash.append(text_area)


    display.show(splash) #send display group to screen
    if mpu.acceleration[0] < -9 or mpu.acceleration[0] > 9:
        led_red.value = True  #at 90 degrees led is on

    else:
        led_red.value = False  #if not led is off

```

### Reflection

The setup for the accelerometer and the screen was pretty straightforward but the code for the xyz values had me confused for a bit. Once I figured out how to do the code for x values to show up on the screen, I was able to set up the y and z values right after. 


## Landing_Area_P1

### Assignment Description

I had to get my serial monitor to take my chosen coordinates of a triangl and tell me the area.  

### Evidence 

![](images/gif3.gif)

### Code

``` python
import math
def tri_area(x1, y1, x2, y2, x3, y3):
    niceAreaValue = (abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))/2
    print(f"The area of the triangle with vertices ({x1}, {y1}), ({x2}, {y2}), ({x3}, {y3}) is {niceAreaValue}")
while True:
    try:
        txt1 = input("Input coord set 1 (x,y)")
        set1 = txt1.split(",")

        a1 = float(set1[0])
        b1 = float(set1[1])

        txt2 = input("Input coord set 2 (x,y)")
        set2 = txt2.split(",")

        a2 = float(set2[0])
        b2 = float(set2[1])

        txt3 = input("Input coord set 3 (x,y)")
        set3 = txt3.split(",")

        a3 = float(set3[0])
        b3 = float(set3[1])

        tri_area(a1, b1, a2, b2, a3, b3)
    except:
        print("Please input valid coordinates (remember format x,y)")

```

### Reflection



