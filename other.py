from pygame import mouse
from board import Board
from pygame import Rect, font, display
from constants import WHITE, WEIRD_GREEN, BIG_FONT_SIZE, FONT, FONT_BIG_TEXT
from constants import YELLOW


def rectangle_clicked(board: Board):
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


def draw_text(window, font: font, text: str,
              percent: float, colour_r_g_b, y=15):
    """
    Method that allows to write some text in space of padding
    at the top of the window;
    percent - 0.00 - 1.00
    The bigger the percent the more on the right the text will be
    """
    # percent 0.5 means center 0.25 means left quarter etc
    img_font = font.render(text, True, colour_r_g_b)
    font_width, _ = font.size(text)
    font_width = font_width * percent
    width = window.get_width() * percent
    x = width - font_width
    window.blit(img_font, (x, y))


def draw_after_end(window: display, game, if_draw=False, winner=None):
    """
    This method should be called after detecting winning in
    an instance of Game
    Draws who won more or less at the center of the window and
    information about what to press to restart the game
    """
    y_around_center = window.get_size()[1]//2-BIG_FONT_SIZE//2
    ending_text = f"{winner} WON" if not if_draw else "DRAW"
    color = WEIRD_GREEN if not if_draw else YELLOW
    draw_text(window, FONT_BIG_TEXT,
              ending_text, 0.5, color,
              y=y_around_center)
    draw_text(window, FONT, "Press 'space' to restart", 0.5, WHITE)
    draw_text(window, FONT, "Press 'Esc' to exit", 0.96, WHITE)
