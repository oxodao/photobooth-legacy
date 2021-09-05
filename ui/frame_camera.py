import pygame.camera
from input.consts import *
from .frame import Frame
from .flash import Flash
from .countdown import Countdown
from .camera import Camera

from ui.frame_display_picture import *

from utils.files import *

class FrameCamera(Frame):

    def __init__(self, pbui):
        super().__init__(pbui)

        self.camera = Camera()
        self.font = pygame.font.SysFont(None, 24)

        self.flash = Flash(pbui.size, 1000, lambda: self.take_picture(self.camera.get_raw_frame), 800)
        self.countdown = Countdown(self._pbui.size, 3000, self.flash.flash)

        self.filters = [self.countdown, self.flash]

    def render(self, display: pygame.display):
        scaled = self.camera.get_scaled_frame()

        for filter in self.filters:
            scaled = filter.render(scaled)

        self._frame.blit(scaled, (0, 0))
        super().render(display)

    def take_picture(self, picture):
        if callable(picture):
            picture = picture()

        pygame.image.save(picture, get_picture_file())
        self._pbui.set_frame(FrameDisplayPicture(self._pbui))

    def process_input(self, action: str):
        if action == KEYBIND_TAKE_SHOT:
            self.countdown.start()
        elif action == KEYBIND_MULTI_SHOT:
            self.flash.flash()

    def quit(self):
        self.camera.stop()


