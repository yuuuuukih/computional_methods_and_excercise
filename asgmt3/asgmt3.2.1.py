import numpy as np
from constant.const32 import x0, y0, f
from function.Runge_Kutta_method import Runge_Kutta_method
import matplotlib.pyplot as plt

def f321(Y):
    return f(Y, gamma=0)

def main():
    # Runge Kutta法で解く
    Y0 = np.array([x0, y0])
    tmax = 10
    delta_t = 0.1
    Y = Runge_Kutta_method(f321, Y0, delta_t, tmax)

    x = np.array([])
    y = np.array([])

    for i in range(len(Y)):
        el = Y[i]
        x = np.append(x, el[0])
        y = np.append(y, el[1])

    # 収束先を描画
    plt.rcParams['font.family'] = "Meiryo"
    fig = plt.figure(figsize=(6, 6), dpi=100)
    fig.subplots_adjust(left=0.2, bottom=0.2)
    ax = fig.add_subplot(1, 1, 1, xlabel='x', ylabel='y')
    ax.grid(color="#eeeeee", which="both")
    ax.set_axisbelow(True)

    ax.scatter(x, y, label='x-y', s=2)
    ax.legend()
    plt.show()

if __name__ == '__main__':
    main()