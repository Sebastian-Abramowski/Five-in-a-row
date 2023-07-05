from board import Board
from pygame import display, RESIZABLE
import pytest
from board import WrongUseOfCheckForNoneDiagonal
from game import Game
from minimax.algorithms import minimax

NUM_TO_WIN = 5  # for testing


def test_evaluation_basic_O_horizontal_1():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['X', 'X', 'X', 'X'],
                   ['O', 'O', None, None],
                   ['X', 'X', 'X', 'X']]
    assert board._check_for_evaluation('O', 2) == (True, True)
    assert board._check_for_evaluation('O', 1) == (True, True)
    assert board._check_for_evaluation('O', 0) == (True, True)
    assert board._check_for_evaluation('O', 3) == (False, False)
    assert board._check_for_evaluation('O', 4) == (False, False)


def test_evaluation_basic_O_horizontal_2():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [[None, None, 'O', 'O'],
                   ['X', 'X', 'X', 'X'],
                   ['X', 'X', 'O', 'X']]
    assert board._check_for_evaluation('O', 2) == (True, True)
    assert board._check_for_evaluation('O', 1) == (True, True)
    assert board._check_for_evaluation('O', 0) == (True, True)
    assert board._check_for_evaluation('O', 3) == (False, False)
    assert board._check_for_evaluation('O', 4) == (False, False)


def test_evaluation_basic_X_horitonal_3():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [[None, None, None, 'X'],
                   ['X', 'X', None, None],
                   ['X', 'X', None, 'X']]

    assert board._check_for_evaluation('X', 2) == (True, False)
    assert board._check_for_evaluation('X', 1) == (True, True)
    assert board._check_for_evaluation('X', 0) == (True, True)
    assert board._check_for_evaluation('X', 3) == (True, False)
    assert board._check_for_evaluation('X', 4) == (False, False)


def test_evaluation_basic_O_horizontal_4():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['X', None, 'O', 'O'],
                   ['X', 'X', 'X', 'X'],
                   ['X', 'X', 'O', 'X']]
    assert board._check_for_evaluation('O', 2) == (True, True)
    assert board._check_for_evaluation('O', 1) == (True, True)
    assert board._check_for_evaluation('O', 0) == (True, True)
    assert board._check_for_evaluation('O', 3) == (False, False)
    assert board._check_for_evaluation('O', 4) == (False, False)


def test_evaluation_basic_O_horizontal_5():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['X', 'X', 'X', 'X'],
                   ['O', 'O', None, 'X'],
                   ['X', 'X', 'X', 'X']]
    assert board._check_for_evaluation('O', 2) == (True, True)
    assert board._check_for_evaluation('O', 1) == (True, True)
    assert board._check_for_evaluation('O', 0) == (True, True)
    assert board._check_for_evaluation('O', 3) == (False, False)
    assert board._check_for_evaluation('O', 4) == (False, False)


def test_evaluation_basic_O_vertical_1():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', None, None, None],
                   ['O', None, 'X', None],
                   [None, None, None, None]]
    assert board._check_for_evaluation('O', 2) == (True, True)
    assert board._check_for_evaluation('O', 1) == (True, True)
    assert board._check_for_evaluation('O', 0) == (True, True)
    assert board._check_for_evaluation('O', 3) == (False, False)
    assert board._check_for_evaluation('O', 4) == (False, False)


def test_evaluation_basic_O_vertical_2():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', None, 'X', None],
                   [None, None, None, 'O'],
                   ['X', None, 'X', 'O']]
    assert board._check_for_evaluation('O', 2) == (True, True)
    assert board._check_for_evaluation('O', 1) == (True, True)
    assert board._check_for_evaluation('O', 0) == (True, True)
    assert board._check_for_evaluation('O', 3) == (False, False)
    assert board._check_for_evaluation('O', 4) == (False, False)


def test_evaluation_basic_O_vertical_3():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', None, None, None],
                   ['O', None, 'X', None],
                   [None, None, None, None]]
    assert board._check_for_evaluation('O', 2) == (True, True)
    assert board._check_for_evaluation('O', 1) == (True, True)
    assert board._check_for_evaluation('O', 0) == (True, True)
    assert board._check_for_evaluation('O', 3) == (False, False)
    assert board._check_for_evaluation('O', 4) == (False, False)


