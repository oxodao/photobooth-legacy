import pygame

class Countdown:
    def __init__(self, size: tuple, duration: int, font):
        self.size = size
        self.font = font
        self.countdown = False
        self.countdown_start = 0
        self.duration = duration
        self.processed_callback = False

        self.last_count = int(duration/1000)
        self.build_surface(self.last_count)

    def start(self):
        if not self.countdown:
            self.countdown = True
            self.countdown_start = pygame.time.get_ticks()
            self.processed_callback = False

    def render(self, surface, callback):
        if self.countdown:
            surface.blit(self.surface, (0, 0))

            diff = pygame.time.get_ticks() - self.countdown_start
            if self.countdown and diff >= self.duration+999: # We don't want 0 to display so.. 999 (:
                self.countdown = False
                callback()

            diff_seconds = int(diff/1000)
            if self.last_count is not diff_seconds:
                self.build_surface((self.duration/1000 - diff_seconds))

        return surface

    def build_surface(self, seconds):
        surface = pygame.surface.Surface(self.size, pygame.SRCALPHA, self.size)

        txt = self.font.render(str(int(seconds)), True, (255, 255, 255))
        rect = txt.get_rect(center=(self.size[0]/2, self.size[1]/2))
        surface.blit(txt, rect)

        self.surface = surface
