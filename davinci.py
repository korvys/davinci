from PIL import Image, ImageDraw
import random

class Poly:
	def __init__(self):
		self.point1 = (random.randint(0, 500), random.randint(0, 500))
		self.point2 = (random.randint(0, 500), random.randint(0, 500))
		self.point3 = (random.randint(0, 500), random.randint(0, 500))
		self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

class Solution:
	def __init__(self):
		self.polys = []

	def random(self, size=25):
		for i in xrange(0, size):
			self.polys.append(Poly())


background = Image.new('RGBA', (500, 500), (0, 0, 255, 0))

sol = Solution()
sol.random()
print(len(sol.polys))


for poly in sol.polys:
	imgpoly = Image.new('RGBA', (500, 500), (0, 0, 255, 0))
	ImageDraw.ImageDraw(imgpoly).polygon([poly.point1, poly.point2, poly.point3], fill=poly.color)
	background = Image.alpha_composite(background, imgpoly)

background.save('out.png')

