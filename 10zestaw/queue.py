import unittest


class FullQueueException(Exception):
    pass


class EmptyQueueException(Exception):
    pass


class Queue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0           # pierwszy do pobrania
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise FullQueueException
        else:
            self.items[self.tail] = data
            self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise EmptyQueueException
        else:
            data = self.items[self.head]
            self.items[self.head] = None      # usuwam referencję
            self.head = (self.head + 1) % self.n
            return data


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.empty = Queue(2)

    def test_get(self):
        self.empty.put(2)
        self.empty.put(3)
        self.assertEqual(self.empty.get(), 2)

    def test_get_exception(self):
        self.assertRaises(EmptyQueueException, self.empty.get)

    def test_push_exception(self):
        self.empty.put(2)
        self.empty.put(3)
        self.assertRaises(FullQueueException, self.empty.put, 4)


if __name__ == '__main__':
    unittest.main()