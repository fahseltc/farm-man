
import pygame
from pygame.locals import *
import CONSTANTS
from utils import *
from pytmx.util_pygame import load_pygame
import pyscroll
import pyscroll.data
from pyscroll.group import PyscrollGroup
from hero import Hero
import GLOBALS
from tile_map import TileMap
from input import Input

class FarmGame(object):

    def __init__(self):
        self.screen = pygame.display.get_surface()

        GLOBALS.game_running = False
        GLOBALS.tile_map = TileMap()

        GLOBALS.tile_map.map_layer.zoom = 2

        # pyscroll supports layered rendering.  our map has 3 'under' layers
        # layers begin with 0, so the layers are 0, 1, and 2.
        # since we want the sprite to be on top of layer 1, we set the default
        # layer for sprites as 2
        self.group = PyscrollGroup(map_layer=GLOBALS.tile_map.map_layer, default_layer=2)

        GLOBALS.hero = Hero()
        GLOBALS.hero.position = GLOBALS.tile_map.map_layer.map_rect.center

        self.group.add(GLOBALS.hero)
        for tree in GLOBALS.trees:
            self.group.add(tree)

        self.input = Input()

    def run(self):
        clock = pygame.time.Clock()
        GLOBALS.game_running = True

        try:
            while GLOBALS.game_running:
                dt = clock.tick(60)/1000. # limit to 60fps, but also damn milliseconds, you fast

                self.input.handle()
                self.update(dt)
                self.draw(self.screen)
                pygame.display.flip()

        except KeyboardInterrupt:
            GLOBALS.game_running = False

    def update(self, dt):
        self.group.update(dt)

        # check if the sprite's feet are colliding with wall
        # sprite must have a rect called feet, and move_back method,
        # otherwise this will fail
        # for sprite in self.group.sprites():
        #     if sprite.feet.collidelist(GLOBALS.walls) > -1:
        #         sprite.move_back(dt)

    def draw(self, surface):
        # center the map/screen on our Hero
        self.group.center(GLOBALS.hero.rect.center)

        # draw the map and all sprites
        self.group.draw(surface)
