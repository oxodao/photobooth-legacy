import pygame
from .frame import Frame

class FrameDisplayPicture(Frame):
    def __init__(self, pbui, root_surface, picture_path):
        super().__init__(pbui, root_surface)

        self.shown_at = pygame.time.get_ticks()
        self.timeout = 3000
        self.exited = False

        self.picture_path = picture_path

    def render(self, display: pygame.display):
        font = pygame.font.SysFont(None, 24)

        pict_surface = pygame.surface.Surface(self._pbui.size)
        pict_surface.fill((0, 0, 0))

        pict_surface = font.render('Display the picture/video', True, 0xFFFF00FF)

        rect = pict_surface.get_rect(center=(self._pbui.size[0]/2, self._pbui.size[1]/2))
        self._root_surface.blit(pict_surface, rect)

        now = pygame.time.get_ticks()
        if now - self.shown_at >= self.timeout and self.exited is False:
            self._pbui.set_frame(self._pbui.camera_frame)
            self.exited = True

    def process_input(self, action: str):
        return

    def quit(self):
        return
