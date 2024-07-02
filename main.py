import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from window import Window

win = Window(800, 600)
win.wait_for_close()