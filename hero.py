import pygame
import CONSTANTS
import GLOBALS
from utils import load_image
from direction import Direction

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.velocity = [0, 0]
        self._position = [0, 0]

        self.direction = Direction.DOWN

        self.images = dict()
        self.images['NORTH'] = load_image('player/N/northStanding.png').convert_alpha()
        self.images['SOUTH'] = load_image('player/S/southStanding.png').convert_alpha()
        self.images['EAST'] = load_image('player/E/eastStanding.png').convert_alpha()
        self.images['WEST'] = load_image('player/W/westStanding.png').convert_alpha()

        self.image = self.images['SOUTH']
        self.rect = self.image.get_rect()
        self.feet = pygame.Rect(0, 0, self.rect.width * .5, 8)
        self.tree_count = 0


    @property
    def position(self):
        return list(self._position)

    @position.setter
    def position(self, value):
        self._position = list(value)

    def update(self, dt):
        print 'position: %s' % str(self._position)
        self.set_velocity()
        self.move(dt)

        self.determine_facing_direction()
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

    def move(self, dt):
        future_x = self._position[0] + self.velocity[0] * dt
        future_pos_x = (future_x, self._position[1])
        if not self.check_collision(future_pos_x):
            self._position[0] = future_x
        #GLOBALS.SOUND.play()
        future_y = self._position[1] + self.velocity[1] * dt
        future_pos_y = (self._position[0], future_y)
        if not self.check_collision(future_pos_y):
            self._position[1] = future_y
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom

    def check_collision(self, future_pos):
        temp_rect = self.rect.copy()
        temp_rect.topleft = future_pos
        temp_feet = self.feet.copy()
        temp_feet.midbottom = temp_rect.midbottom
        return (temp_feet.collidelist(GLOBALS.walls) > -1)

    def handle_interactions(self):
        print 'direction: %d, %d' % (self.direction[0], self.direction[1])
        if GLOBALS.ACTION:

            temp_rect = self.rect.copy()
            temp_rect.topleft = (self._position[0] - (20 * self.direction[0]), self._position[1] - (20 * self.direction[1]))

            print 'reach rect: %s' % str(temp_rect.topleft)

            pointing_at_tree = temp_rect.collidelist(GLOBALS.trees)
            if pointing_at_tree > -1 and not GLOBALS.trees[pointing_at_tree].dead > 0:
                GLOBALS.trees[pointing_at_tree].interact()
                if GLOBALS.trees[pointing_at_tree].dead:
                    GLOBALS.SOUND.play()
                    self.tree_count += 1
                    colobj = temp_rect.collidelist(GLOBALS.walls)
                    print 'Rect being deleted x: %d, y: %d' % (GLOBALS.walls[colobj].x, GLOBALS.walls[colobj].y)
                    del GLOBALS.walls[colobj]

    def determine_facing_direction(self):
        if self.velocity[0] > 0:
            self.image = self.images['EAST']
            self.direction = Direction.LEFT
            print 'facing: EAST'
        elif self.velocity[0] < 0:
            self.image = self.images['WEST']
            self.direction = Direction.RIGHT
            print 'facing: WEST'

        if self.velocity[1] > 0:
            self.image = self.images['SOUTH']
            self.direction = Direction.UP
            print 'facing: SOUTH'
        elif self.velocity[1] < 0:
            self.image = self.images['NORTH']
            self.direction = Direction.DOWN
            print 'facing: NORTH'

