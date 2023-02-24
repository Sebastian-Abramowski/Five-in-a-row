from pygame import mouse
from board import Board
from pygame import Rect


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
    for i, row in enumerate(board.rectangles):
        for j, rectangle in enumerate(row):
            if rectangle == rect:
                return i, j
    return None


def is_place_empty(board, rect):
    if row_col_of_rect(board, rect) is None:
        return None
    row, col = row_col_of_rect(board, rect)
    if board.board[row][col] is None:
        return True
    return False


def draw_x_and_o(window, board, x_img, o_img):
    for i, row in enumerate(board.board):
        for j, x_or_o in enumerate(row):
            rect = board.rectangles_borders[i][j]
            if x_or_o == "O":
                window.blit(o_img, rect.topleft)
            elif x_or_o == 'X':
                window.blit(x_img, rect.topleft)
