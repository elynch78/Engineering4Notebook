# Engineering_4_Notebook


## Table of Contents
* [Pico Intro](#Pico_Intro)
* [Launchpad 1-Countdown](#Launchpad_1-Countdown)
* [Launchpad 2-LED](#Launchpad_2-LED)
* [Launchpad 3-Button](#Launchpad_3-Button)
* [Launchpad 4-Servo](#Launchpad_4-Servo)


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

![Link to proof](images/countdown.gif)

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




