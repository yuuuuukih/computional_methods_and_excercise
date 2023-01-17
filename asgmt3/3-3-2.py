import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# const33.py
#===============================================
N = 100
delta_x = 1 / N
delta_t = 0.001
tmax = 2
c = 5
Ts = 0.1
Td = 0.1

a = 0.01

mu = c**2 * delta_t**2 / delta_x**2


# wave_eq_by_FDM.py
#===============================================
# u[k][i]: tmax/delta_t x N
def solve_wave_eq_by_FDM(uk0, bc=0): # boundary condition: 0なら固定端、1なら自由端
    u = np.array([])
    for k in range(int(tmax / delta_t)):
        tk = k * delta_t
        next_uk = np.array([])

        if k == 0:
            next_uk = np.zeros(N)
        else:
            for i in range(N):
                if i == 0:
                    next_uk0 = uk0(tk)
                    next_uk = np.append(next_uk, next_uk0)
                elif i == N-1:
                    if bc == 0:
                        next_ukN_1 = -u[k-2 if k-2 >= 0 else 0][N-1] + mu * u[k-1][N-2] + 2 * (1 - mu) * u[k-1][N-1]
                        next_uk = np.append(next_uk, next_ukN_1)
                    else:
                        next_ukN_1 = -u[k-2 if k-2 >= 0 else 0][N-1] + mu * u[k-1][N-2] + (2 - mu) * u[k-1][N-1]
                        next_uk = np.append(next_uk, next_ukN_1)
                else:
                    next_uki = -u[k - 2 if k - 2 >= 0 else 0][i] + mu * u[k-1][i-1] + 2 * (1 - mu) * u[k-1][i] + mu * u[k-1][i+1]
                    next_uk = np.append(next_uk, next_uki)

        u = np.append(u, next_uk).reshape(-1, N)

    return u


# asgmt3.3.2.py
#===============================================
# x0における境界条件
def uk0(tk):
    return np.tanh((tk - Ts) / a) / 2 - np.tanh((tk - Ts - Td) / a) / 2

def main():
    u = solve_wave_eq_by_FDM(uk0, bc=1) # boundary condition: 0なら固定端、1なら自由端
    x = np.linspace(0, 1, N+1)[:N]

    # 収束先を描画
    plt.rcParams['font.family'] = "Meiryo"
    fig = plt.figure(figsize=(6, 6), dpi=100)
    fig.subplots_adjust(left=0.2, bottom=0.2)
    ax = fig.add_subplot(1, 1, 1, xlabel='x', ylabel='u')
    ax.grid(color="#eeeeee", which="both")
    ax.set_axisbelow(True)

    ims = []

    for i in range(len(u)):
        im = ax.scatter(x, u[i], s=2, color='k')
        title = ax.text(0.3, 1.28, f't={round(i*delta_t, 3)} sec', size='xx-large')
        ims.append([im, title])

    ani = animation.ArtistAnimation(fig, ims, interval=100, repeat_delay=500)
    # saveするときはコメントアウトを外す
    # ani.save('332_free_end.gif', writer='pillow', fps=20)
    plt.show()

if __name__ == '__main__':
    main()