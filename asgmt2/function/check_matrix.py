# Aが上三角行列のときはlower=0
def check_for_tringular_matrix(A, lower=1):
    n = len(A)

    if len(A[0]) != n:
        print('Matrix is not square!')

    name = 'lower' if lower == 1 else 'upper'
    if lower != 1:
        A = A.T

    # Aが下三角行列か否かのチェック
    for i in range(n):
        for j in range(i + 1, n):
            if A[i][j] != 0:
                print(f'Matrix is not {name} triangular matrix!')
                return
            j += 1
        i += 1