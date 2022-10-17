# from function.scatter import simple_scatter
from mytyping.typing import VectorS
from function.newton_onedim import newton


def f(x: float) -> float:
    return x**5 + x**4 - x**3 - x**2 - 2*x -2

def main():
    y: VectorS = newton(f, 100, 1, 1e-6)
    x: list[int] = [i+1 for i in range(len(y))]

    #draw a graph
    # simple_scatter(x, y, ylog=True)




if __name__ == '__main__':
    main()