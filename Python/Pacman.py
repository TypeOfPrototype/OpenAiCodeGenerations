
#define a python function which is a classic pac-man game
#display playing field using pygame library

import pygame
import random

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
CELL = 10
BOARD_WIDTH = WINDOW_WIDTH // CELL
BOARD_HEIGHT = WINDOW_HEIGHT // CELL

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


class Board:
    def __init__(self):
        self.board = [
            [EMPTY for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)
        ]
        self.food = []
        self.generate_food()
        self.player = Player()
        self.walls = Walls()

    def generate_food(self):
        while True:
            x = random.randint(1, BOARD_WIDTH - 2)
            y = random.randint(1, BOARD_HEIGHT - 2)
            if self.board[y][x] == EMPTY:
                self.board[y][x] = FOOD
                self.food.append((x, y))
                break

    def end(self):
        print("Game over")

    def is_player_on_food(self):
        x, y = self.player.head
        if (x, y) in self.food:
            self.food.remove((x, y))
            self.generate_food()
            self.player.increase_length()

    def check_collision(self):
        x, y = self.player.head
        if not 1 <= x <= BOARD_WIDTH - 2 or not 1 <= y <= BOARD_HEIGHT - 2:
            self.end()
        if self.board[y][x] in (HEAD, FOOD, BODY):
            self.end()

    def render(self):
        screen.fill(BLACK)
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                if self.board[y][x] == FOOD:
                    pygame.draw.rect(screen, GREEN,
                                     pygame.Rect(x * CELL, y * CELL, CELL, CELL))
                elif self.board[y][x] == EMPTY:
                    pygame.draw.rect(screen, WHITE,
                                     pygame.Rect(x * CELL, y * CELL, CELL, CELL))
                elif self.board[y][x] == WALL:
                    pygame.draw.rect(screen, RED,
                                     pygame.Rect(x * CELL, y * CELL, CELL, CELL))
        for part in self.player.body:
            pygame.draw.rect(screen, BLUE,
                             pygame.Rect(part[0] * CELL, part[1] * CELL, CELL, CELL))

        pygame.display.flip()

    def update(self):
        self.player.update()
        self.check_collision()
        self.is_player_on_food()
        self.render()


class Player:
    def __init__(self):
        self.head = (BOARD_WIDTH // 2, BOARD_HEIGHT // 2)
        self.body = [self.head]
        self.direction = LEFT
        self.length = 1

    def increase_length(self):
        self.length += 1

    def update(self):
        if not self.length == len(self.body):
            self.body.append(self.head)
        else:
            self.body.pop(0)
        if self.direction == RIGHT:
            self.head = (self.head[0] + 1, self.head[1])
        elif self.direction == LEFT:
            self.head = (self.head[0] - 1, self.head[1])
        elif self.direction == UP:
            self.head = (self.head[0], self.head[1] - 1)
        elif self.direction == DOWN:
            self.head = (self.head[0], self.head[1] + 1)


class Walls:
    def __init__(self):
        pass

    def render(self):
        pass


EMPTY = 0
FOOD = 1
HEAD = 2
BODY = 3
LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4
WALL = 5

game_board = Board()

while True:
    game_board.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game_board.player.direction = LEFT
            elif event.key == pygame.K_RIGHT:
                game_board.player.direction = RIGHT
            elif event.key == pygame.K_UP:
                game_board.player.direction = UP
            elif event.key == pygame.K_DOWN:
                game_board.player.direction = DOWN
            elif event.key == pygame.K_ESCAPE:
                exit()

    pygame.time.delay(100)
    pygame.display.flip()
    pygame.display.update()
    