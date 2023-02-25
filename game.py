from board import Board
from other import symbol_of_taken_space


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

    def check_for_win_hori_or_verti(self, n=5):
        """Checking from the bottom for n the same symbols
           return True/False if there is/isn't a winner horrizontally"""
        for i, row in enumerate(self.board.board):
            for j, symbol in enumerate(row):
                if symbol is not None:
                    sym = symbol_of_taken_space(
                            self.board, self.board.rectangles[i][j])
                    count = 0
                    if i >= (n-1):
                        for num in range(0, n):
                            if symbol_of_taken_space(
                                self.board, self.board.rectangles[
                                    i-num][j]) == sym:
                                count += 1
                    if count == n:
                        return True
                    count = 0
                    if j >= (n-1):
                        for num in range(0, n):
                            if symbol_of_taken_space(
                                self.board, self.board.rectangles[
                                    i][j-num]) == sym:
                                count += 1
                    if count == n:
                        return True
        return False

    def check_for_win_diagonally(self, n=5):
        for i, row in enumerate(self.board.board):
            for j, symbol in enumerate(row):
                if symbol is not None:
                    sym = symbol_of_taken_space(
                            self.board, self.board.rectangles[i][j])
                    count = 0
                    if i >= (n-1):
                        for num in range(0, n):
                            if symbol_of_taken_space(
                                self.board, self.board.rectangles[
                                    i-num][j-num]) == sym:
                                count += 1
                    if count == n:
                        return True
                    count = 0
                    if i >= (n-1):
                        for num in range(0, n):
                            if symbol_of_taken_space(
                                self.board, self.board.rectangles[
                                    i-num][j+num]) == sym:
                                count += 1
                    if count == n:
                        return True
        return False
