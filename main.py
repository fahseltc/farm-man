import pygame
import GLOBALS
from farm_game import FarmGame
from utils import init_screen

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    screen = init_screen(800, 600)
    pygame.display.set_caption('Quest - An epic journey.')


    try:
        game = FarmGame()
        game.run()
    except:
        pygame.quit()
        raise