def test_evaluation_basic_O_vertical_4():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', 'X', 'X', None],
                   ['X', 'X', 'X', 'O'],
                   ['X', 'X', 'X', 'O']]
    assert board._check_for_evaluation('O', 2) == (True, True)
    assert board._check_for_evaluation('O', 1) == (True, True)
    assert board._check_for_evaluation('O', 0) == (True, True)
    assert board._check_for_evaluation('O', 3) == (False, False)
    assert board._check_for_evaluation('O', 4) == (False, False)


def test_evaluation_basic_O_vertical_5():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', 'X', 'X', 'X'],
                   ['O', 'X', 'X', 'X'],
                   [None, 'X', 'X', 'X']]
    assert board._check_for_evaluation('O', 2) == (True, True)
    assert board._check_for_evaluation('O', 1) == (True, True)
    assert board._check_for_evaluation('O', 0) == (True, True)
    assert board._check_for_evaluation('O', 3) == (False, False)
    assert board._check_for_evaluation('O', 4) == (False, False)


def test_evaluation_basic_diagonally_1():
    # \
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', None, 'X', 'X'],
                   ['O', 'X', 'TEST', 'X'],
                   [None, 'X', 'X', 'TEST']]
    assert board._check_for_evaluation('TEST', 2) == (True, True)
    assert board._check_for_evaluation('TEST', 1) == (True, True)
    assert board._check_for_evaluation('TEST', 0) == (True, True)
    assert board._check_for_evaluation('TEST', 3) == (False, False)
    assert board._check_for_evaluation('TEST', 4) == (False, False)


def test_evaluation_basic_diagonally_2():
    # \
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', None, 'X', 'X'],
                   ['O', 'X', 'TEST', 'X'],
                   ['X', 'X', 'X', 'TEST']]
    assert board._check_for_evaluation('TEST', 2) == (True, True)
    assert board._check_for_evaluation('TEST', 1) == (True, True)
    assert board._check_for_evaluation('TEST', 0) == (True, True)
    assert board._check_for_evaluation('TEST', 3) == (False, False)
    assert board._check_for_evaluation('TEST', 4) == (False, False)


def test_evaluation_basic_diagonally_3():
    # \
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', 'O', 'X', 'O'],
                   ['X', 'X', 'O', 'O'],
                   ['X', 'X', 'X', 'O']]
    # because there is no free space, all possibilites are blocked
    assert board._check_for_evaluation('O', 2) == (False, False)
    assert board._check_for_evaluation('O', 1) == (False, False)
    assert board._check_for_evaluation('O', 0) == (True, True)
    assert board._check_for_evaluation('O', 3) == (False, False)
    assert board._check_for_evaluation('O', 4) == (False, False)


def test_evaluation_basic_diagonally_4():
    # \
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['TE', 'TEST', None, 'X'],
                   ['O', 'TE', 'TEST', 'X'],
                   ['X', 'X', None, 'TEST']]
    assert board._check_for_evaluation('TE', 2) == (True, True)
    assert board._check_for_evaluation('TE', 1) == (True, True)
    assert board._check_for_evaluation('TE', 0) == (True, True)
    assert board._check_for_evaluation('TE', 3) == (False, False)
    assert board._check_for_evaluation('TE', 4) == (False, False)


def test_evaluation_basic_diagonally_5():
    # \
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['TE', 'TEST', 'K', 'X'],
                   ['O', 'TE', 'TEST', 'X'],
                   ['X', 'X', 'Zajonc', None]]
    assert board._check_for_evaluation('TEST', 2) == (True, True)
    assert board._check_for_evaluation('TEST', 1) == (True, True)
    assert board._check_for_evaluation('TEST', 0) == (True, True)
    assert board._check_for_evaluation('TEST', 3) == (False, False)
    assert board._check_for_evaluation('TEST', 4) == (False, False)


