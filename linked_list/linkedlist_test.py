from linkedlist import List

import unittest

class ListTest(unittest.TestCase):

    def setUp(self):
        self.lista = List()
        
    def test_add_element(self):
        self.assertIsNotNone(self.lista.add(12))

    def test_remove_element(self):
        self.lista.add(32)
        self.assertTrue(self.lista.remove(32))

    def test_to_list(self):
        lista = self.lista.to_list()
        self.assertIsNotNone(lista)

if __name__ == '__main__':
    unittest.main()
