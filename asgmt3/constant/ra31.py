import numpy as np

# 課題3.1におけるraを定義(omega=1)
def ra31(h, tau):
    r = np.array([])
    for i in range(int(tau / h)):
        r = np.append(r, [-np.cos(i*h), np.sin(i*h)]).reshape(-1, 2)
    return r