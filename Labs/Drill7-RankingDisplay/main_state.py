import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

boy = None
grass = None
font = None



class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None

    LEFT_RUN, RIGHT_RUN = 0, 1

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = random.randint(0, 7)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 1
        self.state = self.RIGHT_RUN
        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')


    def update(self, frame_time):
        self.life_time += frame_time
        distance = Boy.RUN_SPEED_PPS * frame_time
        self.total_frames += Boy.FRAMES_PER_ACTION * Boy.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8
        self.x += (self.dir * distance)

        if self.x > 800:
            self.dir = -1
            self.x = 800
            self.state = self.LEFT_RUN
            print("Change Time: %f, Total Frames: %d" % (self.life_time, self.total_frames))
        elif self.x < 0:
            self.dir = 1
            self.x = 0
            self.state = self.RIGHT_RUN
            print("Change Time: %f, Total Frames: %d" % (self.life_time, self.total_frames))


    def draw(self):
        self.image.opacify(random.random())
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)
        font.draw(self.x - 50, self.y + 40, 'Time: %3.2f' % self.life_time)



def enter():
    global boy, grass, font
    boy = Boy()
    grass = Grass()
    font = load_font('ENCR10B.TTF')
    game_framework.reset_time()


def exit():
    global boy, grass, font

    del(boy)
    del(grass)
    del(font)


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
                game_framework.change_state(title_state)


def update(frame_time):
    global boy
    boy.update(frame_time)


def draw(frame_time):
    global boy, grass

    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()





