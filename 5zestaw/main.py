from math import gcd
from rekurencja import fibonacci as fib
import unittest


def add_frac(frac1, frac2):
    value = [frac1[0] * frac2[1] + frac2[0] * frac1[1], frac1[1] * frac2[1]]
    g = gcd(value[0], value[1])
    if g > 1:
        value[0] /= g
        value[1] /= g
    return value


def sub_frac(frac1, frac2):
    value = [frac1[0] * frac2[1] - frac2[0] * frac1[1], frac1[1] * frac2[1]]
    g = gcd(value[0], value[1])
    if g > 1:
        value[0] /= g
        value[1] /= g
    return value


def mul_frac(frac1, frac2):
    value = [frac1[0] * frac2[0], frac1[1] * frac2[1]]
    g = gcd(value[0], value[1])
    if g > 1:
        value[0] /= g
        value[1] /= g
    return value


def div_frac(frac1, frac2):
    try:
        assert frac2[0] != 0
        value = [frac1[0] * frac2[1], frac1[1] * frac2[0]]
        g = gcd(value[0], value[1])
        if g > 1:
            value[0] /= g
            value[1] /= g
    except AssertionError:
        raise ZeroDivisionError
    return value


def cmp_frac(frac1, frac2):
    if is_positive(frac1) and not is_positive(frac2):
        return 1
    elif is_positive(frac2) and not is_positive(frac1):
        return -1
    else:
        first = frac1[0] * frac2[1]
        second = frac2[0] * frac1[1]
        if first == second:
            return 0
        elif first < second:
            return -1
        else:
            return 1


def is_positive(frac):
    return False if frac[0] * frac[1] < 0 else True


def is_zero(frac):
    return False if frac[0] else True


def frac2float(frac):
    return frac[0] / frac[1]


class TestFractions(unittest.TestCase):
    def setUp(self):
        self.f1 = [1, 3]
        self.f2 = [2, 6]
        self.f3 = [6, 3]
        self.f0 = [0, 2]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], self.f1), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac(self.f2, self.f3), [-5, 3])

    def test_mul_frac(self):
        self.assertEqual(mul_frac(self.f1, self.f3), [2, 3])

    def test_div_frac(self):
        self.assertEqual(div_frac(self.f1, self.f3), [1, 6])
        self.assertEqual(div_frac(self.f2, self.f1), [1, 1])
        with self.assertRaises(ValueError):
            div_frac(self.f1, self.f0)

    def test_is_positive(self):
        f1 = [-1, -5]
        f2 = [1, -5]
        self.assertTrue(is_positive(f1))
        self.assertFalse(is_positive(f2))

    def test_is_zero(self):
        self.assertTrue(is_zero(self.f0))
        self.assertFalse(is_zero(self.f1))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(self.f1, self.f2), 0)
        self.assertEqual(cmp_frac([20, 18], [10, 18]), 1)
        self.assertEqual(cmp_frac([20, -18], [10, 18]), -1)

    def test_frac2float(self):
        self.assertAlmostEqual(frac2float(self.f1), 0.333, places=3, msg=None)

    def tearDown(self):
        pass


if __name__ == '__main__':
    print(fib(5)) #sprawdzam czy działa import z rekurencja.py
    unittest.main()


