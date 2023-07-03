from game import Game
from board import Board
from pygame import display, RESIZABLE
from constants import NUM_TO_WIN


def test_evaluation_basic_O_horizontal_1():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['X', 'X', 'X', 'X'],
                   ['O', 'O', None, None],
                   ['X', 'X', 'X', 'X']]
    game = Game(board)
    assert game._check_for_evaluation('O', 2) is True
    assert game._check_for_evaluation('O', 1) is True
    assert game._check_for_evaluation('O', 0) is True
    assert game._check_for_evaluation('O', 3) is False
    assert game._check_for_evaluation('O', 4) is False


def test_evaluation_basic_O_horizontal_2():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [[None, None, 'O', 'O'],
                   ['X', 'X', 'X', 'X'],
                   ['X', 'X', 'O', 'X']]
    game = Game(board)
    assert game._check_for_evaluation('O', 2) is True
    assert game._check_for_evaluation('O', 1) is True
    assert game._check_for_evaluation('O', 0) is True
    assert game._check_for_evaluation('O', 3) is False
    assert game._check_for_evaluation('O', 4) is False


def test_evaluation_basic_X_horitonal_3():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [[None, None, None, 'X'],
                   ['X', 'X', None, None],
                   [None, None, None, None]]
    game = Game(board)
    assert game._check_for_evaluation('X', 2) is True
    assert game._check_for_evaluation('X', 1) is True
    assert game._check_for_evaluation('X', 0) is True
    assert game._check_for_evaluation('X', 3) is False
    assert game._check_for_evaluation('X', 4) is False


def test_evaluation_basic_O_horizontal_4():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['X', None, 'O', 'O'],
                   ['X', 'X', 'X', 'X'],
                   ['X', 'X', 'O', 'X']]
    game = Game(board)
    assert game._check_for_evaluation('O', 2) is True
    assert game._check_for_evaluation('O', 1) is True
    assert game._check_for_evaluation('O', 0) is True
    assert game._check_for_evaluation('O', 3) is False
    assert game._check_for_evaluation('O', 4) is False


def test_evaluation_basic_O_horizontal_5():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['X', 'X', 'X', 'X'],
                   ['O', 'O', None, 'X'],
                   ['X', 'X', 'X', 'X']]
    game = Game(board)
    assert game._check_for_evaluation('O', 2) is True
    assert game._check_for_evaluation('O', 1) is True
    assert game._check_for_evaluation('O', 0) is True
    assert game._check_for_evaluation('O', 3) is False
    assert game._check_for_evaluation('O', 4) is False


def test_evaluation_basic_O_vertical_1():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', None, None, None],
                   ['O', None, 'X', None],
                   [None, None, None, None]]
    game = Game(board)
    assert game._check_for_evaluation('O', 2) is True
    assert game._check_for_evaluation('O', 1) is True
    assert game._check_for_evaluation('O', 0) is True
    assert game._check_for_evaluation('O', 3) is False
    assert game._check_for_evaluation('O', 4) is False


def test_evaluation_basic_O_vertical_2():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', None, 'X', None],
                   [None, None, None, 'O'],
                   ['X', None, 'X', 'O']]
    game = Game(board)
    assert game._check_for_evaluation('O', 2) is True
    assert game._check_for_evaluation('O', 1) is True
    assert game._check_for_evaluation('O', 0) is True
    assert game._check_for_evaluation('O', 3) is False
    assert game._check_for_evaluation('O', 4) is False


def test_evaluation_basic_O_vertical_3():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', None, None, None],
                   ['O', None, 'X', None],
                   [None, None, None, None]]
    game = Game(board)
    assert game._check_for_evaluation('O', 2) is True
    assert game._check_for_evaluation('O', 1) is True
    assert game._check_for_evaluation('O', 0) is True
    assert game._check_for_evaluation('O', 3) is False
    assert game._check_for_evaluation('O', 4) is False


def test_evaluation_basic_O_vertical_4():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', 'X', 'X', None],
                   ['X', 'X', 'X', 'O'],
                   ['X', 'X', 'X', 'O']]
    game = Game(board)
    assert game._check_for_evaluation('O', 2) is True
    assert game._check_for_evaluation('O', 1) is True
    assert game._check_for_evaluation('O', 0) is True
    assert game._check_for_evaluation('O', 3) is False
    assert game._check_for_evaluation('O', 4) is False


