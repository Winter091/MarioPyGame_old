import pygame as pg


class DebugTable(object):
    def __init__(self):
        self.font = pg.font.SysFont('consolas', 15)
        self.dark_area = pg.Surface((300, 200)).convert_alpha()
        self.dark_area.fill((0, 0, 0, 200))
        self.text = ''
        self.rect = None
        self.x = 5
        self.x_offset = 15
        self.mode = 0

    def render(self, screen):
        self.x = 5
        if self.mode == 2:
            screen.blit(self.dark_area, (0, 0))
            for string in self.text:
                self.rect = self.font.render(string, True, (255, 255, 255))
                screen.blit(self.rect, (5, self.x))
                self.x += self.x_offset
        if self.mode == 1:
            self.rect = self.font.render(self.text, True, (255, 255, 255))
            screen.blit(self.rect, (5, self.x))
