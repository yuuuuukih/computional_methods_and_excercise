import numpy as np
from asgmt3.function.cross_product import cross_product3

r0 = [-1, 0, 0]
v0 = [0, 1, 0]

B = [0, 0, 1]
m = 1
q = 1
tau = 2 * np.pi * m / (q * np.linalg.norm(np.array(B), ord=2))


# fの設定
# Y = [r, v] = [[rx, ry, rz], [vx, vy, vz]]
def f(Y):
    dYdt = np.array([Y[1], q / m * cross_product3(Y[1], B)]).tolist()
    return dYdt