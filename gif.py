import sys

from PIL import Image

im = []

for arg in sys.argv[1:]:
    ims = Image.open(arg)
    im.append(ims)

im[0].save("coustome.gif", save_all = True, append_im=[im[1]], duration = 200, loop = 0)