import numpy as np
from const_value import A, b1, alpha1
from function.iterative_method import calc_iterative_method
import matplotlib.pyplot as plt


def main():
    output_jac = calc_iterative_method(A, b1, alpha1)
    output_gau = calc_iterative_method(A, b1, alpha1, method='gauss_seidel')
    output_sor = calc_iterative_method(A, b1, alpha1, method='sor', omega=1.852)

    # 収束先を描画
    plt.rcParams['font.family'] = "Meiryo"
    plt.rcParams['font.size'] = 8
    fig = plt.figure(figsize=(8, 8), dpi=150)
    # fig.subplots_adjust(left=0.2, bottom=0.2)
    ax0 = fig.add_subplot(2, 2, 1, xlabel='count', ylabel='r, e')
    ax1 = fig.add_subplot(2, 2, 2, xlabel='count', ylabel='r, e')
    ax2 = fig.add_subplot(2, 2, 3, xlabel='count', ylabel='r, e')
    ax3 = fig.add_subplot(2, 2, 4, xlabel='count', ylabel='r, e')

    axs = [ax0, ax1, ax2, ax3]
    for i in range(len(axs)):
        ax = axs[i]
        ax.grid(color="#eeeeee", which="both")
        ax.set_axisbelow(True)
        ax.set_xscale('log')
        ax.set_yscale('log')

        if i == 3:
            ax.scatter(np.arange(len(output_sor['e'])), output_sor['e'], label='e_sor', s=2)
            ax.scatter(np.arange(len(output_sor['r'])), output_sor['r'], label='r_sor', s=2)
        elif i == 2:
            ax.scatter(np.arange(len(output_gau['e'])), output_gau['e'], label='e_gauss_seidel', s=2)
            ax.scatter(np.arange(len(output_gau['r'])), output_gau['r'], label='r_gauss_seidel', s=2)
        elif i == 1:
            ax.scatter(np.arange(len(output_jac['e'])), output_jac['e'], label='e_jacobi', s=2)
            ax.scatter(np.arange(len(output_jac['r'])), output_jac['r'], label='r_jacobi', s=2)
        else:
            ax.scatter(np.arange(len(output_sor['e'])), output_sor['e'], label='e_sor', s=2)
            ax.scatter(np.arange(len(output_gau['e'])), output_gau['e'], label='e_gauss_seidel', s=2)
            ax.scatter(np.arange(len(output_jac['e'])), output_jac['e'], label='e_jacobi', s=2)
            ax.scatter(np.arange(len(output_jac['r'])), output_jac['r'], label='r_jacobi', s=2)
            ax.scatter(np.arange(len(output_gau['r'])), output_gau['r'], label='r_gauss_seidel', s=2)
            ax.scatter(np.arange(len(output_sor['r'])), output_sor['r'], label='r_sor', s=2)

        ax.legend(title='algorithm')

    plt.show()

if __name__ == '__main__':
    main()