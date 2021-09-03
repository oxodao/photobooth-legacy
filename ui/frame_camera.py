import pygame.camera

class FrameCamera:

    def __init__(self, size: tuple):
        self.size = size

        pygame.camera.init()
        camlist = pygame.camera.list_cameras()

        if camlist:
            self.cam = pygame.camera.Camera(camlist[0], self.size)
            self.cam.start()
            self.snapshot = pygame.surface.Surface(self.size, 0, self.size)
        else:
            self.cam = None


    def render(self, display: pygame.display):
        font = pygame.font.SysFont(None, 24)

        if self.cam is None:
            self.snapshot = font.render('No camera detected', True, 0xFF0000FF)
            rect = self.snapshot.get_rect(center=(self.size[0]/2, self.size[1]/2))
            display.blit(self.snapshot, rect)
        elif self.cam.query_image():
            self.snapshot = self.cam.get_image(self.snapshot)
            display.blit(self.snapshot, (0, 0))

        pygame.display.flip()

    def quit(self):
        if self.cam is not None:
            self.cam.stop()
