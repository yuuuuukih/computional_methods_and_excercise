import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


# cross_product.py
#===============================================
# 3次元ベクトルの外積を計算
def cross_product3(a, b):
    cross_vec = np.array([a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]])
    return cross_vec


# const31.py
#===============================================
r0 = [-1, 0, 0]
v0 = [0, 1, 0]
B = [0, 0, 1]
m = 1
q = 1
tau = 2 * np.pi * m / (q * np.linalg.norm(np.array(B), ord=2))

# fの設定
# Y = [r, v] = [[rx, ry, rz], [vx, vy, vz]]
def f(Y):
    dYdt = np.array([Y[1], q / m * cross_product3(Y[1], B)]).tolist()
    return dYdt


# Euler_method.py
#===============================================
def Euler_method(f, Y0, h, tmax):
    Y = [Y0]
    for i in tqdm(range(int(tmax / h))):
        G = f(Y[i])
        next_Y = [[Y[i][j][k] + h * G[j][k] for k in range(3)] for j in range(2)]
        Y.append(next_Y)
    return Y


# Heun_method.py
#===============================================
def Heun_method(f, Y0, h, tmax):
    Y = [Y0]
    for i in tqdm(range(int(tmax / h))):
        k1 = f(Y[i])
        k2 = f([[Y[i][j][k] + h * k1[j][k] for k in range(3)] for j in range(2)])
        next_Y = [[Y[i][j][k] + h * 0.5 * (k1[j][k] + k2[j][k]) for k in range(3)] for j in range(2)]
        Y.append(next_Y)
    return Y


# Runge_kutta_method.py
#===============================================
def Runge_Kutta_method_31(f, Y0, h, tmax):
    Y = [Y0]
    for i in tqdm(range(int(tmax / h))):
        k1 = f(Y[i])
        k2 = f([[Y[i][j][k] + 0.5 * h * k1[j][k] for k in range(3)] for j in range(2)])
        k3 = f([[Y[i][j][k] + 0.5 * h * k2[j][k] for k in range(3)] for j in range(2)])
        k4 = f([[Y[i][j][k] + h * k3[j][k] for k in range(3)] for j in range(2)])
        next_Y = [[Y[i][j][k] + h / 6 * (k1[j][k] + 2*k2[j][k] + 2*k3[j][k] + k4[j][k]) for k in range(3)] for j in range(2)]
        Y.append(next_Y)
    return Y


# ra31.py
#===============================================
def ra31(h, tau):
    r = []
    for i in range(int(tau / h)):
        r.append([-np.cos(i*h), np.sin(i*h)])
    return r


# dislay31_r_e.py
#===============================================
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
    Y = Euler_method(f, Y0, h, tau) if method == 'Euler' else Heun_method(f, Y0, h, tau) if method == 'Heun' else Runge_Kutta_method_31(f, Y0, h, tau) if method == 'Runge_Kutta' else 'Error'
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


# dislay31_Er.py
#===============================================
def plt31_Er(Er):
    # 収束先を描画
    plt.rcParams['font.family'] = "Meiryo"
    fig = plt.figure(figsize=(6, 6), dpi=100)
    fig.subplots_adjust(left=0.2, bottom=0.2)
    ax = fig.add_subplot(1, 1, 1, xlabel='p', ylabel='log2(Er)')
    ax.grid(color="#eeeeee", which="both")
    ax.set_axisbelow(True)

    ax.scatter(np.arange(5, 5+len(Er)), np.log2(Er), label='log2(Er)', s=2)
    ax.legend()
    plt.show()

# pmaxはpの最大値、linear_pmaxは一次関数で近似してよいと思われる区間でのpの最大値
def display31_Er(method, pmax=20, linear_pmax=-1):
    if linear_pmax == -1:
        linear_pmax = pmax

    # 初期値の設定(Y=[r, v]とする)
    Y0 = [r0, v0]

    Er = np.array([])
    for p in range(5, pmax+1):
        h = tau * 2**(-p)

        # Euler法、Heun法、Runge Kutta法で解く
        Y = Euler_method(f, Y0, h, tau) if method == 'Euler' else Heun_method(f, Y0, h, tau) if method == 'Heun' else Runge_Kutta_method_31(f, Y0, h, tau) if method == 'Runge_Kutta' else 'Error'
        if Y == 'Error':
            print('display31_Er.py Error!')
            return


        ra = ra31(h, tau)
        er = []
        for i in range(len(ra)):
            el = Y[i]
            next_er = np.linalg.norm(np.array([el[0][0], el[0][1]]) - np.array(ra[i]), ord=2)
            er.append(next_er)

        next_Er = np.amax(np.abs(er))
        Er = np.append(Er, next_Er)


    # 描画
    plt31_Er(Er)

    # 最小二乗法ではgnuplotやExcelを用いてよいとのことだったため、ライブラリを用いてもよいと解釈し、np.polyfitを使用する。
    coefficient = np.polyfit(np.arange(5, linear_pmax+1), np.log2(Er)[:linear_pmax-4], 1)
    print(f'a: {coefficient[0]}, b: {coefficient[1]}')


# asgmt3.1.4.py
#===============================================
def main():
    # Runge Kutta法で解く
    display31_r_e('Runge_Kutta')
    display31_Er('Runge_Kutta', 20, 14)

if __name__ == '__main__':
    main()