# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec9.pdf

import random
import numpy as np
from matplotlib import pyplot as plt


def readFile(fileName):
    file = open(fileName, 'r')
    x_val = []
    y_val = []
    file.readline()
    for line in file:
        x, y = line.split()
        x_val.append(float(x))
        y_val.append(float(y))
    file.close()
    return x_val, y_val


def avgMeanSquareError(y_data, y_est):
    error = 0.0
    for i in range(len(y_data)):
        error = error + (y_est[i] - y_data[i])**2
    return error/(1.0*len(y_data))


def R2_fit(y_data, y_est):
    num = ((y_data - y_est)**2).sum()
    mean_val = sum(y_data)/(1.0*len(y_data))
    den = ((y_data - mean_val)**2).sum()
    R2 = 1 - (num/(1.0*den))
    return R2


# Linear Fit
print ("\n Spring Data")
x, y = readFile("springData2.txt")
x = np.array(x)
y = np.array(y)
y = y * 9.81

coeff = np.polyfit(x,y,1)
# y_est = coeff[0]*x + coeff[1] # y = ax + b
y_est = np.polyval(coeff, x)    # polyval computes at particular values of x (computes ax + b at given values of x)
plt.plot(x, y_est)              # Plotting the fitted line
plt.plot(x,y, 'ro')             # Plotting the points
plt.show()

print ("\t Spring constant: " + str(coeff[0]))

error_val = avgMeanSquareError(y, y_est)
print ("\t Average mean square error: " + str(error_val))

R2_val = R2_fit(y, y_est)
print ("\t The fit of the data (R2): " + str(R2_val))


# Quadratic fit
print("\n Mystery Data")
x, y = readFile("mysteryData.txt")
x = np.array(x)
y = np.array(y)

coeff = np.polyfit(x,y,2)
# y_est = coeff[0]*x*x + coeff[1]*x + coeff[2]   # y = ax2 + bx + c
y_est = np.polyval(coeff, x)
plt.plot(x, y_est)              # Plotting the fitted line
plt.plot(x,y, 'ro')             # Plotting the points
plt.show()

error_val = avgMeanSquareError(y, y_est)
print ("\t Average mean square error: " + str(error_val))

R2_val = R2_fit(y, y_est)
print ("\t The fit of the data (R2): " + str(R2_val))
