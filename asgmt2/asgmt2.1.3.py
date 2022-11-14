import numpy as np
from const_value import A, b1, alpha1
from function.iterative_method import calc_iterative_method
import matplotlib.pyplot as plt

def get_residual_norm(vecs, TRUE_VECTOR):
    e = np.array([])
    for vec in vecs:
        e = np.append(e, np.linalg.norm((vec - TRUE_VECTOR), ord=2))
    return e

def main():
    output_jac = calc_iterative_method(A, b1)
    output_gau = calc_iterative_method(A, b1, method='gauss_seidel')
    output_sor = calc_iterative_method(A, b1, method='sor', omega=1.852)

    r_jac = get_residual_norm(output_jac['sol'], alpha1)
    r_gau = get_residual_norm(output_gau['sol'], alpha1)
    r_sor = get_residual_norm(output_sor['sol'], alpha1)


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
            ax.scatter(np.arange(len(r_sor)), r_sor, label='e_sor', s=2)
            ax.scatter(np.arange(len(output_sor['err'])), output_sor['err'], label='r_sor', s=2)
        elif i == 2:
            ax.scatter(np.arange(len(r_gau)), r_gau, label='e_gauss_seidel', s=2)
            ax.scatter(np.arange(len(output_gau['err'])), output_gau['err'], label='r_gauss_seidel', s=2)
        elif i == 1:
            ax.scatter(np.arange(len(r_jac)), r_jac, label='e_jacobi', s=2)
            ax.scatter(np.arange(len(output_jac['err'])), output_jac['err'], label='r_jacobi', s=2)
        else:
            ax.scatter(np.arange(len(r_jac)), r_jac, label='e_jacobi', s=2)
            ax.scatter(np.arange(len(r_gau)), r_gau, label='e_gauss_seidel', s=2)
            ax.scatter(np.arange(len(r_sor)), r_sor, label='e_sor', s=2)
            ax.scatter(np.arange(len(output_jac['err'])), output_jac['err'], label='r_jacobi', s=2)
            ax.scatter(np.arange(len(output_gau['err'])), output_gau['err'], label='r_gauss_seidel', s=2)
            ax.scatter(np.arange(len(output_sor['err'])), output_sor['err'], label='r_sor', s=2)

        ax.legend(title='algorithm')

    plt.show()

if __name__ == '__main__':
    main()