## flask_app.py
from flask import Flask, render_template, request
from ui import UI
from game import Game

class FlaskApp:
    def __init__(self, ui: UI):
        self.app = Flask(__name__)
        self.ui = ui
        self.game = Game()
        self.game.start_game()
        self.ui.game = self.game

    def run(self):
        @self.app.route('/')
        def index():
            return render_template('index.html')

        @self.app.route('/move', methods=['POST'])
        def move():
            direction = request.form.get('direction')
            if direction:
                if self.ui.game.move(direction):
                    self.ui.display_board()
                    self.ui.display_score()
            return render_template('index.html', board=self.ui.game.board, score=self.ui.game.get_score())

        self.app.run(debug=True)

if __name__ == '__main__':
    from ui import UI
    from game import Game
    game = Game()
    game.start_game()
    ui = UI(game)
    app = FlaskApp(ui)
    app.run()
