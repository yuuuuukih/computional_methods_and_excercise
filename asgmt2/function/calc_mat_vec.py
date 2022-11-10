import numpy as np

def calc_mat_vec(mat, vec):
    n = len(mat)
    m = len(vec)
    if len(mat[0]) != m:
        print('Dimention Error!')
        return

    ans = np.zeros(n)
    for i in range(n):
        ans[i] = sum([mat[i][j] * vec[j] for j in range(m)])
    return ans