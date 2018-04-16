import pygame as pg

from lib.Constants import *

class Sound(object):
    def __init__(self):
        self.sounds = {}
        self.__load_sounds()
        self.current_playing = [self.sounds['surface_melody']]
        self.current_playing[0].play(loops=9999999)
        self.current_playing[0].set_volume(0.3)

    def __load_sounds(self):
        self.sounds['surface_melody'] = pg.mixer.Sound(SURFACE_MELODY)
