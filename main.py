import random
import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


# population with particles
class Knapsack:
    def __init__(self, data):  # [ (value,weight) ]
        self.data = data

    def value(self, index):
        return self.data[index][0]

    def weight(self, index):
        return self.data[index][1]


class Particle:  # represent one bit
    def __init__(self):
        self.position = random.randint(0, 1)
        self.bestPosition = self.position
        self.velocity = 0

    def move(self):
        self.position = self.position ^ self.velocity


class Swarm:  # search space
    def __init__(self, knapsackList, weightLimit):
        self.particles = [Particle() for _ in range(len(knapsackList))]
        self.globalBestPositions = [x.position for x in self.particles]
        self.globalBestValue = 0
        self.knapsack = Knapsack(knapsackList)
        self.weightLimit = weightLimit

    def fitness(self):
        # check weight first
        if sum([self.knapsack.weight(x) for x in range(len(self.particles))
                if self.particles[x].position == 1]) > self.weightLimit:
            return 0
        else:
            return sum([self.knapsack.value(x) for x in range(len(self.particles))
                        if self.particles[x].position == 1])

    def setGlobalAndPersonalBest(self):
        fitness = self.fitness()
        if fitness == 0:
            return
        else:
            if fitness > self.globalBestValue:
                self.globalBestValue = fitness
                self.globalBestPositions = [x.position for x in self.particles]
                for particle in self.particles:
                    particle.bestPosition = particle.position

    def move(self):
        for i,particle in enumerate(self.particles):
            velocity = sigmoid(particle.velocity +
                               2.5 * random.random() * (particle.bestPosition - particle.position) +
                               2.5 * random.random() *
                               (self.globalBestPositions[i]-particle.position))
            if random.random() < velocity:
                particle.velocity = 1
            else:
                particle.velocity = 0
            particle.move()