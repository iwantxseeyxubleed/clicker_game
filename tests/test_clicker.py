import unittest
from game.clicker import ClickerGame

class TestClickerGame(unittest.TestCase):
    def test_initial_score(self):
        game = ClickerGame()
        self.assertEqual(game.get_score(), 0)

    def test_click_increases_score(self):
        game = ClickerGame()
        game.click()
        self.assertEqual(game.get_score(), 1)

if __name__ == '__main__':
    unittest.main()
