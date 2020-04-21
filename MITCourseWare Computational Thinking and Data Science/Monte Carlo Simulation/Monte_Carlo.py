# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec6.pdf

import random
import numpy as np


class Roulette(object):
    def __init__(self):
        self.pockets = []
        for i in range(1, 37):
            self.pockets.append(i)
        self.ball = 0
        self.pocketOdds = len(self.pockets) - 1

    def spin(self):
        self.ball = random.choice(self.pockets)

    def amountPocket(self, amt, betted_pocket):
        if str(self.ball) == str(betted_pocket):
            return amt * self.pocketOdds
        else:
            return -amt

    def __str__(self):
        return "Setting Roulette"


def playSim(game, num_spins, betted_pocket, amt):
    totalPocket = 0
    totalPocketval = []
    for i in range(num_spins):
        game.spin()
        totalPocket = totalPocket + game.amountPocket(amt, betted_pocket)
        totalPocketval.append(totalPocket/(1.0*num_spins))

    # print ("\n Total pocket amount is: " + str(totalPocket))
    print ("\t Sample Probability is: " + str((100*totalPocket)/(1.0*num_spins)) + "%")
    return totalPocketval


def Mean_and_StdDev(x):
    mean_val = sum(x)/(1.0*len(x))
    tot = 0.0
    for i in x:
        tot = tot + (i - mean_val) ** 2
    std = (tot / len(x)) ** 0.5
    return mean_val, std


game = Roulette()

print ("\n Simulation with less number of spins")
returnpocket = playSim(game, 100, 7, 1)
mean, std = Mean_and_StdDev(returnpocket)
print ("\t Mean: " + str(mean) + " +/- " + str(100*1.96*std) + " with 95% confidence")

print ("\n Simulation with high number of spins")
returnpocket = playSim(game, 1000000, 7, 1)
mean, std = Mean_and_StdDev(returnpocket)
print ("\t Mean: " + str(mean) + " +/- " + str(100*1.96*std) + " with 95% confidence")
