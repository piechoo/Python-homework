import unittest
import random
#8.1 a x + b y + c = 0


class RownanieSprzeczne(Exception): pass


class RownanieNieokreslone(Exception): pass


def solve1(a, b, c):
    if a == 0 and b == 0:
        if c == 0:
            raise RownanieNieokreslone
        else:
            raise RownanieSprzeczne
    if a == 0:
        return "y = " + str(-c/b)
    elif b == 0:
        return "x = " + str(-c/a)
    else:
        return "y = -({0} * x + {1})/{2}".format(a, c, b)

"""
8.3
Obliczyć liczbę pi za pomocą algorytmu Monte Carlo. 
Wykorzystać losowanie punktów z kwadratu z wpisanym kołem. 
Sprawdzić zależność dokładności wyniku od liczby losowań. 
Wskazówka: Skorzystać z modułu random.
"""


def calc_pi(n=100):
    inCircle = 0
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x * x + y * y <= 1:
            inCircle += 1
    return 4 * inCircle / n

"""
8.4
Zaimplementować algorytm obliczający pole powierzchni trójkąta, 
jeżeli dane są trzy liczby będące długościami jego boków. 
Jeżeli podane liczby nie spełniają warunku trójkąta, to program ma generować wyjątek ValueError.
"""


def heron(a, b, c):
    p = (a + b + c) / 2
    result = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    if isinstance(result, complex):
        raise ValueError
    else:
        return result


"""
8.6
Za pomocą techniki programowania dynamicznego napisać program obliczający wartości funkcji P(i, j). 
Porównać z wersją rekurencyjną programu. 
Wskazówka: Wykorzystać tablicę dwuwymiarową (np. słownik) do przechowywania wartości funkcji. 
Wartości w tablicy wypełniać kolejno wierszami.
P(0, 0) = 0.5,
P(i, 0) = 0.0 dla i > 0,
P(0, j) = 1.0 dla j > 0,
P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0.
"""


def recursion_P(i, j):
    if i == 0 and j == 0: return 0.5
    if i == 0 and j > 0: return 1
    if j == 0 and i > 0: return 0
    if j > 0 and i > 0: return 0.5 * (recursion_P(i - 1, j) + recursion_P(i, j - 1))


def dynamic_P(k, l):
    p = {}
    p[(0, 0)] = 0.5
    n = max(k, l)
    for i in range(n + 1):
        p[(i, 0)] = 0
        p[(0, i)] = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            val = 0.5 * (p[(i - 1, j)] + p[(i, j - 1)])
            p[(i, j)] = val
    return p[(k, l)]


class MyTestCase(unittest.TestCase):
    def test_type(self):
        self.assertEqual(heron(3, 4, 5), 6)
        self.assertIsInstance(heron(3, 4, 5), float)
        with self.assertRaises(ValueError):
            heron(3, 4, 30)

    def test_dynamicP(self):
        self.assertEqual(dynamic_P(2, 3), 0.6875)

    def test_rekcursionP(self):
        self.assertEqual(recursion_P(2, 3), 0.6875)

    def test_pi(self):
        self.assertAlmostEqual(calc_pi(1000000), 3.14, places=2, msg=None)


if __name__ == '__main__':
    unittest.main()