import pygame as pg
import os

from pygame.locals import *
from lib.Constants import *
from lib.World import World
from lib.Player import Player
from lib.Camera import Camera
from lib.DebugTable import DebugTable
from lib.Sound import  Sound


class Main(object):
    def __init__(self):
        self.screen = pg.display.set_mode(screen)
        self.timer = pg.time.Clock()

        pg.display.set_caption('Super Mario Bros 2018')
        pg.display.set_icon(pg.image.load(r'lib\img\icon.png').convert_alpha())

        self.world = World()
        self.player = Player(hp=100, spawn_coords=(192, WINDOW_HEIGHT - 32))
        self.camera = Camera(len(self.world.level[0]) * 32, len(self.world.level) * 31)
        self.debugTable = DebugTable()
        self.sound = Sound()

        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.handle_moves()
            self.render()
            self.timer.tick(100)

    def change_debug_text(self):
        if self.debugTable.mode == 2:
            self.debugTable.text = [
                'Mario 2018 ' + VERSION + ' (S&D © 2018)',
                'FPS: ' + str(round(self.timer.get_fps())),
                'OnGr: ' + str(self.player.onground),
                'Spd: ' + str(round(self.player.x_vel, 1)) + ' ' + str(round(self.player.y_vel, 1)),
                'Plr: ' + (str(round(self.player.rect[0], 1)) + ' ' +
                           str(round(self.player.rect[1], 1)) + ' ' +
                           str(round((self.player.rect[0] + self.player.rect[2]) / 32)) + ' ' +
                           str(round((self.player.rect[1] + self.player.rect[3]) / 32))) + ' ' +
                STATE_DICT[self.player.state] + ' ' + DIRECTION_DICT[self.player.direction],
                'Cam Rect: ' + str(round(self.camera.state[0], 1)) + ' ' +
                str(round(self.camera.state[1], 1)),
                'W/ Size: ' + str(round(self.camera.state[2] / 32)) + ' ' +
                str(round(self.camera.state[3] / 32)),
                'Obj Rendering: ' + (str(len(self.world.objects) + len(self.world.bg_objects))),
                'Obj Collision: ' + (str(len(self.world.obj_to_collide)))]
        if self.debugTable.mode == 1:
            self.debugTable.text = 'FPS: ' + str(round(self.timer.get_fps()))

    def handle_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                raise SystemExit('Quit!')
            if e.type == KEYDOWN:
                if e.key == K_RIGHT:
                    self.player.right = 1
                if e.key == K_DOWN:
                    self.player.down = 1
                if e.key == K_LEFT:
                    self.player.left = 1
                if e.key == K_UP:
                    self.player.up = 1
                if e.key == K_F3:
                    if self.debugTable.mode < 2:
                        self.debugTable.mode += 1
                    else:
                        self.debugTable.mode = 0
            if e.type == KEYUP:
                if e.key == K_RIGHT:
                    self.player.right = 0
                if e.key == K_DOWN:
                    self.player.down = 0
                if e.key == K_LEFT:
                    self.player.left = 0
                if e.key == K_UP:
                    self.player.up = 0

    def handle_moves(self):
        self.player.move(self.world.obj_to_collide, self.world)
        self.player.control_image()
        self.camera.update(self.player.rect)

    def render(self):
        self.world.render(self.screen, self.camera)
        self.player.render(self.screen, self.camera)

        if self.debugTable.mode != 0:
            self.change_debug_text()
            self.debugTable.render(self.screen)
        pg.display.update()


if __name__ == '__main__':
    pg.init()
    screen = (WINDOW_WIDTH, WINDOW_HEIGHT)
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    game = Main()
    game.run()
