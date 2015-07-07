import unittest2
from perfect_number import isPerfect


class TestPerfectNumberCases(unittest2.TestCase):

    def test_non_naturals(self):
        self.assertFalse(isPerfect(-1))
        self.assertFalse(isPerfect(-8))
        self.assertFalse(isPerfect(0))

    def test_odd(self):
        self.assertFalse(isPerfect(1))
        self.assertFalse(isPerfect(10 ** 1500 - 1))
        self.assertFalse(isPerfect(10 ** 1500))
        self.assertRaises(ValueError, isPerfect, 10 ** 1500 + 1)

    def test_small_evens(self):
        self.assertTrue(isPerfect(6))
        self.assertTrue(isPerfect(28))
        self.assertTrue(isPerfect(496))
        self.assertTrue(isPerfect(8128))
        self.assertTrue(isPerfect(33550336))

    def test_known_issues_small(self):
        self.assertFalse(isPerfect(120))
        self.assertFalse(isPerfect(2016))

    def test_large_evens(self):
        for mexp in (521, 32582657, 37156667, 57885161):
            pValStr = '1' * mexp + '0' * (mexp - 1)
            pVal = int(pValStr, 2)
            self.assertTrue(isPerfect(pVal))

        mexpFalse = 32582653
        pVal = int('1' * mexpFalse + '0' * (mexpFalse - 1), 2)
        self.assertFalse(isPerfect(pVal))

        mexpRaises = 57885163
        pVal = int('1' * mexpRaises + '0' * (mexpRaises - 1), 2)
        self.assertRaises(ValueError, isPerfect, pVal)


if __name__ == '__main__':
    unittest2.main()
