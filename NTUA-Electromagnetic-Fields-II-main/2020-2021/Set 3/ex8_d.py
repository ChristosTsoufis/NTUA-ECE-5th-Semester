import matplotlib.pyplot as plt
import numpy as np

I = 1
d = 2
h = 1
a = 0.1
M = I*np.pi*a**2
m_0 = 4*np.pi/10000000

def canvas():
    fig, ax = plt.subplots()
    ax.set_title('Vector Potential Α(x,z)')
    ax.set_xlabel('x(m)')
    ax.set_ylabel('z(m)')
    ax.grid()
    return ax

def Ax(x, y, z):
    f1 = 1/(np.sqrt((x-d)**2 + (y-h)**2 + z**2))
    f2 = 1/(np.sqrt((x-d)**2 + (y+h)**2 + z**2))
    f3 = 1/(np.sqrt((x+d)**2 + (y-h)**2 + z**2))
    f4 = 1/(np.sqrt((x+d)**2 + (y+h)**2 + z**2))
    return (m_0*M/(4*np.pi))*z*(f1**3 - f2**3 + f3**3 - f4**3)

def Az(x, y, z):
    f1 = 1/(np.sqrt((x-d)**2 + (y-h)**2 + z**2))
    f2 = 1/(np.sqrt((x-d)**2 + (y+h)**2 + z**2))
    f3 = 1/(np.sqrt((x+d)**2 + (y-h)**2 + z**2))
    f4 = 1/(np.sqrt((x+d)**2 + (y+h)**2 + z**2))
    return (m_0*M/(4*np.pi))*(-(x-d)*f1**3 + (x-d)*f2**3 - (x+d)*f3**3 - (x+d)*f4**3)

def Ax_aux(x, z):
    return Ax(x, 1, z)

def Az_aux(x, z):
    return Az(x, 1, z)

a_x = np.vectorize(Ax_aux)
a_z = np.vectorize(Az_aux)

x = np.linspace(0, 4, 50)
z = np.linspace(-2, 2, 50)
X, Z = np.meshgrid(x, z)

Ax = a_x(X, Z)
Az = a_z(X, Z)
ax = canvas()
ax.streamplot(X, Z, Ax/(2*((Ax**2 + Az**2)**0.5)),
              Az/(2*((Ax**2 + Az**2)**0.5)))
plt.show()
ax = canvas()
ax.quiver(X, Z, Ax/(2*((Ax**2 + Az**2)**0.5)), Az/(2*((Ax**2 + Az**2)**0.5)),
          (Ax**2 + Az**2)**0.5, cmap='inferno', units='xy', width=0.0035, 
          headwidth=3., headlength=4.)
plt.show()