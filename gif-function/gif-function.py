import numpy as np
from PIL import Image

def open_gif_image(path):
    img = Image.open(path).convert('RGB')

    # get dimensions of image
    dimensions = img.size

    # height, width, number of channels in image
    height = dimensions[0]
    width = dimensions[1]
    channels = len(img.getbands())

    # Print Information
    print(f"Image Height: {height}; Width: {width}; Channels: {channels}")
    return np.array(img)

print(open_gif_image("alo.gif"))