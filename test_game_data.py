
import unittest
from src.game_data import GameData

class TestGameData(unittest.TestCase):

    def setUp(self):
        self.game_data = GameData('data/sample_20_paid_games.csv')
        self.game_data.load_data()

    def test_calculate_free_paid_percentage(self):
        result = self.game_data.calculate_free_paid_percentage()
        self.assertAlmostEqual(result['free_percentage'], 0.0, places=1)
        self.assertAlmostEqual(result['paid_percentage'], 100.0, places=1)

    def test_count_games_with_portuguese_support(self):
        result = self.game_data.count_games_with_portuguese_support()
        self.assertTrue(result >= 0)

if __name__ == '__main__':
    unittest.main()
