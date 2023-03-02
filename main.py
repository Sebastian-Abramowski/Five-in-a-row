import pygame
import sys
from constants import BLACK, FPS, MIN_WIDTH, MIN_HEIGHT, WHITE
from constants import SQUARE_SIZE, SQUARE_BORDER_SIZE, FONT
from board import Board
from other import what_rectangle_was_clicked, draw_x_and_o
from other import row_col_of_rect, is_place_empty
from game import Game
from other import draw_text, drawing_after_winning


pygame.init()
pygame.display.set_caption("Five-in-a-row")
window = pygame.display.set_mode((2000, 700),  pygame.RESIZABLE)
clock = pygame.time.Clock()

# Images
X_IMG = pygame.image.load(
        'Images/x2.png').convert_alpha()
X_IMG = pygame.transform.scale(
    X_IMG, (
        SQUARE_SIZE-2*SQUARE_BORDER_SIZE,
        SQUARE_SIZE-2*SQUARE_BORDER_SIZE))
O_IMG = pygame.image.load(
        'Images/o2.png').convert_alpha()
O_IMG = pygame.transform.scale(
    O_IMG, (
        SQUARE_SIZE-2*SQUARE_BORDER_SIZE,
        SQUARE_SIZE-2*SQUARE_BORDER_SIZE))


def main():
    global window
    board = Board(window)
    game = Game(board)
    board.update_rectangles()

    play = True
    while play:
        clock.tick(FPS)
        window.fill(BLACK)
        board.draw()
        if game.start is True:
            draw_x_and_o(window, board, X_IMG, O_IMG)
            if game.check_for_win():
                drawing_after_winning(window, game)
                game.end = True

        text_to_draw = f"Turn: {game.turn}"
        draw_text(window, FONT, text_to_draw, 0.04, WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                width, height = event.size
                # setting the minimal screen size
                if width < MIN_WIDTH:
                    width = MIN_WIDTH
                if height < MIN_HEIGHT:
                    height = MIN_HEIGHT
                window = pygame.display.set_mode(
                    (width, height), pygame.RESIZABLE)
                if game.start is False:
                    board.update()
                else:
                    print(
                        "[INFO] Changing size of the window won't change "
                        "the board after starting the game")
            if event.type == pygame.MOUSEBUTTONDOWN:
                # left click
                if event.button == 1:
                    if game.end is False:
                        rect = what_rectangle_was_clicked(board)
                        if rect is not None:
                            if game.start is False:
                                game.start = True
                                board.update_empty_board()
                            if row_col_of_rect(board, rect) is not None:
                                row, col = row_col_of_rect(board, rect)
                                if is_place_empty(board, rect):
                                    board.board[row][col] = game.turn
                                    game.change_turn()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game.end is True:
                        main()
                if event.key == pygame.K_ESCAPE:
                    if game.end is True:
                        sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main()
