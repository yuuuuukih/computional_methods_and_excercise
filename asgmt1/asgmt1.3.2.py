import numpy as np
import pandas as pd
from mytyping.typing import VectorS, VectorF, MatrixS, TrueSolDict
from function.newton_mutidim import newton_multidim
from typing import Final
import matplotlib.pyplot as plt


def f1(vec_x: VectorS) -> float:
    x1, x2 = vec_x
    return x1**3 - 3 * x1 * x2**2 - 1

def f2(vec_x: VectorS) -> float:
    x1, x2 = vec_x
    return 3 * x1**2 * x2 - x2**3

#PとQのユークリッド距離を求める
def calc_distance(P: VectorS, Q: VectorS) -> float:
    dist_squared: float = 0
    for i in range(len(P)):
        dist_squared += (P[i] - Q[i])**2
    return np.sqrt(dist_squared)

def generate_vectors(x_min: float, x_max: float, y_min: float, y_max: float, number_of_1d_partitions: int) -> MatrixS:
    vecs: MatrixS = []

    # 初期値ベクトルのリストを、縦横[-2, 2]かつNUMBER_OF_1D_PARTITIONSで分割
    for i in range(number_of_1d_partitions):
        x = np.linspace(x_min, x_max, number_of_1d_partitions)
        for j in range(number_of_1d_partitions):
            y = np.linspace(y_min, y_max, number_of_1d_partitions)
            vecs.append([x[i], y[j]])
    # 初期値が[0, 0]のときは計算不可なので取り除く
    vecs = [vec for vec in vecs if vec != [0, 0]]

    return vecs

def main():
    vec_f: VectorF = [f1, f2]
    #[-2,2]x[-2,2]を分割し、初期値としてvec_x0sに保存
    vec_x0s: MatrixS = generate_vectors(-2, 2, -2, 2, 80)
    df1 = pd.DataFrame(vec_x0s, columns=['x_ini', 'y_ini'])

    #それぞれの初期値に対する数値解をvec_solsに保尊
    vec_sols: MatrixS = []
    for vec_x0 in vec_x0s:
        vec_sols.append(newton_multidim(vec_f, 80, vec_x0)['sol'])
    df2 = pd.DataFrame(vec_sols, columns=['x_sol', 'y_sol'])

    #colがx_ini, y_ini, x_sol, y_solになるdfを生成
    df = pd.concat([df1, df2], axis=1)

    TRUE_SOLS: Final[list[TrueSolDict]] = [
        {'label': '(1, 0)', 'true_sol': [1, 0]},
        {'label': '(-1/2, √3/2)', 'true_sol': [-1/2, np.sqrt(3)/2]},
        {'label': '(-1/2, -√3/2)', 'true_sol': [-1/2, -np.sqrt(3)/2]},
        {'label': 'other'}
    ]

    #解に応じて分類分けする
    eps = 1e-3
    for i in range(len(df.index)):
        if calc_distance(df.loc[i, 'x_sol': 'y_sol'], TRUE_SOLS[0]['true_sol']) < eps:
            df.loc[i, 'type_of_sol'] = TRUE_SOLS[0]['label']
        elif calc_distance(df.loc[i, 'x_sol': 'y_sol'], TRUE_SOLS[1]['true_sol']) < eps:
            df.loc[i, 'type_of_sol'] = TRUE_SOLS[1]['label']
        elif calc_distance(df.loc[i, 'x_sol': 'y_sol'], TRUE_SOLS[2]['true_sol']) < eps:
            df.loc[i, 'type_of_sol'] = TRUE_SOLS[2]['label']
        else:
            df.loc[i, 'type_of_sol'] = TRUE_SOLS[3]['label']


    #描画
    plt.rcParams['font.family'] = "Meiryo"
    fig = plt.figure(figsize=(6,6), dpi=100)
    fig.subplots_adjust(left=0.2, bottom=0.2)
    ax = fig.add_subplot(1, 1, 1, xlabel="x_ini", ylabel="y_ini")
    ax.grid(color="#eeeeee", which="both")
    ax.set_axisbelow(True)

    for i in range(len(TRUE_SOLS)):
        ax.scatter(df[df['type_of_sol'] == TRUE_SOLS[i]['label']]['x_ini'],
                   df[df['type_of_sol'] == TRUE_SOLS[i]['label']]['y_ini'],
                   label=TRUE_SOLS[i]['label'])

    ax.legend(title='type_of_sol')
    plt.show()

    return 0

if __name__ == '__main__':
    main()