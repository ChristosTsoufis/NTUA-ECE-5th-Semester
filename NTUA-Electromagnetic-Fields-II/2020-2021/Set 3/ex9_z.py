import matplotlib.pyplot as plt
import numpy as np

# h = 0.025
# h = 0.05
h = 0.1
monte_carlo = 100

def L_aux(a, th1, th2):
	f1 = 1/(np.sqrt(2*a**2 + 4*h**2 - 2*a**2*np.cos(th1-th2)))
	l = (a**2/(4*np.pi)) * np.cos(th1-th2)*f1
	return l

th1 = np.linspace(0, 2 * np.pi, monte_carlo)
th2 = np.linspace(0, 2 * np.pi, monte_carlo)

def L(a):
	val = np.array([[L_aux(a, i, j) for i in th1] for j in th2])
	return (2*np.pi) * (2*np.pi) * (val.sum() / val.size)
L = np.vectorize(L)
a = np.linspace(0, 0.25, 1000) # for h = 0.025, 0.05, 0.1

fig, ax = plt.subplots()
ax.set(xlabel ='a(m)', ylabel ="L(a)(H)", title ='Inductor L(a)')
ax.grid()
ax.plot(a, L(a))
plt.show()