import sys
from sources.explorer import Explorer
import logging

logging.basicConfig(filename="C:\\src\\fazcrm_handler\\log.txt",
                    level=logging.ERROR)

GOOGLE_DRIVE_PATH = r"G:\Meu Drive"

e = Explorer(GOOGLE_DRIVE_PATH)
if len(sys.argv) > 1:
    url = sys.argv[1]
    relative_path = url.replace("fazcrm://", "").rstrip("/")
    logging.debug("Open File {}".format(relative_path))
    e.open(relative_path)
