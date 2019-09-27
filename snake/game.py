import pygame

from random import randint
from threading import Thread
from time import sleep

from draw import Drawer
from object import Object, ObjectName
from snake import Direction, Snake


class Game():

    DEFAULT_FRAME_RATE = 20

    def __init__(self, grid_width=60, grid_height=40, ai=None):
        pygame.init()

        self.ai = ai
        self.frame_rate = Game.DEFAULT_FRAME_RATE
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.drawer = Drawer(self.grid_width, self.grid_height)
        self.apple = None
        self.snake = None
        self.score = None
        self.game_running = False

    def init_game(self):
        self.snake = Snake(self.get_random_object())
        self.apple = self.get_random_object()
        self.score = 0
        self.game_running = True

    def get_random_object(self):
        if self.snake:
            curr_head = self.snake.head
        else:
            curr_head = None

        random_object = Object(
            randint(0, self.grid_width - 1),
            randint(0, self.grid_height - 1)
        )
        while random_object == curr_head or random_object == self.apple:
            random_object = Object(
                randint(0, self.grid_width - 1),
                randint(0, self.grid_height - 1)
            )

        return random_object

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        key_presses = pygame.key.get_pressed()

        if key_presses[pygame.K_DOWN]:
            self.snake.direction = Direction.DOWN
        elif key_presses[pygame.K_UP]:
            self.snake.direction = Direction.UP
        elif key_presses[pygame.K_LEFT]:
            self.snake.direction = Direction.LEFT
        elif key_presses[pygame.K_RIGHT]:
            self.snake.direction = Direction.RIGHT

    def step(self):
        collision = self.snake.move(
            self.apple, self.grid_width-1, self.grid_height-1)

        if(collision == ObjectName.APPLE):
            self.score += 1
            self.apple = self.get_random_object()
        elif(collision == ObjectName.TAIL or collision == ObjectName.WALL):
            self.init_game()

    def game_loop(self):
        if(self.ai):
            Thread(target=self.ai, args=[self], daemon=True).start()

        while self.game_running:

            self.handle_events()
            self.step()
            self.drawer.draw(self.snake, self.apple, self.score)
            pygame.display.flip()
            pygame.time.delay(1000//self.frame_rate)


def simple_apple_ai(game):
    while True:
        if game.snake.head.x > game.apple.x:
            game.snake.direction = Direction.LEFT
        elif game.snake.head.x < game.apple.x:
            game.snake.direction = Direction.RIGHT
        elif game.snake.head.y > game.apple.y:
            game.snake.direction = Direction.UP
        else:
            game.snake.direction = Direction.DOWN
