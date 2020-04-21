# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec10.pdf
import numpy as np
import random
from matplotlib import pyplot as plt


class TempData(object):
    def __init__(self, line):
        info = line.split(",")
        self.high = float(info[1])
        self.year = int(info[2][0:4])

    def getHigh(self):
        return self.high

    def getYear(self):
        return self.year

    def __str__(self):
        return "US temperature dataset"


def readData():
    inFile = open('temperatures.csv')
    data = []
    for line in inFile:
        data.append(TempData(line))
    inFile.close()
    return data


def getMean(data):
    years = {}
    for i in data:
        try:
            years[i.getYear()].append(i.getHigh())
        except:
            years[i.getYear()] = [i.getHigh()]

    for j in years:
        years[j] = sum(years[j])/len(years[j])

    return years


def splitData(x_val,y_val):
    x_train, y_train, x_test, y_test = [], [], [], []
    toTrain = random.sample(range(len(x_val)), len(x_val)/2)

    for i in range(len(x_val)):
        if i in toTrain:
            x_train.append(x_val[i])
            y_train.append(y_val[i])
        else:
            x_test.append(x_val[i])
            y_test.append(y_val[i])

    return x_train, y_train, x_test, y_test


data = readData()
years = getMean(data)
x = []
y = []

for i in years:
    x.append(i)
    y.append(years[i])

plt.plot(x,y, "ro")
plt.title("Actual data set")
plt.show()

x_train, y_train, x_test, y_test = splitData(x,y)
model = np.polyfit(x_train, y_train, 3)     # Change the last argument to 2, 3, 4, .... for different order polynomials
test_model = np.polyval(model, x_test)

plt.plot(x_test, test_model)
plt.plot(x_test, y_test, "ro")
plt.title("Plot showing the actual test points and the fitted model")
plt.show()
