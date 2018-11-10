import json


static_icons = ['red', 'book', 'coins', 'yellow', 
                'map', 'crown', 'keys', 'skull', 
                'ring', 'chest', 'jewel', 'sword', 
                'green', 'candlestick', 'helmet', 'blue']
slider_icons = ['moth', 'beetle', 'mouse', 'spider', 'owl', 'lizard', 'princess', 'troll', 'ghost', 'djinn', 'dragon', 'bat']

tiles_dict = {'red': {'image': 'red_start.png', 'type': 'static'},
              'book': {'image': 'book.png', 'type': 'static'}, 
              'coins': {'image': 'coins.png', 'type': 'static'},  
              'yellow': {'image': 'yellow_start.png', 'type': 'static'}, 
              'map': {'image': 'map.png', 'type': 'static'}, 
              'crown': {'image': 'crown.png', 'type': 'static'}, 
              'keys': {'image': 'keys.png', 'type': 'static'}, 
              'skull': {'image': 'skull.png', 'type': 'static'}, 
              'ring': {'image': 'ring.png', 'type': 'static'}, 
              'chest': {'image': 'chest.png', 'type': 'static'}, 
              'jewel': {'image': 'jewel.png', 'type': 'static'}, 
              'sword': {'image': 'sword.png', 'type': 'static'}, 
              'green': {'image': 'green_start.png', 'type': 'static'}, 
              'candlestick': {'image': 'candlestick.png', 'type': 'static'}, 
              'helmet': {'image': 'helmet.png', 'type': 'static'}, 
              'blue': {'image': 'blue_start.png', 'type': 'static'},
              'moth': {'image': 'moth.png', 'type': 'slider'}, 
              'beetle': {'image': 'beetle.png', 'type': 'slider'}, 
              'mouse': {'image': 'mouse.png', 'type': 'slider'}, 
              'spider': {'image': 'spider.png', 'type': 'slider'}, 
              'owl': {'image': 'owl.png', 'type': 'slider'}, 
              'lizard': {'image': 'lizard.png', 'type': 'slider'}, 
              'princess': {'image': 'princess.png', 'type': 'slider'}, 
              'troll': {'image': 'troll.png', 'type': 'slider'}, 
              'ghost': {'image': 'ghost.png', 'type': 'slider'}, 
              'djinn': {'image': 'djinn.png', 'type': 'slider'}, 
              'dragon': {'image': 'dragon.png', 'type': 'slider'}, 
              'bat': {'image': 'bat.png', 'type': 'slider'}
             }

if __name__ == '__main__':
    with open('tiles.json', 'w') as fp:
        json.dump(tiles_dict, fp, indent=2, sort_keys=True)
