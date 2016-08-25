import CONSTANTS
import pygame
import os

# simple wrapper to keep the screen resizeable
def init_screen(width, height):
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    return screen

# make loading maps a little easier
def get_map(filename):
    return os.path.join(CONSTANTS.RESOURCES_DIR, filename)


# make loading images a little easier
def load_image(filename):
    return pygame.image.load(os.path.join(CONSTANTS.RESOURCES_DIR, filename))

def load_sound(filename):
    return pygame.mixer.Sound(os.path.join(CONSTANTS.RESOURCES_DIR, filename))