def test_evaluation_basic_diagonally_opposite_1():
    # /
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', 'O_O', 'X', 'TEST'],
                   ['O', 'X', 'TEST', 'X'],
                   ['X', None, 'X', 'X']]
    assert board._check_for_evaluation('TEST', 2) == (True, True)
    assert board._check_for_evaluation('TEST', 1) == (True, True)
    assert board._check_for_evaluation('TEST', 0) == (True, True)
    assert board._check_for_evaluation('TEST', 3) == (False, False)
    assert board._check_for_evaluation('TEST', 4) == (False, False)


def test_evaluation_basic_diagonally_opposite_2():
    # /
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', 'O_O', 'X', None],
                   ['O', 'X', 'TEST', 'X'],
                   ['X', 'TEST', 'X', 'X']]
    assert board._check_for_evaluation('TEST', 2) == (True, True)
    assert board._check_for_evaluation('TEST', 1) == (True, True)
    assert board._check_for_evaluation('TEST', 0) == (True, True)
    assert board._check_for_evaluation('TEST', 3) == (False, False)
    assert board._check_for_evaluation('TEST', 4) == (False, False)


def test_evaluation_basic_diagonally_opposite_3():
    # /
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', 'O_O', None, 'X'],
                   ['O', 'X', 'X', 'X'],
                   ['X', 'O_O', 'X', 'X']]
    assert board._check_for_evaluation('X', 2) == (True, True)
    assert board._check_for_evaluation('X', 1) == (True, True)
    assert board._check_for_evaluation('X', 0) == (True, True)
    assert board._check_for_evaluation('X', 3) == (False, False)
    assert board._check_for_evaluation('X', 4) == (False, False)


def test_evaluation_basic_diagonally_opposite_4():
    # /
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', 'O', 'T', 'X'],
                   ['O', 'T', 'X', 'X'],
                   [None, 'O', 'X', 'X']]
    assert board._check_for_evaluation('T', 2) == (True, True)
    assert board._check_for_evaluation('T', 1) == (True, True)
    assert board._check_for_evaluation('T', 0) == (True, True)
    assert board._check_for_evaluation('T', 3) == (False, False)
    assert board._check_for_evaluation('T', 4) == (False, False)


def test_evaluation_basic_diagonally_opposite_5():
    # /
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', 'O', 'T', 'X'],
                   ['O', 'T', 'X', 'X'],
                   ['T', 'O', 'X', 'X']]
    assert board._check_for_evaluation('T', 2) == (False, False)
    assert board._check_for_evaluation('T', 1) == (False, False)
    assert board._check_for_evaluation('T', 0) == (True, True)
    assert board._check_for_evaluation('T', 3) == (False, False)
    assert board._check_for_evaluation('T', 4) == (False, False)


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
    assert board._check_for_evaluation('E', 6) == (True, True)
    assert board._check_for_evaluation('E', 7) == (False, False)
    assert board._check_for_evaluation('E', 8) == (False, False)
    assert board._check_for_evaluation('K', 7) == (True, True)
    assert board._check_for_evaluation('K', 8) == (True, False)
    assert board._check_for_evaluation('O', 3) == (True, True)
    assert board._check_for_evaluation('O', 4) == (False, False)
    assert board._check_for_evaluation('Z', 4) == (True, True)
    assert board._check_for_evaluation('Z', 5) == (False, False)
    assert board._check_for_evaluation('Q', 4) == (True, True)
    assert board._check_for_evaluation('Q', 5) == (False, False)
    assert board._check_for_evaluation('J', 2) == (True, True)
    assert board._check_for_evaluation('J', 3) == (False, False)
    assert board._check_for_evaluation('R', 1) == (False, False)
    assert board._check_for_evaluation('R', 2) == (False, False)
    assert board._check_for_evaluation('-', 0) == (True, True)


def test_evaluation_basic():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['X', None, 'O', 'O'],
                   ['X', 'X', 'X', 'X'],
                   ['X', 'X', 'O', 'X']]
    assert board._evaluate('X') == 2
    assert board.evaluate() == 0


