import unittest
from prediction.QueryStatistics import QueryStatistics


class QueryStatisticsTest(unittest.TestCase):
    def setUp(self):
        self.cut = QueryStatistics()

    def test_performance_33(self):
        self.cut.add_result(1, 1)
        self.cut.add_result(2, 1)
        self.cut.add_result(0, 1)

        self.assertEqual(self.cut.get_performance(), 33)

    def test_performance_66(self):
        self.cut.add_result(1, 1)
        self.cut.add_result(2, 2)
        self.cut.add_result(0, 1)

        self.assertEqual(self.cut.get_performance(), 66)

    def test_performance_0(self):
        self.assertEqual(self.cut.get_performance(), 0)

    def test_performane_in_result(self):
        self.cut.add_result(1, 1)
        self.cut.add_result(0, 1)

        self.assertRegexpMatches(self.cut.__str__(), "50%")

    def test_performane_default(self):
        self.assertRegexpMatches(self.cut.__str__(), "^0%")


if __name__ == '__main__':
    unittest.main()
