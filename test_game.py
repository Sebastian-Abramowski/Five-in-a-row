from game import Game
from board import Board
from pygame import display, RESIZABLE


def test_check_for_win_horizontal():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', 'X', 'X'],
                   [None, None, None],
                   ['O', 'O', 'O']]
    game = Game(board)
    assert game.check_for_win(None, 3)[0] is True


def test_check_for_win_vertical():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['Z', 'X', 'X'],
                   ['Z', None, None],
                   ['Z', 'O', 'Z']]
    game = Game(board)
    assert game.check_for_win(None, 3)[0] is True


def test_check_for_win_diagonal_1():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['K', 'X', 'X'],
                   ['Z', 'K', None],
                   ['Z', 'O', 'K']]
    game = Game(board)
    assert game.check_for_win(None, 3)[0] is True


def test_check_for_win_diagonal_2():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['Z', 'X', 'U'],
                   ['Z', 'U', None],
                   ['U', 'O', 'Z']]
    game = Game(board)
    assert game.check_for_win(None, 3)[0] is True


def test_check_for_win():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    game = Game(board)
    board.board = [[None, 'X', 'O', None, None, None, None, None],
                   [None, None, None, 'O', None, None, None, None],
                   [None, None, None, None, 'O', None, None, None],
                   ['X', None, None, None, None, 'O', None, None],
                   ['O', None, 'X', None, None, None, 'O', None],
                   ['X', None, 'O', None, None, None, None, None],
                   ['X', None, 'X', None, None, None, None, None],
                   ['X', 'X', None, None, 'O', 'O', 'O', 'X']]
    assert game.check_for_win(None, 5)[0] is True


def test_check_for_win_2():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    game = Game(None)
    board.board = [[None, 'X', 'O', None, None, None, None, None],
                   [None, None, None, 'O', None, None, None, None],
                   [None, None, None, None, 'O', None, None, None],
                   ['X', None, None, None, None, 'O', None, None],
                   ['O', None, 'X', None, None, None, 'O', None],
                   ['X', None, 'O', None, None, None, None, None],
                   ['X', None, 'X', None, None, None, None, None],
                   ['X', 'X', None, None, 'O', 'O', 'O', 'X']]
    assert game.check_for_win(board, 5)[0] is True


def test_check_for_draw_false():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', 'X', 'X'],
                   ['X', 'X', None],
                   ['O', 'X', 'O']]
    game = Game(board)
    assert game.check_for_draw(board) is False
    assert game.check_for_draw(None) is False
    assert game.check_for_draw() is False


def test_check_for_draw_true():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', 'X', 'X'],
                   ['X', 'X', '#'],
                   ['O', 'X', 'O']]
    game = Game(board)
    assert game.check_for_draw(board) is True
    assert game.check_for_draw(None) is True
    assert game.check_for_draw() is True
