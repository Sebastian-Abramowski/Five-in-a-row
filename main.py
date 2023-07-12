import pygame
from constants import BLACK, FPS, MIN_WIDTH, MIN_HEIGHT, WHITE
from constants import FONT, GREY2, NUM_TO_WIN, get_X_IMG, get_O_IMG
from board import Board
from button import Button
from other import rectangle_clicked, draw_x_and_o
from other import row_col_of_rect, is_place_empty
from other import draw_num_to_win_info
from game import Game
from other import draw_text, draw_after_end
import sys
from minimax import minimax
from termcolor import colored


pygame.init()
pygame.display.set_caption("Five-in-a-row")
window = pygame.display.set_mode((700, 700),  pygame.RESIZABLE)
clock = pygame.time.Clock()

X_IMG = get_X_IMG()
O_IMG = get_O_IMG()
BUTTON_SIMULATE = pygame.image.load('Images/simulate_button_2.png')


def main():
    global window

    if (NUM_TO_WIN == 3):
        window = pygame.display.set_mode((MIN_WIDTH, MIN_HEIGHT), pygame.RESIZABLE)

    if (NUM_TO_WIN == 4):
        window = pygame.display.set_mode((450, 450), pygame.RESIZABLE)
    # in other cases, the player is able to change size of the window

    board = Board(window)
    game = Game(board)
    board.update_rectangles()

    game.get_board().initialize_empty_board()

    alpha = float('-inf')
    beta = float('inf')
    if_simulation = False
    play = True

    while play:
        clock.tick(FPS)
        window.fill(BLACK)
        game.get_board().draw()
        draw_x_and_o(window, board, X_IMG, O_IMG)
        draw_num_to_win_info(window, color=GREY2)

        if game.start is False:
            button_width = BUTTON_SIMULATE.get_width()
            button_simulate = Button((window.get_width() - button_width) // 2, 13, BUTTON_SIMULATE)

            if button_simulate.draw(window) is True:
                if_simulation = True

        if game.check_for_draw():
            draw_after_end(window, True)
            game.end = True

        if game.check_for_win()[0]:
            draw_after_end(window, False, game.check_for_win()[1])
            game.end = True

        if (game.turn == 'O' and game.end is False):
            if game.if_first_ai_move:
                game.ai_move_first(game.get_board())
            else:
                _, new_board = minimax(game.get_board(), 2, True, game, alpha, beta)
                game.ai_move(new_board)
            continue
        elif (game.turn == 'X' and game.end is False):  # BOT opponent
            if (if_simulation):
                _, new_board = minimax(game.get_board(), 2, False, game, alpha, beta)
                game.ai_move(new_board)
                game.start = True

        if (game.end is False):
            text_to_draw = f"Turn: {game.turn}"
            draw_text(window, FONT, text_to_draw, 0.04, WHITE)

        old_width, old_height = window.get_size()
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

                if game.start is False and NUM_TO_WIN not in [3, 4]:
                    window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                    if (width >= 850 or height >= 850):
                        print(colored("[INFO] ", "light_magenta"), end='')
                        print("It is advised to play on smaller boards due to"
                              "the time that the bot needs to take to make a decision")
                    game.get_board().reset()
                else:
                    print(colored("[INFO] ", "light_blue"), end='')
                    if (game.end is True or NUM_TO_WIN in [3, 4]):
                        window = pygame.display.set_mode((old_width, old_height), pygame.RESIZABLE)
                        if (game.end is True):
                            print("You can change the window's size only "
                                  "before starting the game on the plain board")
                        else:
                            print("You can change the window's size when "
                                  "the number of symbols needed to win is equal to 3 or 4")

            if event.type == pygame.MOUSEBUTTONDOWN:
                # left click
                if event.button == 1:
                    if (game.end is False and if_simulation is False):
                        rect = rectangle_clicked(board)
                        if rect:
                            if row_col_of_rect(board, rect):
                                row, col = row_col_of_rect(board, rect)
                                if is_place_empty(board, rect):
                                    game.get_board().board[row][col] = game.turn
                                    game.change_turn()
                                    game.start = True
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
