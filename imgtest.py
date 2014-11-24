from PIL import Image
from pylab import array

im1 = Image.new('RGBA', (500, 500), (255, 255, 255, 255))
im2 = Image.new('RGBA', (500, 500), (255, 0, 0, 255))

im1.show()
im2.show()

im3 = im1 - im2
im3.show()