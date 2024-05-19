## ui.py
import pygame
from game import Game

class UI:
    def __init__(self, game: Game):
        self.game = game
        self.screen_width = 400
        self.screen_height = 400
        self.tile_size = self.screen_width // 4
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('2048 Game')

    def display_board(self):
        self.screen.fill((187, 173, 160))
        for row in range(4):
            for col in range(4):
                value = self.game.board[row][col]
                if value != 0:
                    font = pygame.font.Font(None, 36)
                    text = font.render(str(value), True, (255, 255, 255))
                    x = col * self.tile_size + (self.tile_size - text.get_width()) // 2
                    y = row * self.tile_size + (self.tile_size - text.get_height()) // 2
                    pygame.draw.rect(self.screen, (205, 193, 180), (col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size))
                    self.screen.blit(text, (x, y))
        pygame.display.flip()

    def display_score(self):
        font = pygame.font.Font(None, 24)
        score_text = font.render(f'Score: {self.game.get_score()}', True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        pygame.display.flip()

    def handle_input(self, input: str):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.game.move('up')
                elif event.key == pygame.K_DOWN:
                    self.game.move('down')
                elif event.key == pygame.K_LEFT:
                    self.game.move('left')
                elif event.key == pygame.K_RIGHT:
                    self.game.move('right')
        self.display_board()
        self.display_score()
