from tqdm import tqdm

def Runge_Kutta_method_31(f, Y0, h, tmax):
    Y = [Y0]
    for i in tqdm(range(int(tmax / h))):
        k1 = f(Y[i])
        k2 = f([[Y[i][j][k] + 0.5 * h * k1[j][k] for k in range(3)] for j in range(2)])
        k3 = f([[Y[i][j][k] + 0.5 * h * k2[j][k] for k in range(3)] for j in range(2)])
        k4 = f([[Y[i][j][k] + h * k3[j][k] for k in range(3)] for j in range(2)])
        next_Y = [[Y[i][j][k] + h / 6 * (k1[j][k] + 2*k2[j][k] + 2*k3[j][k] + k4[j][k]) for k in range(3)] for j in range(2)]
        Y.append(next_Y)
    return Y


def Runge_Kutta_method_32(f, Y0, h, tmax):
    Y = [Y0]
    for i in tqdm(range(int(tmax / h))):
        k1 = f(Y[i])
        k2 = f([Y[i][j] + 0.5 * h * k1[j] for j in range(2)])
        k3 = f([Y[i][j] + 0.5 * h * k2[j] for j in range(2)])
        k4 = f([Y[i][j] + h * k3[j] for j in range(2)])
        next_Y = [Y[i][j] + h / 6 * (k1[j] + 2*k2[j] + 2*k3[j] + k4[j]) for j in range(2)]
        Y.append(next_Y)
    return Y