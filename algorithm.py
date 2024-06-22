""" In this algorithm we take a set of data points and use gradient descent to try and find an accurate slope for the line of best fit

We assume that the y-intercept is 0
"""

import matplotlib.pyplot as plt
import numpy as np

xpoints = [1,2,3,4]
ypoints = [2,5,7,8]

# Equation: x^3-5x    Derivative/Slope: 3x^2-5
# Does the entire algorithm for gradient descent
m = 5 # initial guess for the value of x
lr = 0.015
mlist = [m]
for i in range(6):
    m = m-lr*((m-2) + (2*m-5)*2 + (3*m-7)*3 + (4*m-8)*4)
    mlist.append(m)
#print(x)
#plt.plot(xlist)

# Graphs the error curve
xcurve = np.arange(-1,5,0.001) # range of possible slope values
ycurve = ((xcurve-2)**2)+((2*xcurve-5)**2)+((3*xcurve-7)**2+((4*xcurve-8)**2))/2 # equation that shows the error for every possible slope
plt.plot(xcurve,ycurve)
plt.xlabel("Possible Slopes")
plt.ylabel("Error")
#plt.axis("equal")

# Plots the points being used in the path for gradient descent
xdescent = np.array(mlist)
ydescent = ((xdescent-2)**2)+((2*xdescent-5)**2)+((3*xdescent-7)**2+((4*xdescent-8)**2))/2 # shows the points being placed on the error curve
plt.scatter(xdescent,ydescent,s = 20)
plt.figure()

# Plots the data points and draws the line of best fit using the error curve

plt.scatter(xpoints,ypoints)
xgraph = [0,1,2,3,4,5]
ygraph = m*np.array(xgraph)
plt.plot(xgraph,ygraph) 
print("The most accurate slope is" , xcurve[np.argmin(ycurve)])
