from board import Board
from constants import NUM_TO_WIN


class Game:
    def __init__(self, board: Board):
        self.start = False
        self.turn = 'O'
        self.end = False
        self.board = board

    def change_turn(self):
        """Changes the attribute that indicate whose turn is it"""
        if self.turn == 'O':
            self.turn = 'X'
        else:
            self.turn = 'O'

    def check_for_win(self, n=NUM_TO_WIN):
        """Checking from the bottom for n the same symbols
           return True/False if there is/isn't a winner horrizontally"""
        for i, row in enumerate(self.board.board):
            for j, symbol in enumerate(row):
                if symbol is not None:
                    two_dim_board = self.board.board
                    sym = two_dim_board[i][j]
                    # checking vertically
                    count = self.board._counting_versatile(
                        (i >= (n-1)), sym, i, j, 1, 0, n)
                    if count == n:
                        return True
                    # checking horizontally
                    count = self.board._counting_versatile(
                        (j >= (n-1)), sym, i, j, 0, -1, n)
                    if count == n:
                        return True
                    # checking diagonally 1
                    count = self.board._counting_versatile(
                        (i >= (n-1) and (j+n <= len(self.board.board[0]))), sym, i, j, 1, 1, n)
                    if count == n:
                        return True
                    # checking diagonally 2
                    count = self.board._counting_versatile(
                        (i >= (n-1) and (j-(n-1)) >= 0), sym, i, j, 1, -1, n)
                    if count == n:
                        return True
        return False

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()
