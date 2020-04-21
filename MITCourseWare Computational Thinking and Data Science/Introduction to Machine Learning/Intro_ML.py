# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec11.pdf
import numpy as np


def Manhattan_Distance(X1, X2):
    dist = 0
    for i in range(len(X1)):
        dist = dist + abs(X1[i] - X2[i])**2
    return dist**0.5


class animal(object):
    def __init__(self, name, features):
        self.name = name
        self.features = np.array(features)

    def getName(self):
        return self.name

    def getFeatures(self):
        return self.features

    def getDistance(self, other):
        return Manhattan_Distance(self.getFeatures(), other.getFeatures())

    def __str__(self):
        return "Animal Class - Reptilian"


def comparisonTable(animals):
    rowval, colval, tableval = [], [], []
    for i in animals:
        rowval.append(i.getName())
        colval.append(i.getName())
    print rowval

    for i in animals:
        row = []
        for j in animals:
            if i == j:
                row.append('----')
            else:
                dist = i.getDistance(j)
                row.append(dist)

        print (row)
        tableval.append(row)

    return tableval

print ("Manhattan Distance \n")
rattlesnake = animal('rattlesnake', [1,1,1,1,0])
boa = animal('boa constrictor', [0,1,0,1,0])
dartFrog = animal('dart frog', [1,0,1,0,4])
animal_list = [rattlesnake, boa, dartFrog]
table_val = comparisonTable(animal_list)
