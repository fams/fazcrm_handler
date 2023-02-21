import sys
from sources.explorer import Explorer

GOOGLE_DRIVE_PATH = r"G:\Meu Drive"

e = Explorer(GOOGLE_DRIVE_PATH)

if len(sys.argv) > 1:
    url = sys.argv[1]
    relative_path = url.replace("fazcrm://", "")
    e.open(relative_path)