def test_evaluation_basic_O_vertical_5():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', 'X', 'X', 'X'],
                   ['O', 'X', 'X', 'X'],
                   [None, 'X', 'X', 'X']]
    game = Game(board)
    assert game._check_for_evaluation('O', 2) is True
    assert game._check_for_evaluation('O', 1) is True
    assert game._check_for_evaluation('O', 0) is True
    assert game._check_for_evaluation('O', 3) is False
    assert game._check_for_evaluation('O', 4) is False


def test_evaluation_basic_diagonally_1():
    # \
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', None, 'X', 'X'],
                   ['O', 'X', 'TEST', 'X'],
                   [None, 'X', 'X', 'TEST']]
    game = Game(board)
    assert game._check_for_evaluation('TEST', 2) is True
    assert game._check_for_evaluation('TEST', 1) is True
    assert game._check_for_evaluation('TEST', 0) is True
    assert game._check_for_evaluation('TEST', 3) is False
    assert game._check_for_evaluation('TEST', 4) is False


def test_evaluation_basic_diagonally_2():
    # \
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', None, 'X', 'X'],
                   ['O', 'X', 'TEST', 'X'],
                   ['X', 'X', 'X', 'TEST']]
    game = Game(board)
    assert game._check_for_evaluation('TEST', 2) is True
    assert game._check_for_evaluation('TEST', 1) is True
    assert game._check_for_evaluation('TEST', 0) is True
    assert game._check_for_evaluation('TEST', 3) is False
    assert game._check_for_evaluation('TEST', 4) is False


def test_evaluation_basic_diagonally_3():
    # \
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', 'X', 'X', 'O'],
                   ['X', 'X', 'X', 'O'],
                   ['X', 'X', 'X', 'O']]
    game = Game(board)
    assert game._check_for_evaluation('X', 2) is False
    assert game._check_for_evaluation('X', 1) is False
    assert game._check_for_evaluation('X', 0) is True
    assert game._check_for_evaluation('X', 3) is False
    assert game._check_for_evaluation('X', 4) is False


def test_evaluation_basic_diagonally_4():
    # \
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['TE', 'TEST', None, 'X'],
                   ['O', 'TE', 'TEST', 'X'],
                   ['X', 'X', None, 'TEST']]
    game = Game(board)
    assert game._check_for_evaluation('TE', 2) is True
    assert game._check_for_evaluation('TE', 1) is True
    assert game._check_for_evaluation('TE', 0) is True
    assert game._check_for_evaluation('TE', 3) is False
    assert game._check_for_evaluation('TE', 4) is False


def test_evaluation_basic_diagonally_5():
    # \
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['TE', 'TEST', 'K', 'X'],
                   ['O', 'TE', 'TEST', 'X'],
                   ['X', 'X', 'Zajonc', None]]
    game = Game(board)
    assert game._check_for_evaluation('TEST', 2) is True
    assert game._check_for_evaluation('TEST', 1) is True
    assert game._check_for_evaluation('TEST', 0) is True
    assert game._check_for_evaluation('TEST', 3) is False
    assert game._check_for_evaluation('TEST', 4) is False


def test_evaluation_basic_diagonally_opposite_1():
    # /
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', 'O_O', 'X', 'TEST'],
                   ['O', 'X', 'TEST', 'X'],
                   ['X', None, 'X', 'X']]
    game = Game(board)
    assert game._check_for_evaluation('TEST', 2) is True
    assert game._check_for_evaluation('TEST', 1) is True
    assert game._check_for_evaluation('TEST', 0) is True
    assert game._check_for_evaluation('TEST', 3) is False
    assert game._check_for_evaluation('TEST', 4) is False


def test_evaluation_basic_diagonally_opposite_2():
    # /
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', 'O_O', 'X', None],
                   ['O', 'X', 'TEST', 'X'],
                   ['X', 'TEST', 'X', 'X']]
    game = Game(board)
    assert game._check_for_evaluation('TEST', 2) is True
    assert game._check_for_evaluation('TEST', 1) is True
    assert game._check_for_evaluation('TEST', 0) is True
    assert game._check_for_evaluation('TEST', 3) is False
    assert game._check_for_evaluation('TEST', 4) is False


def test_evaluation_basic_diagonally_opposite_3():
    # /
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', 'O_O', None, 'X'],
                   ['O', 'X', 'X', 'X'],
                   ['X', 'O_O', 'X', 'X']]
    game = Game(board)
    assert game._check_for_evaluation('X', 2) is True
    assert game._check_for_evaluation('X', 1) is True
    assert game._check_for_evaluation('X', 0) is True
    assert game._check_for_evaluation('X', 3) is False
    assert game._check_for_evaluation('X', 4) is False


