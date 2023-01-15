from display31_r_e import display31_r_e
from display31_Er import display31_Er

def main():
    # Runge Kutta法で解く
    display31_r_e('Runge_Kutta')
    display31_Er('Runge_Kutta', 20, 14)

if __name__ == '__main__':
    main()