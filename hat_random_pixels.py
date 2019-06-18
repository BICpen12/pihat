#!usr/bin/env python 

from sense_hat import SenseHat 
sense = SenseHat()
import time 
import random


while True:
    sense.clear()
    x = random.randint(0, 7)
    y = random.randint(0, 7)   
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    sense.set_pixel(x, y, (red, green, blue))
    time.sleep(1)

