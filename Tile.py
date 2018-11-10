#!/usr/bin/env python
import pygame

# possible icons:
# players: red, green, blue, yellow
# objects:
#    red, book (l,d,r) , coins (l,d,r), yellow
#    map (u,r,d), crown (u,r,d), keys (l,d,r), skull (u,l,d)
#    ring (u,r,d), chest (l,u,d), jewel (u,l,d), sword (u,l,d)
#    green, candlestick (l,u,r), helmet (l,u,r), blue

# (l,d,r) = [book, coins, keys]
# (u,r,d) = [map, crown, ring]
# (l,u,d) = [chest, jewel, sword, skull]
# (l,u,r) = [candlestick, helmet

# sliders:
#   90 degrees
#    moth 
#    beetle
#    mouse
#    spider
#    owl
#    lizard

#   T junction
#    princess warrior
#    troll
#    ghost
#    djinn
#    dragon
#    bat

#    9 blank 90 degrees
#    13 blank straight


# Define some colors
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
RED    = (255,   0,   0)
GREEN  = (  0, 255,   0)
BLUE   = (  0,   0, 255)
YELLOW = (255, 255,   0)

class MazeTile(pygame.sprite.Sprite):
    def __init__(self, name, image_path):
        super(MazeTile, self).__init__()
        self.name = name
        self.image = pygame.image.load(image_path).convert()
        self.image.set_colorkey(WHITE)  # set white as transparent
        self.rect = self.image.get_rect()

    def move_left(self):
        for i in range(self.rect.w):
            self._update_left(1)

    def _update_left(self, amt):
        self.rect.y -= amt

    def move_right(self):
        for i in range(self.rect.w):
            self._update_right(1)

    def _update_right(self, amt):
        self.rect.y += amt

    def move_up(self):
        for i in range(self.rect.h):
            self._update_up(1)

    def _update_up(self, amt):
        self.rect.x += amt

    def move_down(self):
        for i in range(self.rect.h):
            self._update_down(1)

    def _update_down(self, amt):
        self.rect.x -= amt

