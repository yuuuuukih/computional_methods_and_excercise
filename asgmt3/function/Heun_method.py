from tqdm import tqdm

def Heun_method(f, Y0, h, tmax):
    Y = [Y0]
    for i in tqdm(range(int(tmax / h))):
        k1 = f(Y[i])
        k2 = f([[Y[i][j][k] + h * k1[j][k] for k in range(3)] for j in range(2)])
        next_Y = [[Y[i][j][k] + h * 0.5 * (k1[j][k] + k2[j][k]) for k in range(3)] for j in range(2)]
        Y.append(next_Y)
    return Y