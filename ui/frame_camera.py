import pygame.camera
from input.consts import *
from .frame import Frame
from .flash import Flash
from .countdown import Countdown

from ui.frame_display_picture import *

class FrameCamera(Frame):

    def __init__(self, pbui):
        super().__init__(pbui)
        pygame.camera.init()
        camlist = pygame.camera.list_cameras()

        self.flash = Flash(pbui.size, 1000, 800)
        self.countdown = None

        if camlist:
            self.cam = pygame.camera.Camera(camlist[0], self._pbui.size)
            self.cam.start()
            self.frame = pygame.surface.Surface(self._pbui.size, 0, self._pbui.size)
        else:
            self.cam = None


    def render(self, display: pygame.display):
        font = pygame.font.SysFont(None, 24)
        if self.countdown is None:
            self.countdown = Countdown(self._pbui.size, 3000, pygame.font.SysFont(None, 128))

        if self.cam is None:
            text = font.render('No camera detected', True, 0xFF0000FF)
            rect = text.get_rect(center=(self._pbui.size[0]/2, self._pbui.size[1]/2))
            self._frame.blit(text, rect)

        elif self.cam.query_image():
            picture = pygame.surface.Surface(self._pbui.size, 0, self._pbui.size)
            picture = self.cam.get_image(picture)
            if self.countdown is not None:
                picture = self.countdown.render(picture, self.take_picture)
            # @TODO: Find a way to make flash work w/ picture :)
            #picture = self.flash.render(picture, self.take_picture)

            self._frame.blit(picture, (0, 0))
        super().render(display)

    def take_picture(self):
        self._pbui.set_frame(FrameDisplayPicture(self._pbui))

    def process_input(self, action: str):
        if action == KEYBIND_TAKE_SHOT:
            print("Taking one shot")
            self.countdown.start()
        elif action == KEYBIND_MULTI_SHOT:
            print("Taking multi shot")
            self.flash.flash()

    def quit(self):
        if self.cam is not None:
            self.cam.stop()
