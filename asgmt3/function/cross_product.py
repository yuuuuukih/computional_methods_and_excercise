import numpy as np

def cross_product3(a, b):
    cross_vec = np.array([a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]])
    return cross_vec