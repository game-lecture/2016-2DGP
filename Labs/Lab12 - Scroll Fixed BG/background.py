import random

from pico2d import *


class FixedBackground:

    def __init__(self):
        self.image = load_image('KPU_GROUND.png')
        self.speed = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def set_center_object(self, boy):
        # fill here
        pass


    def draw(self):
        # fill here
        pass


    def update(self, frame_time):
        # fill here
        pass


    def handle_event(self, event):
        pass



