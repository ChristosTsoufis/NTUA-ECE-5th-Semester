import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

L = 0.99
h = 1
N = 3
I = np.array([0 for i in range(2*N)])
VDF_inv = np.array([[0 for j in range(2*N)] for i in range(2*N)])
D = 1.5
a = 0.005
pi = np.pi
Dz = L/N
s0 = 1/160

def z_bar(i):
    if (i <= N):
        zi = -h + (L/2) - i*Dz
        return zi + (Dz/2)
    return z_bar(i - N)

# the horizontal bar has not been calculated here
def VDF(i, j):
    if ((0 < i <= N and N < j <= 2*N) or (N < i <= 2*N and 0 < j <= N)):
        fraction1 = 1 / (np.sqrt((z_bar(i) - z_bar(j))**2 + D**2))
        fraction2 = 1 / (np.sqrt((z_bar(i) + z_bar(j))**2 + D**2))
        return (Dz / (4*pi*s0)) * (fraction1 + fraction2)
    else:
        fraction1 = 1 / (abs(z_bar(i) + z_bar(j)))
        if (i == j):
            root = np.sqrt(a**2 + (Dz/2)**2)
            log = np.log(((Dz/2) + root) / ((Dz/-2) + root))
            return (1/(4*pi*s0)) * (log + (Dz*fraction1))
        fraction2 = 1 / (abs(z_bar(i) - z_bar(j)))
        return (Dz / (4*pi*s0)) * (fraction1 + fraction2)

def F(x, y, z):
    def r1(i):
        return np.sqrt((x+(D/2))**2 + y**2 + (z - z_bar(i))**2)

    def r2(i):
        return np.sqrt((x-(D/2))**2 + y**2 + (z - z_bar(i))**2)
    return 2*(Dz / (4*pi*s0)) * np.sum([(1 / r1(i) + 1 / r2(i)) * I[i - 1] for i in range(1, N + 1)])

F = np.vectorize(F)

def plot_a_lot1():
    x = np.linspace(-3, 3, 100)
    fig, ax = plt.subplots()
    ax.plot(x, F(x, 0, 0))
    ax.set(xlabel='X(m)', ylabel='Phi(V)', title='Potential Φ(x), N=' + str(N))
    ax.grid()
    fig.savefig("ask8_Fi_N=" + str(N) + ".png")
    plt.clf()

def plot_a_lot2():
    x = np.array([z_bar(i) for i in range(1, N + 1)])
    fig, ax = plt.subplots()
    ax.plot(x, I[:N])
    ax.set(xlabel='Z(m)', ylabel='I(A/m)',
           title='Linear Power Distribution Ι(z), N=' + str(N))
    ax.grid()
    fig.savefig("ask8_I_N=" + str(N) + ".png")
    plt.clf()

def row_sum_vdf(i):
    sum = 0
    for j in range(2*N):
        sum += VDF_inv[i][j]
    return sum

def updateN(n):
    global N
    global Dz
    N = n
    Dz = L / n

# calculation of array
pinakas = [[]]
pinakas[0].append('N')
pinakas[0].append('Phi')
pinakas[0].append('Rg')
pinakas[0].append('F(0,0,0)')

for i in range(16):
    if (i == 0):
        updateN(3)
    else:
        updateN(5 * i)
    pinakas.append([])
    row = pinakas[i + 1]

    VDF_inv = inv(
        np.array([[VDF(i, j) for j in range(1, 2*N + 1)] for i in range(1, 2*N + 1)]))

    Phi = 250 / (Dz*np.sum(VDF_inv))

    I = Phi * np.array([row_sum_vdf(i) for i in range(2*N)])

    Rg = Phi / (250)

    row.append(N)
    row.append(Phi)
    row.append(Rg)
    row.append(F(0, 0, 0))
    
    plot_a_lot1()
    plot_a_lot2()

pinakas = np.array(pinakas)
print(pinakas)