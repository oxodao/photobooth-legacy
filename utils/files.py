import os
from datetime import datetime

def get_picture_file():
    path = os.environ.get('PICTURE_PATH')
    if not path.endswith('/'):
        path += '/'

    path += "{}.jpg"

    date = datetime.now()
    return path.format(date.strftime("%Y%m%d-%H%M%S.%f"))
