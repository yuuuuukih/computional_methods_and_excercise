from asgmt1.mytyping.typing import VectorS, MatrixS

def exchange_with_computable_row(mat: MatrixS, i: int) -> None:
    eps: float = 1e-4
    if abs(mat[i][i]) < eps:
        j: int = 0
        exchangeable_vector: VectorS = mat[i + 1 + j]
        while abs(exchangeable_vector[i]) < eps:
            j += 1
            exchangeable_vector = mat[i + 1 + j]

        mat[i], exchangeable_vector = exchangeable_vector, mat[i]
        mat[i + 1 + j] = exchangeable_vector

def devide_a_vec_by_a_const(vec: VectorS, divisor: float) -> VectorS:
    return [el / divisor for el in vec]

#メインアルゴリズム
def solve_by_gaussian_elimination(A: MatrixS, b: VectorS) -> VectorS:
    if len(A) != len(b):
        return -1
    dim: int = len(b)

    #拡大係数行列の生成
    aug_mat: MatrixS = [A[i] + [b[i]] for i in range(dim)]

    #拡大係数行列を上三角行列に変換する(A|b)->(A'|b')
    # -------------------------------------------
    for i in range(dim):
        #aug_matのii成分が０にならないようにする
        exchange_with_computable_row(aug_mat, i)

        #ii成分の係数を1にする
        aug_mat[i] = devide_a_vec_by_a_const(aug_mat[i], aug_mat[i][i])

        #i+1行以降のi列の係数をすべて0にする
        for k in range(1, dim - i):
            aug_mat[i + k] = [aug_mat[i + k][j] - aug_mat[i][j] * aug_mat[i + k][i] for j in range(dim + 1)]
    # -------------------------------------------

    # 拡大係数行列の左を単位行列にする(A'|b')->(E|x)
    # -------------------------------------------
    row: int = dim - 1
    while row > 0:
        for i in range(row):
            aug_mat[i] = [aug_mat[i][j] - aug_mat[i][row] * aug_mat[row][j] for j in range(dim + 1)]
        row -= 1
    # -------------------------------------------

    #拡大係数行列の最も右をxに当てはめる
    x: VectorS = [aug_mat[i][dim] for i in range(dim)]

    # print(aug_mat)
    # print(x)

    return x