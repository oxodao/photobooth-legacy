from pygame.locals import *
from input.consts import *

def process_input(frame, key):
    if key == K_SPACE:
        frame.process_input(KEYBIND_TAKE_SHOT)
    elif key == K_s:
        frame.process_input(KEYBIND_MULTI_SHOT)
