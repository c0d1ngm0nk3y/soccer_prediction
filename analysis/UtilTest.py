#encoding=utf8
import unittest
from analysis.Util import string_with_fixed_length


class UtilTest(unittest.TestCase):
    def test_length_standard(self):
        string = string_with_fixed_length('abcd')
        self.assertEquals(len(string), 4)

    def test_length_unicode(self):
        string = string_with_fixed_length('äöü')
        self.assertEquals(len(string), 3)
