import json


static_icons = ['red', 'book', 'coins', 'yellow', 
                'map', 'crown', 'keys', 'skull', 
                'ring', 'chest', 'jewel', 'sword', 
                'green', 'candlestick', 'helmet', 'blue']
slider_icons = ['moth', 'beetle', 'mouse', 'spider', 'owl', 'lizard', 'princess', 'troll', 'ghost', 'djinn', 'dragon', 'bat']

tiles_dict = {'red': {'image': 'images/red_start.png', 'type': 'static', 'square': [0,0]},
              'book': {'image': 'images/book.png', 'type': 'static', 'square': [2,0]}, 
              'coins': {'image': 'images/coins.png', 'type': 'static', 'square': [4,0]},  
              'yellow': {'image': 'images/yellow_start.png', 'type': 'static', 'square': [6,0]}, 
              'map': {'image': 'images/map.png', 'type': 'static', 'square': [0,2]}, 
              'crown': {'image': 'images/crown.png', 'type': 'static', 'square': [2,2]}, 
              'keys': {'image': 'images/keys.png', 'type': 'static', 'square': [4,2]}, 
              'skull': {'image': 'images/skull.png', 'type': 'static', 'square': [6,2]}, 
              'ring': {'image': 'images/ring.png', 'type': 'static', 'square': [0,4]}, 
              'chest': {'image': 'images/chest.png', 'type': 'static', 'square': [2,4]}, 
              'jewel': {'image': 'images/jewel.png', 'type': 'static', 'square': [4,4]}, 
              'sword': {'image': 'images/sword.png', 'type': 'static', 'square': [6,4]}, 
              'green': {'image': 'images/green_start.png', 'type': 'static', 'square': [0,6]}, 
              'candlestick': {'image': 'images/candlestick.png', 'type': 'static', 'square': [2,6]}, 
              'helmet': {'image': 'images/helmet.png', 'type': 'static', 'square': [4,6]}, 
              'blue': {'image': 'images/blue_start.png', 'type': 'static', 'square': [6,6]},
              'moth': {'image': 'images/moth.png', 'type': 'slider'}, 
              'beetle': {'image': 'images/beetle.png', 'type': 'slider'}, 
              'mouse': {'image': 'images/mouse.png', 'type': 'slider'}, 
              'spider': {'image': 'images/spider.png', 'type': 'slider'}, 
              'owl': {'image': 'images/owl.png', 'type': 'slider'}, 
              'lizard': {'image': 'images/lizard.png', 'type': 'slider'}, 
              'princess': {'image': 'images/princess.png', 'type': 'slider'}, 
              'troll': {'image': 'images/troll.png', 'type': 'slider'}, 
              'ghost': {'image': 'images/ghost.png', 'type': 'slider'}, 
              'djinn': {'image': 'images/djinn.png', 'type': 'slider'}, 
              'dragon': {'image': 'images/dragon.png', 'type': 'slider'}, 
              'bat': {'image': 'images/bat.png', 'type': 'slider'},
              'blank_ninety': {'image': 'images/blank_ninety.png', 'type': 'slider'}, 
              'blank_straight': {'image': 'images/blank_straight.png', 'type': 'slider'}
             }

if __name__ == '__main__':
    with open('tiles.json', 'w') as fp:
        json.dump(tiles_dict, fp, indent=2, sort_keys=True)