def test_evaluation():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['E', 'E', 'E', 'E', 'E', 'E', None, None],
                   ['Q', 'T', 'T', 'T', 'T', 'O', 'T', 'K'],
                   ['Q', 'T', 'T', 'T', 'O', 'T', 'T', 'K'],
                   ['Q', None, 'O', 'O', 'T', 'T', 'T', 'K'],
                   ['Q', 'T', 'T', 'Z', 'T', 'T', 'T', 'K'],
                   [None, 'T', 'T', 'T', 'Z', 'T', 'T', 'K'],
                   ['T', 'T', 'T', 'J', 'T', 'Z', 'T', 'K'],
                   ['T', 'T', 'J', 'T', 'R', 'T', 'Z', 'K'],
                   ['T', None, 'T', 'T', 'R', 'T', 'T', None],
                   ['T', 'T', 'T', 'T', 'R', 'T', 'T', 'K']]
    assert board._evaluate('Q') == min(NUM_TO_WIN, 4)
    # because NUM_TO_WIN is set to 5
    assert board._evaluate('K') == 50
    assert board._evaluate('E') == 50
    assert board._evaluate('R') == 0
    assert board._evaluate('O') == min(NUM_TO_WIN, 3)
    assert board._evaluate('Z') == min(NUM_TO_WIN, 4)
    assert board._evaluate('J') == min(NUM_TO_WIN, 2)
    assert board._evaluate('O') == min(NUM_TO_WIN, 3)
    assert board.evaluate() == min(NUM_TO_WIN, 3)


def test_problematic_evaluation():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [[None, None, None, 'O'],
                   [None, None, None, 'O'],
                   [None, None, None, None],
                   [None, None, None, 'O'],
                   [None, None, None, 'O']]
    assert board.evaluate() == 4


def test_problematic_evaluation_2():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [[None, None, None, 'O'],
                   [None, None, None, 'O'],
                   [None, None, None, None],
                   [None, None, None, 'O'],
                   [None, None, None, None]]
    assert board.evaluate() == 3


def test_problematic_evaluation_3():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [[None, None, None, None],
                   [None, None, None, 'O'],
                   [None, None, None, 'O'],
                   [None, None, None, None],
                   [None, None, None, 'O'],
                   [None, None, None, 'O'],
                   [None, None, None, None]]
    assert board.evaluate() == 4


def test_problematic_evaluation_4():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [[None, None, None, None],
                   [None, None, None, None],
                   [None, 'O', None, 'O'],
                   [None, None, None, None],
                   [None, None, None, None]]
    assert board.evaluate() == 2


def test_problematic_evaluation_5():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', None, 'O', 'O'],
                   [None, None, None, None],
                   [None, None, None, None],
                   [None, None, None, None],
                   [None, None, None, None]]
    assert board.evaluate() == 3


def test_problematic_evaluation_6():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [[None, None, None, None, None],
                   [None, 'O', None, 'O', None],
                   [None, None, None, None, None],
                   [None, None, None, None, None],
                   [None, None, None, None, None],
                   [None, None, None, None, None],
                   [None, None, None, None, None]]
    assert board.evaluate() == 2


def test_problematic_evaluation_3_additional():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [[None, 'O', None, None],
                   [None, 'O', None, None],
                   [None, None, None, None],
                   [None, 'O', None, None],
                   [None, 'O', None, None],
                   [None, None, None, None],
                   [None, None, None, None]]
    assert board.evaluate() == 4


def test_problematic_evaluation_3_additional_2():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [[None, 'O', None, None],
                   [None, 'O', None, None],
                   [None, 'Z', None, None],
                   [None, 'O', None, None],
                   [None, 'O', None, None],
                   [None, None, None, None],
                   [None, None, None, None]]
    assert board.evaluate() == 2
    assert board.check_for_none_horizontal_vertical(4, 0, 1, 1) is False


def test_problematic_evaluation_3_additional_3():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['O', 'O', 'K', 'O'],
                   [None, None, None, None],
                   [None, None, None, None],
                   [None, None, None, None],
                   [None, None, None, None],
                   [None, None, None, None],
                   [None, None, None, None]]
    assert board.evaluate() == 1


