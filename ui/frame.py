import pygame

class Frame:
    def __init__(self, pbui):
        self._pbui = pbui
        self._frame = pygame.surface.Surface(pbui.size, 0, pbui.size)

    def render(self, display: pygame.display):
        display.blit(self._frame, (0, 0))
        pygame.display.flip()
