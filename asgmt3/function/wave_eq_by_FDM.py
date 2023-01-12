import numpy as np
from asgmt3.constant.const33 import N, delta_t, tmax, mu

# u[k][i]: tmax/delta_t x N
def solve_wave_eq_by_FDM(uk0, bc=0): # boundary condition: 0なら固定端、1なら自由端
    u = np.array([])
    for k in range(int(tmax / delta_t)):
        tk = k * delta_t
        next_uk = np.array([])

        if k == 0:
            next_uk = np.zeros(N)
        else:
            for i in range(N):
                if i == 0:
                    next_uk0 = uk0(tk)
                    next_uk = np.append(next_uk, next_uk0)
                elif i == N-1:
                    if bc == 0:
                        next_ukN_1 = -u[k-2 if k-2 >= 0 else 0][N-1] + mu * u[k-1][N-2] + 2 * (1 - mu) * u[k-1][N-1]
                        next_uk = np.append(next_uk, next_ukN_1)
                    else:
                        next_ukN_1 = -u[k-2 if k-2 >= 0 else 0][N-1] + mu * u[k-1][N-2] + (2 - mu) * u[k-1][N-1]
                        next_uk = np.append(next_uk, next_ukN_1)
                else:
                    next_uki = -u[k - 2 if k - 2 >= 0 else 0][i] + mu * u[k-1][i-1] + 2 * (1 - mu) * u[k-1][i] + mu * u[k-1][i+1]
                    next_uk = np.append(next_uk, next_uki)

        u = np.append(u, next_uk).reshape(-1, N)

    return u