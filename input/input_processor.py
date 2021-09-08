from input.consts import is_raspberrypi
from input.desktop import DesktopInputProcessor

if is_raspberrypi():
    from input.rpi import RaspberryInputProcessor

import pygame

class InputProcessor:
    def __init__(self):
        self._desktop_processor = DesktopInputProcessor()

        if is_raspberrypi():
            self._rpi_processor = RaspberryInputProcessor()

    def process(self, events, frame):
        # Desktop
        for e in events:
            if e.type == pygame.locals.KEYDOWN:
                self._desktop_processor.process(frame, e.key)

        # Raspberry pi
        if is_raspberrypi():
            self._rpi_processor.process(frame)
