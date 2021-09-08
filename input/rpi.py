from input.consts import *

import RPi.GPIO as GPIO

INPUT_TAKE_ONE = 3

class RaspberryInputProcessor:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(INPUT_TAKE_ONE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def process(self, frame):
        if GPIO.input(INPUT_TAKE_ONE):
            print("PRESSING TAKE ONE KEY")
