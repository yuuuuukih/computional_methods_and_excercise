import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


# const32.py
#===============================================
x0 = 1.5
y0 = 1

alpha1 = 2
alpha2 = 1.5
beta1 = 4
beta2 = 1.5

# fの設定
# Y = [x, y]
def f(Y, gamma):
    dxdt = (alpha1 - gamma * Y[0] - beta1 * Y[1]) * Y[0]
    dydt = (-alpha2 + beta2 * Y[0]) * Y[1]
    dYdt = [dxdt, dydt]
    return dYdt


# Runge_Kutta_method.py
#===============================================
def Runge_Kutta_method_32(f, Y0, h, tmax):
    Y = [Y0]
    for i in tqdm(range(int(tmax / h))):
        k1 = f(Y[i])
        k2 = f([Y[i][j] + 0.5 * h * k1[j] for j in range(2)])
        k3 = f([Y[i][j] + 0.5 * h * k2[j] for j in range(2)])
        k4 = f([Y[i][j] + h * k3[j] for j in range(2)])
        next_Y = [Y[i][j] + h / 6 * (k1[j] + 2*k2[j] + 2*k3[j] + k4[j]) for j in range(2)]
        Y.append(next_Y)
    return Y


# asgmt3.2.1.py
#===============================================
def f321(Y):
    return f(Y, gamma=0)

def main():
    # Runge Kutta法で解く
    Y0 = [x0, y0]
    tmax = 10
    delta_t = 0.1
    Y = Runge_Kutta_method_32(f321, Y0, delta_t, tmax)

    x = []
    y = []

    for i in range(len(Y)):
        x.append(Y[i][0])
        y.append(Y[i][1])


    # 収束先を描画
    plt.rcParams['font.family'] = "Meiryo"
    fig = plt.figure(figsize=(6, 6), dpi=100)
    fig.subplots_adjust(left=0.2, bottom=0.2)
    ax = fig.add_subplot(1, 1, 1, xlabel='time', ylabel='')
    ax.grid(color="#eeeeee", which="both")
    ax.set_axisbelow(True)

    ax.scatter(np.arange(101)/10, x, label='x', s=2)
    ax.scatter(np.arange(101)/10, y, label='y', s=2)
    ax.legend()
    plt.show()

if __name__ == '__main__':
    main()