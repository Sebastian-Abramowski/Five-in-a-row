from pygame import font, image, transform

FPS = 60

# Colours
BLACK = (0, 0, 0)
GREY = (43, 43, 59)
WHITE = (255, 255, 255)
BLUE1 = (102, 153, 255)
BLUE2 = (51, 153, 255)
RED = (200, 0, 0)
WEIRD_GREEN = (65, 250, 159)
YELLOW = (245, 203, 66)

# Window
MIN_WIDTH = 350
MIN_HEIGHT = 350
PADDING = 50
SQUARE_SIZE = 75
SQUARE_BORDER_SIZE = 8

# Font
font.init()
BIG_FONT_SIZE = 100
FONT = font.SysFont('calibri', 18, True)
SMALL_FONT = font.SysFont('calibri', 12, True)
FONT_BIG_TEXT = font.SysFont('calibri', BIG_FONT_SIZE, True)

# Game
NUM_TO_WIN = 3  # num of symbols to win the game

"""is it done that way since you can't use
   convert alpha without pygame.display initialized)"""


# Images
def get_X_IMG():
    X_IMG = image.load(
            'Images/x2.png').convert_alpha()
    X_IMG = transform.scale(
        X_IMG, (
            SQUARE_SIZE-2*SQUARE_BORDER_SIZE,
            SQUARE_SIZE-2*SQUARE_BORDER_SIZE))
    return X_IMG


def get_O_IMG():
    O_IMG = image.load(
            'Images/o2.png').convert_alpha()
    O_IMG = transform.scale(
        O_IMG, (
            SQUARE_SIZE-2*SQUARE_BORDER_SIZE,
            SQUARE_SIZE-2*SQUARE_BORDER_SIZE))
    return O_IMG
