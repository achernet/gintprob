import unittest2
import conv_camelcase


class MyTestCase(unittest2.TestCase):

    def test_camelcase_conversion(self):
        expectedConvDict = {('marketBit_buf', True): 'MarketBitBuf',
                            ('markedBit', False): 'markedBit',
                            ('new_buf', True): 'NewBuf',
                            ('_private_method', False): '_privateMethod',
                            ('__hidden_method', False): '__hiddenMethod',
                            ('_private_method_qt_', False): '_privateMethodQt_'}
        for (inputStr, capFirst), expectedOutputStr in expectedConvDict.items():
            actualOutput = conv_camelcase.conv_camelcase(inputStr, capitalize_first=capFirst)
            self.assertEquals(actualOutput, expectedOutputStr)

    def test_camelcase_multiple_words(self):
        self.assertRaises(ValueError, conv_camelcase.conv_camelcase, 'multi words')


if __name__ == '__main__':
    unittest2.main()
