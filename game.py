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

    def check_for_win(self, board=None, num_to_win=NUM_TO_WIN):
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
                    count = board.count_symbols_universal(
                        (i >= (num_to_win-1)), sym, i, j, 1, 0, num_to_win, True)
                    if count == num_to_win:
                        return True, symbol
                    # checking horizontally
                    count = board.count_symbols_universal(
                        (j >= (num_to_win-1)), sym, i, j, 0, -1, num_to_win, True)
                    if count == num_to_win:
                        return True, symbol
                    # checking diagonally 1
                    count = board.count_symbols_universal(
                        (i >= (num_to_win-1) and (j+num_to_win <= len(board.board[0]))),
                        sym, i, j, 1, 1, num_to_win, True)
                    if count == num_to_win:
                        return True, symbol
                    # checking diagonally 2
                    count = board.count_symbols_universal(
                        (i >= (num_to_win-1) and (j-(num_to_win-1)) >= 0),
                        sym, i, j, 1, -1, num_to_win, True)
                    if count == num_to_win:
                        return True, symbol
        return False, None

    def check_for_draw(self, board=None):
        if board is None:
            board = self.board

        for row in board.board:
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

    def ai_move_first(self, board, num_to_win=NUM_TO_WIN):
        if (num_to_win == 3):
            if (board.board[1][1] == 'X'):
                board.board[0][0] = 'O'
            else:
                board.board[1][1] = 'O'
        else:
            for i, row in enumerate(board.board):
                for j, symbol in enumerate(row):
                    if symbol == 'X':
                        try:
                            board.board[i][j+1] = 'O'
                        except IndexError:
                            board.board[i][j-1] = 'O'
        self.if_first_ai_move = False
        self.change_turn()
