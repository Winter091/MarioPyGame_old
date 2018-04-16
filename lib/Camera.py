import pygame as pg
from lib.Constants import *


class Camera(object):
    def __init__(self, width, height):
        self.state = pg.Rect(0, 0, width, height)
        self.complex_camera(self.state)

    def complex_camera(self, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = self.state
        l, t, _, _ = -l + HALF_WIDTH, -t + HALF_HEIGHT, w, h  # center player

        l = min(0, l)  # stop scrolling at the left edge
        l = max(-(self.state[2] - WINDOW_WIDTH), l)  # stop scrolling at the right edge
        t = max(-(self.state[3] - WINDOW_HEIGHT), t)  # stop scrolling at the bottom
        t = min(0, t)  # stop scrolling at the top
        return pg.Rect(l, t - 48, w, h) # - 48 для того, чтобы было видно 2 блока снизу экрана

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.complex_camera(target)
