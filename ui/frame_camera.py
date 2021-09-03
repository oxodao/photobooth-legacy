import pygame.camera
from input.consts import *
from .frame import Frame

from ui.frame_display_picture import *

class FrameCamera(Frame):

    flashing_start: int
    flashing_duration: int

    def __init__(self, pbui):
        super().__init__(pbui)
        pygame.camera.init()
        camlist = pygame.camera.list_cameras()

        self.flashing = False
        self.flashing_duration = 1000

        if camlist:
            self.cam = pygame.camera.Camera(camlist[0], self._pbui.size)
            self.cam.start()
            self.frame = pygame.surface.Surface(self._pbui.size, 0, self._pbui.size)
        else:
            self.cam = None


    def render(self, display: pygame.display):
        font = pygame.font.SysFont(None, 24)

        if self.cam is None:
            text = font.render('No camera detected', True, 0xFF0000FF)
            rect = text.get_rect(center=(self._pbui.size[0]/2, self._pbui.size[1]/2))
            self._frame.blit(text, rect)

        elif self.cam.query_image():
            picture = pygame.surface.Surface(self._pbui.size, 0, self._pbui.size)
            picture = self.cam.get_image(picture)

            if self.flashing:
                flash = pygame.surface.Surface(self._pbui.size, pygame.SRCALPHA)
                flash.fill((255, 255, 255, 180))
                picture.blit(flash, (0, 0))

                now = pygame.time.get_ticks()
                if now - self.flashing_start >= self.flashing_duration:
                    self.flashing = False

            self._frame.blit(picture, (0, 0))
        super().render(display)

    def process_input(self, action: str):
        if action == KEYBIND_TAKE_SHOT:
            print("Taking one shot")
            self._pbui.set_frame(FrameDisplayPicture(self._pbui))
        elif action == KEYBIND_MULTI_SHOT:
            print("Taking multi shot")
            self.flashing = True
            self.flashing_start = pygame.time.get_ticks()

    def quit(self):
        if self.cam is not None:
            self.cam.stop()
