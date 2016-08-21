
import pygame
import CONSTANTS
import GLOBALS
from utils import load_image
class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('southStanding.png').convert_alpha()
        self.velocity = [0, 0]
        self._position = [0, 0]
        self.rect = self.image.get_rect()
        self.feet = pygame.Rect(0, 0, self.rect.width * .5, 8)

    @property
    def position(self):
        return list(self._position)

    @position.setter
    def position(self, value):
        self._position = list(value)

    def update(self, dt):
        print 'position: %s' % str(self._position)
        self.set_velocity()

        future_x = self._position[0] + self.velocity[0] * dt
        future_pos_x = (future_x, self._position[1])
        if not self.check_collision(future_pos_x):
            self._position[0] = future_x

        future_y = self._position[1] + self.velocity[1] * dt
        future_pos_y = (self._position[0], future_y)
        if not self.check_collision(future_pos_y):
            self._position[1] = future_y

        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom

        self.handle_interactions()

    def set_velocity(self):
        self.velocity[1] = 0
        if GLOBALS.MOVE_UP:
            self.velocity[1] = -CONSTANTS.HERO_MOVE_SPEED
        if GLOBALS.MOVE_DOWN:
            self.velocity[1] = +CONSTANTS.HERO_MOVE_SPEED

        self.velocity[0] = 0
        if GLOBALS.MOVE_LEFT:
            self.velocity[0] = -CONSTANTS.HERO_MOVE_SPEED
        if GLOBALS.MOVE_RIGHT:
            self.velocity[0] = +CONSTANTS.HERO_MOVE_SPEED

    def check_collision(self, future_pos):
        temp_rect = self.rect.copy()
        temp_rect.topleft = future_pos
        temp_feet = self.feet.copy()
        temp_feet.midbottom = temp_rect.midbottom
        return (temp_feet.collidelist(GLOBALS.walls) > -1)

    def handle_interactions(self):
        if GLOBALS.ACTION:
            GLOBALS.ACTION = False
            # get the tile above for now I guess?
            target_tile = (self._position[0], self._position[1] - 20)
            temp_rect = self.rect.copy()
            temp_rect.topleft = target_tile
            print 'reach rect: %s' % str(temp_rect.topleft)

            pointing_at_tree = temp_rect.collidelist(GLOBALS.trees)
            if pointing_at_tree > -1 and GLOBALS.trees[pointing_at_tree].life > 0:
                GLOBALS.trees[pointing_at_tree].change_image()
                # remove collision obj there too?
                colobj = temp_rect.collidelist(GLOBALS.walls)
                print 'Rect being deleted x: %d, y: %d' % (GLOBALS.walls[colobj].x, GLOBALS.walls[colobj].y)
                del GLOBALS.walls[colobj]