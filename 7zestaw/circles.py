from math import sqrt
from math import pi

import unittest


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.x == other.pt.x and self.y == other.pt.y
        else:
            return self.x == other.x and self.y == other.y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return Point(self.x, self.y)

    def __str__(self):
        return str(self.x) + ", " + str(self.y)


class Circle:
    def __init__(self, x=0, y=0, radius=1):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __str__(self):
        return self.pt + "  " + self.radius

    def __repr__(self):
        return "Circle({0}, {1}, {2})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return pi * self.radius ** 2

    def move(self, x, y):
        return self.pt + Point(x, y)

    def cover(self, other):

        distance = sqrt((self.pt.x - other.pt.x)**2 + (self.pt.y - other.pt.y)**2)
        # sprawdzam czy okregi sie zawieraja
        if distance <= abs(self.radius - other.radius):
            if self.radius >= other.radius:
                return self
            else:
                return other

        else:
            new_radius = (distance + self.radius + other.radius)/2

            if other.radius >= self.radius:
                theta = 1 / 2 + (other.radius - self.radius) / (2 * distance)
                new_x = (1.0 - theta) * self.pt.x + theta * other.pt.x
                new_y = (1.0 - theta) * self.pt.y + theta * other.pt.y
            else:
                theta = 1 / 2 + (self.radius - other.radius) / (2 * distance)
                new_x = (1.0 - theta) * other.pt.x + theta * self.pt.x
                new_y = (1.0 - theta) * other.pt.y + theta * self.pt.y

        return Circle(new_x, new_y, new_radius)


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.c1 = Circle(1, 2, 3)
        self.c2 = Circle(0, 0, 10)
        self.c3 = Circle(4, 3, 2)

    def test_equal(self):
        self.assertFalse(self.c1 == self.c2)
        self.assertTrue(self.c1 == Circle(1, 2, 3))

    def test_move(self):
        self.assertEqual(self.c1.move(2, 3), Circle(3, 5, 3))
        self.assertEqual(self.c3.move(-2, -3), Circle(2, 0, 2))

    def test_area(self):
        self.assertEqual(self.c3.area(), 12.566370614359172)

    def test_cover(self):
        self.assertEqual(self.c2.cover(self.c3), Circle(0, 0, 10))
        self.assertEqual(Circle(0,0,1).cover(Circle(0, -4, 1)), Circle(0, -2, 3))


if __name__ == '__main__':
    unittest.main()