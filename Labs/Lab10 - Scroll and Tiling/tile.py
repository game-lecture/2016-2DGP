__author__ = 'dustinlee'

import json

from pico2d import *

class TileMap:


    def get_tile_image_rect(self, id):
        y = self.tile_rows - id // self.tile_cols - 1
        x = id % self.tile_cols
        return self.image_margin+x*(self.tile_width+self.image_spacing), \
               self.image_margin+y*(self.tile_height+self.image_spacing), \
               self.tile_width, self.tile_height

    def draw_to_origin(self, left, bottom, w=None, h=None):
        if w == None and h == None:
            w,h = self.map_width, self.map_height

        for y in range(h):
            for x in range(w):
                id = self.map2d[y][x]
                self.tileset_image.clip_draw_to_origin(*self.get_tile_image_rect(id), x=(x+left)*self.tile_width, y=(y+bottom)*self.tile_height)



    def clip_draw_to_origin(self, left, bottom, width, height, target_left, target_bottom, w=None, h=None):
        if w == None and h == None:
            w,h = width, height

        for y in range(h):
            for x in range(w):
                id = self.map2d[bottom+y][left+x]
                self.tileset_image.clip_draw_to_origin(*self.get_tile_image_rect(id), x=(x+target_left)*self.tile_width, y=(y+target_bottom)*self.tile_height)


def load_tile_map(name):
    with open(name) as f:
        data = json.load(f)

    tile_map = TileMap()

    base_tile_width = data['tilewidth']
    base_tile_height = data['tileheight']

    tileset = data['tilesets'][0]
    tileset_image_file_name = tileset['image']
    image_height = tileset['imageheight']
    image_width = tileset['imagewidth']
    image_margin = tileset['margin']
    image_spacing = tileset['spacing']
    tile_height = tileset['tileheight']
    tile_width = tileset['tilewidth']
    first_gid = tileset['firstgid']
    num_tiles = len(tileset['tiles'])

    tile_cols = (image_width - 1) // (tile_width + 1)
    tile_rows = (image_height - 1) // (tile_height + 1)

    layers = data['layers']
    layer = layers[0]
    #print(layer['type'])
    #print(data['renderorder'])
    map_height = layer['height']
    map_width = layer['width']
    tile_data = layer['data']
    render_order = data['renderorder']

    '''
    h = 4
    w = 8
    tile_data = [i for i in range(h*w)]
    '''

    map2d = []

    if render_order == 'right-up':
        for i in range(map_height):
            line = [x - first_gid for x in tile_data[i*map_width:i*map_width+map_width]]
            map2d.append(line)
    else:
        for i in reversed(range(map_height)):
            line = [x - first_gid for x in tile_data[i*map_width:i*map_width+map_width]]
            map2d.append(line)

    tile_map.tileset_image = load_image(tileset_image_file_name)
    tile_map.map2d = map2d
    tile_map.image_margin = image_margin
    tile_map.image_spacing = image_spacing
    tile_map.map_width = map_width
    tile_map.map_height = map_height
    tile_map.tile_width = tile_width
    tile_map.tile_height = tile_height
    tile_map.tile_rows = tile_rows
    tile_map.tile_cols = tile_cols
    return tile_map