from constants import PADDING, SQUARE_SIZE, GREY
from constants import SQUARE_BORDER_SIZE, BLACK, NUM_TO_WIN
from pygame import Rect, draw
from copy import deepcopy


class GeneratingBoardError(Exception):
    def __init__(self):
        super().__init__("You cannot generate empty board")


class WrongUseOfCheckForNoneDiagonal(Exception):
    def __init__(self):
        super().__init__("Passed indexes don't form diagonal line")


class Board:
    def __init__(self, window, padding=PADDING, square_size=SQUARE_SIZE):
        self.window = window
        self._padding = padding
        self._square_size = square_size
        self.rectangles = self.array_of_rectangles()
        self.rectangles_borders = self._rects_for_borders()
        self.board = None
        self.if_potencial_lose = False
        self.if_potencial_win = False
        self.counter_nearly_x_win = 0
        self.validation_empty()

    def __deepcopy__(self, memo=None):
        new_board = Board(self.window, self._padding, self._square_size)
        new_board.board = deepcopy(self.board, memo)

        return new_board

    def __str__(self):
        """Returns string of result of the method - self._center_of_rects()
           in an appropriate way"""
        return "\n".join([str(row) for row in self.board])

    def _board_empty(self):
        """
        Creates a plain board that will hold symbols later
        Everyplace is filled with None value
        """
        board_empty = []
        for row in self.rectangles:
            new_row = []
            for _ in row:
                new_row.append(None)
            board_empty.append(new_row)
        return board_empty

    def update_empty_board(self):
        """
        Updates board.board attribute with the plain board
        with None values

        Important to use before allowing players to move or
        at the start of the game
        """
        self.board = self._board_empty()

    def _get_window_width_height(self):
        "Returns (width, height) of the window (attribute)"
        window_widht, window_height = self.window.get_size()
        return window_widht, window_height

    def _how_many_rectangles(self):
        """Returns number of possible empty squares
           horizontally and vertically as a tuple"""
        window_width, window_height = self._get_window_width_height()
        num_rect_vertical = (window_height - 2*self._padding) // self._square_size
        num_rect_horizontal = (window_width - 2*self._padding) // self._square_size
        return num_rect_horizontal, num_rect_vertical

    def calc_starting_points(self):
        """Returns (x, y) where x, y are coordinates of
           the first empty square"""
        width, height = self._get_window_width_height()
        num_rect_horizontal, num_rect_vertical = self._how_many_rectangles()
        starting_x = self._padding + (
            width - 2*self._padding - num_rect_horizontal*self._square_size)//2
        starting_y = self._padding + (
            height - 2*self._padding - num_rect_vertical*self._square_size)//2
        return starting_x, starting_y

    def array_of_rectangles(self):
        """Returns two-dimensional array of rectangles
           that represents empty spaces on the board"""
        array_of_rects = []
        num_rect_horizontal, num_rect_vertical = self._how_many_rectangles()
        start_x, start_y = self.calc_starting_points()

        coordinate_y = start_y
        for _ in range(num_rect_vertical):
            coordinate_x = start_x
            row_of_rectangles = []
            for _ in range(num_rect_horizontal):
                rect = Rect(
                    coordinate_x, coordinate_y,
                    self._square_size, self._square_size)
                row_of_rectangles.append(rect)
                coordinate_x += self._square_size
            array_of_rects.append(row_of_rectangles)
            coordinate_y += self._square_size
        return array_of_rects

    def update_rectangles(self):
        self.rectangles = self.array_of_rectangles()

    def update_rectangles_for_borders(self):
        self.rectangles_borders = self._rects_for_borders()

    def update(self):
        """
        Updates rectangles in the board, it is important to do
        so after changing the size of the board

        for example when before starting the game when someone changes
        size of the window
        """
        self.update_rectangles()
        self.update_rectangles_for_borders()
        self.update_empty_board()

    def draw(self, border_color=BLACK, rectangle_color=GREY):
        self.draw_rectangles(self.rectangles, border_color)
        self.draw_rectangles(self.rectangles_borders, rectangle_color)

    def draw_rectangles(self, array_of_rows_of_rects, colour):
        """
        Draws the rectangles passed in array with passed colour
        """
        for row_of_rects in array_of_rows_of_rects:
            for rectangle in row_of_rects:
                draw.rect(self.window, colour, rectangle)

    def _rects_for_borders(self, square_border_size=SQUARE_BORDER_SIZE):
        """Returns two-dimensional array of rectangles
           that will be inside spaces on the board(self.rectangles)
           in order to imitate borders"""
        rect_for_borders = []
        for row_of_rects in self.rectangles:
            rects_in_row = []
            for rectangle in row_of_rects:
                rectangle.left += square_border_size
                rectangle.top += square_border_size
                rectangle.width -= 2*square_border_size
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

    def validation_empty(self):
        """If no rectangles can be generated, it raises
           GeneratingBoardError"""
        if len(self.rectangles) == 0:
            raise GeneratingBoardError()

    def _check_condition_for_evaluation(self, num_symbols, num_to_win, num_indirect_symbols,
                                        num_direct_symbols, if_none_beside_starting_place,
                                        if_none_beside_place_at_end, if_symbol_beside_place_at_end,
                                        if_none_between_symbols, if_none_beside_final_or_starting_place,
                                        additional_data, result_if_max_n):
        if (num_direct_symbols == num_to_win):
            return True, True
        elif ((num_direct_symbols == num_symbols and if_none_beside_final_or_starting_place)):
            if (if_none_beside_starting_place and if_none_beside_place_at_end):
                if (num_symbols == (num_to_win - 2)):
                    self.if_potencial_lose = True
                if (num_symbols == (num_to_win - 1)):
                    self.if_potencial_win = True
                return True, True
            if (num_symbols == (num_to_win - 1)):
                additional_data["counter_nearly_x_win"] += 1
                additional_data["if_direct"] = True
            else:
                return True, True
        elif (num_indirect_symbols == num_symbols and (if_symbol_beside_place_at_end and if_none_between_symbols)):
            if (num_symbols == num_to_win):
                result_if_max_n[0] = True
            elif (num_symbols == (num_to_win - 1)):
                additional_data["counter_nearly_x_win"] += 1
            else:
                return True, False

    def _check_for_evaluation(self, symbol_to_check, num_symbols=NUM_TO_WIN, num_to_win=NUM_TO_WIN):
        result_if_max_n = [None, None]
        additional_data = {"counter_nearly_x_win": 0, "if_direct": False}
        self.counter_nearly_x_win = 0

        if num_symbols == 0:
            return True, True

        for row_index, row in enumerate(self.board):
            for column_index, symbol in enumerate(row):
                if symbol == symbol_to_check:
                    two_dimensional_board = self.board
                    # checking horitonally
                    num_indirect_symbols = self.count_symbols_universal(
                        ((column_index >= (num_symbols-1))), symbol, row_index, column_index, 0, -1, num_symbols)
                    num_direct_symbols = self.count_symbols_universal(
                        ((column_index >= (num_symbols-1))), symbol, row_index,
                        column_index, 0, -1, num_symbols, True)
                    if_none_on_right = (column_index+1 < len(two_dimensional_board[0])) and (
                        two_dimensional_board[row_index][column_index+1] is None)
                    if_none_on_left = (column_index-num_symbols >= 0) and (two_dimensional_board[
                        row_index][column_index-num_symbols] is None)
                    if_symbol_on_left = ((column_index-num_symbols) >= 0) and (two_dimensional_board[
                        row_index][column_index-num_symbols] == symbol)
                    if_none_between_symbols = (
                        (column_index-num_symbols) >= 0) and self.check_for_none_horizontal_vertical(
                        row_index, row_index, column_index, column_index-num_symbols)
                    if_none_on_right_or_left = if_none_on_right or if_none_on_left

                    result = self._check_condition_for_evaluation(num_symbols, num_to_win, num_indirect_symbols,
                                                                  num_direct_symbols, if_none_on_right,
                                                                  if_none_on_left, if_symbol_on_left,
                                                                  if_none_between_symbols,
                                                                  if_none_on_right_or_left,
                                                                  additional_data, result_if_max_n)
                    if result:
                        return result

                    # checking vertically
                    num_indirect_symbols = self.count_symbols_universal(
                        (row_index >= (num_symbols-1)), symbol, row_index, column_index, 1, 0, num_symbols)
                    num_direct_symbols = self.count_symbols_universal(
                        (row_index >= (num_symbols-1)), symbol, row_index, column_index, 1, 0, num_symbols, True)
                    if_none_down_below = (row_index+1 < len(two_dimensional_board)) and (two_dimensional_board[
                        row_index+1][column_index] is None)
                    if_none_up = (row_index-num_symbols >= 0) and (two_dimensional_board[
                        row_index-num_symbols][column_index] is None)
                    if_symbol_up = ((row_index-num_symbols) >= 0) and (two_dimensional_board[
                        row_index-num_symbols][column_index] == symbol)
                    if_none_between_symbols = (
                        (row_index-num_symbols) >= 0) and self.check_for_none_horizontal_vertical(
                        row_index, row_index-num_symbols, column_index, column_index)
                    if_none_below_or_up = if_none_down_below or if_none_up

                    result = self._check_condition_for_evaluation(num_symbols, num_to_win, num_indirect_symbols,
                                                                  num_direct_symbols, if_none_down_below,
                                                                  if_none_up, if_symbol_up,
                                                                  if_none_between_symbols,
                                                                  if_none_below_or_up,
                                                                  additional_data, result_if_max_n)
                    if result:
                        return result

                    # checking diagonally /
                    num_indirect_symbols = self.count_symbols_universal(
                        (((row_index+num_symbols) <= len(
                            two_dimensional_board)) and (column_index-num_symbols+1) >= 0),
                        symbol, row_index, column_index, -1, -1, num_symbols)
                    num_direct_symbols = self.count_symbols_universal(
                        (((row_index+num_symbols) <= len(
                            two_dimensional_board)) and (column_index-num_symbols+1) >= 0),
                        symbol, row_index, column_index, -1, -1, num_symbols, True)
                    if_place_right_top_exists = ((column_index+1) < len(two_dimensional_board[0])) and (
                        (row_index-1) >= 0)
                    if_none_top_right = if_place_right_top_exists and (two_dimensional_board[
                        row_index-1][column_index+1] is None)
                    if_none_bottom_left = ((row_index+num_symbols) < len(two_dimensional_board)) and (
                        (column_index-num_symbols) >= 0) and (two_dimensional_board[row_index+num_symbols][
                            column_index-num_symbols] is None)
                    if_none_top_right_or_bottom_left = if_none_top_right or if_none_bottom_left
                    if_symbol_bottom_left = ((row_index+num_symbols) < len(two_dimensional_board)) and (
                        (column_index-num_symbols) >= 0) and (two_dimensional_board[row_index+num_symbols][
                            column_index-num_symbols] == symbol)
                    if_none_between_symbols = ((row_index+num_symbols) < len(two_dimensional_board)) and (
                        (column_index-num_symbols) >= 0) and self.check_for_none_diagonal(row_index,
                                                                                          row_index+num_symbols,
                                                                                          column_index,
                                                                                          column_index-num_symbols)

                    result = self._check_condition_for_evaluation(num_symbols, num_to_win, num_indirect_symbols,
                                                                  num_direct_symbols, if_none_top_right,
                                                                  if_none_bottom_left,
                                                                  if_none_between_symbols,
                                                                  if_symbol_bottom_left,
                                                                  if_none_top_right_or_bottom_left,
                                                                  additional_data, result_if_max_n)
                    if result:
                        return result

                    # checking diagonally \
                    num_indirect_symbols = self.count_symbols_universal(
                        ((column_index >= (num_symbols-1)) and (row_index >= (num_symbols-1))), symbol, row_index,
                        column_index, 1, -1, num_symbols)
                    num_direct_symbols = self.count_symbols_universal(
                        ((column_index >= (num_symbols-1)) and (row_index >= (num_symbols-1))), symbol,
                        row_index, column_index, 1, -1, num_symbols, True)
                    if_none_bottom_right = ((row_index+1) < len(two_dimensional_board)) and (
                        (column_index+1) < len(two_dimensional_board[0])) and (two_dimensional_board[
                            row_index+1][column_index+1] is None)
                    if_place_top_left_exists = ((column_index-num_symbols) >= 0) and ((row_index-num_symbols) >= 0)
                    if_none_top_left = if_place_top_left_exists and (two_dimensional_board[
                        row_index-num_symbols][column_index-num_symbols] is None)
                    if_none_bottom_right_or_top_left = if_none_bottom_right or if_none_top_left
                    if_symbol_top_left = (row_index-num_symbols) >= 0 and ((column_index-num_symbols) >= 0) and (
                        two_dimensional_board[row_index-num_symbols][column_index-num_symbols] == symbol)
                    if_none_between_symbols = (row_index-num_symbols) >= 0 and (
                        (column_index-num_symbols) >= 0) and self.check_for_none_diagonal(row_index,
                                                                                          row_index-num_symbols,
                                                                                          column_index,
                                                                                          column_index-num_symbols)

                    result = self._check_condition_for_evaluation(num_symbols, num_to_win, num_indirect_symbols,
                                                                  num_direct_symbols, if_none_bottom_right,
                                                                  if_none_top_left, if_none_between_symbols,
                                                                  if_symbol_top_left,
                                                                  if_none_bottom_right_or_top_left,
                                                                  additional_data, result_if_max_n)
                    if result:
                        return result

        if ((num_symbols == num_to_win) and (result_if_max_n[0] is True)):
            result_if_max_n[1] = False
            return tuple(result_if_max_n)

        if (num_symbols == (num_to_win - 1) and additional_data["counter_nearly_x_win"] >= 1):
            self.counter_nearly_x_win = additional_data["counter_nearly_x_win"]
            return True, additional_data["if_direct"]

        return False, False

    def evaluate(self, num_symbols=NUM_TO_WIN, num_to_win=NUM_TO_WIN):
        """Returns score of the board, the bigger, the better for 'O'

           it takes into account max number of symbols that are not blocked"""
        return (self._evaluate('O', num_symbols, num_to_win) - self._evaluate(
            'X', num_symbols, num_to_win))

    def _evaluate(self, symbol_to_check, num_symbols=NUM_TO_WIN, num_to_win=NUM_TO_WIN):
        if_got_eval, direct_result = self._check_for_evaluation(symbol_to_check, num_symbols, num_to_win)
        if if_got_eval:
            if direct_result:
                if (num_symbols == num_to_win):
                    return 10*num_symbols
                if self.if_potencial_win:
                    self.if_potencial_win = False
                    return 5*num_symbols
                if (self.if_potencial_lose and symbol_to_check == 'X'):
                    self.if_potencial_lose = False
                    return 2*num_symbols
            if (num_symbols == (num_to_win - 1) and self.counter_nearly_x_win >= 2):
                return 3*num_symbols
            return num_symbols
        return self._evaluate(symbol_to_check, num_symbols-1, num_to_win)

    def _count_symbols(self, data_for_counting, up, right, upper_limit, symbol):
        row_index = data_for_counting["row_index"]
        column_index = data_for_counting["column_index"]
        temp_row_index = row_index
        temp_column_index = column_index
        count = data_for_counting["count"]

        for num in range(0, upper_limit):
            if up == 1:
                if ((row_index-num) >= 0):
                    temp_row_index = row_index-num
                else:
                    break
            elif up == -1:
                if ((row_index+num) < len(self.board)):
                    temp_row_index = row_index+num
                else:
                    break
            if right == 1:
                if ((column_index+num) < len(self.board[0])):
                    temp_column_index = column_index+num
                else:
                    break
            elif right == -1:
                if ((column_index-num) >= 0):
                    temp_column_index = column_index-num
                else:
                    break
            if (self.board[temp_row_index][temp_column_index] == symbol):
                count += 1

        data_for_counting["count"] = count

    def count_symbols_universal(
            self, condition, symbol, row_index, column_index,
            up, right, num_symbols=NUM_TO_WIN, check_for_win=False):
        """Method that helps count symbols in check_for_win function
           depending on the conditions and arguments

           i - nth row
           column_index - nth column
           left, right indicate direction

           returns a number of counted arguemnts (a number from 0 to n)"""
        data_for_counting = {"count": 0, "row_index": row_index,  "column_index": column_index}

        if condition:
            upper_limit = num_symbols if check_for_win else (num_symbols+1)
            self._count_symbols(data_for_counting, up, right, upper_limit, symbol)
        return data_for_counting["count"]

    def get_board(self):
        return self.board

    def check_for_none_horizontal_vertical(self, row_index_start, row_index_end,
                                           column_index_start, column_index_end):
        for index_i in range(abs(row_index_end - row_index_start) + 1):
            for index_j in range(abs(column_index_end - column_index_start) + 1):
                if (row_index_end - row_index_start) >= 0:
                    temp_row_index = row_index_start + index_i
                else:
                    temp_row_index = row_index_start - index_i

                if (column_index_end - column_index_start) >= 0:
                    temp_column_index = column_index_start + index_j
                else:
                    temp_column_index = column_index_start - index_j

                if self.board[temp_row_index][temp_column_index] is None:
                    return True
        return False

    def check_for_none_diagonal(self, row_index_start, row_index_end,
                                column_index_start, column_index_end):
        if (abs(row_index_start - row_index_end)) != abs(column_index_start - column_index_end):
            raise WrongUseOfCheckForNoneDiagonal()

        while True:
            try:
                if (self.board[row_index_start][column_index_start] is None):
                    return True
            except IndexError:
                raise WrongUseOfCheckForNoneDiagonal()

            if ((row_index_start == row_index_end) and (column_index_start == column_index_end)):
                break

            if row_index_start > row_index_end:
                row_index_start -= 1
            elif row_index_start < row_index_end:
                row_index_start += 1
            if column_index_start > column_index_end:
                column_index_start -= 1
            elif column_index_start < column_index_end:
                column_index_start += 1

        return False
