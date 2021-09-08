import pygame
from .frame import Frame

class FrameDisplayPicture(Frame):
    def __init__(self, pbui, root_surface, picture_path):
        super().__init__(pbui, root_surface)

        self.shown_at = pygame.time.get_ticks()
        self.timeout = 3000
        self.exited = False

        self.picture_path = picture_path

        self.frame_picture = pygame.image.load(r'assets/frame.png')
        self.frame_picture = pygame.transform.smoothscale(self.frame_picture, pbui.size)
        self.last_picture = pygame.image.load(picture_path)

    def render(self):

        self._root_surface.blit(self.last_picture, (0, 0))
        self._root_surface.blit(self.frame_picture, (0, 0))

        now = pygame.time.get_ticks()
        if now - self.shown_at >= self.timeout and self.exited is False:
            self._pbui.set_frame(self._pbui.camera_frame)
            self.exited = True

    def process_input(self, action: str):
        return

    def quit(self):
        return
