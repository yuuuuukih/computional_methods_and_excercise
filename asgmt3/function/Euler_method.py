import numpy as np

def Euler_method(Phi, Y0, h, tau):
    Y = np.array([Y0])
    for i in range(int(tau / h)):
        next_Y = Y[i] + h * Phi(Y[i])
        Y = np.append(Y, next_Y).reshape(i+2, 2, 3)

    return Y