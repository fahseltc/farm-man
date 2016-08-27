import pygame
from pygame.locals import *
import CONSTANTS
from utils import *
from pytmx.util_pygame import load_pygame
import pyscroll
import pyscroll.data
import GLOBALS
from tree import Tree
from ground import Ground


class TileMap:
    filename = get_map(CONSTANTS.MAP_FILENAME)

    def __init__(self):
        tmx_data = load_pygame(self.filename)

        self.make_walls(tmx_data.get_layer_by_name('collision'))
        self.make_trees(tmx_data.get_layer_by_name('tree'))
        self.make_ground(tmx_data.get_layer_by_name('ground'))

        map_data = pyscroll.data.TiledMapData(tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, pygame.display.get_surface().get_size())

    def make_walls(self, layer):
        GLOBALS.walls = list()
        for object in layer:
            GLOBALS.walls.append(pygame.Rect(
                object.x, object.y,
                object.width, object.height))

    def make_trees(self, layer):
        # each tree in the tree object layer needs to make a wall above (and some tree object?)
        GLOBALS.trees = list()
        for object in layer:
            rect = pygame.Rect(
                object.x, object.y,
                object.width, object.height)

            GLOBALS.walls.append(rect) # needs to be moved elsewhere probably
            GLOBALS.trees.append(Tree(rect))

    def make_ground(self, layer):
        GLOBALS.ground = list()
        for object in layer:
            rect = pygame.Rect(
                object.x, object.y,
                object.width, object.height)

            GLOBALS.ground.append(Ground(rect))
