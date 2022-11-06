from mytyping.typing import VectorS
from function.newton_onedim import newton
from function.dichotomy_onedim import dichotomy
import matplotlib.pyplot as plt


def f(x: float) -> float:
    return x**5 + x**4 - x**3 - x**2 - 2*x -2

def scatter_asgmt121(x_newton, y_newton, x_dichotomy, y_dichotomy):
    plt.rcParams['font.family'] = "Meiryo"
    fig = plt.figure(figsize=(4,4), dpi=100)
    fig.subplots_adjust(left=0.2, bottom=0.2)
    ax = fig.add_subplot(1, 1, 1, xlabel="count", ylabel="error")
    ax.grid(color="#eeeeee", which="both")
    ax.set_axisbelow(True)

    ax.set_yscale('log')

    ax.scatter(x_newton, y_newton, label='newton')
    ax.scatter(x_dichotomy, y_dichotomy, label='dichotomy')
    ax.legend(title="algorithm")
    plt.show()

def main():
    y_newton: VectorS = newton(f, 100, 1, 1e-6)['err']
    x_newton: list[int] = [i+1 for i in range(len(y_newton))]

    y_dichotomy: VectorS = dichotomy(f, 0, 2, 1e-6)['err']
    x_dichotomy: list[int] = [i + 1 for i in range(len(y_dichotomy))]

    #誤差を描画
    scatter_asgmt121(x_newton, y_newton, x_dichotomy, y_dichotomy)


if __name__ == '__main__':
    main()