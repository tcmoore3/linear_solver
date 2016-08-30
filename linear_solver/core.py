import numpy as np


def _check_inverse(coeffs):
    det = np.linalg.det(coeffs)
    #import ipdb; ipdb.set_trace()
    if np.isclose(det, 0.0):
        raise ZeroDivisionError

def _load_coefficients(coefficients_file):
    coeffs = np.genfromtxt(coefficients_file, dtype=str)
    assert(coeffs.ndim == 2)#, 'Input matrix must be 2 dimensional')
    assert(coeffs.shape[0]+1 == coeffs.shape[1])
    coeffs = np.matrix([[eval(x) for x in row] for row in coeffs])
    return coeffs

def _check_matrices(coeffs, consts):
    assert(coeffs.shape[0] == coeffs.shape[1])
    assert(coeffs.shape[0] == consts.shape[0])
    assert(consts.shape[1] == 1)

def solve_linear_system(coefficients_file):
    coeffs = _load_coefficients(coefficients_file)
    a, b = coeffs[:, :-1], coeffs[:, -1]
    _check_matrices(a, b)
    try:
        _check_inverse(a)
        return a.I * b
    except ZeroDivisionError:
        print('Determinant of coefficients matrix is 0. No unique solution.')
        return None
