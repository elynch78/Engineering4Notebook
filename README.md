# Engineering_4_Notebook


## Table of Contents
* [Launchpad 1-Countdown](#Launchpad_1-Countdown)
* [Launchpad 2-LED](#Launchpad_2-LED)
* [Launchpad 3-Button](#Launchpad_3-Button)

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

<img src="images/L3BUTTON.jpeg" alt="" width="200" height="200" />


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


