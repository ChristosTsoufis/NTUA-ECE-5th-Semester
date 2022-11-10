import matplotlib.pyplot as plt
import numpy as np

a = 0.1
I = 1
d = 2
h = 1
M = I*np.pi*a**2

def canvas():
    fig, ax = plt.subplots()
    ax.set_title('Magnetic field Η(x,y)')
    ax.set_xlabel('x(m)')
    ax.set_ylabel('y(m)')
    ax.grid()
    return ax

def Hx(x, y):
    f1 = 1/(np.sqrt((x-d)**2 + (y-h)**2))
    f2 = 1/(np.sqrt((x-d)**2 + (y+h)**2))
    f3 = 1/(np.sqrt((x+d)**2 + (y-h)**2))
    f4 = 1/(np.sqrt((x+d)**2 + (y+h)**2))
    return (M/(4*np.pi)) * 3 * ((x-d)*(y-h)*(f1**5) - 
    (x-d)*(y+h)*(f2**5) + (x+d)*(y-h)*(f3**5) - (x+d)*(y+h)*(f4**5))

def Hy(x, y):
    f1 = (np.sqrt((x-d)**2 + (y-h)**2))
    f2 = (np.sqrt((x-d)**2 + (y+h)**2))
    f3 = (np.sqrt((x+d)**2 + (y-h)**2))
    f4 = (np.sqrt((x+d)**2 + (y+h)**2))
    return (M/(4*np.pi)) * ((3*(y-h)**2-f1**2)/(f1**5) -
    (3*(y+h)**2-f2**2)/(f2**5) + (3*(y-h)**2-f3**2)/(f3**5) - (3*(y+h)**2-f4**2)/(f4**5))

h_x = np.vectorize(Hx)
h_y = np.vectorize(Hy)

x = np.linspace(0, 4, 50)
y = np.linspace(0, 4, 50)
X, Y = np.meshgrid(x, y)

Hx = h_x(X, Y)
Hy = h_y(X, Y)

ax = canvas()
ax.quiver(X, Y, Hx/(2*((Hx**2 + Hy**2)**0.5)), Hy/(2*((Hx**2 + Hy**2)**0.5)),
          (Hx**2 + Hy**2)**0.5, cmap='plasma', units='xy', width=0.0035,
          headwidth=3., headlength=4.)
plt.show()
ax = canvas()
ax.streamplot(X, Y, Hx/(2*((Hx**2 + Hy**2)**0.5)),
              Hy/(2*((Hx**2 + Hy**2)**0.5)))
plt.show()