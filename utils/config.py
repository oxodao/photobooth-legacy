RESOLUTION = (960, 540)
CAMERA_RESOLUTION = (1280, 720)
REFRESH_TIMEOUT = 50

FRAME_BORDERS = (120, 120, 120, 120)

def get_frame_borders_scaled(original_frame_size):
    ratioX = RESOLUTION[0] / original_frame_size[0]
    ratioY =  RESOLUTION[1] / original_frame_size[1]

    return (
        int(FRAME_BORDERS[0] * ratioX),
        int(FRAME_BORDERS[1] * ratioY),
        int(FRAME_BORDERS[2] * ratioX),
        int(FRAME_BORDERS[3] * ratioY)
    )
