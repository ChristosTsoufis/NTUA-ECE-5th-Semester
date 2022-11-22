from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

a = 0.1
I1 = 1
# h = 0.025
# h = 0.05
h = 0.1
monte_carlo = 1000

th = np.linspace(0, 2*np.pi, monte_carlo)

def Ax_aux(x, z, th):
    f1 = 1/(np.sqrt(x**2 + a**2 - 2*a*x*np.cos(th) + (z+h)**2))
    f2 = 1/(np.sqrt(x**2 + a**2 - 2*a*x*np.cos(th) + (z-h)**2))
    Ax_1 = (I1*a/(4*np.pi)) * (-1)*np.sin(th)*f1
    Ax_2 = (I1*a/(4*np.pi)) * (-1)*np.sin(th)*f2
    return Ax_1 + Ax_2

def Ax(x, z):
    val = np.array([Ax_aux(x, z, i) for i in th])
    return (2 * np.pi) * (val.sum() / val.size)

def Ay_aux(x, z, th):
    f1 = 1/(np.sqrt(x**2 + a**2 - 2*a*x*np.cos(th) + (z+h)**2))
    f2 = 1/(np.sqrt(x**2 + a**2 - 2*a*x*np.cos(th) + (z-h)**2))
    Ay_1 = (I1*a/(4*np.pi)) * np.cos(th)*f1
    Ay_2 = (I1*a/(4*np.pi)) * np.cos(th)*f2
    return Ay_1 + Ay_2

def Ay(x, z):
    val = np.array([Ay_aux(x, z, i) for i in th])
    return (2 * np.pi) * (val.sum() / val.size)

a_y = np.vectorize(Ay)
a_x = np.vectorize(Ax)

x = np.linspace(-0.3, 0.3, 50)
z = np.linspace(-0.25, 0.25, 50)
X, Z = np.meshgrid(x, z)
Ay = a_y(X, Z)
Ax = a_x(X, Z)

Ay = Ay * Ay
Ax = Ax * Ax

levels = [0.01, 0.025, 0.05, 0.075, 0.1, 0.15, 0.175, 0.2, 0.25, 0.3,
          0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.25, 1.5, 2.0, 3.0, 5.0]

fig, ax = plt.subplots()
ax.set(xlabel='x(m)', ylabel="z(m)",
       title='Vector Dynamic Equivalent Lines Α(x,z)/μ0')
cs = ax.contour(X, Z, np.power(Ax + Ay, 0.5), levels, cmap='plasma')
ax.clabel(cs, cs.levels, inline=True, fontsize=10)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set(xlabel='x(m)', ylabel='z(m)', zlabel='Α(x,z)/μ0',
       title='Vector Potential Α(x,z)/μ0')
surf = ax.plot_surface(X, Z, np.power(Ax + Ay, 0.5),
                       cmap='plasma', shade=True)
fig.colorbar(surf)
plt.show()