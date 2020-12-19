#ZADANIE 10.8
import random
import unittest


class RandomQueue:

    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        x = random.randint(0, len(self.items)-1)
        return self.items.pop(x)

    def is_empty(self):
        return not self.items

    def is_full(self):
        return False

    def clear(self):
        self.items = []


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.empty = RandomQueue()

    def test_get(self):
        self.empty.insert(2)
        self.empty.insert(3)
        self.empty.insert(4)
        self.empty.insert(5)
        self.empty.insert(6)

        print(self.empty.remove())
        print(self.empty.remove())


if __name__ == '__main__':
    unittest.main()