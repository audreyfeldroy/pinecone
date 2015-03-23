# -*- coding: utf-8 -*-
import atexit

from PIL import Image, ImageDraw

im = None
draw = None

def size(width, height):
    global im
    global draw
    im = Image.new(mode="RGB", size=(width, height))
    draw = ImageDraw.Draw(im)
    return im

def ellipse(x, y, w, h):
    x0 = x - w / 2
    y0 = y - h / 2
    x1 = x + w / 2
    y1 = y + h / 2
    draw.ellipse(xy=[x0, y0, x1, y1], fill=(126, 243, 21))

def show_in_ipynb():
    """ Display a PIL Image in IPython Notebook. Requires an IPython Notebook
        instance. """
    try:
        get_ipython().magic('matplotlib inline')
        import numpy as np
        from matplotlib.pyplot import imshow
        imshow(np.asarray(im))
    except Exception:
        print("Couldn't get IPython Notebook instance")

def exit_handler():
    global im
    im.show()

atexit.register(exit_handler)
