# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec5.pdf

import random
from matplotlib import pyplot as plt


class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delx, dely):
        return Location(self.x + delx, self.y + dely)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        return ((self.x - other.getX())**2 + (self.y - other.getY())**2)**0.5

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"


class Drunk(object):
    def __init__(self, name):
        self.name = name

    def takeSteps(self):
        stepchoices = [(1,0), (-1,0), (0,1), (0,-1)]
        return random.choice(stepchoices)

    def __str__(self):
        return self.name


class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError("Drunk already present in Field")
        else:
            self.drunks[drunk] = loc

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not in Field")
        else:
            return self.drunks[drunk]

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not in Field")
        else:
            x_dist, y_dist = drunk.takeSteps()
            self.drunks[drunk] = self.drunks[drunk].move(x_dist, y_dist)


def Walk(f, d, numsteps):
    start_pos = f.getLoc(d)
    for i in range(numsteps):
        f.moveDrunk(d)
    end_pos = f.getLoc(d)
    return start_pos.distFrom(end_pos)


def simWalk(numsteps, ntrials):
    start = Location(0,0)
    distances = []
    drunk_person = Drunk("Robert")   # name of the drunk person in Robert

    for i in range(ntrials):
        f = Field()
        f.addDrunk(drunk_person, start)
        distances.append(Walk(f, drunk_person, numsteps))

    print ("\t Mean distance covered: " + str(sum(distances)/ (1.0* len(distances))))
    print ("\t Maximum distance covered: " + str(max(distances)))
    print ("\t Minimum distance covered: " + str(min(distances)))
    return distances


print ("\n Simulating walk for less number of steps")
dist_low = simWalk(10,100)

print ("\n Simulating walk for large number of steps")
dist_high = simWalk(1000,100)

plt.plot(dist_low)
plt.plot(dist_high)
plt.show()
