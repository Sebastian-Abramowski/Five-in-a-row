import pygame
from constants import BLACK, FPS, MIN_WIDTH, MIN_HEIGHT, WHITE
from constants import FONT, get_X_IMG, get_O_IMG
from board import Board
from other import rectangle_clicked, draw_x_and_o
from other import row_col_of_rect, is_place_empty
from game import Game
from other import draw_text, drawing_after_winning
import sys
from minimax.algorithms import minimax

pygame.init()
pygame.display.set_caption("Five-in-a-row")
window = pygame.display.set_mode((700, 700),  pygame.RESIZABLE)
clock = pygame.time.Clock()

X_IMG = get_X_IMG()
O_IMG = get_O_IMG()


def main():
    global window
    board = Board(window)
    game = Game(board)
    board.update_rectangles()

    play = True
    while play:
        clock.tick(FPS)
        window.fill(BLACK)
        game.get_board().draw()

        if game.start is True:
            draw_x_and_o(window, board, X_IMG, O_IMG)
            if game.check_for_win():
                drawing_after_winning(window, game)
                game.end = True

        if game.start is False:
            game.start = True
            game.get_board().update_empty_board()

        if game.turn == 'O':
            value, new_board = minimax(game.get_board(), 2, 'O', game)
            game.ai_move(new_board)

        text_to_draw = f"Turn: {game.turn}"
        draw_text(window, FONT, text_to_draw, 0.04, WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
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
                    game.get_board().update()
                else:
                    print(
                        "[INFO] Changing size of the window won't change "
                        "the board after starting the game")
            if event.type == pygame.MOUSEBUTTONDOWN:
                # left click
                if event.button == 1:
                    if game.end is False:
                        rect = rectangle_clicked(board)
                        if rect is not None:
                            if row_col_of_rect(board, rect) is not None:
                                row, col = row_col_of_rect(board, rect)
                                if is_place_empty(board, rect):
                                    game.get_board().board[row][col] = game.turn
                                    game.change_turn()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game.end is True:
                        main()
                if event.key == pygame.K_ESCAPE:
                    play = False
                    sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main()



#TODO: jeśli jest możliwość skończenia to niech kończy
#TODO: pierwszy ruch jak najbliżej postawionego 'X'a
#TODO: spróbuj podmieniać cały obiekt Board
#TODO: refactor nazw
#TODO: ogólny refactor
#TODO: zaktualizuj kiedy można zmieniać plansza a kiedy nie, bo się trochę pozmieniało
#TODO: dodataj uwagi w README i jakieś gify na koniec
#TODO: informacja o remisie
