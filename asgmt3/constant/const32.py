import numpy as np

x0 = 1.5
y0 = 1

alpha1 = 2
alpha2 = 1.5
beta1 = 4
beta2 = 1.5

# fの設定
# Y = [x, y]
def f(Y, gamma):
    dxdt = (alpha1 - gamma * Y[0] - beta1 * Y[1]) * Y[0]
    dydt = (-alpha2 + beta2 * Y[0]) * Y[1]
    dYdt = np.array([dxdt, dydt])
    return dYdt