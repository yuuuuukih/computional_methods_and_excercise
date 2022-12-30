import numpy as np
from tqdm import tqdm

def Runge_Kutta_method(f, Y0, h, tau):
    Y = np.array([Y0])
    for i in tqdm(range(int(tau / h))):
        k1 = f(Y[i])
        k2 = f(Y[i] + 0.5 * h * k1)
        k3 = f(Y[i] + 0.5 * h * k2)
        k4 = f(Y[i] + h * k3)
        next_Y = Y[i] + h / 6 * (k1 + 2*k2 + 2*k3 + k4)
        Y = np.append(Y, next_Y).reshape(i+2, 2, 3)

    return Y