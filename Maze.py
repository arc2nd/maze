#!/usr/bin/env python

import os
import json
import types
import random

import pygame

import Tile
import Board

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

class Maze(object):
    def __init__(self):
        return

    def get_tiles(self):
        if os.path.exists('tiles.json'):
            with open('tiles.json', 'r') as fp:
                tiles_dict = json.load(fp)
        return tiles_dict


    def gen_tiles(self, tile_dict):
        all_tiles = []
        for t in tile_dict:
            local = tile_dict[t]
            this_tile = Tile.MazeTile(name=t, image_path=local['image'], t_type=local['type'])
            if local['type'] == 'static':
                this_tile.square = [local['square'][0], local['square'][1]]
            all_tiles.append(this_tile)
        for i in range(9): # actually 9, for the spare
            all_tiles.append(Tile.MazeTile(name='blank_ninety_{}'.format(i), image_path='images/blank_ninety.png'))
        for i in range(13):
            all_tiles.append(Tile.MazeTile(name='blank_straight_{}'.format(i), image_path='images/blank_straight.png'))
        return all_tiles


    # def gen_players(self, player_dict):
    #    import Player
    #    all_players = []
    #    for p in player_dict:
    #        # all_players.append(Player.MazePlayer(color=p))
    #        all_players.append(Tile.MazeTile(name=p, image_path=player_dict[p]['image']


    def place_statics(self, board, tile_list, tileW):
        for t in tile_list:
            if t.type == 'static':
                t.rect.x = t.square[0] * tileW
                t.rect.y = t.square[1] * tileW
                board.array[t.square[0] + (t.square[1]*7)] = t

    def place_dyns(self, board, tile_list, tileW):
        i = 0
        for t in tile_list:
            if t.type != 'static':
                spotX, spotY = board.find_free()
                # print('I: {} X: {} Y: {}'.format(i, spotX, spotY))
                if spotX:
                    t.rect.x = spotX * tileW
                if spotY:
                    t.rect.y = spotY * tileW
                if spotX >= 0 and spotY >= 0:
                    # print(spotX + (spotY*7))
                    board.array[spotX + (spotY*7)] = t
                if isinstance(spotX, types.NoneType) or isinstance(spotY, types.NoneType):
                    t.rect.x = 8 * tileW
                    t.rect.y = 2 * tileW
                    board.array[-1] = t
            i+=1


    def scale_all(self, tile_list, factorX, factorY):
        for t in tile_list:
            t.scale(factorX, factorY)

    def rotate_spare(self, board, direction):
        if 'left' in direction:
            board.array[-1].rotate(90)
        if 'right' in direction:
            board.array[-1].rotate(-90)

    def update(self, tile_list, sprite_list, screen):
        tile_list.draw(screen)
        sprite_list.draw(screen)
        pygame.display.flip()


    def setup(self, screenX, screenY):
        screen = pygame.display.set_mode((screenX, screenY))
        tile_list = pygame.sprite.Group()
        sprite_list = pygame.sprite.Group()
        tile_dict = self.get_tiles()
        for t in self.gen_tiles(tile_dict):
            tile_list.add(t)
            #sprite_list.add(t)
        # for p in gen_players(PLAYERS_DICT):
        #     sprite_list.add(p)
        return tile_list, sprite_list, screen

    def quit(self):
        pygame.quit()

    def main(self, screenW=700):
        #screenW = 700
        orig_tileW = 195

        # figure out scales based on screen width
        scale = float(screenW / 7) / float(orig_tileW)
        tileW = float(orig_tileW) * scale

        # build board and screen and lists of things we can affect
        board = Board.MazeBoard(lenX=7, lenY=7)
        tile_list, sprite_list, screen = self.setup(screenW + int(2*tileW), screenW + int(1*tileW))
        self.scale_all(tile_list, scale, scale)

        # place tiles
        self.place_statics(board, tile_list, tileW)
        self.place_dyns(board, tile_list, tileW)
        # self.update(sprite_list, screen)
        clock = pygame.time.Clock()

        # game loop
        done = False
        while not done:
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.rotate_spare(board, 'left')
                    if event.key == pygame.K_RIGHT:
                        self.rotate_spare(board, 'right')
            clock.tick(60)
            self.update(tile_list, sprite_list, screen)
        pygame.quit()

if __name__ == '__main__':
    myMaze = Maze()
    myMaze.main(500)
