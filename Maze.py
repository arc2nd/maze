#!/usr/bin/env python

import os
import json

import pygame

import Tile

"""
https://qq.readthedocs.io/en/latest/main_loop.html
https://www.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/
http://programarcadegames.com/index.php?chapter=introduction_to_sprites
"""

#PLAYERS_DICT = {'red', 'green', 'yellow', 'blue'}
PLAYERS_DICT = {'red': {'image': 'red.png'}, 
                'green': {'image': 'green.png'}, 
                'yellow': {'image': 'yellow.png'}, 
                'blue': {'image': 'blue.png'}
               }

def get_tiles():
    if os.path.exists('tiles.json'):
        with open('tiles.json', 'r') as fp:
            tiles_dict = json.load(fp)
    return tiles_dict


def gen_tiles(tile_dict):
    all_tiles = []
    for t in tile_dict:
        local = tile_dict[t]
        this_tile = Tile.MazeTile(name=t, image_path=local['image'], t_type=local['type'])
        if local['type'] == 'static':
            this_tile.square = [local['square'][0], local['square'][1]]
        all_tiles.append(this_tile)
    for i in range(9):
        all_tiles.append(Tile.MazeTile(name='blank_ninety_{}'.format(i), image_path='images/blank_ninety.png'))
    for i in range(13):
        all_tiles.append(Tile.MazeTile(name='blank_straight_{}'.format(i), image_path='images/blank_straight.png'))
    return all_tiles


# def gen_players(player_dict):
#    import Player
#    all_players = []
#    for p in player_dict:
#        # all_players.append(Player.MazePlayer(color=p))
#        all_players.append(Tile.MazeTile(name=p, image_path=player_dict[p]['image']


def place_statics(tile_list, tileW):
    for t in tile_list:
        if t.type == 'static':
            t.rect.x = t.square[0] * tileW
            t.rect.y = t.square[1] * tileW
        else:
            t.rect.x = 10 * tileW
            t.rect.y = 10 * tileW


def scale_all(tile_list, factorX, factorY):
    for t in tile_list:
        t.scale(factorX, factorY)


def update(sprite_list, screen):
    sprite_list.draw(screen)
    pygame.display.flip()


def setup(screenX, screenY):
    screen = pygame.display.set_mode((screenX, screenY))
    tile_list = pygame.sprite.Group()
    sprite_list = pygame.sprite.Group()
    tile_dict = get_tiles()
    for t in gen_tiles(tile_dict):
        tile_list.add(t)
        sprite_list.add(t)
    # for p in gen_players(PLAYERS_DICT):
    #     sprite_list.add(p)
    return tile_list, sprite_list, screen

def quit():
    pygame.quit()

def test(screenW=700):
    #screenW = 700
    orig_tileW = 195
    tile_list, sprite_list, screen = setup(screenW, screenW)
    scale = float(screenW / 7) / float(orig_tileW)
    tileW = float(orig_tileW) * scale
    scale_all(tile_list, scale, scale)
    place_statics(tile_list, tileW)
    update(sprite_list, screen)
#    clock = pygame.time.Clock()


#    done = False
#    while not done:
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                done = True
#        clock.tick(60)
#        update(sprite_list, screen)
#    pygame.quit()

