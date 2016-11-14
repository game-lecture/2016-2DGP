import random

from pico2d import *
from tile import load_tile_map


class Background:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 20.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self, w, h):
        self.image = load_image('background.png') # 960x272
        self.speed = 0
        self.left = 0
        self.screen_width = w
        self.screen_height = h

    def draw(self):
        pass

    def update(self, frame_time):
        pass

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT: self.speed -= Background.SCROLL_SPEED_PPS
            elif event.key == SDLK_RIGHT: self.speed += Background.SCROLL_SPEED_PPS
        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT: self.speed += Background.SCROLL_SPEED_PPS
            elif event.key == SDLK_RIGHT: self.speed -= Background.SCROLL_SPEED_PPS


class TileBackground:

    SCROLL_SPEED_PPS = 1

    def __init__(self, width, height):
        self.tile_map = load_tile_map('field.json')
        self.speed = 0
        self.left = 0
        self.width = width
        self.height = height

    def draw(self):
        pass

    def update(self, frame_time):
        pass

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT: self.speed -= TileBackground.SCROLL_SPEED_PPS
            elif event.key == SDLK_RIGHT: self.speed += TileBackground.SCROLL_SPEED_PPS
        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT: self.speed += TileBackground.SCROLL_SPEED_PPS
            elif event.key == SDLK_RIGHT: self.speed -= TileBackground.SCROLL_SPEED_PPS




