import pygame
import GLOBALS
from sound_manager import SoundManager
from farm_game import FarmGame
from utils import init_screen

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    GLOBALS.SCREEN_RES = (800, 600)
    screen = init_screen(GLOBALS.SCREEN_RES[0], GLOBALS.SCREEN_RES[1])
    pygame.display.set_caption('Trees and Boxes')

    GLOBALS.SOUND = SoundManager()

    try:
        game = FarmGame()
        game.run()
    except:
        pygame.quit()
        raise