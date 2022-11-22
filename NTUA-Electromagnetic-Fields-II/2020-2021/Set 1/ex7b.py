import numpy as np
import scipy as sp
from scipy import integrate
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def f(x, y):
    def Ex1(TH): return (x - 1 - 0.1*np.cos(TH))/(((x - 1 - 0.1 * np.cos(TH))**2 + (y - 1)**2 + 0.01*(np.sin(TH))**2)**1.5)
    ex1, error1 = integrate.quad(Ex1, 0, np.pi*2)

    def Ey1(TH): return (y-1)/(((x - 1 - 0.1*np.cos(TH)) ** 2 + (y-1)**2 + 0.01 * (np.sin(TH))**2)**1.5)
    ey1, error1 = integrate.quad(Ey1, 0, np.pi*2)

    def Ex2(TH): return (-1)*(x + 1 - 0.1*np.cos(TH))/(((x + 1 - 0.1*np.cos(TH))**2 + (y - 1)**2 + 0.01*(np.sin(TH))**2)**1.5)
    ex2, error2 = integrate.quad(Ex2, 0, np.pi*2)

    def Ey2(TH): return (-1)*(y-1)/(((x + 1 - 0.1*np.cos(TH)) ** 2 + (y-1)**2 + 0.01 * (np.sin(TH))**2)**1.5)
    ey2, error2 = integrate.quad(Ey2, 0, np.pi*2)

    def Ex3(TH): return (x + 1 - 0.1*np.cos(TH))/(((x + 1 - 0.1 * np.cos(TH))**2 + (y + 1)**2 + 0.01*(np.sin(TH))**2)**1.5)
    ex3, error3 = integrate.quad(Ex3, 0, np.pi*2)

    def Ey3(TH): return (y+1)/(((x + 1 - 0.1*np.cos(TH)) ** 2 + (y+1)**2 + 0.01 * (np.sin(TH))**2)**1.5)
    ey3, error3 = integrate.quad(Ey3, 0, np.pi*2)

    def Ex4(TH): return (-1)*(x - 1 - 0.1*np.cos(TH))/(((x - 1 - 0.1*np.cos(TH))**2 + (y + 1)**2 + 0.01*(np.sin(TH))**2)**1.5)
    ex4, error4 = integrate.quad(Ex4, 0, np.pi*2)

    def Ey4(TH): return (-1)*(y+1)/(((x - 1 - 0.1*np.cos(TH)) ** 2 + (y+1)**2 + 0.01 * (np.sin(TH))**2)**1.5)
    ey4, error4 = integrate.quad(Ey4, 0, np.pi*2)

    Ex = ex1 + ex2 + ex3 + ex4
    Ey = ey1 + ey2 + ey3 + ey4
    return Ex, Ey


f1 = np.vectorize(f)
x = np.linspace(0, 2, 100)
y = np.linspace(0, 2, 100)
X, Y = np.meshgrid(x, y)
Ex, Ez = f1(X, Y)

fig, ax = plt.subplots()

ax.quiver(X, Y, Ex/((Ex**2+Ez**2)**0.5), Ez/((Ex**2+Ez**2)**0.5), (Ex**2+Ez**2)**0.5,
          cmap=matplotlib.cm.inferno, units='xy',
          scale=15, zorder=3, width=0.0035, headwidth=3., headlength=4.)
ax.set_title('Dynamic Electric Field Lines')
ax.set_xlabel('X(m)')
ax.set_ylabel('Υ(m)')
plt.show()