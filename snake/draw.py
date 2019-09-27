import pygame


class Drawer():

    DEFAULT_BACKGROUND_COLOR = 0, 0, 0
    DEFAULT_GRID_COLOR = 40, 40, 40
    DEFAULT_SNAKE_COLOR = 0, 255, 0
    DEFAULT_APPLE_COLOR = 255, 0, 0
    DEFAULT_SCORE_COLOR = 255, 255, 255
    DEFAULT_CELL_WIDTH = 10
    DEFAULT_CELL_HEIGHT = 10

    def __init__(self, grid_width, grid_height):
        self.cell_width = Drawer.DEFAULT_CELL_WIDTH
        self.cell_height = Drawer.DEFAULT_CELL_HEIGHT
        self.size = self.width, self.height = self.calculate_size(
            grid_width, grid_height
        )
        self.screen = pygame.display.set_mode(self.size)
        self.backgorund_color = Drawer.DEFAULT_BACKGROUND_COLOR
        self.grid_color = Drawer.DEFAULT_GRID_COLOR
        self.snake_color = Drawer.DEFAULT_SNAKE_COLOR
        self.apple_color = Drawer.DEFAULT_APPLE_COLOR
        self.score_color = Drawer.DEFAULT_SCORE_COLOR

    def draw(self, snake, apple, score):
        self.screen.fill(self.backgorund_color)
        self.draw_grid()
        self.draw_snake(snake)
        self.draw_apple(apple)
        self.draw_score(score)

    def draw_grid(self):
        for x in range(0, self.width, self.cell_width):
            for y in range(0, self.height, self.cell_height):
                rect = x, y, self.cell_width, self.cell_height
                pygame.draw.rect(self.screen, self.grid_color, rect, 1)

    def draw_snake(self, snake):
        head = snake.head.x * self.cell_width, snake.head.y * \
            self.cell_height, self.cell_width, self.cell_height
        pygame.draw.rect(self.screen, self.snake_color, head)
        for x, y in snake.tail:
            tail = x * self.cell_width, y * self.cell_height, self.cell_width, self.cell_height
            pygame.draw.rect(self.screen, self.snake_color, tail)

    def draw_apple(self, apple):
        apple = apple.x * self.cell_width, apple.y * \
            self.cell_height, self.cell_width, self.cell_height
        pygame.draw.rect(self.screen, self.apple_color, apple)

    def draw_score(self, score):
        font = pygame.font.Font(None, 40)
        text_surface = font.render(
            'Score: {}'.format(score), True, self.score_color)
        position = 0, 0
        self.screen.blit(text_surface, position)

    def calculate_size(self, grid_width, grid_height):
        return self.cell_width * grid_width, self.cell_height * grid_height
