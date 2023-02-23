from constants import PADDING, SQUARE_SIZE, GREY
from constants import SQUARE_BORDER_SIZE, BLACK
from pygame import Rect, draw


class Board:
    def __init__(self, window):
        self.window = window
        self._padding = PADDING
        self._square_size = SQUARE_SIZE
        self.rectangles = self.array_of_rectangles()
        self.rectangles_borders = self._rects_for_borders()

    def _width_height_window(self):
        w, h = self.window.get_size()
        return w, h

    def _how_many_rectangles(self):
        w, h = self._width_height_window()
        how_many_ver = (h - 2*self._padding) // self._square_size
        how_many_hori = (w - 2*self._padding) // self._square_size
        return how_many_hori, how_many_ver

    def calc_starting_points(self):
        w, h = self._width_height_window()
        hw_hori, hw_ver = self._how_many_rectangles()
        starting_x = self._padding + (
            w - 2*self._padding - hw_hori*self._square_size)//2
        starting_y = self._padding + (
            h - 2*self._padding - hw_ver*self._square_size)//2
        return starting_x, starting_y

    def array_of_rectangles(self):
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
        centers_of_rects = []
        for row_of_rects in self.rectangles:
            centers_of_rects.append([rect.center for rect in row_of_rects])
        return centers_of_rects

    def __str__(self):
        return "\n".join([str(row) for row in self._centers_of_rects()])
