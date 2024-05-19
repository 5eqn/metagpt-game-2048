## game.py

class Game:
    def __init__(self):
        self.board = [[0 for _ in range(4)] for _ in range(4)]
        self.score = 0
        self._initialize_board()

    def _initialize_board(self):
        # Initialize the board with two random tiles
        from random import randint
        for _ in range(2):
            self._add_random_tile()

    def _add_random_tile(self):
        from random import randint
        while True:
            row, col = randint(0, 3), randint(0, 3)
            if self.board[row][col] == 0:
                self.board[row][col] = 2 if randint(1, 10) == 10 else 4
                break

    def start_game(self):
        self._initialize_board()

    def move(self, direction: str) -> bool:
        # Implement the logic for moving the tiles in the specified direction
        # Return True if the board changed, False otherwise
        moved = False
        if direction == 'up':
            for col in range(4):
                for row in range(1, 4):
                    if self.board[row][col] != 0:
                        for i in range(row, 0, -1):
                            if self.board[i - 1][col] == 0:
                                self.board[i - 1][col] = self.board[i][col]
                                self.board[i][col] = 0
                                moved = True
                            elif self.board[i - 1][col] == self.board[i][col]:
                                self.board[i - 1][col] *= 2
                                self.board[i][col] = 0
                                self.score += self.board[i - 1][col]
                                moved = True
                                break
        elif direction == 'down':
            for col in range(4):
                for row in range(2, -1, -1):
                    if self.board[row][col] != 0:
                        for i in range(row, 3):
                            if self.board[i + 1][col] == 0:
                                self.board[i + 1][col] = self.board[i][col]
                                self.board[i][col] = 0
                                moved = True
                            elif self.board[i + 1][col] == self.board[i][col]:
                                self.board[i + 1][col] *= 2
                                self.board[i][col] = 0
                                self.score += self.board[i + 1][col]
                                moved = True
                                break
        elif direction == 'left':
            for row in range(4):
                for col in range(1, 4):
                    if self.board[row][col] != 0:
                        for i in range(col, 0, -1):
                            if self.board[row][i - 1] == 0:
                                self.board[row][i - 1] = self.board[row][i]
                                self.board[row][i] = 0
                                moved = True
                            elif self.board[row][i - 1] == self.board[row][i]:
                                self.board[row][i - 1] *= 2
                                self.board[row][i] = 0
                                self.score += self.board[row][i - 1]
                                moved = True
                                break
        elif direction == 'right':
            for row in range(4):
                for col in range(2, -1, -1):
                    if self.board[row][col] != 0:
                        for i in range(col, 3):
                            if self.board[row][i + 1] == 0:
                                self.board[row][i + 1] = self.board[row][i]
                                self.board[row][i] = 0
                                moved = True
                            elif self.board[row][i + 1] == self.board[row][i]:
                                self.board[row][i + 1] *= 2
                                self.board[row][i] = 0
                                self.score += self.board[row][i + 1]
                                moved = True
                                break
        if moved:
            self._add_random_tile()
        return moved

    def is_game_over(self) -> bool:
        # Check if the game is over
        for row in range(4):
            for col in range(4):
                if self.board[row][col] == 0:
                    return False
                if row < 3 and self.board[row][col] == self.board[row + 1][col]:
                    return False
                if col < 3 and self.board[row][col] == self.board[row][col + 1]:
                    return False
        return True

    def get_score(self) -> int:
        return self.score
