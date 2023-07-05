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
        self.validation_empty()

    def __deepcopy__(self, memo=None):
        new_board = Board(self.window, self._padding, self._square_size)
        new_board.board = deepcopy(self.board, memo)

        return new_board

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
        """
        Updates rectangles in the board, it is important to do
        so after changing the size of the board

        for example when before starting the game when someone changes
        size of the window
        """
        self.update_rectangles()
        self.update_rectangles_for_borders()

    def draw(self):
        self.draw_rectangles(self.rectangles, BLACK)
        self.draw_rectangles(self.rectangles_borders, GREY)

    def draw_rectangles(self, array_of_rows_of_rects, colour):
        """
        Draws the rectangles passed in array with passed colour
        """
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
        """If no rectangles can be generated, it raises
           GeneratingBoardError"""
        if len(self.rectangles) == 0:
            raise GeneratingBoardError()

    def _check_for_evaluation(self, symbol_to_check, n=NUM_TO_WIN):
        result_if_max_n = [None, None]
        if n == 0:
            return True, True
        for i, row in enumerate(self.board):
            for j, symbol in enumerate(row):
                if symbol == symbol_to_check:
                    two_dim_board = self.board
                    sym = two_dim_board[i][j]
                    # checking horitonally
                    count = self._counting_versatile(
                        ((j >= (n-1))), sym, i, j, 0, -1, n)
                    count2 = self._counting_versatile(
                        ((j >= (n-1))), sym, i, j, 0, -1, n, True)
                    cond1 = (j+1 < len(two_dim_board[0])) and (two_dim_board[i][j+1] is None)
                    cond2 = (j-n >= 0) and (two_dim_board[i][j-n] is None)
                    cond3 = ((j-n) >= 0) and (two_dim_board[i][j-n] == symbol)
                    cond4 = ((j-n) >= 0) and self.check_for_none_horizontal_vertical(i, i, j, j-n)
                    evaluation_cond = cond1 or cond2
                    if ((count2 == n and evaluation_cond) or (count2 == NUM_TO_WIN)):
                        if ((cond1 and cond2) and (n == (NUM_TO_WIN - 2))):
                            self.if_potencial_lose = True
                        if ((cond1 and cond2) and (n == (NUM_TO_WIN - 1))):
                            self.if_potencial_win = True
                        return True, True
                    elif (count == n and (cond3 and cond4)):
                        if (n == NUM_TO_WIN):
                            result_if_max_n[0] = True
                        else:
                            return True, False
                    # checking vertically
                    count = self._counting_versatile(
                        (i >= (n-1)), sym, i, j, 1, 0, n)
                    count2 = self._counting_versatile(
                        (i >= (n-1)), sym, i, j, 1, 0, n, True)
                    cond1 = (i+1 < len(two_dim_board)) and (two_dim_board[i+1][j] is None)
                    cond2 = (i-n >= 0) and (two_dim_board[i-n][j] is None)
                    cond3 = ((i-n) >= 0) and (two_dim_board[i-n][j] == symbol)
                    cond4 = ((i-n) >= 0) and self.check_for_none_horizontal_vertical(i, i-n, j, j)
                    evaluation_cond = cond1 or cond2
                    if ((count2 == n and evaluation_cond) or (count2 == NUM_TO_WIN)):
                        if ((cond1 and cond2) and (n == (NUM_TO_WIN - 2))):
                            self.if_potencial_lose = True
                        if ((cond1 and cond2) and (n == (NUM_TO_WIN - 1))):
                            self.if_potencial_win = True
                        return True, True
                    elif (count == n and (cond3 and cond4)):
                        if (n == NUM_TO_WIN):
                            result_if_max_n[0] = True
                        else:
                            return True, False
                    # checking diagonally /
                    count = self._counting_versatile(
                        (((i+n) <= len(two_dim_board)) and (j-n+1) >= 0),
                        sym, i, j, -1, -1, n)
                    count2 = self._counting_versatile(
                        (((i+n) <= len(two_dim_board)) and (j-n+1) >= 0),
                        sym, i, j, -1, -1, n, True)
                    additional_cond = ((j+1) < len(two_dim_board[0])) and ((i-1) >= 0)
                    cond1 = additional_cond and (two_dim_board[i-1][j+1] is None)
                    cond2 = ((i+n) < len(two_dim_board)) and ((j-n) >= 0) and (
                        two_dim_board[i+n][j-n] is None)
                    evaluation_cond = cond1 or cond2
                    cond4 = ((i+n) < len(two_dim_board)) and ((j-n) >= 0) and (
                        two_dim_board[i+n][j-n] == symbol)
                    cond3 = ((i+n) < len(two_dim_board)) and (
                        (j-n) >= 0) and self.check_for_none_diagonal(i, i+n, j, j-n)
                    if ((count2 == n and evaluation_cond) or (count2 == NUM_TO_WIN)):
                        if ((cond1 and cond2) and (n == (NUM_TO_WIN - 2))):
                            self.if_potencial_lose = True
                        if ((cond1 and cond2) and (n == (NUM_TO_WIN - 1))):
                            self.if_potencial_win = True
                        return True, True
                    elif (count == n and (cond4 and cond3)):
                        if (n == NUM_TO_WIN):
                            result_if_max_n[0] = True
                        else:
                            return True, False
                    # checking diagonally \
                    count = self._counting_versatile(
                        ((j >= (n-1)) and (i >= (n-1))), sym, i, j, 1, -1, n)
                    count2 = self._counting_versatile(
                        ((j >= (n-1)) and (i >= (n-1))), sym, i, j, 1, -1, n, True)
                    cond1 = ((i+1) < len(two_dim_board)) and ((j+1) < len(two_dim_board[0])
                                                              ) and (two_dim_board[i+1][j+1] is None)
                    additional_cond = ((j-n) >= 0) and ((i-n) >= 0)
                    cond2 = additional_cond and (two_dim_board[i-n][j-n] is None)
                    evaluation_cond = cond1 or cond2
                    cond4 = (i-n) >= 0 and ((j-n) >= 0) and (two_dim_board[i-n][j-n] == symbol)
                    cond3 = (i-n) >= 0 and (
                        (j-n) >= 0) and self.check_for_none_diagonal(i, i-n, j, j-n)
                    if ((count2 == n and evaluation_cond) or (count2 == NUM_TO_WIN)):
                        if ((cond1 and cond2) and (n == (NUM_TO_WIN - 2))):
                            self.if_potencial_lose = True
                        if ((cond1 and cond2) and (n == (NUM_TO_WIN - 1))):
                            self.if_potencial_win = True
                        return True, True
                    elif (count == n and (cond4 and cond3)):
                        if (n == NUM_TO_WIN):
                            result_if_max_n[0] = True
                        else:
                            return True, False

        if ((n == NUM_TO_WIN) and (result_if_max_n[0] is True)):
            result_if_max_n[1] = False
            return tuple(result_if_max_n)

        return False, False

    def evaluate(self, n=NUM_TO_WIN):
        """Returns score of the board, the bigger, the better for 'O'

           it takes into account max number of symbols that are not blocked"""
        return (self._evaluate('O') - self._evaluate('X'))

    def _evaluate(self, symbol_to_check, n=NUM_TO_WIN):
        if_got_eval, direct_result = self._check_for_evaluation(symbol_to_check, n)
        if if_got_eval:
            if direct_result:
                if (n == NUM_TO_WIN):
                    return 10*n
                if (self.if_potencial_lose and symbol_to_check == 'X') or (self.if_potencial_win
                                                                           and symbol_to_check == 'O'):
                    self.if_potencial_win = False
                    self.if_potencial_lose = False
                    return 5*n
            return n
        return self._evaluate(symbol_to_check, n-1)

    def _counting_versatile(
            self, condition, symbol, i, j, up, right, n=NUM_TO_WIN, check_for_win=False):
        """Method that helps count symbols in check_for_win function
           depending on the conditions and arguments

           i - nth row
           j - nth column
           left, right indicate direction

           returns a number of counted arguemnts (a number from 0 to n)"""
        count = 0
        left_index = i
        right_index = j
        if condition:
            upper_limit = n if check_for_win else (n+1)
            for num in range(0, upper_limit):
                if up == 1:
                    if ((i-num) >= 0):
                        left_index = i-num
                    else:
                        break
                elif up == -1:
                    if ((i+num) < len(self.board)):
                        left_index = i+num
                    else:
                        break
                if right == 1:
                    if ((j+num) < len(self.board[0])):
                        right_index = j+num
                    else:
                        break
                elif right == -1:
                    if ((j-num) >= 0):
                        right_index = j-num
                    else:
                        break
                if (self.board[left_index][right_index] == symbol):
                    count += 1
        return count

    def get_board(self):
        return self.board

    def check_for_none_horizontal_vertical(self, start_i, end_i, start_j, end_j):
        for index_i in range(abs(end_i - start_i) + 1):
            for index_j in range(abs(end_j - start_j) + 1):
                if (end_i - start_i) >= 0:
                    index_i_check = start_i + index_i
                else:
                    index_i_check = start_i - index_i

                if (end_j - start_j) >= 0:
                    index_j_check = start_j + index_j
                else:
                    index_j_check = start_j - index_j

                if self.board[index_i_check][index_j_check] is None:
                    return True
        return False

    def check_for_none_diagonal(self, start_i, end_i, start_j, end_j):
        if (abs(start_i - end_i)) != abs(start_j - end_j):
            raise WrongUseOfCheckForNoneDiagonal()

        while True:
            try:
                if (self.board[start_i][start_j] is None):
                    return True
            except IndexError:
                raise WrongUseOfCheckForNoneDiagonal()

            if ((start_i == end_i) and (start_j == end_j)):
                break

            if start_i > end_i:
                start_i -= 1
            elif start_i < end_i:
                start_i += 1
            if start_j > end_j:
                start_j -= 1
            elif start_j < end_j:
                start_j += 1

        return False
