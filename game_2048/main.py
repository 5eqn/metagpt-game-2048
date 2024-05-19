## main.py
from game import Game
from ui import UI
from flask_app import FlaskApp
import pygame

def main():
    # Initialize the game
    game = Game()
    game.start_game()

    # Initialize the UI
    ui = UI(game)

    # Initialize the Flask application
    flask_app = FlaskApp(ui)

    # Start the game loop for the Pygame UI
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ui.game.move('up')
                elif event.key == pygame.K_DOWN:
                    ui.game.move('down')
                elif event.key == pygame.K_LEFT:
                    ui.game.move('left')
                elif event.key == pygame.K_RIGHT:
                    ui.game.move('right')
        ui.display_board()
        ui.display_score()

    # Run the Flask application
    flask_app.run()

if __name__ == '__main__':
    main()
