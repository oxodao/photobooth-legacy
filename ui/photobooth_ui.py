import pygame
import pygame.camera

from pygame.locals import *

from ui.frame_camera import *

class PhotoboothUI:

    def __init__(self, monitor_size: tuple, fullscreen: bool = True):
        self.monitor_size = monitor_size
        self.running = True
        self.current_frame = FrameCamera(monitor_size)
        self.fullscreen = fullscreen

    def init(self):
        pygame.init()
        pygame.camera.init()
        pygame.mouse.set_visible(False)
        self.display = pygame.display.set_mode(self.monitor_size)
        if self.fullscreen:
            pygame.display.toggle_fullscreen()

    def loop(self):
        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                    self.current_frame.quit()
                    self.running = False

            self.current_frame.render(self.display)