def test_evaluation_basic_diagonally_opposite_4():
    # /
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', 'O', 'T', 'X'],
                   ['O', 'T', 'X', 'X'],
                   [None, 'O', 'X', 'X']]
    game = Game(board)
    assert game._check_for_evaluation('T', 2) is True
    assert game._check_for_evaluation('T', 1) is True
    assert game._check_for_evaluation('T', 0) is True
    assert game._check_for_evaluation('T', 3) is False
    assert game._check_for_evaluation('T', 4) is False


def test_evaluation_basic_diagonally_opposite_5():
    # /
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', 'O', 'T', 'X'],
                   ['O', 'T', 'X', 'X'],
                   ['T', 'O', 'X', 'X']]
    game = Game(board)
    assert game._check_for_evaluation('T', 2) is False
    assert game._check_for_evaluation('T', 1) is False
    assert game._check_for_evaluation('T', 0) is True
    assert game._check_for_evaluation('T', 3) is False
    assert game._check_for_evaluation('T', 4) is False


def test_check_for_evaluation():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['E', 'E', 'E', 'E', 'E', 'E', None, None],
                   ['Q', 'T', 'T', 'T', 'T', 'O', 'T', 'K'],
                   ['Q', 'T', 'T', 'T', 'O', 'T', 'T', 'K'],
                   ['Q', 'T', 'T', 'O', 'T', 'T', 'T', 'K'],
                   ['Q', 'T', 'T', 'Z', 'T', 'T', 'T', 'K'],
                   [None, 'T', 'T', 'T', 'Z', 'T', 'T', 'K'],
                   ['T', 'T', 'T', 'J', 'T', 'Z', 'T', 'K'],
                   ['T', 'T', 'J', 'T', 'R', 'T', 'Z', 'K'],
                   ['T', None, 'T', 'T', 'R', 'T', 'T', None],
                   ['T', 'T', 'T', 'T', 'R', 'T', 'T', 'K']]
    game = Game(board)
    assert game._check_for_evaluation('E', 6) is True
    assert game._check_for_evaluation('E', 7) is False
    assert game._check_for_evaluation('K', 7) is True
    assert game._check_for_evaluation('E', 8) is False
    assert game._check_for_evaluation('O', 3) is True
    assert game._check_for_evaluation('O', 4) is False
    assert game._check_for_evaluation('Z', 4) is True
    assert game._check_for_evaluation('Z', 5) is False
    assert game._check_for_evaluation('Q', 4) is True
    assert game._check_for_evaluation('Q', 5) is False
    assert game._check_for_evaluation('J', 2) is True
    assert game._check_for_evaluation('J', 3) is False
    assert game._check_for_evaluation('R', 1) is False
    assert game._check_for_evaluation('R', 2) is False
    assert game._check_for_evaluation('-', 0) is True


def test_evaluation_basic():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['X', None, 'O', 'O'],
                   ['X', 'X', 'X', 'X'],
                   ['X', 'X', 'O', 'X']]
    game = Game(board)
    assert game.evaluation('X') == 2


def test_evaluation():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['E', 'E', 'E', 'E', 'E', 'E', None, None],
                   ['Q', 'T', 'T', 'T', 'T', 'O', 'T', 'K'],
                   ['Q', 'T', 'T', 'T', 'O', 'T', 'T', 'K'],
                   ['Q', 'T', 'T', 'O', 'T', 'T', 'T', 'K'],
                   ['Q', 'T', 'T', 'Z', 'T', 'T', 'T', 'K'],
                   [None, 'T', 'T', 'T', 'Z', 'T', 'T', 'K'],
                   ['T', 'T', 'T', 'J', 'T', 'Z', 'T', 'K'],
                   ['T', 'T', 'J', 'T', 'R', 'T', 'Z', 'K'],
                   ['T', None, 'T', 'T', 'R', 'T', 'T', None],
                   ['T', 'T', 'T', 'T', 'R', 'T', 'T', 'K']]
    game = Game(board)
    assert game.evaluation('Q') == min(NUM_TO_WIN, 4)
    assert game.evaluation('K') == min(NUM_TO_WIN, 7)
    assert game.evaluation('E') == min(NUM_TO_WIN, 6)
    assert game.evaluation('O') == min(NUM_TO_WIN, 3)
    assert game.evaluation('R') == 0
    assert game.evaluation('Z') == min(NUM_TO_WIN, 4)
    assert game.evaluation('J') == min(NUM_TO_WIN, 2)
