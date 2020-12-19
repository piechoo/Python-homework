import unittest


class FullStackException(Exception):
    pass


class EmptyStackException(Exception):
    pass


class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise FullStackException
        else:
            self.items[self.n] = data
            self.n += 1

    def pop(self):
        if self.is_empty():
            raise EmptyStackException
        else:
            self.n -= 1
            data = self.items[self.n]
            self.items[self.n] = None    # usuwam referencję
            return data


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.empty = Stack(1)

    def test_pop(self):
        self.empty.push(2)
        self.assertEqual(self.empty.pop(), 2)

    def test_pop_exception(self):
        self.assertRaises(EmptyStackException, self.empty.pop)

    def test_push_exception(self):
        self.empty.push(2)
        self.assertRaises(FullStackException, self.empty.push, 3)


if __name__ == '__main__':
    unittest.main()