import pygame
import pygame.camera
import input.desktop

from pygame.locals import *
from ui.frame_camera import *
from input.consts import *

from utils.config import RESOLUTION

if is_raspberrypi():
    import input.rpi

class PhotoboothUI:

    def __init__(self, fullscreen: bool = True):
        self.size = RESOLUTION
        self.fullscreen = fullscreen

        pygame.init()
        pygame.mouse.set_visible(False)
        self.display = pygame.display.set_mode(self.size)
        if self.fullscreen:
            pygame.display.toggle_fullscreen()

        self.running = True
        self.camera_frame = FrameCamera(self)
        self.current_frame = self.camera_frame

    def loop(self):
        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE) or (e.type == KEYDOWN and e.key == K_q):
                    self.current_frame.quit()
                    self.running = False
                elif e.type == KEYDOWN:
                    input.desktop.process_input(self.current_frame, e.key)
                    if is_raspberrypi():
                        input.rpi.process_input(self.current_frame, None)

            self.current_frame.render(self.display)

    def set_frame(self, frame):
        self.current_frame = frame
