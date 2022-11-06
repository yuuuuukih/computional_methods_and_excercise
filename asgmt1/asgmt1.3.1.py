import numpy as np
from mytyping.typing import VectorS, VectorF, MatrixS
from function.newton_mutidim import newton_multidim
import matplotlib.pyplot as plt

def f1(vec_x: VectorS) -> float:
    x1, x2 = vec_x
    return x1**3 - 3 * x1 * x2**2 - 1

def f2(vec_x: VectorS) -> float:
    x1, x2 = vec_x
    return 3 * x1**2 * x2 - x2**3

def main():
    vec_f: VectorF = [f1, f2]
    vec_x0: VectorS = [np.sqrt(2), np.sqrt(2)]
    sols: MatrixS = []
    for i in range(20):
        output = newton_multidim(vec_f, i, vec_x0)
        sols.append(output['sol'])
        i += 1


    np_sols = np.array(sols).T
    print(np_sols.T[-1])

    plt.rcParams['font.family'] = "Meiryo"
    fig = plt.figure(figsize=(4, 4), dpi=100)
    fig.subplots_adjust(left=0.2, bottom=0.2)
    ax = fig.add_subplot(1, 1, 1, xlabel="x", ylabel="y")
    ax.grid(color="#eeeeee", which="both")
    ax.set_axisbelow(True)

    ax.plot(np_sols[0], np_sols[1], label='(√2, √2)')
    ax.legend()
    plt.show()


if __name__ == '__main__':
    main()