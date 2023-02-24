from board import Board


class Game:
    def __init__(self, board: Board):
        self.start = False
        self.turn = 'O'
        self.end = False
        self.board = board

    def change_turn(self):
        if self.turn == 'O':
            self.turn = 'X'
        else:
            self.turn = "O"
