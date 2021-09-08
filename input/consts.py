KEYBIND_GALLERY = 'GALLERY'
KEYBIND_TAKE_SHOT = 'TAKE_SHOT'
KEYBIND_MULTI_SHOT = 'TAKE_MULTI_SHOT'

import io

# Thing that checks if it is running on a RPi
# https://raspberrypi.stackexchange.com/questions/5100/detect-that-a-python-program-is-running-on-the-pi
def is_raspberrypi():
    try:
        with io.open('/sys/firmware/devicetree/base/model', 'r') as m:
            if 'raspberry pi' in m.read().lower(): return True

    except Exception: pass

    return False
