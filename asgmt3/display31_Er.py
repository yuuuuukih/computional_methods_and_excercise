import numpy as np
from asgmt3.constant.const31 import r0, v0, tau, f
from function.Euler_method import Euler_method
from function.Heun_method import Heun_method
from function.Runge_Kutta_method import Runge_Kutta_method_31
from asgmt3.constant.ra31 import ra31
import matplotlib.pyplot as plt


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
