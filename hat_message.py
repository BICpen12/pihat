#!usr/bin/env python3

#needs to run on python3 
from sense_hat import SenseHat 
sense = SenseHat()

color= (255, 0, 0)
speed = 0.05


x = input('Enter your name: ') #imput allows for input from user
message = ('Hello, ' + str (x) ) #str converts x into a string 
print (message) 
sense.show_message(message, speed, text_colour=color) #tells sense.show_message what variables you need 


