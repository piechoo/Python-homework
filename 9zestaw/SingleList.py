"""ZADANIE 9.1 (SINGLELIST)"""
import unittest


class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(N)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def remove_tail(self):
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.tail
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            check=self.head
            while check.next.next is not None:
                check = check.next
            self.tail = check
            self.tail.next = None
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node
    # Zwraca cały węzeł, skraca listę.
    # Dla pustej listy rzuca wyjątek ValueError.

    def merge(self, other):
        if self.is_empty():
            self.head = other.head
            self.tail = other.tail
            self.length = other.length
        else:
            self.tail.next = other.head
            self.tail = other.tail
            self.length = self.length + other.length

    # Węzły z listy other są przepinane do listy self na jej koniec.
    # Po zakończeniu operacji lista other ma być pusta.

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.alist = SingleList()
        self.alist.insert_head(Node(11))  # [11]
        self.alist.insert_head(Node(22))  # [22, 11]
        self.alist.insert_tail(Node(33))  # [22, 11, 33]

        self.blist = SingleList()
        self.blist.insert_head(Node(1))  # [11]
        self.blist.insert_head(Node(2))  # [22, 11]
        self.blist.insert_tail(Node(3))  # [22, 11, 33]

        self.clist = SingleList()

    def test_remove_tail(self):
        self.assertEqual(self.alist.remove_tail().data, 33)
        with self.assertRaises(ValueError):
            self.clist.remove_tail()

    def test_merge(self):
        self.alist.merge(self.blist)
        self.assertEqual(self.alist.length, 6)
        self.assertEqual(self.alist.head.data, 22)
        self.assertEqual(self.alist.tail.data, self.blist.tail.data)
        self.clist.merge(self.blist)
        self.assertEqual(self.clist.head.data, self.blist.head.data)

    def test_clear(self):
        self.alist.clear()
        self.assertIsNone(self.alist.head)
        self.assertIsNone(self.alist.tail)
        self.assertEqual(self.alist.length, 0)


if __name__ == '__main__':
    unittest.main()