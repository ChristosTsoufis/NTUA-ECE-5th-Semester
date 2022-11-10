import numpy as np
import scipy as sp
from scipy import integrate
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def f(x, y):
    e0 = 8.854 * (10**(-12))

    def Sx(TH): return (2*e0) / (((x + 1 - 0.1*np.cos(TH))**2 + 1 + 0.01*(np.sin(TH))**2)**1.5)
    sx, error1 = integrate.quad(Sx, 0, np.pi*2)

    def Sy(TH): return (-1)/(((x - 1 - 0.1*np.cos(TH)) ** 2 + 1 + 0.01 * (np.sin(TH))**2)**1.5)
    sy, error1 = integrate.quad(Sy, 0, np.pi*2)

    return sx+sy

f1 = np.vectorize(f)

x = np.linspace(0, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = f1(X, Y)

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z, zdir='xy', offset=11, cmap=matplotlib.cm.cividis, color='blue')
ax.clabel(CS, CS.levels, inline=True, fontsize=5)
ax.set_title('Surface Load Density')
ax.set_xlabel('X(m)')
ax.set_ylabel('Z(m)')
plt.show()