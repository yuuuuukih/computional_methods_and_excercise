from function.QR_method import get_eigen_value_by_QR
from const_value import A

def main():
    ev = get_eigen_value_by_QR(A)
    print(ev)

if __name__ == '__main__':
    main()