from display31_r_e import display31_r_e
from display31_Er import display31_Er

def main():
    # Heun法で解く
    display31_r_e('Heun')
    display31_Er('Heun', 20)

if __name__ == '__main__':
    main()