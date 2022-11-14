import numpy as np
from const_value import A, b1
from function.iterative_method import calc_iterative_method
import matplotlib.pyplot as plt

def main():
    output_jac = calc_iterative_method(A, b1)
    output_gau = calc_iterative_method(A, b1, method='gauss_seidel')
    output_sor = calc_iterative_method(A, b1, method='sor', omega=1.852)


    # 収束先を描画
    plt.rcParams['font.family'] = "Meiryo"
    fig = plt.figure(figsize=(6, 6), dpi=100)
    fig.subplots_adjust(left=0.2, bottom=0.2)
    ax = fig.add_subplot(1, 1, 1, xlabel='count', ylabel='r')
    ax.grid(color="#eeeeee", which="both")
    ax.set_axisbelow(True)
    ax.set_xscale('log')
    ax.set_yscale('log')

    ax.scatter(np.arange(len(output_jac['r'])), output_jac['r'], label='jacobi', s=2)
    ax.scatter(np.arange(len(output_gau['r'])), output_gau['r'], label='gauss_seidel', s=2)
    ax.scatter(np.arange(len(output_sor['r'])), output_sor['r'], label='sor', s=2)
    ax.legend(title='algorithm')
    plt.show()

if __name__ == '__main__':
    main()