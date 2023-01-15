import numpy as np
from asgmt3.constant.const31 import r0, v0, tau, f
from function.Euler_method import Euler_method
from function.Heun_method import Heun_method
from function.Runge_Kutta_method import Runge_Kutta_method
from asgmt3.constant.ra31 import ra31
import matplotlib.pyplot as plt

def plt31_r(rx, ry):
    # 収束先を描画
    plt.rcParams['font.family'] = "Meiryo"
    fig = plt.figure(figsize=(6, 6), dpi=100)
    fig.subplots_adjust(left=0.2, bottom=0.2)
    ax = fig.add_subplot(1, 1, 1, xlabel='x', ylabel='y')
    ax.grid(color="#eeeeee", which="both")
    ax.set_axisbelow(True)

    ax.scatter(rx, ry, label='r', s=2)
    ax.legend()
    plt.show()

def plt31_er(er):
    # 収束先を描画
    plt.rcParams['font.family'] = "Meiryo"
    fig = plt.figure(figsize=(6, 6), dpi=100)
    fig.subplots_adjust(left=0.2, bottom=0.2)
    ax = fig.add_subplot(1, 1, 1, xlabel='time', ylabel='er')
    ax.grid(color="#eeeeee", which="both")
    ax.set_axisbelow(True)

    ax.scatter(np.arange(len(er)), er, label='er', s=2)
    ax.legend()
    plt.show()

def display31_r_e(method):
    # 初期値の設定(Y=[r, v]とする)
    Y0 = [r0, v0]
    h = tau / 64

    # Euler法、Heun法、Runge Kutta法で解く
    Y = Euler_method(f, Y0, h, tau) if method == 'Euler' else Heun_method(f, Y0, h, tau) if method == 'Heun' else Runge_Kutta_method(f, Y0, h, tau) if method == 'Runge_Kutta' else 'Error'
    if Y == 'Error':
        print('display31_r_e.py Error!')
        return

    rx = []
    ry = []
    for i in range(len(Y)):
        el = Y[i]
        rx.append(el[0][0])
        ry.append(el[0][1])

    # 誤差を計算
    ra = ra31(h, tau)
    er = []
    for i in range(len(ra)):
        next_er = np.linalg.norm(np.array([rx[i], ry[i]]) - np.array(ra[i]), ord=2)
        er.append(next_er)

    # 描画
    plt31_r(rx, ry)
    plt31_er(er)
