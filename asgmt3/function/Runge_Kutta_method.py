import numpy as np
from tqdm import tqdm

def Runge_Kutta_method(f, Y0, h, tmax):
    Y = np.array([Y0])
    for i in tqdm(range(int(tmax / h))):
        k1 = f(Y[i])
        k2 = f(Y[i] + 0.5 * h * k1)
        k3 = f(Y[i] + 0.5 * h * k2)
        k4 = f(Y[i] + h * k3)
        next_Y = Y[i] + h / 6 * (k1 + 2*k2 + 2*k3 + k4)
        # 3.1と3.2でY0の次元が異なるため、ndim=1,2で場合分けして対応
        Y = np.append(Y, next_Y).reshape(i+2, Y0.shape[0], Y0.shape[1]) if Y0.ndim == 2 else np.append(Y, next_Y).reshape(i+2, Y0.shape[0])

    return Y