import pygame

class Flash:
    def __init__(self, size: tuple, duration: int, duration_callback: int):
        self.flashing = False
        self.flashing_start = 0
        self.duration = duration
        self.duration_callback = duration_callback
        self.processed_callback = False
        self.flash_surface = pygame.surface.Surface(size, pygame.SRCALPHA)
        self.flash_surface.fill((255, 255, 255, 180))


    def flash(self):
        if not self.flashing:
            self.flashing = True
            self.flashing_start = pygame.time.get_ticks()
            self.processed_callback = False

    def render(self, surface, callback):
        if self.flashing:
            surface.blit(self.flash_surface, (0, 0))

            diff = pygame.time.get_ticks() - self.flashing_start
            if not self.processed_callback and self.duration < diff >= self.duration_callback: 
                callback()
                self.processed_callback = True
            elif diff >= self.duration:
                self.flashing = False

        return surface
