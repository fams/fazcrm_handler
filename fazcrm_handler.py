import sys
import os
from sources.explorer import Explorer


e = Explorer(r"G:\Meu Drive")

if len(sys.argv) > 1:
    url = sys.argv[1]
    relative_path = url.replace("fazapp://", "")
    e.open(relative_path)