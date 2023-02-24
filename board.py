from constants import PADDING, SQUARE_SIZE, GREY
from constants import SQUARE_BORDER_SIZE, BLACK
from pygame import Rect, draw


class GeneratingBoardError(Exception):
    def __init__(self):
        super().__init__("You cannot generate empty board")


class Board:
    def __init__(self, window, padding=PADDING, square_size=SQUARE_SIZE):
        self.window = window
        self._padding = padding
        self._square_size = square_size
        self.rectangles = self.array_of_rectangles()
        self.rectangles_borders = self._rects_for_borders()
        self.board = None
        self.validation_empty()

    def _board_empty(self):
        board_empty = []
        for row in self.rectangles:
            new_row = []
            for rect in row:
                new_row.append(None)
            board_empty.append(new_row)
        return board_empty

    def update_empty_board(self):
        self.board = self._board_empty()

    def _width_height_window(self):
        "Returns (width, height) of the window (attribute)"
        w, h = self.window.get_size()
        return w, h

    def _how_many_rectangles(self):
        """Returns number of possible empty squares
           horizontally and vertically as a tuple"""
        w, h = self._width_height_window()
        how_many_ver = (h - 2*self._padding) // self._square_size
        how_many_hori = (w - 2*self._padding) // self._square_size
        return how_many_hori, how_many_ver

    def calc_starting_points(self):
        """Returns (x, y) where x, y are coordinates of
           the first empty square"""
        w, h = self._width_height_window()
        hw_hori, hw_ver = self._how_many_rectangles()
        starting_x = self._padding + (
            w - 2*self._padding - hw_hori*self._square_size)//2
        starting_y = self._padding + (
            h - 2*self._padding - hw_ver*self._square_size)//2
        return starting_x, starting_y

    def array_of_rectangles(self):
        """Returns two-dimensional array of rectangles
           that represents empty spaces on the board"""
        array_of_rects = []
        hw_hori, hw_ver = self._how_many_rectangles()
        start_x, start_y = self.calc_starting_points()

        y = start_y
        for i in range(hw_ver):
            x = start_x
            row_of_rectangles = []
            for j in range(hw_hori):
                rect = Rect(
                    x, y,
                    self._square_size, self._square_size)
                row_of_rectangles.append(rect)
                x += self._square_size
            array_of_rects.append(row_of_rectangles)
            y += self._square_size
        return array_of_rects

    def update_rectangles(self):
        self.rectangles = self.array_of_rectangles()

    def update_rectangles_for_borders(self):
        self.rectangles_borders = self._rects_for_borders()

    def update(self):
        self.update_rectangles()
        self.update_rectangles_for_borders()

    def draw(self):
        self.draw_rectangles(self.rectangles, BLACK)
        self.draw_rectangles(self.rectangles_borders, GREY)

    def draw_rectangles(self, array_of_rows_of_rects, colour):
        for row_of_rects in array_of_rows_of_rects:
            for rectangle in row_of_rects:
                draw.rect(self.window, colour, rectangle)

    def _rects_for_borders(self):
        """Returns two-dimensional array of rectangles
           that will be inside spaces on the board(self.rectangles)
           in order to imitate borders"""
        rect_for_borders = []
        for row_of_rects in self.rectangles:
            rects_in_row = []
            for rectangle in row_of_rects:
                rectangle.left += SQUARE_BORDER_SIZE
                rectangle.top += SQUARE_BORDER_SIZE
                rectangle.width -= 2*SQUARE_BORDER_SIZE
                rectangle.height = rectangle.width
                rects_in_row.append(rectangle)
            rect_for_borders.append(rects_in_row)
        return rect_for_borders

    def _centers_of_rects(self):
        """Returns two-dimensional array of centers of rectangles
           that represents possible spaces on the board"""
        centers_of_rects = []
        for row_of_rects in self.rectangles:
            centers_of_rects.append([rect.center for rect in row_of_rects])
        return centers_of_rects

    def __str__(self):
        """Returns string of result of the method - self._center_of_rects()
           in an appropriate way"""
        return "\n".join([str(row) for row in self._centers_of_rects()])

    def validation_empty(self):
        """If no rectangles can be generates, it raises
           GeneratingBoardError"""
        if len(self.rectangles) == 0:
            raise GeneratingBoardError()
