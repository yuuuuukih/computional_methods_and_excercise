import numpy as np

def ra31(h, tau):
    r = np.array([])
    for i in range(int(tau / h)):
        r = np.append(r, [-np.cos(i*h), np.sin(i*h)]).reshape(-1, 2)
    return r