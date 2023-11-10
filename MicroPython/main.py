"""
Created by: Ihor Chernyshev
Created on: Nov 2023
This program shows a while loop
"""

# import libraries
from microbit import *

# variables
loop_counter = 0
variable1 = 1

# setup
display.clear()
display.show(Image.HAPPY)

while True:
    # button A
    if button_a.was_pressed():
        loop_counter = 0
        display.clear()
        # goes from the upper left corner to lower right corner
        while loop_counter <= 5:
            sleep(500)
            display.set_pixel(loop_counter, loop_counter, 9)
            display.set_pixel(variable1, variable1, 0)
            loop_counter = loop_counter + 1
            variable1 = variable1 + 1
        display.show(Image.HAPPY)
    # button B
    if button_b.was_pressed():
        loop_counter = 5
        display.clear()
        # goes from the lower right corner to the upper left corner
        while loop_counter <= 5:
            sleep(500)
            display.set_pixel(loop_counter, loop_counter, 9)
            display.set_pixel(loop_counter + 1, loop_counter + 1, 0)
            loop_counter = loop_counter - 1
        display.show(Image.HAPPY)
