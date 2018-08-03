from __future__ import absolute_import

import unittest

from actions.CompareAction import CompareAction


class CompareActionTest(unittest.TestCase):

    def setUp(self):
        self.action = CompareAction()

    def test_comparing_all_bl1_nets(self):
        list_of_nets = self.action.compare_nets('bl1')
        self.assertTrue(len(list_of_nets) > 0)

        prev_points = 1000
        for entry in list_of_nets:
            points = entry.points
            self.assertTrue(points > 0)
            self.assertLessEqual(points, prev_points)
            prev_points = points
