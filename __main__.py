import os
import ui.photobooth_ui as ui
from pathlib import Path

from dotenv import load_dotenv

def main():
    load_dotenv()

    picturePath = os.environ.get('PICTURE_PATH')
    if picturePath is None:
        print('Please set the PICTURE_PATH env var!')
        quit()

    Path(picturePath).mkdir(parents=True, exist_ok=True)

    pb_ui = ui.PhotoboothUI(False)
    pb_ui.loop()

if __name__ == '__main__':
    main()
