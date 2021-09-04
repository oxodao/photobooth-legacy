import ui.photobooth_ui as ui

def main():
    pb_ui = ui.PhotoboothUI((1280,720), False)
    pb_ui.init()
    pb_ui.loop()

if __name__ == '__main__':
    main()
