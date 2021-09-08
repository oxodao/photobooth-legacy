from pygame.locals import *
from input.consts import *

class DesktopInputProcessor:

    def process(self, frame, key):
        if key == K_SPACE:
            frame.process_input(KEYBIND_TAKE_SHOT)
        elif key == K_s:
            frame.process_input(KEYBIND_MULTI_SHOT)
