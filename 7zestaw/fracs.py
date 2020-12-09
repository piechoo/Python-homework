from math import gcd
import unittest


class Frac:
    def __init__(self, x=0, y=1):
        try:
            assert y != 0
            self.x = x
            self.y = y
            g = gcd(self.x, self.y)
            if g > 1:
                self.x /= g
                self.y /= g
        except AssertionError:
            raise ValueError

    def __str__(self):
        if self.y == 1:
            return "{}".format(self.x)
        else:
            return "{0} / {1}".format(self.x, self.y)

    def __repr__(self):
        return "Frac({0},{1})".format(self.x, self.y)

    def __eq__(self, other):
        if type(other) is float:
            temp = other.as_integer_ratio()
            other = Frac(temp[0], temp[1])
        elif type(other) is not Frac:
            other = Frac(other, 1)
        if self.y == other.y and self.x == other.x:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        first = self.x * other.y
        second = self.y * other.x
        return first < second

    def __le__(self, other):
        first = self.x * other.y
        second = self.y * other.x
        return first <= second

    def __add__(self, other):
        if type(other) is float:
            temp = other.as_integer_ratio()
            other = Frac(temp[0], temp[1])
        if isinstance(other, Frac):
            return Frac(int(self.x * other.y + self.y * other.x), int(self.y * other.y))
        else:
            return Frac(int(self.x + self.y * other), self.y)

    def __radd__(self, other):
        if type(other) is float:
            temp = other.as_integer_ratio()
            other = Frac(temp[0], temp[1])
        if isinstance(other, Frac):
            return self + other
        else:
            return Frac(int(self.x + self.y * other), self.y)

    def __sub__(self, other):
        if type(other) is int:
            other = Frac(other, 1)
        elif type(other) is float:
            temp = other.as_integer_ratio()
            other = Frac(temp[0], temp[1])
        return Frac(int(self.x * other.y - self.y * other.x),
                    int(self.y * other.y))

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if type(other) is int:
            other = Frac(other, 1)
        elif type(other) is float:
            temp = other.as_integer_ratio()
            other = Frac(temp[0], temp[1])
        return Frac(self.x * other.x,
                    self.y * other.y)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other) is int:
            other = Frac(other, 1)
        elif type(other) is float:
            temp = other.as_integer_ratio()
            other = Frac(temp[0], temp[1])
        try:
            assert other.x != 0
        except AssertionError:
            raise ZeroDivisionError
        return Frac(int(self.x * other.y),
                    int(self.y * other.x))

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):
        return Frac(self.y, self.x)

    def __float__(self):
        return self.x / self.y


class TestFractions(unittest.TestCase):
    def setUp(self):
        self.f1 = Frac(1, 3)
        self.f2 = Frac(2, 6)
        self.f3 = Frac(3, 10)
        self.f0 = Frac(0, 1)

    def test_print(self):
        pass  # test str() i repr()
        self.assertEqual(str(self.f1), "1 / 3")
        self.assertEqual(str(Frac(3, 1)), "3")
        self.assertEqual(repr(self.f1), "Frac(1,3)")

    def test_add_frac(self):
        self.assertEqual(self.f1 + self.f2 + self.f2, Frac(1))
        self.assertEqual(self.f1 + 3, Frac(10, 3))
        self.assertEqual(5 + self.f1, Frac(16, 3))
        self.assertEqual(Frac(5, 10) + 0.5, Frac(1,1))


    def test_sub_frac(self):
        self.assertEqual(self.f2 - self.f3, Frac(1, 30))

    def test_mul_frac(self):
        self.assertEqual(self.f1 * self.f3, Frac(1, 10))
        self.assertEqual(self.f1 * self.f0, Frac(0, 3))

    def test_div_frac(self):
        self.assertEqual(self.f1 / self.f3, Frac(20, 18))
        self.assertEqual(self.f1 / self.f3, Frac(10, 9))
        with self.assertRaises(ZeroDivisionError):
            self.f1 / self.f0

    def test_cmp_frac(self):
        self.assertTrue(self.f2 > self.f3)
        self.assertFalse(Frac(20, 18) < Frac(10, 18))
        self.assertTrue(Frac(2, 2) == Frac(2, 2))
        self.assertFalse(Frac(2, 3) == Frac(3, 3))
        self.assertTrue(Frac(2, 2) != Frac(3, 2))
        self.assertFalse(Frac(2, 2) != Frac(2, 2))
        self.assertTrue(Frac(2, 2) < Frac(3, 2))
        self.assertFalse(Frac(4, 2) < Frac(3, 2))
        self.assertTrue(Frac(2, 2) <= Frac(3, 1))
        self.assertFalse(Frac(4, 2) <= Frac(3, 2))
        self.assertTrue(Frac(4, 3) > Frac(3, 3))
        self.assertTrue(Frac(1, 2) == 0.5)

    def test_frac2float(self):
        self.assertAlmostEqual(float(self.f1), 0.333, places=3, msg=None)

    def test_invert_frac(self):
        self.assertEqual(~self.f1, 3)


if __name__ == '__main__':
    unittest.main()
