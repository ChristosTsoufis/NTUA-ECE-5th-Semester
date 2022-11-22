import numpy as np
from mpl_toolkits import mplot3d
import matplotlib
import matplotlib.pyplot as plt
from numpy.linalg import inv

L = 0.5
h = 0.5
N = 100
eps1 = 1
eps2 = 5
a = 0.0025
pi = np.pi
Dx = (2*L)/N
#Fi = 1/np.sum()

def x(i):
    xi = -L + i*Dx
    return xi

x = np.vectorize(x)

def x_bar(i):
    xi_bar = x(i) - Dx/2
    return xi_bar

x_bar = np.vectorize(x_bar)

def A(i, j):
    if (i != j):
        Aij = (Dx/(4*pi*eps1)) * (1/(abs(x_bar(i) - x_bar(j))) + ((eps1 - eps2)/(eps1 + eps2)) * (1/(np.sqrt((x_bar(i) - x_bar(j))**2 + 4*h**2))))
        return Aij
    else:
        Aii = (1/(4*pi*eps1)) * (np.log((Dx/2 + np.sqrt(a**2 + (Dx/2)**2))/(Dx/-2 + np.sqrt(a**2 + (Dx/2)**2))) + ((eps1-eps2)*Dx)/(2*h*(eps1+eps2)))
        return Aii

A = np.vectorize(A)
A_inv = inv(np.fromfunction(lambda i, j: A(i, j), (N, N), dtype=int))

I = np.vstack([1 for x in range(N)])

Fi = 1/np.sum(Dx*np.dot(A_inv, I))

def lamdak(i):
    lamda = Fi*(np.dot(A_inv, I)[i][0])
    return lamda

lamda = [n[0] for n in Fi*np.dot(A_inv, I)]
i = np.linspace(-N, N, N)
fig, ax = plt.subplots(figsize=(10, 10))
ax.plot((i/N)*L, lamda, color='red')

ax.set(xlabel='X-Coordinate', ylabel='λ(x)/ε0 (C/m)', title='Normalized Line Charge Density λ(x)/ε0')

plt.show()

def F(x):
    f = (Dx/(4*eps2*pi)) * np.sum([(lamdak(i) * ((2*eps2)/(eps1 + eps2)) * ((1) / (np.sqrt((x - x_bar(i))**2 + h**2)))) for i in range(N)])
    return f

F = np.vectorize(F)

xv = np.linspace(-2, 2, N)
fig, ax = plt.subplots(figsize=(10, 10))
ax.plot(xv, F(xv), color='red')

ax.set(xlabel='X-Coordinate', ylabel='Φ(x) (Volt)', title='Potential Φ(x)')

plt.show()