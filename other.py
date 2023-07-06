from pygame import mouse
from board import Board
from pygame import Rect, font, display
from constants import WHITE, WEIRD_GREEN, FONT, FONT_BIG_TEXT
from constants import YELLOW, NUM_TO_WIN, PADDING, FONT_SIZE
from constants import BIG_FONT_SIZE


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


def draw_after_end(window: display, if_draw=False, winner=None, small_font=FONT, small_font_color=WHITE,
                   big_font=FONT_BIG_TEXT, big_font_size=BIG_FONT_SIZE, win_text_color=WEIRD_GREEN,
                   draw_text_color=YELLOW):
    """
    This method should be called after detecting winning in
    an instance of Game
    Draws who won more or less at the center of the window and
    information about what to press to restart the game
    """
    y_around_center = (window.get_size()[1]-big_font_size)//2
    ending_text = f"{winner} WON" if not if_draw else "DRAW"
    color = win_text_color if not if_draw else draw_text_color
    draw_text(window, big_font,
              ending_text, 0.5, color,
              y=y_around_center)
    draw_text(window, small_font, "Press 'space' to restart", 0.05, small_font_color)
    draw_text(window, small_font, "Press 'Esc' to exit", 0.95, small_font_color)


def draw_num_to_win_info(window: display, num_to_win=NUM_TO_WIN,
                         font=FONT, font_size=FONT_SIZE, padding=PADDING, color=WHITE):
    num_to_win_info = f"NUM_TO_WIN={num_to_win}"
    y_bottom = window.get_size()[1] - (padding + 1.5*font_size) // 2
    draw_text(window, font, num_to_win_info, 0.5, color, y_bottom)
