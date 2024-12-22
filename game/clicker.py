class ClickerGame:
    def __init__(self):
        self.score = 0

    def click(self):
        self.score += 1

    def get_score(self):
        return self.score

if __name__ == '__main__':
    game = ClickerGame()
    print('Welcome to the Clicker Game!')
    while True:
        input('Press Enter to click...')
        game.click()
        print(f'Score: {game.get_score()}')
