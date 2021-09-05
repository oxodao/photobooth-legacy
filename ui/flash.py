import pygame

class Flash:
    def __init__(self, size: tuple, duration: int, callback, duration_callback: int):
        self._flashing = False
        self._flashing_start = 0
        self._duration = duration

        self._callback = callback
        self._duration_callback = duration_callback
        self._processed_callback = False

        self._flash_surface = pygame.surface.Surface(size, pygame.SRCALPHA)
        self._flash_surface.fill((255, 255, 255, 180))

    def flash(self):
        if not self._flashing:
            self._flashing = True
            self._flashing_start = pygame.time.get_ticks()
            self._processed_callback = False

    def render(self, surface):
        if self._flashing:
            surface.blit(self._flash_surface, (0, 0))

            diff = pygame.time.get_ticks() - self._flashing_start
            if not self._processed_callback and self._duration < diff >= self._duration_callback: 
                self._callback()
                self._processed_callback = True
            elif diff >= self._duration:
                self._flashing = False

        return surface
