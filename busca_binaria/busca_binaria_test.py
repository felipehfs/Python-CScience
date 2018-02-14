from busca_binaria import busca_binaria
import unittest


class BinarySearchTest(unittest.TestCase):

    def test_busca(self):
        self.assertEqual(busca_binaria([2, 4, 6], 2), 2)

if __name__ == '__main__':
    unittest.main()
