import json
import pico2d

with open('field.json') as f:
    data = json.load(f)

#print(data)


# decode tile set

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
print(tileset_image_file_name, image_width, image_height, image_margin, image_spacing, num_tiles)


tile_cols = (image_width - 1) // (tile_width + 1)
tile_rows = (image_height - 1) // (tile_height + 1)

print(tile_cols, tile_rows)



def get_tile_image_rect(id):
    y = tile_rows - id // tile_cols - 1
    x = id % tile_cols
    return image_margin+x*(tile_width+image_spacing), image_margin+y*(tile_height+image_spacing), tile_width, tile_height



# decode map data



layers = data['layers']
layer = layers[0]
#print(layer['type'])
print(data['renderorder'])
h = layer['height']
w = layer['width']
tile_data = layer['data']
render_order = data['renderorder']

'''
h = 4
w = 8
tile_data = [i for i in range(h*w)]
'''

tile_map = []

if render_order == 'right-up':
    for i in range(h):
        line = tile_data[i*w:i*w+w]
        tile_map.append(line)
else:
    for i in reversed(range(h)):
        line = tile_data[i*w:i*w+w]
        tile_map.append(line)


for line in tile_map:
    print(line)



from pico2d import *
open_canvas(w * tile_width, h * tile_height)
tile_image = load_image('tmw_desert_spacing.png')
font = load_font('ENCR10B.TTF', 15)


running = True
while running:
    clear_canvas()


    '''
    #draw_rectangle(100,100,200,200)


    tile_image.draw_to_origin(0, 0)


    for x in range(tile_cols):
        for y in range(tile_rows):
            draw_rectangle(image_margin+x*(tile_width+image_spacing), image_margin+y*(tile_height+image_spacing),
                           image_margin+x*(tile_width+image_spacing)+tile_width-1,image_margin+y*(tile_height+image_spacing)+tile_height-1)


    for i in range(num_tiles):
        y = tile_rows - i // tile_cols - 1
        x = i % tile_cols
        font.draw(5+image_margin+x*(tile_width+image_spacing), 10+image_margin+y*(tile_height+image_spacing), '%d' % i)


    '''

    for y in range(h):
        for x in range(w):
            id = tile_map[y][x] - 1
            tile_image.clip_draw_to_origin(*get_tile_image_rect(id), x=x*tile_width, y=y*tile_height)


    update_canvas()
    for event in get_events():
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

close_canvas()







