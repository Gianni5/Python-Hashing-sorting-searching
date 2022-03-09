import unittest
from Sorting.QuickSort import *
from Hashing.Hash import *


class TestHash(unittest.TestCase):
    """
    testing hashing, add, sorting functions
    """

    def test_get_hash(self):
        hash_table = HashTable(sorted_number)
        self.assertEqual(hash_table.get_hash_key(432), 43)

    def test_add(self):
        hash_table = HashTable(sorted_number)
        self.assertTrue(hash_table.add(149))

    def test_sorting(self):
        self.assertEqual(quicksort(sorted_number)[11], 27)
