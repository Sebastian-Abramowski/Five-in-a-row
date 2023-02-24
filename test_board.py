import pytest
from board import Board, GeneratingBoardError
from pygame import Rect


class Window:
    def get_size():
        return None


def size():
    return 1000, 2000
    # width, height


def test_board_init(monkeypatch):
    window = Window()

    monkeypatch.setattr(window, "get_size", size)

    board = Board(window, 100, 200)
    assert board.window == window
    assert board._padding == 100
    assert board._square_size == 200
    assert len(board.rectangles) == 9
    assert len(board.rectangles[0]) == 4
    assert len(board.rectangles_borders) == 9
    assert len(board.rectangles_borders[0]) == 4
    assert isinstance(board.rectangles[0][0], Rect) is True


def test_width_height_of_window(monkeypatch):
    window = Window()
    monkeypatch.setattr(window, "get_size", size)
    board = Board(window, 100, 200)
    assert board._width_height_window() == (1000, 2000)


def test_how_many_rectangles(monkeypatch):
    window = Window()
    monkeypatch.setattr(window, "get_size", size)
    board = Board(window, 100, 200)
    assert board._how_many_rectangles() == (4, 9)


def test_calc_starting_points_easy(monkeypatch):
    window = Window()
    monkeypatch.setattr(window, "get_size", size)
    board = Board(window, 100, 200)
    board.calc_starting_points() == (
        board._padding, board._padding)


def test_calc_starting_points_hard(monkeypatch):
    window = Window()

    # covering global size() function
    def size():
        return 900, 1000

    monkeypatch.setattr(window, "get_size", size)
    board = Board(window, 100, 200)
    assert board.calc_starting_points() == (board._padding+50, board._padding)

# methods array_of_rectangles and _rects_for_borders where
# checked manually, they seem fine


def test_update_rectangles(monkeypatch):
    window = Window()
    monkeypatch.setattr(window, "get_size", size)
    board = Board(window, 100, 200)

    def returnSth():
        return "test"
    monkeypatch.setattr(board, "array_of_rectangles", returnSth)
    board.update_rectangles()
    assert board.rectangles == "test"


def test_update_rectangles_for_borders(monkeypatch):
    window = Window()
    monkeypatch.setattr(window, "get_size", size)
    board = Board(window, 100, 200)

    def returnSth():
        return "test"
    monkeypatch.setattr(board, "_rects_for_borders", returnSth)
    board.update_rectangles_for_borders()
    assert board.rectangles_borders == "test"


def test_centers_of_rects_basic(monkeypatch):
    window = Window()

    # covering global size() function
    def size():
        return 300, 500

    monkeypatch.setattr(window, "get_size", size)
    board = Board(window, 100, 200)
    board._centers_of_rects() == [[150, 250]]


def test_generating_board_error(monkeypatch):
    with pytest.raises(GeneratingBoardError):
        window = Window()

        # covering global size() function
        def size():
            return 200, 300

        monkeypatch.setattr(window, "get_size", size)
        board = Board(window, 100, 200)  # noqa: F841


def test_board_empty(monkeypatch):
    window = Window()
    monkeypatch.setattr(window, "get_size", size)
    board = Board(window, 100, 200)
    empty_b = board._board_empty()
    assert len(empty_b) == 9
    assert len(empty_b[0]) == 4
    assert empty_b[0][0] is None
