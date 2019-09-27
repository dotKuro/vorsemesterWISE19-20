from game import Game, simple_apple_ai

if __name__ == '__main__':
    game = Game(ai=simple_apple_ai)
    game.init_game()
    game.game_loop()
