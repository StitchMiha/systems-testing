import unittest
from tree import Tree
from node import Node


class TestTreeFind(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        self.tree.add(5)
        self.tree.add(3)
        self.tree.add(7)
        self.tree.add(1)
        self.tree.add(9)

    def test_find_existing_node(self):
        # Test finding an existing node
        result = self.tree.find(7)
        self.assertIsNotNone(result)
        self.assertEqual(result.data, 7)

    def test_find_non_existing_node(self):
        # Test finding a non-existing node
        result = self.tree.find(10)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main() 