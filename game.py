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
            self.turn = "O"

    def check_for_win(self, n=NUM_TO_WIN):
        """Checking from the bottom for n the same symbols
           return True/False if there is/isn't a winner horrizontally"""
        for i, row in enumerate(self.board.board):
            for j, symbol in enumerate(row):
                if symbol is not None:
                    two_dim_board = self.board.board
                    sym = two_dim_board[i][j]
                    # checking vertically
                    count = self._counting_versatile(
                        (i >= (n-1)), sym, i, j, -1, 0, n)
                    if count == n:
                        return True
                    # checking horizontally
                    count = self._counting_versatile(
                        (j >= (n-1)), sym, i, j, 0, -1, n)
                    if count == n:
                        return True
                    # checking diagonally 1
                    count = self._counting_versatile(
                        (i >= (n-1) and j >= (n-1)), sym, i, j, -1, -1, n)
                    if count == n:
                        return True
                    # checking diagonally 2
                    count = self._counting_versatile(
                        (i >= (n-1) and j <= len(row)-n), sym, i, j, -1, 1, n)
                    if count == n:
                        return True
        return False

    def _check_for_evaluation(self, symbol_to_check, n=NUM_TO_WIN):
        if n == 0:
            return True
        for i, row in enumerate(self.board.board):
            for j, symbol in enumerate(row):
                if symbol == symbol_to_check:
                    two_dim_board = self.board.board
                    sym = two_dim_board[i][j]
                    # checking horitonally
                    count = self._counting_versatile(
                        ((j >= (n-1))), sym, i, j, 0, -1, n)
                    cond1 = (j+1 < len(two_dim_board[0])) and (two_dim_board[i][j+1] is None)
                    cond2 = (j-n >= 0) and (two_dim_board[i][j-n] is None)
                    evaluation_cond = cond1 or cond2
                    if count == n and evaluation_cond:
                        return True
                    # checking vertically
                    count = self._counting_versatile(
                        (i >= (n-1)), sym, i, j, 1, 0, n)
                    cond1 = (i+1 < len(two_dim_board)) and (two_dim_board[i+1][j] is None)
                    cond2 = (i-n >= 0) and (two_dim_board[i-n][j] is None)
                    evaluation_cond = cond1 or cond2
                    if count == n and evaluation_cond:
                        return True
                    # checking diagonally /
                    count = self._counting_versatile(
                        (((i+n) <= len(two_dim_board)) and (j-n+1) >= 0),
                        sym, i, j, -1, -1, n)
                    additional_cond = ((j+1) < len(two_dim_board[0])) and ((i-1) >= 0)
                    cond1 = additional_cond and (two_dim_board[i-1][j+1] is None)
                    cond2 = ((i+n) < len(two_dim_board)) and ((j-n) >= 0) and (
                        two_dim_board[i+n][j-n] is None)
                    evaluation_cond = cond1 or cond2
                    if count == n and evaluation_cond:
                        return True
                    # checking diagonally \
                    count = self._counting_versatile(
                        ((j >= (n-1)) and (i >= (n-1))), sym, i, j, 1, -1, n)
                    cond1 = ((i+1) < len(two_dim_board)) and ((j+1) < len(two_dim_board[0])
                                                              ) and (two_dim_board[i+1][j+1] is None)
                    additional_cond = ((j-n) >= 0) and ((i-n) >= 0)
                    cond2 = additional_cond and (two_dim_board[i-n][j-n] is None)
                    evaluation_cond = cond1 or cond2
                    if count == n and evaluation_cond:
                        return True
        return False

    def _counting_versatile(
            self, condition, symbol, i, j, up, right, n=NUM_TO_WIN):
        """Method that helps count symbols in check_for_win function
           depending on the conditions and arguments

           i - nth row
           j - nth column
           left, right indicate direction

           returns a number of counted arguemnts (a number from 0 to n)"""
        count = 0
        left_index = i
        right_index = j
        if condition:
            for num in range(0, n):
                if up == 1:
                    if ((i-num) >= 0):
                        left_index = i-num
                    else:
                        break
                elif up == -1:
                    if ((i+num) < len(self.board.board)):
                        left_index = i+num
                    else:
                        break
                if right == 1:
                    if ((j+num) < len(self.board.board[0])):
                        right_index = j+num
                    else:
                        break
                elif right == -1:
                    if ((j-num) >= 0):
                        right_index = j-num
                    else:
                        break
                two_dim_board = self.board.board
                if two_dim_board[left_index][right_index] == symbol:
                    count += 1
        return count

    def evaluation(self, symbol_to_check, n=NUM_TO_WIN):
        if (self._check_for_evaluation(symbol_to_check, n)):
            return n
        return self.evaluation(symbol_to_check, n-1)
