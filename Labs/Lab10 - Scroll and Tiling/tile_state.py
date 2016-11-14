from pico2d import *

import game_framework


from boy import ScrollBoy as Boy # import Boy class from boy.py
from background import TileBackground as Background

import tile






name = "tile_state"


background_width = 20 # in tiles
background_height = 10  # in tiles
tile_width = 32
tile_height = 32

boy = None
background = None

def create_world():
    global boy, background
    boy = Boy()
    background = Background(background_width,background_height)


def destroy_world():
    global boy, background
    del(boy)
    del(background)


def enter():
    open_canvas(background_width * tile_width, background_height * tile_height)
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                boy.handle_event(event)
                background.handle_event(event)



def update(frame_time):
    boy.update(frame_time)
    background.update(frame_time)



def draw(frame_time):
    clear_canvas()
    background.draw()
    boy.draw()
    update_canvas()






