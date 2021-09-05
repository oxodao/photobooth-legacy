import pygame 

from utils.config import RESOLUTION

class Camera:
    def __init__(self):
        pygame.camera.init()
        self._font = pygame.font.SysFont(None, 24)
        self._camera_resolution = (1280, 720)

        self._no_camera_surface = build_no_camera_surface(self._font, self._camera_resolution)
        self._camPicture = pygame.surface.Surface(self._camera_resolution)
        self._scaledPicture = None

        camlist = pygame.camera.list_cameras()

        if camlist:
            self._cam = pygame.camera.Camera(camlist[0], self._camera_resolution)
            self._cam.start()
        else:
            self._cam = None

        self._last_frame = None
        self._last_scaled_frame = None

    def get_raw_frame(self):
        if self._cam is None:
            return self._no_camera_surface
        else:
            self.fetch_cam_frame()
            return self._last_frame

    def get_scaled_frame(self):
        if self._cam is None:
            return self._no_camera_surface

        # Should be done in order to create the scaled version
        self.get_raw_frame()

        # Let pywright be happy
        if self._last_scaled_frame is None:
            return self._no_camera_surface

        return self._last_scaled_frame.copy()

    # @TODO: Do not fetch cam every frame, add a framerate
    def fetch_cam_frame(self):
        if self._cam is not None and self._cam.query_image():
            self._last_frame = pygame.surface.Surface(self._camera_resolution)
            self._last_frame = self._cam.get_image(self._camPicture)
            self._last_scaled_frame = pygame.transform.scale(self._last_frame, RESOLUTION)

    def stop(self):
        if self._cam is not None:
            self._cam.stop()

def build_no_camera_surface(font, resolution: tuple):
    surface = pygame.surface.Surface(resolution)
    text = font.render('No camera detected', True, 0xFF0000FF)
    rect = text.get_rect(center=(resolution[0]/2, resolution[1]/2))
    surface.blit(text, rect)

    return surface

