#!usr/bin/env python 

from sense_hat import SenseHat 
sense = SenseHat()

r =(255, 0, 0)
g =(0, 255, 0)
b =(0, 0, 255)
sense.clear()
pixels = [
    b, b, b, b, r, r, r, r,
    b, b, b, b, g, g, g, g,
    b, b, b, b, r, r, r, r,
    b, b, b, b, g, g, g, g,
    r, r, r, r, r, r, r, r,
    g, g, g, g, g, g, g, g,
    r, r, r, r, r, r, r, r,
    g, g, g, g, g, g, g, g,
]

sense.set_pixels(pixels)

