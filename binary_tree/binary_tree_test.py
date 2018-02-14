from binary_tree import Tree
import unittest

class TreeTest(unittest.TestCase):

    def test_insert(self):
        t = Tree()
        t.insert(2)
        self.assertEqual(list(t.display()), [2])

if __name__ == '__main__':
    unittest.main()
