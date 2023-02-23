import pygame
import sys
from constants import BLACK, FPS, MIN_WIDTH, MIN_HEIGHT
from board import Board

pygame.init()
pygame.display.set_caption("Five-in-a-row")
window = pygame.display.set_mode((2000, 1000),  pygame.RESIZABLE)
clock = pygame.time.Clock()


def main():
    global window
    board = Board(window)
    board.update_rectangles()
    print(str(board))

    play = True
    while play:
        clock.tick(FPS)
        window.fill(BLACK)
        board.draw()

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
                board.update()
        pygame.display.update()


if __name__ == "__main__":
    main()
