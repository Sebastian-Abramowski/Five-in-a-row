from board import Board
from other import symbol_of_taken_space
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
                    sym = symbol_of_taken_space(
                            self.board, self.board.rectangles[i][j])
                    # checking horitonally
                    count = self._counting_versatile(
                        (i >= (n-1)), sym, i, j, -1, 0, n)
                    if count == n:
                        return True
                    # checking diagonally
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

    def _counting_versatile(
            self, condition, sym, i, j, left, right, n=NUM_TO_WIN):
        """Method that helps count symbols in check_for_win function
           depending on the conditions and arguments

           returns a number of counted arguemnts (a number from 0 to n)"""
        count = 0
        left_index = i
        right_index = j
        if condition:
            for num in range(0, n):
                if left == 1:
                    left_index = i+num
                elif left == -1:
                    left_index = i-num
                if right == 1:
                    right_index = j+num
                elif right == -1:
                    right_index = j-num
                if symbol_of_taken_space(
                    self.board, self.board.rectangles[
                        left_index][right_index]) == sym:
                    count += 1
        return count
