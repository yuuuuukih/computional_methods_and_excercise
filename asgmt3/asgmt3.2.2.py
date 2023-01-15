from constant.const32 import x0, y0, alpha1, beta1, alpha2, beta2 ,f
from function.Runge_Kutta_method import Runge_Kutta_method_32
import matplotlib.pyplot as plt


def get_balanced_solution(gamma):
    x = alpha2 / beta2
    y = (alpha1 * beta2 - alpha2 * gamma) / (beta1 * beta2)
    return x, y

def f322(Y):
    return f(Y, gamma=0.6)

def main():
    # Runge Kutta法で解く
    Y0 = [x0, y0]
    tmax = 20
    delta_t = 0.1
    Y = Runge_Kutta_method_32(f322, Y0, delta_t, tmax)

    x = []
    y = []

    for i in range(len(Y)):
        x.append(Y[i][0])
        y.append(Y[i][1])

    # 平衡解を取得
    balanced_x, balanced_y = get_balanced_solution(0.6)

    # 収束先を描画
    plt.rcParams['font.family'] = "Meiryo"
    fig = plt.figure(figsize=(6, 6), dpi=100)
    fig.subplots_adjust(left=0.2, bottom=0.2)
    ax = fig.add_subplot(1, 1, 1, xlabel='x', ylabel='y')
    ax.grid(color="#eeeeee", which="both")
    ax.set_axisbelow(True)

    ax.scatter(x, y, label='x-y', s=2)
    ax.scatter(balanced_x, balanced_y, label='balanced solution', s=2)
    ax.legend()
    plt.show()

if __name__ == '__main__':
    main()