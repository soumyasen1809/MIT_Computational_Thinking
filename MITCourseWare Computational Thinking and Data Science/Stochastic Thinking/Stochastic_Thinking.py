# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec4.pdf

import random
import math

# Testing rolling a dice - Eg. 1
print ("--------------Eg. 1--------------")


def rollDice():
    return random.choice([1,2,3,4,5,6])


def testRoll(n):
    result = ''
    for i in range(n):
        result = result + str(rollDice()) + str("\t")
    print result


testRoll(10)


# Testing sample and actual probability - rolling 5 dices - Eg. 2
print ("\n")
print ("--------------Eg. 2--------------")


def runSim(test, ntrials):
    result = ''
    count = 0

    for i in range(ntrials):
        result = ''
        for j in range(len(test)):
            result = result + str(rollDice())
        if result == test:
            count = count + 1

    print ("Actual probability = " + str(1.0/(1.0*(6**len(test)))))
    print ("Sample probability = " + str(count/(1.0*ntrials)))
    return 0


print ("\n" + "Smaller number of trials")
runSim("11111", 1000)

print ("\n" + "Larger number of trials")
runSim("11111", 100000)


# Two People sharing the same birthday in a month- E.g. 3
print ("\n")
print ("--------------Eg. 3--------------")


def sameDate(num_people, ntrials):
    possible_dates = range(31)
    result = [0]*31

    count = 0
    for i in range(ntrials):
        count = 0
        for j in range(num_people):
            birthdate = random.choice(possible_dates)
            result[birthdate] = result[birthdate] + 1

        if max(result) >= 2:    # Finding if 2 people share a birthday. Change to 3 to find if 3 people share a birthday
            count = count + 1

    numerator = math.factorial(31)
    denominator = (31**num_people)*math.factorial(31-num_people)
    print ("Actual probability:" + str(1-(numerator/(1.0*denominator))) +"\n")
    print ("Sample probability:" + str(count/(1.0*ntrials)) +"\n")
    return 0


print ("\n" + "Less number of people: ")
sameDate(5, 10000)

print ("\n" + "More number of people: ")
sameDate(25, 10000)
