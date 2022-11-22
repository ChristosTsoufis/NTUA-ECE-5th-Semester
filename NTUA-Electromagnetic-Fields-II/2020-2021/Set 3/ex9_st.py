import matplotlib.pyplot as plt
import numpy as np

a = 0.1
I1 = 1
# h = 0.1
# h = 0.05
h = 0.025

monte_carlo = 1000

def canvas():
    fig, ax = plt.subplots()
    ax.set(xlabel='x(m)', ylabel="z(m)", title='Magnetic Field Η(x,z)')
    ax.grid()
    return ax

th = np.linspace(0, 2*np.pi, monte_carlo)

def Hx_aux(x, z, th):
    f1 = 1/(np.sqrt(x**2 + a**2 - 2*a*x*np.cos(th) + (z+h)**2))
    f2 = 1/(np.sqrt(x**2 + a**2 - 2*a*x*np.cos(th) + (z-h)**2))
    Hx_1 = (I1*a/(4*np.pi)) * (z+h)*np.cos(th)*f1**3
    Hx_2 = (I1*a/(4*np.pi)) * (z-h)*np.cos(th)*f2**3
    return Hx_1 + Hx_2

def Hx(x, z):
    val = np.array([Hx_aux(x, z, i) for i in th])
    return (2 * np.pi) * (val.sum() / val.size)

def Hz_aux(x, z, th):
    f1 = 1/(np.sqrt(x**2 + a**2 - 2*a*x*np.cos(th) + (z+h)**2))
    f2 = 1/(np.sqrt(x**2 + a**2 - 2*a*x*np.cos(th) + (z-h)**2))
    Hz_1 = (I1*a/(4*np.pi)) * (a - x*np.cos(th))*f1**3
    Hz_2 = (I1*a/(4*np.pi)) * (a - x*np.cos(th))*f2**3
    return Hz_1 + Hz_2

def Hz(x, z):
    val = np.array([Hz_aux(x, z, i) for i in th])
    return (2 * np.pi) * (val.sum() / val.size)

h_x = np.vectorize(Hx)
h_z = np.vectorize(Hz)

x = np.linspace(-0.3, 0.3, 50)
z = np.linspace(-h-0.2, h+0.2, 50)  # 3 times for h = 0.025, 0.05, 0.1

X, Z = np.meshgrid(x, z)

Hx = h_x(X, Z)
Hz = h_z(X, Z)

ax = canvas()
ax.streamplot(X, Z, Hx/(2*((Hx**2 + Hz**2)**0.5)),
              Hz/(2*((Hx**2 + Hz**2)**0.5)))
plt.show()
ax = canvas()
ax.quiver(X, Z, Hx/(2*((Hx**2 + Hz**2)**0.5)), Hz/(2*((Hx**2 + Hz**2)**0.5)),
          (Hx**2 + Hz**2)**0.5, cmap='plasma', units='xy', width=0.0009, headwidth=3., headlength=4.)
plt.show()