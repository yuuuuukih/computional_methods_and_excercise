from tqdm import tqdm

def Euler_method(f, Y0, h, tmax):
    Y = [Y0]
    for i in tqdm(range(int(tmax / h))):
        G = f(Y[i])
        next_Y = [[Y[i][j][k] + h * G[j][k] for k in range(3)] for j in range(2)]
        Y.append(next_Y)
    return Y