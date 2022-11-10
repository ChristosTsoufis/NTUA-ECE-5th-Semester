import numpy as np
from mpl_toolkits import mplot3d
import matplotlib
import matplotlib.pyplot as plt

L = 0.5
h = 0.5

def F1(x, z):
    global L
    global h
    f1 = (np.log((x-L - np.sqrt((x-L)**2 + (z-h)**2))/(x+L - np.sqrt((x+L)**2 + (z-h)**2))) -
         (2/3)*np.log((x-L - np.sqrt((x-L)**2 + (z+h)**2))/(x+L - np.sqrt((x+L)**2 + (z+h)**2))))/(4*np.pi)
    return f1

def F2(x, z):
    global L
    global h
    f2 = (np.log((x-L - np.sqrt((x-L)**2 + (z-h)**2))/(x+L - np.sqrt((x+L)**2 + (z-h)**2))))/(12*np.pi)
    return f2

f1 = np.vectorize(F1)
f2 = np.vectorize(F2)
x = np.linspace(-4, 4, 100)
z_pos = np.linspace(0, 4, 100)
z_neg = np.linspace(-4, 0, 100)
X1, Z1 = np.meshgrid(x, z_pos)
X2, Z2 = np.meshgrid(x, z_neg)
Y1 = f1(X1, Z1)
Y2 = f2(X2, Z2)
fig, ax = plt.subplots(figsize=(10, 10))
cs1 = ax.contourf(X1, Z1, Y1, zdir='xz', offset=11,
                  levels=[0.01, 0.02, 0.03, 0.04, 0.05, 0.075, 0.1, 0.2, 0.3, 0.4, 0.5],
                  cmap='viridis')
cs2 = ax.contourf(X2, Z2, Y2, zdir='xz', offset=11,
                  levels=[0.01, 0.02, 0.03, 0.04, 0.05, 0.075, 0.1, 0.2, 0.3, 0.4, 0.5],
                  cmap='viridis')

cbar = fig.colorbar(cs1)
ax.set_title('Potential Φ(x,z)')
ax.set_xlabel('X-Coordinate')
ax.set_ylabel('Z-Coordinate')
plt.show()