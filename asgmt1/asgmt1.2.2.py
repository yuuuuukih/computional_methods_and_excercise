import numpy as np
from mytyping.typing import VectorS
from function.newton_onedim import newton
import matplotlib.pyplot as plt

def f(x: float) -> float:
    return x**5 + x**4 - x**3 - x**2 - 2*x -2

def main():
    vec_x_ini: VectorS = np.linspace(-3, 3, 100)
    # print(vec_x_ini)
    vec_y_newton: VectorS = [newton(f, 100, x_ini, 1e-6)['sol'] for x_ini in vec_x_ini]
    # print(vec_y_newton)

    #誤差を描画
    plt.rcParams['font.family'] = "Meiryo"
    fig = plt.figure(figsize=(4,4), dpi=100)
    fig.subplots_adjust(left=0.2, bottom=0.2)
    ax = fig.add_subplot(1, 1, 1, xlabel="initial value", ylabel="answer")
    ax.grid(color="#eeeeee", which="both")
    ax.set_axisbelow(True)

    ax.scatter(vec_x_ini, vec_y_newton, label='newton')
    ax.legend()
    plt.show()

if __name__ == '__main__':
    main()