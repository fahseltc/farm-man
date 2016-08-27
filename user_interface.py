import pygame
from pygame.locals import *
import CONSTANTS
import GLOBALS
from utils import load_image

class UserInterface:
    def __init__(self):
        self.elements = list()
        self.screen_size = background = pygame.display.get_surface().get_size()

        self.elements.append(ImageElement('tree32.png', (40, 50)))
        self.elements.append(PlayerTreeCountElement((1, 50)))


        self.ui_screen = pygame.Surface(GLOBALS.SCREEN_RES, pygame.SRCALPHA, 32).convert_alpha()


    def draw(self, screen):
        self.ui_screen.fill(CONSTANTS.CLEAR)
        for element in self.elements:
            element.draw(self.ui_screen)
        screen.blit(self.ui_screen, (0,0))

    def set_size(self):
         self.ui_screen = pygame.Surface(GLOBALS.SCREEN_RES, pygame.SRCALPHA, 32).convert_alpha()

class ImageElement(pygame.sprite.Sprite):
    def __init__(self, path, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(path).convert_alpha()
        self.position = position

    def draw(self, screen):
        self.rect = self.image.get_rect(centerx=GLOBALS.SCREEN_RES[0]/2 - self.position[0], centery=self.position[1])
        pygame.draw.rect(screen, CONSTANTS.BLACK, self.rect.inflate(60,10).move(20,0))
        pygame.draw.rect(screen, CONSTANTS.WHITE, self.rect.inflate(60,10).move(20,0), 1)
        #pygame.draw.rect(screen, CONSTANTS.WHITE, self.rect.inflate(3,3), 1)

        screen.blit(self.image, self.rect)


class TextElement:
    #positions need to be scaled by resolution!
    def __init__(self, text, position):
        font = pygame.font.Font(None, 36)
        self.text = font.render(text, 1, CONSTANTS.WHITE)
        pos = self.text.get_rect(centerx=position[0], centery=position[1])
        self.textpos = pos

    def draw(self, screen):
        screen.blit(self.text, self.textpos)

class VariableTextElement:
    def __init__(self, position):
        self.font = pygame.font.Font(None, 36)
        self.position = position

    def draw(self, screen):
        self.text = self.font.render("%d %d" % (GLOBALS.SCREEN_RES[0], GLOBALS.SCREEN_RES[1]), 1, CONSTANTS.WHITE)
        pos = self.text.get_rect(centerx=GLOBALS.SCREEN_RES[0]/2, centery=self.position[1])
        screen.blit(self.text, pos)


class PlayerTreeCountElement:
    def __init__(self, position):
        self.font = pygame.font.Font(None, 36)
        self.position = position

    def draw(self, screen):
        self.text = self.font.render("%d" % GLOBALS.hero.tree_count, 1, CONSTANTS.WHITE)
        pos = self.text.get_rect(centerx=GLOBALS.SCREEN_RES[0]/2, centery=self.position[1])
        screen.blit(self.text, pos)
