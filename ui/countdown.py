import pygame

class TimedSurface:
    def __init__(self, font, size, number):
        self.number = number

        self._txt = font.render(str(int(number)), True, (255, 255, 255))
        self._rect = self._txt.get_rect(center=(size[0]/2, size[1]/2))

    def render(self, root_surface):
        root_surface.blit(self._txt, self._rect)

class Countdown:
    def __init__(self, pbui, duration: int, callback):
        self.pbui = pbui
        self.font = pygame.font.SysFont(None, 128)

        self.countdown = False
        self.countdown_start = 0
        self.duration = duration

        self._callback = callback
        self.processed_callback = False

        self._last_action_tick = 0

    def start(self):
        if not self.countdown:
            self.countdown = True
            self._last_action_tick = self.pbui._clock.tick()
            self.processed_callback = False
            self.remaining = self.duration
            self.surface = TimedSurface(self.font, self.pbui.size, self.remaining)

    def render(self, root_surface):
        if self.countdown:
            self._last_action_tick += self.pbui.tick()

            if self._last_action_tick >= 500: # Not real seconds but meh
                self.remaining -= 1
                self._last_action_tick = 0
                if self.remaining == 0:
                    self.countdown = False
                    self._callback()
                    self.processed_callback = True
                else:
                    self.surface = TimedSurface(self.font, self.pbui.size, self.remaining)

            self.surface.render(root_surface)

