"""
Created by: Ihor Chernyshev
Created on: Nov 2023
This program shows a while loop
"""

# import libraries
from microbit import *

# variables
loop_counter = 0

# setup
display.show(Image.HAPPY)
display.clear()

while True:
    # button A
    if button_a.was_pressed():
        loop_counter = 0
        display.clear()
        # goes from the upper left corner to lower right corner
        while loop_counter <= 5:
            sleep(500)
            display.set_pixel(loop_counter, loop_counter, 9)
            loop_counter = loop_counter + 1
        display.show(Image.HAPPY)
    # button B
    if button_b.was_pressed():
        loop_counter = 5
        display.clear()
        # goes from the lower right corner to the upper left corner
        while loop_counter <= 5:
            sleep(500)
            display.set_pixel(loop_counter, loop_counter, 9)
            loop_counter = loop_counter - 1
        display.show(Image.HAPPY)
