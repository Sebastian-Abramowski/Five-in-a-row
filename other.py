from pygame import mouse
from board import Board
from pygame import Rect
from constants import FONT, WHITE


def what_rectangle_was_clicked(board: Board):
    """
    Returns either an instance of pygame.Rect or None
    """
    mouse_pos = mouse.get_pos()
    for rectangles_row in board.rectangles:
        for rectangle in rectangles_row:
            if rectangle.collidepoint(mouse_pos):
                return rectangle
    return None


def row_col_of_rect(board: Board, rect: Rect):
    """
    Returns (row, col) of the passed rectangle that is
    in board.board
    Returns None if no such rectangle was found
    """
    for i, row in enumerate(board.rectangles):
        for j, rectangle in enumerate(row):
            if rectangle == rect:
                return i, j
    return None


def is_place_empty(board, rect):
    """
    Returns True/False depending if the place
    in the passed rectangle is empty in the board
    """
    if row_col_of_rect(board, rect) is None:
        return None
    row, col = row_col_of_rect(board, rect)
    if board.board[row][col] is None:
        return True
    return False


def symbol_of_taken_space(board, rect):
    """
    Returns the symbol of the place taken that is
    inside passed rectangle, otherwise returns None
    """
    if row_col_of_rect(board, rect) is None:
        return None
    row, col = row_col_of_rect(board, rect)
    if board.board[row][col] is None:
        return None
    else:
        return board.board[row][col]


def draw_x_and_o(window, board, x_img, o_img):
    """
    Draws symbols "O"/"X" on the board
    """
    for i, row in enumerate(board.board):
        for j, x_or_o in enumerate(row):
            rect = board.rectangles_borders[i][j]
            if x_or_o == "O":
                window.blit(o_img, rect.topleft)
            elif x_or_o == 'X':
                window.blit(x_img, rect.topleft)


def draw_text(window, text: str, percent: float):
    """
    Method that allows to write some text in space of padding
    at the top of the window;
    percent - 0.00 - 1.00
    The bigger the percent the more on the right the text will be
    """
    # percent 0.5 means center 0.25 means left quarter etc
    img_font = FONT.render(text, True, WHITE)
    font_width, _ = FONT.size(text)
    font_width = font_width * percent
    width = window.get_width() * percent
    x = width - font_width
    window.blit(img_font, (x, 15))
