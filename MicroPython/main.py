"""
Created by: Ihor Chernyshev
Created on: Nov 2023
This program shows a while loop
"""

from microbit import *

loop_counter = 0

display.show(Image.HAPPY)
display.clear()

while True:
    if button_a.was_pressed():
        loop_counter = 0
        display.clear()
        while loop_counter <= 5:
            sleep(500)
            display.set_pixel(loop_counter, loop_counter, 9)
            loop_counter = loop_counter + 1
        display.show(Image.HAPPY)
    if button_b.was_pressed():
        loop_counter = 5
        display.clear()
        while loop_counter <= 5:
            sleep(500)
            display.set_pixel(loop_counter, loop_counter, 9)
            loop_counter = loop_counter - 1
        display.show(Image.HAPPY)
