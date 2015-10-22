import sys
path = "/Projects/webhook/"

if path not in sys.path:
    sys.path.insert(0, path)

from receiver import app
application = app
