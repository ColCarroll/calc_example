import math
import unittest
from calc import Function


class TestFunction(unittest.TestCase):
    def setUp(self):
        self.x_squared = Function(lambda x: x * x)
        self.sine = Function(lambda x: math.sin(x))

    def test_call(self):
        self.assertEqual(self.x_squared(2), 2 * 2)
        self.assertEqual(self.sine(2), math.sin(2))

    def test_derivatives(self):
        self.assertAlmostEqual(self.x_squared.prime()(2), 2 * 2, places=3)  # (x^2)' = 2x
        self.assertAlmostEqual(self.sine.prime()(2), math.cos(2), places=3)  # (sin(x))' = cos(x)

    def test_indefinite_integral(self):
        for side in ("left", "right", "center"):
            self.assertAlmostEqual(self.x_squared.integral(side=side)(3), 3 ** 3 / 3., places=3)
            self.assertAlmostEqual(self.sine.integral(side=side)(3), 1-math.cos(3), places=3)

    def test_definite_integral(self):
        for side in ("left", "right", "center"):
            self.assertAlmostEqual(self.x_squared.integral(lims=[-2, 3], side=side), 3 ** 3 / 3. - (-2) ** 3 / 3., places=3)
            self.assertAlmostEqual(self.sine.integral(lims=[1, 3], side=side), -math.cos(3) - (-math.cos(1)), places=3)

    def test_fundamental_theorem_of_calculus(self):
        for j in range(-5, 5):
            self.assertAlmostEqual(self.x_squared.integral().prime()(j), self.x_squared(j), places=3)
            self.assertAlmostEqual(self.sine.integral().prime()(j), self.sine(j), places=3)
