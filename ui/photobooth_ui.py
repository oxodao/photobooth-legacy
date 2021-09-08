import pygame
import pygame.camera
from input.input_processor import InputProcessor

from pygame.locals import *
from ui.frame_camera import *
from ui.fps_counter import *
from input.consts import *

from utils.config import RESOLUTION

class PhotoboothUI:

    def __init__(self, fullscreen: bool = True):
        self.size = RESOLUTION
        self.fullscreen = fullscreen

        pygame.init()
        pygame.mouse.set_visible(False)

        self.screen = pygame.display.set_mode(self.size)
        if self.fullscreen:
            pygame.display.toggle_fullscreen()

        self.running = True
        self.camera_frame = FrameCamera(self, self.screen)
        self.current_frame = self.camera_frame

        self._clock = pygame.time.Clock()
        self._show_fps = False
        self._fps_frame = FpsCounter(self, self.screen, self._clock)

        self.input_processor = InputProcessor()

    def loop(self):
        while self.running:
            events = []
            for e in pygame.event.get():
                if e.type == pygame.QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE) or (e.type == KEYDOWN and e.key == K_q):
                    self.current_frame.quit()
                    self.running = False
                elif e.type == KEYDOWN and e.key == K_f:
                    self._show_fps = not self._show_fps
                elif e.type == KEYDOWN:
                    events.append(e)

            self.input_processor.process(events, self.current_frame)

            self.current_frame.render()

            if self._show_fps:
                self._fps_frame.render()

            pygame.display.flip()
            self.tick()


    def set_frame(self, frame):
        if frame is not None:
            self.current_frame = frame

    def tick(self):
        return self._clock.tick(30)
