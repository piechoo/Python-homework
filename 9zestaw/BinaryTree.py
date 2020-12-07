import unittest

"""ZADANIE 9.6 (BINARYTREE)"""
class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def traverse_preorder(top, visit):
    if top is None:
        return
    visit(top)
    traverse_preorder(top.left, visit)
    traverse_preorder(top.right, visit)


def traverse_inorder(top, visit):
    if top is None:
        return
    traverse_inorder(top.left, visit)
    visit(top)
    traverse_inorder(top.right, visit)


def traverse_postorder(top, visit):
    if top is None:
        return
    traverse_postorder(top.left, visit)
    traverse_postorder(top.right, visit)
    visit(top)


def btree_count(top):
    if top is None:
        return 0
    return btree_count(top.left) + 1 + btree_count(top.right)


def btree_height(top):
    if top is None:
        return 0
    left = btree_height(top.left)
    right = btree_height(top.right)
    return 1 + max(left, right)


def btree_print_indented(top, level=0):
    if top is None:
        return
    btree_print_indented(top.right, level+1)
    print ( "{}* {}".format('   '*level, top) )
    btree_print_indented(top.left, level+1)


def count_leafs(top):
    if top is None:
        return 0
    if top.left is None and top.right is None:
        return 1
    return count_leafs(top.left) + count_leafs(top.right)


def count_total(top):
    if top is None:
        return 0
    return count_total(top.left) + top.data + count_total(top.right)


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)
        self.root.right.left = Node(6)
        self.root.right.right = Node(7)

    def test_leafs(self):
        self.assertEqual(count_leafs(self.root), 4)

    def test_total(self):
        self.assertEqual(count_total(self.root), 28)


if __name__ == '__main__':
    unittest.main()