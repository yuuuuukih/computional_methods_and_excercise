import numpy as np
from tqdm import tqdm

def Runge_Kutta_method(f, Y0, h, tmax):
    Y = [Y0]
    for i in tqdm(range(int(tmax / h))):
        k1 = f(Y[i])
        k2 = f([[Y[i][j][k] + 0.5 * h * k1[j][k] for k in range(3)] for j in range(2)])
        k3 = f([[Y[i][j][k] + 0.5 * h * k2[j][k] for k in range(3)] for j in range(2)])
        k4 = f([[Y[i][j][k] + h * k3[j][k] for k in range(3)] for j in range(2)])
        next_Y = [[Y[i][j][k] + h / 6 * (k1[j][k] + 2*k2[j][k] + 2*k3[j][k] + k4[j][k]) for k in range(3)] for j in range(2)]
        # 3.1と3.2でY0の次元が異なるため、ndim=1,2で場合分けして対応
        # Y = np.append(Y, next_Y).reshape(i+2, Y0.shape[0], Y0.shape[1]) if Y0.ndim == 2 else np.append(Y, next_Y).reshape(i+2, Y0.shape[0])
        Y.append(next_Y)
    return Y