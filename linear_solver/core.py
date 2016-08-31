import numpy as np


def _check_inverse(coeffs):
    det = np.linalg.det(coeffs)
    #import ipdb; ipdb.set_trace()
    if np.isclose(det, 0.0):
        raise ZeroDivisionError

def _matrix_sanity(coeffs):
    assert(coeffs.ndim == 2)#, 'Input matrix must be 2 dimensional')
    assert(coeffs.shape[0]+1 == coeffs.shape[1])

def _load_coefficients(coefficients_file):
    coeffs = np.genfromtxt(coefficients_file, dtype=str)
    _matrix_sanity(coeffs)
    coeffs = np.matrix([[eval(x) for x in row] for row in coeffs])
    return coeffs

def _check_matrices(coeffs, consts):
    assert(coeffs.shape[0] == coeffs.shape[1])
    assert(coeffs.shape[0] == consts.shape[0])
    assert(consts.shape[1] == 1)

def _list_to_matrix(coefficients):
    for l in coefficients:
        assert(len(l) == len(coefficients[0]))
    coeffs = np.matrix(coefficients)
    _matrix_sanity(coeffs)
    return coeffs

def handle_input(coefficients):
    if isinstance(coefficients, str):
        return _load_coefficients(coefficients)
    elif isinstance(coefficients, list):
        return _list_to_matrix(coefficients)
    elif isinstance(coefficients, np.ndarray):
        _matrix_sanity(coefficients)
        return np.matrix(coefficients)
    else:
        raise(TypeError, 'Unsupported input type.')

def solve_linear_system(coefficients):
    coeffs = handle_input(coefficients)
    A = coeffs[:, :-1]
    B = coeffs[:, -1].reshape((-1, 1))
    _check_matrices(A, B)
    try:
        _check_inverse(A)
        return A.I * B
    except ZeroDivisionError:
        print('Determinant of coefficients matrix is 0. No unique solution.')
        return None
