import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from constant.const33 import N, delta_t, Ts, Td, a
from function.wave_eq_by_FDM import solve_wave_eq_by_FDM

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