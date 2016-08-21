import pygame
from utils import load_image

class Tree(pygame.sprite.Sprite):
    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        self.rect = rect
        self.image = load_image('tree32.png').convert_alpha()
        self.life = 10

        pass

    def interact(self):
        if self.life >= 0:
            self.life -= 1
            print 'tree life lowered' # LOL NOT RUBY
        else:
            pass

    def change_image(self):
        self.image = load_image('empty.png').convert_alpha()
