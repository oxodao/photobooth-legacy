import os
import ui.photobooth_ui as ui
from pathlib import Path

from dotenv import load_dotenv

def main():
    load_dotenv()

    if os.environ.get('PICTURE_PATH') is None:
        print('Please set the PICTURE_PATH env var!')
        quit()

    Path(os.environ.get('PICTURE_PATH')).mkdir(parents=True, exist_ok=True)

    pb_ui = ui.PhotoboothUI((1280,720), False)
    pb_ui.init()
    pb_ui.loop()

if __name__ == '__main__':
    main()
