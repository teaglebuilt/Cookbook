import unittest
from cookbook.collections import SortedSet


class TestConstruction(unittest.TestCase):

    def test_empty(self):
        s = SortedSet([])

    def test_from_sequence(self):
        s = SortedSet([7, 8, 3, 1])

    def test_from_iterable(self):
        def numbergen():
            yield 6
            yield 8
            yield 4
            yield 2
        g = numbergen()
        s = SortedSet(g)
    
    def test_default_empty(self):
        s = SortedSet()


        
if __name__ == "__main__":
    unittest.main()
