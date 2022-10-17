from asgmt1.mytyping.typing import VectorS
from function.dichotomy_onedim import dichotomy
from function.scatter import simple_scatter

def f(x: float) -> float:
    return x**5 + x**4 - x**3 - x**2 - 2*x -2

def main():
    y: VectorS = dichotomy(f, 0, 2, 1e-6)
    x: list[int] = [i+1 for i in range(len(y))]

    simple_scatter(x, y, ylog=True)

if __name__ == '__main__':
    main()