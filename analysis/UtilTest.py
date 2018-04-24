#encoding=utf8
import unittest
from analysis.Util import string_with_fixed_length, normalize_team_name


class UtilTest(unittest.TestCase):
    def test_length_standard(self):
        string = string_with_fixed_length('abcd')
        self.assertEquals(len(string), 4)

    def test_length_unicode(self):
        string = string_with_fixed_length('äöü')
        self.assertEquals(len(string), 3)

    def test_norm_standard(self):
        team = normalize_team_name("Schlumpfhausen")
        self.assertEquals(team, "Schlumpfhausen")

    def test_norm_bayern(self):
        team = normalize_team_name("FC Bayern")
        self.assertEquals(team, u"Bayern München")

    def test_norm_leverkusen(self):
        team = normalize_team_name("Leverkusen")
        self.assertEquals(team, "Bayer 04 Leverkusen")