def test_check_for_none_horitontal_and_vertical():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [[None, 'O', None, 'K'],
                   [None, 'O', None, 'K'],
                   [None, None, 'K', 'K'],
                   [None, 'O', None, None],
                   [None, 'O', None, None],
                   [None, None, None, None],
                   [None, None, None, None]]
    assert board.check_for_none_horizontal_vertical(0, 4, 1, 1) is True
    assert board.check_for_none_horizontal_vertical(0, 1, 1, 1) is False
    assert board.check_for_none_horizontal_vertical(0, 3, 3, 3) is True
    assert board.check_for_none_horizontal_vertical(0, 2, 3, 3) is False
    assert board.check_for_none_horizontal_vertical(0, 3, 3, 3) is True
    assert board.check_for_none_horizontal_vertical(3, 0, 3, 3) is True
    assert board.check_for_none_horizontal_vertical(2, 2, 2, 3) is False
    assert board.check_for_none_horizontal_vertical(2, 2, 1, 3) is True
    assert board.check_for_none_horizontal_vertical(2, 2, 3, 2) is False
    assert board.check_for_none_horizontal_vertical(2, 2, 3, 1) is True


def test_check_for_none_diagonal():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [[None, 'O', None, 'K'],
                   [None, 'O', None, 'K'],
                   [None, None, 'K', 'K'],
                   [None, 'O', None, None],
                   [None, 'O', None, None],
                   [None, None, None, None],
                   [None, None, None, None]]
    assert board.check_for_none_diagonal(0, 2, 1, 3) is True
    assert board.check_for_none_diagonal(3, 1, 3, 1) is True
    assert board.check_for_none_diagonal(1, 3, 1, 3) is True
    assert board.check_for_none_diagonal(4, 1, 0, 3) is True
    assert board.check_for_none_diagonal(3, 1, 1, 3) is False
    with pytest.raises(WrongUseOfCheckForNoneDiagonal):
        board.check_for_none_diagonal(1, 2, 1, 3)
    with pytest.raises(WrongUseOfCheckForNoneDiagonal):
        board.check_for_none_diagonal(-10, 10, 0, 20)


def test_problematic_evaluation_diagonal():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [[None, None, None, None],
                   [None, None, 'O', None],
                   [None, None, None, None],
                   ['O', None, None, None],
                   [None, None, None, None]]
    assert board.evaluate() == 2


def test_problematic_evaluation_diagonal2():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [[None, None, None, None],
                   [None, None, None, 'O'],
                   [None, None, None, None],
                   [None, 'O', None, None],
                   ['O', None, None, None]]
    assert board.evaluate() == 3


def test_problematic_evaluation_diagonal_opposite():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [[None, None, None, None],
                   ['O', None, None, None],
                   [None, 'O', None, None],
                   [None, None, None, None],
                   [None, None, None, 'O']]
    assert board.evaluate() == 3


def test_problematic_evaluation_diagonal_opposite_2():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [[None, None, None, None],
                   ['O', None, None, None],
                   [None, None, None, None],
                   [None, None, 'O', None],
                   [None, None, None, None]]
    assert board.evaluate() == 2


def test_weird_decision():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['X', 'O', None, None, None, None, None, None],
                   ['X', None, 'X', None, None, None, 'X', None],
                   ['O', 'X', 'O', 'O', None, 'O', 'O', None],
                   ['X', None, 'X', None, 'O', None, 'X', None],
                   ['X', 'O', None, 'O', None, 'X', None, None],
                   ['O', None, 'X', None, 'X', None, 'O', None],
                   ['X', 'O', None, 'X', None, None, None, None],
                   [None, None, None, None, None, None, None, 'O']]
    assert board._check_for_evaluation('O', 4)[0] is True
    assert board._check_for_evaluation('X', 4)[0] is True


def test_winning_bug():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [[None, None, None, None, None, None, None, None],
                   [None, 'O', None, None, None, None, 'K', None],
                   [None, None, 'O', None, None, None, 'K', None],
                   [None, None, None, 'O', None, None, None, None],
                   [None, None, None, None, 'O', None, 'K', None],
                   [None, None, None, None, None, 'O', 'K', None],
                   [None, None, None, None, None, None, 'K', None],
                   [None, None, None, None, None, None, None, None]]
    assert board._evaluate('O') > board._evaluate('K')


