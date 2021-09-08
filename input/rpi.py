from input.consts import *

import RPi.GPIO as GPIO

LEFT_GALLERY = 11
RIGHT_TAKE_ONE = 11
BACK_MULTI_SHOT = 15

class RaspberryInputProcessor:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(LEFT_GALLERY, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(RIGHT_TAKE_ONE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(BACK_MULTI_SHOT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def process(self, frame):
        if GPIO.input(LEFT_GALLERY):
            frame.process_input(KEYBIND_GALLERY)
        if GPIO.input(RIGHT_TAKE_ONE):
            frame.process_input(KEYBIND_TAKE_SHOT)
        if GPIO.input(BACK_MULTI_SHOT):
            frame.process_input(KEYBIND_MULTI_SHOT)

