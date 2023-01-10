import numpy as np
from tqdm import tqdm

def Heun_method(f, Y0, h, tmax):
    Y = np.array([Y0])
    for i in tqdm(range(int(tmax / h))):
        k1 = f(Y[i])
        k2 = f(Y[i] + h * k1)
        next_Y = Y[i] + h * 0.5 * (k1 + k2)
        Y = np.append(Y, next_Y).reshape(i+2, 2, 3)

    return Y