import numpy as np

from linear_solver.core import solve_linear_system
from linear_solver.utils.general import get_fn

def test_zero_determinant():
    x = solve_linear_system(get_fn('p1coeffs.txt'))
    assert(x == None)

def test_integer_coefficients():
    x = solve_linear_system(get_fn('p2coeffs.txt'))
    assert(x.shape == (2, 1))

def test_eval_expressions():
    x = solve_linear_system(get_fn('p2coeffs.txt'))
    y = solve_linear_system(get_fn('exp_coeffs.txt'))
    assert(np.all(x==y))
