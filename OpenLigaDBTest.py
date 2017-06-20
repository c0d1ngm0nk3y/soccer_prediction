import unittest
from OpenLigaDB import OpenLigaDB


class MyTestCase(unittest.TestCase):
    def test_data_retrieval(self):
        api = OpenLigaDB()
        data = api.request_data('bl1', '2016')
        self.assertEquals(306, len(data))

        game1 = data[0]

        self.assertEquals(1, game1['Group']['GroupOrderID'])
        self.assertEquals('FC Bayern', game1['Team1']['ShortName'])
        print(game1['Team2'])
        self.assertEquals('x', game1['Team2']['ShortName'])
        self.assertEquals(6, game1['Goals'][-1]['ScoreTeam1'])

        game305 = data [305]
        self.assertEquals(34, game305['Group']['GroupOrderID'])


if __name__ == '__main__':
    unittest.main()
