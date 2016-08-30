import numpy as np

def check_inverse(coeffs):
    det = np.linalg.det(coeffs)
    #import ipdb; ipdb.set_trace()
    if np.isclose(det, 0.0):
        raise ZeroDivisionError

def load_files(coefficients_file, constants_file):
    coeffs = np.matrix([[eval(x) for x in row] for row in 
        np.genfromtxt(coefficients_file, dtype=str)])
    consts = np.matrix([[eval(x) for x in row] for row in 
        np.genfromtxt(constants_file, dtype=str).reshape((-1, 1))])
    return coeffs, consts

def solve_linear_system(coefficients_file, constants_file):
    coeffs, consts = load_files(coefficients_file, constants_file)
    try:
        check_inverse(coeffs)
        return coeffs.I * consts
    except ZeroDivisionError:
        print('Determinant of coefficients matrix is 0. No solution.')
        return ZeroDivisionError
