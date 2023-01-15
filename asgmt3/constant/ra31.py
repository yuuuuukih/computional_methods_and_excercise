import numpy as np

def ra31(h, tau):
    r = []
    for i in range(int(tau / h)):
        r.append([-np.cos(i*h), np.sin(i*h)])
    return r