def test_weird_evaluation_bug():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    game = Game(board)
    board.board = [[None, 'X', 'O', None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, 'O', None, None, None],
                   ['X', None, None, None, None, 'O', None, None],
                   ['O', None, 'X', None, None, None, 'O', None],
                   ['X', None, 'O', None, None, None, None, None],
                   ['X', None, 'X', None, None, None, None, None],
                   ['X', 'X', None, None, 'O', 'O', 'O', 'X']]
    value, new_board = minimax(game.get_board(), 2, 'O', game)
    assert new_board.board == [[None, 'X', 'O', None, None, None, None, None],
                               [None, None, None, 'O', None, None, None, None],
                               [None, None, None, None, 'O', None, None, None],
                               ['X', None, None, None, None, 'O', None, None],
                               ['O', None, 'X', None, None, None, 'O', None],
                               ['X', None, 'O', None, None, None, None, None],
                               ['X', None, 'X', None, None, None, None, None],
                               ['X', 'X', None, None, 'O', 'O', 'O', 'X']]


def test_weird_evaluation_bug_2():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    game = Game(board)
    board.board = [[None, None, None, None, None, None, None, None],
                   [None, None, 'X', None, None, None, None, None],
                   [None, None, None, 'X', 'O', None, None, None],
                   [None, None, 'X', None, 'X', 'X', 'X', None],
                   [None, None, None, None, None, 'O', 'O', 'O'],
                   [None, None, None, None, None, None, 'X', None],
                   [None, None, None, None, None, None, 'O', None],
                   [None, None, None, None, None, None, 'O', None]]
    value, new_board = minimax(game.get_board(), 2, True, game)
    assert new_board.board[3][3] == 'O'


def test_cause_of_weird_evaluation_bug_3():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [[None, None, None, None, None, None, 'X', None],
                   [None, None, 'X', 'O', None, 'X', None, None],
                   [None, None, 'X', None, 'X', 'X', None, None],
                   [None, None, None, 'X', None, 'O', None, None],
                   [None, None, 'X', None, 'O', 'X', 'O', None],
                   [None, 'O', None, 'X', 'O', 'X', 'X', 'X'],
                   [None, None, None, 'X', 'O', 'O', 'O', 'O'],
                   [None, None, None, None, 'X', 'O', 'O', 'O']]
    assert board._evaluate('X') >= 5


def test_direct_or_indirect_winning():
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    board.board = [['X', 'X', 'X', None, 'X', 'X', None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, 'X', None, None],
                   [None, None, None, None, 'X', None, None, None],
                   [None, None, None, 'X', None, None, None, None],
                   [None, None, 'X', None, None, None, None, None],
                   [None, 'X', None, None, None, None, None, None]]
    board._check_for_evaluation('X', 5) == (True, True)


def test_ai_weird_decision():
    """
    The purpose of this test is to block potential win or
    move that can easily result in winning, but not
    in spite of your own winning move
    """
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    game = Game(board)
    board.board = [[None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, 'X', 'X', 'X', None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, 'O'],
                   [None, None, None, None, None, None, None, 'O'],
                   [None, None, None, None, 'X', 'O', 'X', 'O']]
    value, new_board = minimax(game.get_board(), 2, True, game)
    assert new_board.board[7][3] != 'O'
    board.board = [[None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, 'X', 'X', 'X', None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, 'O'],
                   [None, None, None, None, None, None, None, 'O'],
                   [None, None, None, None, None, None, None, 'O'],
                   [None, None, None, None, 'X', 'O', 'X', 'O']]
    value, new_board = minimax(game.get_board(), 2, True, game)
    assert new_board.board[3][7] == 'O'


def test_potencial_win():
    """
    The purpose of this test is to check whether having
    potencial win have higher priority than blocking potencial
    lose (potencial lose needs more rounds that potencial win)
    """
    window = display.set_mode((2000, 700),  RESIZABLE)
    board = Board(window)
    game = Game(board)
    board.board = [[None, None, None, 'O', 'O', 'O', None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, 'X', None, None, None, None, None],
                   [None, None, None, 'X', None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None]]
    value, new_board = minimax(game.get_board(), 2, True, game)
    assert new_board.board[0][6] == 'O'


def test_effects_of_higher_priority_of_potencial_win():
    """
    Checking why it doesn't pick blocking the potencial lose
    """


def test_decision_before_losing_anyway():
    """
    It should try prevent the player from winning, even if it
    is not possible assuming player would make the best possible
    choice
    """
