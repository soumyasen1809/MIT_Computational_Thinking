# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec7.pdf

import numpy as np
from matplotlib import pyplot as plt
import random


def gaussian(x, mu, sigma):
    fac1 = (1.0/(sigma*((2.0*np.pi)**0.5)))
    fac2 = np.e**(-(((x-mu)**2)/(2.0*sigma**2)))
    return fac1*fac2


mu, sigma = 0.0, 1.0
x = np.linspace(-4.0,4.0,200)
y = gaussian(x, mu, sigma)
plt.plot(x,y)
plt.show()


# Central Limit Theorem
def rollDice(numDices, ntrials):
    mean_val = []
    for i in range(ntrials):
        val = 0
        for j in range(numDices):
            val = val + random.random()
        mean_val.append(val)

    plt.hist(mean_val, bins=1000)
    plt.show()
    return 0

numDices = 50
ntrials = 10000
rollDice(numDices,ntrials)


# Simulating Buffon Laplace Method - Calculate pi value
def throwNeedle(num_needles):
    count_needles = 0
    for i in range(num_needles):
        x = random.random()
        y = random.random()

        if x*x + y*y <= 1.0:
            count_needles = count_needles + 1

    return 4.0 * count_needles / (1.0 * num_needles)


def simPi(ntrials, num_needles):
    pi_est = []
    for i in range(ntrials):
        pi_est.append(throwNeedle(num_needles))

    plt.hist(pi_est,bins=1000)
    plt.show()
    return pi_est


simPi(10000, 1000)
