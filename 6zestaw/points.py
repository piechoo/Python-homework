import math
import unittest


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        if self.y == other.y and self.x == other.x:
            return True
        else:
            return False

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other): # v1 + v2
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny
        return Point(self.x * other.x, self.y * other.y)

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):           # długość wektora
        return math.sqrt(self.x * self.x + self.y * self.y)

# Kod testujący moduł.


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.f1 = Point(1, 3)
        self.f2 = Point(2, 6)
        self.f3 = Point(3, -10)
        self.f0 = Point(0, 1)

    def test_print(self):
        pass  # test str() i repr()
        self.assertEqual(str(self.f1), "(1, 3)")
        self.assertEqual(str(Point(-3, 1)), "(-3, 1)")
        self.assertEqual(repr(self.f1), "Point(1, 3)")

    def test_add_point(self):
        self.assertEqual(self.f1 + self.f2, Point(3, 9))

    def test_sub_point(self):
        self.assertEqual(self.f2 - self.f3, Point(-1, 16))

    def test_mul_point(self):
        self.assertEqual(self.f1 * self.f3, Point(3, -30))

    def test_length_point(self):
        self.assertEqual(self.f1.length(), math.sqrt(10))

    def test_cross_point(self):
        self.assertEqual(self.f1.cross(self.f3), -19)
        self.assertTrue(Point(2, 2) == Point(2, 2))
        self.assertFalse(Point(2, 3) == Point(3, 3))
        self.assertTrue(Point(2, 2) != Point(3, 2))
        self.assertFalse(Point(2, 2) != Point(2, 2))


if __name__ == '__main__':
    unittest.main()
