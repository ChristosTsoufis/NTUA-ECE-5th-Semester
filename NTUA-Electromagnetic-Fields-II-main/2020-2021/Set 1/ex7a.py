import numpy as np
import scipy as sp
from scipy import integrate
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def f(x, y):
    def Fi1(TH): return (0.1)/(np.sqrt((x - 1 - 0.1*np.cos(TH)) ** 2 + (y-1)**2 + 0.01*((np.sin(TH))**2)))
    fi1, error1 = integrate.quad(Fi1, 0, np.pi*2)

    def Fi2(TH): return (-0.1)/(np.sqrt((x + 1 - 0.1*np.cos(TH)) ** 2 + (y-1)**2 + 0.01*((np.sin(TH))**2)))
    fi2, error2 = integrate.quad(Fi2, 0, np.pi*2)

    def Fi3(TH): return (0.1)/(np.sqrt((x + 1 - 0.1*np.cos(TH)) ** 2 + (y+1)**2 + 0.01*((np.sin(TH))**2)))
    fi3, error3 = integrate.quad(Fi3, 0, np.pi*2)

    def Fi4(TH): return (-0.1)/(np.sqrt((x - 1 - 0.1*np.cos(TH))** 2 + (y+1)**2 + 0.01*((np.sin(TH))**2)))
    fi4, error4 = integrate.quad(Fi4, 0, np.pi*2)

    return fi1 + fi2 + fi3 + fi4

f1 = np.vectorize(f)

x = np.linspace(0, 2, 100)
y = np.linspace(0, 2, 100)
X, Y = np.meshgrid(x, y)
Z = f1(X, Y)

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z, zdir = 'xy', offset = 11,
                levels = [0.01, 0.1, 0.2, 0.4, 0.8, 1.0, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7.5],
                cmap = matplotlib.cm.magma,
                color = 'blue')
ax.clabel(CS, CS.levels, inline = True, fontsize = 5)
ax.set_title('Normalized Potential')
ax.set_xlabel('X(m)')
ax.set_ylabel('Υ(m)')
plt.show()