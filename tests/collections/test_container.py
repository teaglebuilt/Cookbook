import unittest
from cookbook.collections import SortedSet


class TestContainerProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([6, 7, 3, 9])

    def test_positive_contained(self):
        self.assertTrue(6 in self.s)


if __name__ == "__main__":
    unittest.main()
