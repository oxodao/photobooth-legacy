import pygame.camera
from input.consts import *
from .frame import Frame
from .flash import Flash
from .countdown import Countdown
from .camera import Camera

from ui.frame_display_picture import *

from utils.files import *

class FrameCamera(Frame):

    def __init__(self, pbui, root_surface):
        super().__init__(pbui, root_surface)

        self.camera = Camera()
        self.font = pygame.font.SysFont(None, 24)

        self.flash = Flash(pbui.size, 1000, lambda: self.take_picture(self.camera.get_raw_frame), 800)
        self.countdown = Countdown(pbui, 3, self.flash.flash)

        self.filters = [self.countdown, self.flash]

        self.somethings_happening = False

    def render(self):
        scaled = self.camera.get_scaled_frame()

        self._root_surface.blit(scaled, (0, 0))

        for filter in self.filters:
            filter.render(self._root_surface)


    def take_picture(self, picture):
        if callable(picture):
            picture = picture()

        last_taken_picture = get_picture_file()
        pygame.image.save(picture, last_taken_picture)
        self.somethings_happening = False
        self._pbui.set_frame(FrameDisplayPicture(self._pbui, self._root_surface, last_taken_picture))

    def process_input(self, action: str):
        if action == KEYBIND_TAKE_SHOT:
            self.somethings_happening = True
            self.countdown.start()
        elif action == KEYBIND_MULTI_SHOT:
            self.somethings_happening = True
            self.flash.flash()

    def quit(self):
        self.camera.stop()


