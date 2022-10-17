import matplotlib.pyplot as plt

def simple_scatter(x: list[int | float], y: list[int | float], xlabel='xlabel', ylabel='ylabel', xlog=False, ylog=False):
    plt.rcParams['font.family'] = "Meiryo"
    fig = plt.figure(figsize=(4,4), dpi=100)
    fig.subplots_adjust(left=0.2, bottom=0.2)
    ax = fig.add_subplot(1, 1, 1, xlabel=xlabel, ylabel=ylabel)
    ax.grid(color="#eeeeee", which="both")
    ax.set_axisbelow(True)

    if xlog:
        ax.set_xscale('log')
    if ylog:
        ax.set_yscale('log')

    ax.scatter(x, y)
    ax.legend()
    plt.show()