import pygame
import operator

class FpsCounter:
    def __init__(self, pbui, root_surface, clock):
        self._pbui = pbui
        self._root_surface = root_surface
        self._font = pygame.font.SysFont(None, 24)
        self._clock = clock
        self._offset = (20, 20)

    def render(self):
        text = self._font.render(f"{self._clock.get_fps():2.0f} FPS", 0, pygame.Color(255, 255, 255))
        rect = text.get_rect()

        rect[0] = self._offset[0]
        rect[1] = self._offset[1]

        pygame.draw.rect(self._root_surface, pygame.Color(0, 0, 0, 100), rect)
        self._root_surface.blit(text, self._offset)
