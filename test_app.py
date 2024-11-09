import unittest
from app import add


class TestMathFuntions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4, 6), 10)
        self.assertEqual(add(0, 1), 1)


if __name__ == "__main__":
    unittest.main()
