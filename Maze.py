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
        all_tiles.append(Tile.MazeTile(name=t, image_path=td[t]['image']))
    for i in range(9):
        all_tiles.append(Tile.MazeTile(name='blank_ninety_{}'.format(i), image_path='blank_ninety.png')
    for i in range(13):
        all_tiles.append(Tile.MazeTile(name='blank_tee_{}'.format(i), image_path='blank_tee.png')
    return all_tiles


def gen_players(player_dict):
    import Player
    all_players = []
    for p in player_dict:
        # all_players.append(Player.MazePlayer(color=p))
        all_players.append(Tile.MazeTile(name=p, image_path=player_dict[p]['image']


if __name__ == '__main__':
    screen = pygame.display.set_mode((800, 600))

    tile_list = pygame.sprite.Group()
    sprite_list = pygame.sprite.Group()
    tile_dict = get_tiles()
    for t in gen_tiles(tile_dict):
        tile_list.add(t)
        sprite_list.add(t)
    for p in gen_players(PLAYERS_DICT):
        sprite_list.add(p)

    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        clock.tick(60)
        sprite_list.draw(screen)
        pygame.display.flip()
    pygame.quit()

