from PIL import Image, ImageDraw
import random
import numpy as np
from operator import attrgetter

class Poly:
    def __init__(self):
        self.point1 = (random.randint(0, 500), random.randint(0, 500))
        self.point2 = (random.randint(0, 500), random.randint(0, 500))
        self.point3 = (random.randint(0, 500), random.randint(0, 500))
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


class Solution:
    def __init__(self):
        self.polys = []
        self.fitness = 0

    def random(self, size=25):
        for i in range(0, size):
            self.polys.append(Poly())

    def build(self):
        background = Image.new('RGBA', (500, 500), (0, 0, 255, 0))

        for poly in self.polys:
            imgpoly = Image.new('RGBA', (500, 500), (0, 0, 255, 0))
            ImageDraw.ImageDraw(imgpoly).polygon([poly.point1, poly.point2, poly.point3], fill=poly.color)
            background = Image.alpha_composite(background, imgpoly)

        return background

    def mutate(self):
        for i in range(len(self.polys)):
            if random.random() < 0.01:
                self.polys[i] = Poly()

def breed(parent1, parent2):
    temppolys = []
    temppolys.extend(parent1.polys)
    temppolys.extend(parent2.polys)
    child = Solution()
    child.polys = random.sample(temppolys, 25)
    child.mutate()
    return child

def fitness(target, sol):
    solimg = sol.build()

    im = np.array(solimg) - np.array(target)
    im = np.absolute(im)

    s = im.sum(axis=0).sum(axis=0).sum(axis=0)

    return s


def main():

    generation = 0
    target = Image.open('kitten.jpg').convert(mode='RGBA')

    population = []
    for x in range(100):
        sol = Solution()
        sol.random()
        sol.fitness = fitness(target, sol)
        population.append(sol)



    while(1):
        generation += 1

        breeders = random.sample(population, 40)
        children = []
        for i in range(0, 40, 2):
            child = breed(breeders[i], breeders[i+1])
            child.fitness = fitness(target, child)
            children.append(child)

        population.extend(children)
        population = sorted(population, key=attrgetter('fitness'))
        population = population[:100]
        print(population[0].fitness)
        print(population[99].fitness)

main()
