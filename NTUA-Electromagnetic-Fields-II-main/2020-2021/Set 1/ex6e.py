import numpy as np
import scipy as sp
from scipy import integrate
import matplotlib
import matplotlib.pyplot as plt

def f(t):
    def x(theta): return (-2.5*8.85)/((5-4*np.cos(t - theta))**1.5)
    a, error = integrate.quad(x, -0.75, 0.75)
    return a

f2 = np.vectorize(f)
t = np.arange(0.0, 2*np.pi, 0.001)
fig, ax = plt.subplots()
ax.plot(t, f2(t), color='blue')
ax.set(xlabel='θ', ylabel='σ', title='Surface Load Desnity')
plt.show()