import numpy as np
from const_value import A, b2, b3, alpha2, alpha3
from function.iterative_method import calc_iterative_method
import matplotlib.pyplot as plt

def plt_asgmt222(b, alpha, omega, eps=1e-10):
    output_jac = calc_iterative_method(A, b, alpha, EPS=eps)
    output_gau = calc_iterative_method(A, b, alpha, method='gauss_seidel', EPS=eps)
    output_sor = calc_iterative_method(A, b, alpha, method='sor', omega=omega, EPS=eps)  # 1: 1.852, 2: , 3: 1

    # 収束先を描画
    plt.rcParams['font.family'] = "Meiryo"
    plt.rcParams['font.size'] = 8
    fig = plt.figure(figsize=(8, 8), dpi=150)

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

def main():
    plt_asgmt222(b2, alpha2, omega=1.9, eps=1e-2)
    plt_asgmt222(b3, alpha3, omega=1.8, eps=1e-20)

if __name__ == '__main__':
    main()