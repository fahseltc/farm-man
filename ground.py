import pygame
from utils import load_image

# ground can be in some set of states
# can also have something on it, like a plant or a item

# we want ground to be grass / dirt / tilled?

class Ground(pygame.sprite.Sprite):
    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        self.rect = rect
        self.tilled = False

        self.images = dict()
        self.images['DIRT'] = load_image('eww_dirt.png').convert_alpha()
        self.images['GRASS'] = load_image('grass.png').convert_alpha()
        self.image = self.images['DIRT']

    def interact(self):
        self.tilled = True
        print ' AM I INTERACTING YET'
        self.change_image()

    def change_image(self):
        self.images['GRASS'] = load_image('grass.png').convert_alpha()
