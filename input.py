import pygame
from pygame.locals import *
import GLOBALS
import CONSTANTS
from utils import init_screen

class Input:
    def __init__(self):
        pass

    def handle(self):
        """ Handle pygame input events
        """
        poll = pygame.event.poll

        event = poll()
        while event:
            if event.type == QUIT:
                GLOBALS.game_running = False
                break

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    GLOBALS.game_running = False
                    break

                elif event.key == K_EQUALS:
                    GLOBALS.tile_map.map_layer.zoom += .25

                elif event.key == K_MINUS:
                    value = GLOBALS.tile_map.map_layer.zoom - .25
                    if value > 0:
                        GLOBALS.tile_map.map_layer.zoom = value

            # this will be handled if the window is resized
            elif event.type == VIDEORESIZE:
                init_screen(event.w, event.h)
                GLOBALS.tile_map.map_layer.set_size((event.w, event.h))

            event = poll()

        # using get_pressed is slightly less accurate than testing for events
        # but is much easier to use.
        pressed = pygame.key.get_pressed()
        if pressed[K_UP] or pressed[K_w]:
            GLOBALS.MOVE_UP = True
        else:
            GLOBALS.MOVE_UP = False

        if pressed[K_DOWN] or pressed[K_s]:
            GLOBALS.MOVE_DOWN = True
        else:
            GLOBALS.MOVE_DOWN = False

        if pressed[K_LEFT] or pressed[K_a]:
            GLOBALS.MOVE_LEFT = True
        else:
            GLOBALS.MOVE_LEFT = False

        if pressed[K_RIGHT] or pressed[K_d]:
            GLOBALS.MOVE_RIGHT = True
        else:
            GLOBALS.MOVE_RIGHT = False

        if pressed[K_SPACE]:
            GLOBALS.ACTION = True
        else:
            GLOBALS.ACTION = False
