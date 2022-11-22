import scipy as sp
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy import integrate
from mpl_toolkits import mplot3d

L = 0.5
h = 0.5

def E1(x, z):
    global L, h
    Ex1 = ((1/(np.sqrt((x-L)**2 + (z-h)**2)) - 1/(np.sqrt((x+L)**2 + (z-h)**2))) +
        (2/3)*(1/(np.sqrt((x-L)**2 + (z+h)**2)) - 1/(np.sqrt((x+L)**2 + (z+h)**2))))/(4*np.pi)
    Ez1 = ((1/(z-h))*((x+L)/(np.sqrt((x+L)**2 + (z-h)**2)) - (x-L)/(np.sqrt((x-L)**2 + (z-h)**2))) +
        (2/3)*((1/(z+h))*((x+L)/(np.sqrt((x+L)**2 + (z+h)**2)) - (x-L)/(np.sqrt((x-L)**2 + (z+h)**2)))))/(4*np.pi)
    return Ex1, Ez1

def E2(x, z):
    global L, h
    Ex2 = ((1/(np.sqrt((x-L)**2 + (z-h)**2)) - 1/(np.sqrt((x+L)**2 + (z-h)**2))))/(12*np.pi)
    Ez2 = ((1/(z-h))*((x+L)/(np.sqrt((x+L)**2 + (z-h)**2)) - (x-L)/(np.sqrt((x-L)**2 + (z-h)**2))))/(12*np.pi)
    return Ex2, Ez2

e1 = np.vectorize(E1)
e2 = np.vectorize(E2)

x = np.linspace(-2, 2, 50)
z_pos = np.linspace(0, 2, 50)
z_neg = np.linspace(-2, 0, 50)
X1, Z1 = np.meshgrid(x, z_pos)
X2, Z2 = np.meshgrid(x, z_neg)
Ex1, Ez1 = e1(X1, Z1)
Ex2, Ez2 = e2(X2, Z2)

fig, ax = plt.subplots(figsize=(10, 10))

ax.quiver(X1, Z1, Ex1/((Ex1**2+Ez1**2)**0.5), Ez1/((Ex1**2+Ez1**2)**0.5), (Ex1**2+Ez1**2) **
          0.5, cmap='turbo', units='xy', scale=15, zorder=3, width=0.0035, headwidth=3., headlength=4.)
ax.quiver(X2, Z2, Ex2/((Ex2**2+Ez2**2)**0.5), Ez2/((Ex2**2+Ez2**2)**0.5), (Ex2**2+Ez2**2) **
          0.5, cmap='turbo', units='xy', scale=15, zorder=3, width=0.0035, headwidth=3., headlength=4.)

ax.set_title('Electric Field F(x,z)')
ax.set_xlabel('X-Coordinate')
ax.set_ylabel('Z-Coordinate')
ax.grid()
plt.show()