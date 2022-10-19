import board
import digitalio
import time #imports

MORSE_CODE = { 'A':'.-', 'B':'-...',  #dictionary, goes on top
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ',':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    ' ': '/',
    '(':'-.--.', ')':'-.--.-'}

modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier  #timing of flashes
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier

led1 = digitalio.DigitalInOut(board.GP13)
led1.direction = digitalio.Direction.OUTPUT #led setup

mouse1 = input("Mouse code set 1 (x,y)")  #input
mouse1 = mouse1.upper() #make things uppercase

cheese = " " #total strings

for letter in mouse1: # use MORSE_CODE[letter] here to translate from input into morse code
   cheese = cheese + (MORSE_CODE[letter]) + " " #stacks letters

print(cheese) #write it

for letter in cheese: #sets up spaces bwteen instances
    if letter == ".": #for dots
        led1.value = True #led turns on
        time.sleep(dot_time) #sleeps for the set time for dots
        led1.value = False #led is off

    if letter == "-": #now for dashes
        led1.value = True #led on
        time.sleep(dash_time) #dash sleep time
        led1.value = False #led off

    if letter == " ": #for spaces
        time.sleep(between_letters)  #rest for set space time between letters

    if letter == "/":  #for spaces between words which show as dashes
        time.sleep(between_words) #rest between words for set time

    
    time.sleep(dot_time) #stop led between uses of the code


