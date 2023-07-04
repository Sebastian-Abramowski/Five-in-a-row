from board import Board
from constants import NUM_TO_WIN


class Game:
    def __init__(self, board: Board):
        self.start = False
        self.turn = 'X'
        self.end = False
        self.board = board
        self.if_first_ai_move = True

    def change_turn(self):
        """Changes the attribute that indicate whose turn is it"""
        if self.turn == 'O':
            self.turn = 'X'
        else:
            self.turn = 'O'

    def check_for_win(self, board=None, n=NUM_TO_WIN):
        if board is None:
            board = self.board
        """Checking from the bottom for n the same symbols
           return True/False if there is/isn't a winner horrizontally"""
        for i, row in enumerate(board.board):
            for j, symbol in enumerate(row):
                if symbol is not None:
                    two_dim_board = board.board
                    sym = two_dim_board[i][j]
                    # checking vertically
                    count = board._counting_versatile(
                        (i >= (n-1)), sym, i, j, 1, 0, n, True)
                    if count == n:
                        return True, symbol
                    # checking horizontally
                    count = board._counting_versatile(
                        (j >= (n-1)), sym, i, j, 0, -1, n, True)
                    if count == n:
                        return True, symbol
                    # checking diagonally 1
                    count = board._counting_versatile(
                        (i >= (n-1) and (j+n <= len(board.board[0]))), sym, i, j, 1, 1, n, True)
                    if count == n:
                        return True, symbol
                    # checking diagonally 2
                    count = board._counting_versatile(
                        (i >= (n-1) and (j-(n-1)) >= 0), sym, i, j, 1, -1, n, True)
                    if count == n:
                        return True, symbol
        return False, None

    def check_for_draw(self):
        for row in self.board.board:
            if None in row:
                return False
        return True

    def get_board(self):
        return self.board

    def ai_move(self, board):
        """
        if we had got rid of pygame.display in the Board's attribute,
        there would be no problem with just replacing the whole instances
        of Boards
        """
        self.board.board = board.board  # replacing content of board
        self.change_turn()

    def ai_move_first(self, board):
        for i, row in enumerate(board.board):
            for j, symbol in enumerate(row):
                if symbol == 'X':
                    try:
                        board.board[i][j+1] = 'O'
                    except IndexError:
                        board.board[i][j-1] = 'O'
        self.if_first_ai_move = False
        self.change_turn()
