from game import Game
from board import Board
from pygame import display, RESIZABLE


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
    # assert game._check_for_evaluation('O', 1) is True
    # assert game._check_for_evaluation('O', 0) is True
    # assert game._check_for_evaluation('O', 3) is False
    # assert game._check_for_evaluation('O', 4) is False
# test_evaluation_basic_O_horizontal_4()


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
