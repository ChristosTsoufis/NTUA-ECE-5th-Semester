import matplotlib.pyplot as plt
import numpy as np

a = 0.1
I = 1
d = 2
h = 1
M = I*np.pi*a**2

def canvas1():
    fig, ax = plt.subplots()
    ax.set_title('Surface Current Density Κ(x,z)')
    ax.set_xlabel('x(m)')
    ax.set_ylabel('z(m)')
    ax.grid()
    return ax

def canvas2():
    fig, ax = plt.subplots()
    ax.set_title('Surface Current Density Κ(y,z)')
    ax.set_xlabel('y(m)')
    ax.set_ylabel('z(m)')
    ax.grid()
    return ax

def Kx(x, z):
    f1 = 1/(np.sqrt((x-d)**2 + h**2 + z**2))
    f2 = 1/(np.sqrt((x+d)**2 + h**2 + z**2))
    return M/(4*np.pi) * 6*h*z*((-1)*(f1**5 + f2**5))

def Kz_1(x, z):
    f1 = 1/(np.sqrt((x-d)**2 + h**2 + z**2))
    f2 = 1/(np.sqrt((x+d)**2 + h**2 + z**2))
    return M/(4*np.pi) * 6*h*((x-d)*f1**5 + (x+d)*f2**5)

def Ky(y, z):
    f1 = 1/(np.sqrt(d**2 + (y-h)**2 + z**2))
    f2 = 1/(np.sqrt(d**2 + (y+h)**2 + z**2))
    return M/(4*np.pi) * 6*z*((-1)*((y-h)*f1**5 - (y+h)*f2**5))

def Kz_2(y, z):
    f1 = (np.sqrt(d**2 + (y-h)**2 + z**2))
    f2 = (np.sqrt(d**2 + (y+h)**2 + z**2))
    return M/(4*np.pi) * 2*((3*(y-h)**2-f1**2)/f1**5 - (3*(y+h)**2-f2**2)/f2**5)

Kx = np.vectorize(Kx)
Kz_2 = np.vectorize(Kz_2)
Ky = np.vectorize(Ky)
Kz_1 = np.vectorize(Kz_1)

x = np.linspace(0, 4, 50)
y = np.linspace(0, 4, 50)
z = np.linspace(-2, 2, 50)

# y = 0
X, Z = np.meshgrid(x, z)
Kx = Kx(X, Z)
Kz = Kz_1(X, Z)
ax = canvas1()
ax.quiver(X, Z, Kx/(2*((Kx**2 + Kz**2)**0.5)), Kz/(2*((Kx**2 + Kz**2)**0.5)),
          (Kx**2 + Kz**2)**0.5, cmap='plasma', units='xy', width=0.0035, 
          headwidth=3., headlength=4.)
plt.show()
ax = canvas1()
ax.streamplot(X, Z, Kx/(2*((Kx**2 + Kz**2)**0.5)), Kz/(2*((Kx**2 + Kz**2)**0.5)))
plt.show()

# x = 0
Y, Z = np.meshgrid(y, z)
Ky = Ky(Y, Z)
Kz = Kz_2(Y, Z)
ax = canvas2()
ax.quiver(Y, Z, Ky/(2*((Ky**2 + Kz**2)**0.5)), Kz/(2*((Ky**2 + Kz**2)**0.5)),
          (Ky**2 + Kz**2)**0.5, cmap='plasma', units='xy', width=0.0035,
          headwidth=3., headlength=4.)
plt.show()
ax = canvas2()
ax.streamplot(Y, Z, Ky/(2*((Ky**2 + Kz**2)**0.5)), Kz/(2*((Ky**2 + Kz**2)**0.5)))
plt.show()