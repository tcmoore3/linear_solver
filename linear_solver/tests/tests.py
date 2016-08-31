import numpy as np
import unittest

from linear_solver.core import solve_linear_system
from linear_solver.utils.general import get_fn

class TestSolverMethods(unittest.TestCase):
    def test_zero_determinant(self):
        x = solve_linear_system(get_fn('p1coeffs.txt'))
        self.assertEqual(x, None)

    def test_integer_coefficients(self):
        x = solve_linear_system(get_fn('p2coeffs.txt'))
        self.assertEqual(x.shape, (2, 1))

    def test_eval_expressions(self):
        x = solve_linear_system(get_fn('p2coeffs.txt'))
        y = solve_linear_system(get_fn('exp_coeffs.txt'))
        self.assertTrue(np.all(x==y))

    def test_good_list_input(self):
        x = solve_linear_system([
            [22, 22, -1, 0],
            [0.1*22, 22*0.9, -0.6, 0],
            [22/0.68, 22/0.78, 0, 500*3.78541]])

    def test_bad_list_input(self):
        with self.assertRaises(AssertionError):
            x = solve_linear_system([
                [22, 22, -1, 0],
                [0.1*22, 22*0.9, -0.6, 0],
                [22/0.68, 22/0.78, 500*3.78541]])

    def test_good_array_input(self):
        x = solve_linear_system(
            np.asarray([
            [22, 22, -1, 0],
            [0.1*22, 22*0.9, -0.6, 0],
            [22/0.68, 22/0.78, 0, 500*3.78541]]))

    def test_bad_array_input(self):
        x = solve_linear_system(
            np.asarray([
            [22, 22, -1, 0],
            [0.1*22, 22*0.9, -0.6, 0],
            [22/0.68, 22/0.78, 0, 500*3.78541]]))

    def test_good_matrix_input(self):
        x = solve_linear_system(
            np.matrix([
            [22, 22, -1, 0],
            [0.1*22, 22*0.9, -0.6, 0],
            [22/0.68, 22/0.78, 0, 500*3.78541]]))

    def test_bad_matrix_input(self):
        x = solve_linear_system(
            np.matrix([
            [22, 22, -1, 0],
            [0.1*22, 22*0.9, -0.6, 0],
            [22/0.68, 22/0.78, 0, 500*3.78541]]))

if __name__ == '__main__':
    unittest.main()
