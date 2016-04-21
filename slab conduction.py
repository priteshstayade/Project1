# Simple Numerical Laplace Equation Solution using Finite Difference Method
import numpy as np
import math
import matplotlib.pyplot as plt

# Set maximum iteration
maxIter = 500

# Set Dimension and delta
lenX = lenY = 20 #we set it rectangular
delta = 1

RPM = float(raw_input("RPM: "))
Tbottom = float(raw_input("CPU Temp: "))
force = 63.1655*(RPM/60)*(RPM/60)
flow_rate = (math.sqrt(force/0.6125))*(3.1416*8*8)
dQdT = 0.03085*flow_rate
c = 0.7 #specific heat of silicon
# Boundary condition
Tright = 27
Ttop = (Tbottom) - (dQdT/14)
Tleft = (Tright) + (dQdT/14)


# Initial guess of interior grid
Tguess = 30

# Set colour interpolation and colour map
colorinterpolation = 50
colourMap = plt.cm.jet 

# Set meshgrid
X, Y = np.meshgrid(np.arange(0, lenX), np.arange(0, lenY))

# Set array size and set the interior value with Tguess
T = np.empty((lenX, lenY))
T.fill(Tguess)

# Set Boundary condition
T[(lenY-1):, :] = Ttop
T[:1, :] = Tbottom
T[:, (lenX-1):] = Tright
T[:, :1] = Tleft

# Iteration (We assume that the iteration is convergence in maxIter = 500)
print("Please wait for a moment")
for iteration in range(0, maxIter):
    for i in range(1, lenX-1, delta):
        for j in range(1, lenY-1, delta):
            T[i, j] = 0.25 * (T[i+1][j] + T[i-1][j] + T[i][j+1] + T[i][j-1])

print("Iteration finished")

# Title and Contour
plt.title("Contour of Temperature")
plt.contourf(X, Y, T, colorinterpolation, cmap=colourMap)

# Set Colorbar
plt.colorbar()

# Results
plt.show()

print("")