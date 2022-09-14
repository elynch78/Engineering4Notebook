import time
time.sleep 
import board
import digitalio

while(True):
    led = digitalio.DigitalInOut(board.LED)