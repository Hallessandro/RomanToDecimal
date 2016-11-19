import unittest

from RomanToDecimal import RomanToDecimal


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_I(self):
        self.assertEqual(1, RomanToDecimal("I"))

    def test_V(self):
        self.assertEqual(5, RomanToDecimal("V"))

    def test_XV(self):
        self.assertEqual(15, RomanToDecimal("XV"))

    def test_III(self):
        self.assertEqual(3, RomanToDecimal("III"))

    def test_LXXIV(self):
        self.assertEqual(74, RomanToDecimal("LXXIV"))

    def test_MCXCVIII(self):
        self.assertEqual(1198, RomanToDecimal("MCXCVIII"))

if __name__ == '__main__':
    unittest.main()