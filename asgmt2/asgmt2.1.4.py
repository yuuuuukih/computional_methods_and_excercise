from const_value import A, b1
from function.ICCG_method import calc_ICCG_method

def main():
    x = calc_ICCG_method(A, b1)
    print(x[-1])

if __name__ == '__main__':
    main()