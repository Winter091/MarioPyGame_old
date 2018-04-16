import pygame as pg
from lib.Constants import *
from lib.Entity import *


class World(object):
    def __init__(self):
        self.objects = []
        self.bg_objects = []
        self.obj_to_collide = []

        self.level = []

        self.textures = {}
        self.__load_textures()

        self.__generate_world_1()

    def __generate_world_1(self):
        """
        Осязаемые объекты:
            P (platform) - Обычная платформа
            B (brick) - Кирпичная платформа
            Q (question) - Платформа-вопрос
            L (ladder) - Платформа-ступенька
            T (tube) - Труба
            F - Флаг в конце уровня
        BackGround:
            M/m (mountain) - Большая/Маленькая гора
            S/s (shrub) - Большой/Маленький куст
            C/c (cloud) - Большое/Маленькое облако
        """
        self.level = [
            'P                                                                                                            c                         C                                                                                   ',
            'P                                                                                               C                               c             C                                                                            ',
            'P                                                    C                                                              C                                       C                                          C                   ',
            'P                                                                                 C                    C                                   c                                          C                                    ',
            'P       C                             C                                                                                        C                      c                      c               c                 c           ',
            'P                  C                                               c          c                    c                                                                                                                   C   ',
            'P                                                    c                                   C                                           c                            C                    C                c                  ',
            'P                       c               c                                                                         c                                                      c                                      C          ',
            'P        c                                                    C                                                                                                                                                            ',
            'P                                                                                                                                                                                                                          ',
            'P                                                                                                                                                                                                                          ',
            'P                                                                                       BBBBBBBB   BBBQ              Q           BBB    BQQB                                                                               ',
            'P                           Q                                                                                                                                                                               F              ',
            'P                                                                                                                                                                                                   LL                     ',
            'P                                                                                                                                                                                                  LLL                     ',
            'P                                                                                                                                                                                                 LLLL                     ',
            'P                     Q   BQBQB                        T         T                   BQB              B     BB    Q  Q  Q     B          BB                                     BBQB             LLLLL                     ',
            'P                                                                                                                                                 L  L          LL  L                           LLLLLL                     ',
            'P                                             T                                                                                                  LL  LL        LLL  LL                         LLLLLLL                     ',
            'P   M                                T                   M                                              M                                       LLL  LLL M    LLLL  LLL    T               T  LLLLLLLL  M                  ',
            'P                 S   m       s                   S                 S   m      s                 S                  S   m      s               LLLLS LLLL    LLLLL  LLLL m      s            LLLLLLLLL       L             ',
            'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP  PPPPPPPPPPPPPPPP   PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP  PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP',
            'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP  PPPPPPPPPPPPPPPP   PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP  PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP']

        """
        Для того, чтобы внести блоки, по которым передвигается игрок, в list,
        который будет использоваться для проверки коллизий. Блоки ниже
        в коллизиях учитываться не будут, и это немного ускоряет игру.
        """
        pl_to_collide = True
        row_counter = 0

        y = 0
        for row in self.level:
            row_counter += 1
            x = 0
            y += 32

            # Платформы, по которым никогда не наступит игрок, в коллизии участвовать не будут
            if len(self.level) - row_counter + 1 < WORLD_GROUND_HEIGHT:
                pl_to_collide = False

            for symbol in row:
                if symbol == 'P':
                    B = Platform(x, y, self.textures['ground'])
                    self.objects.append(B)
                    if pl_to_collide:
                        self.obj_to_collide.append(B)
                elif symbol == 'B':
                    B = BrickPlatform(x, y, self.textures['brick'])
                    self.objects.append(B)
                    self.obj_to_collide.append(B)
                elif symbol == 'Q':
                    B = QuestionPlatform(x, y, (
                        self.textures['question1'], self.textures['question2'], self.textures['question3'], self.textures['question_activated']))
                    self.objects.append(B)
                    self.obj_to_collide.append(B)
                elif symbol == 'L':
                    B = Platform(x, y, self.textures['stair'])
                    self.objects.append(B)
                    self.obj_to_collide.append(B)
                elif symbol == 'T':
                    B = Tube(x, y, self.textures['tube'],
                             (len(self.level) * 32) - ((len(self.level) * 32) - ((len(self.level) * 32) - y) + 32))
                    self.objects.append(B)
                    self.obj_to_collide.append(B)
                elif symbol == 'F':
                    B = Flag(x, y, self.textures['flag'],
                             (len(self.level) * 32) - ((len(self.level) * 32) - ((len(self.level) * 32) - y) + 64))
                    self.objects.append(B)
                elif symbol == 'c':
                    B = BGObject(x, y, CLOUD1_SIZE, self.textures['cloud1'])
                    self.bg_objects.append(B)
                elif symbol == 'C':
                    B = BGObject(x, y, CLOUD2_SIZE, self.textures['cloud2'])
                    self.bg_objects.append(B)
                elif symbol == 'm':
                    B = BGObject(x, y, MOUNTAIN1_SIZE, self.textures['mountain1'])
                    self.bg_objects.append(B)
                elif symbol == 'M':
                    B = BGObject(x, y, MOUNTAIN2_SIZE, self.textures['mountain2'])
                    self.bg_objects.append(B)
                elif symbol == 's':
                    B = BGObject(x, y, SHRUB1_SIZE, self.textures['shrub1'])
                    self.bg_objects.append(B)
                elif symbol == 'S':
                    B = BGObject(x, y, SHRUB2_SIZE, self.textures['shrub2'])
                    self.bg_objects.append(B)

                x += 32

        del pl_to_collide, row_counter, B

    def __load_textures(self):
        self.textures['ground'] = pg.image.load(GROUND_TEXTURE).convert()
        self.textures['sky'] = pg.image.load(SKY_TEXTURE).convert()
        self.textures['brick'] = pg.image.load(BRICK_TEXTURE).convert()
        self.textures['cloud1'] = pg.image.load(CLOUD1_TEXTURE).convert_alpha()
        self.textures['cloud2'] = pg.image.load(CLOUD2_TEXTURE).convert_alpha()
        self.textures['mountain1'] = pg.image.load(MOUNTAIN1_TEXTURE).convert_alpha()
        self.textures['mountain2'] = pg.image.load(MOUNTAIN2_TEXTURE).convert_alpha()
        self.textures['shrub1'] = pg.image.load(SHRUB1_TEXTURE).convert_alpha()
        self.textures['shrub2'] = pg.image.load(SHRUB2_TEXTURE).convert_alpha()
        self.textures['question1'] = pg.image.load(QUESTION1_TEXTURE).convert()
        self.textures['question2'] = pg.image.load(QUESTION2_TEXTURE).convert()
        self.textures['question3'] = pg.image.load(QUESTION3_TEXTURE).convert()
        self.textures['question_activated'] = pg.image.load(QUESTION_ACTIVATED_TEXTURE).convert_alpha()
        self.textures['tube'] = pg.image.load(TUBE_TEXTURE).convert_alpha()
        self.textures['stair'] = pg.image.load(STAIR_TEXTURE).convert()
        self.textures['flag'] = pg.image.load(FLAG_TEXTURE).convert_alpha()

    def render(self, screen, camera):
        screen.blit(self.textures['sky'], (0, 0))
        for obj_group in self.bg_objects, self.objects:
            for obj in obj_group:
                obj.render(screen, camera)


class WorldObject(pg.sprite.Sprite):
    def __init__(self, x, y, size, type):
        super().__init__()
        self.rect = pg.Rect(x, y, size[0], size[1])
        self.type = type

    def render(self, screen, camera):
        screen.blit(self.image, camera.apply(self))


class Platform(WorldObject):
    def __init__(self, x, y, image):
        super().__init__(x, y, (32, 32), 'platform')
        self.image = image


class BrickPlatform(WorldObject):
    def __init__(self, x, y, image):
        super().__init__(x, y, (32, 32), 'brick_platform')
        self.image = image

    def destroy(self, world):
        world.obj_to_collide.remove(self)
        world.objects.remove(self)


class QuestionPlatform(WorldObject):
    def __init__(self, x, y, images_pack):
        super().__init__(x, y, (32, 32), 'question_platform')
        self._curr_image = 0
        self._timer_for_imagecounter = 0
        self.image = images_pack
        self.activated = False

    def activate(self):
        if not self.activated:
            self.activated = True
            self.image = self.image[3]

    def render(self, screen, camera):
        # Переливание цвета у блока
        if not self.activated:
            self._timer_for_imagecounter += 1
            if self._timer_for_imagecounter < 60:
                self._curr_image = int(self._timer_for_imagecounter / 20)
            else:
                self._curr_image = 1 if self._timer_for_imagecounter <= 80 else 0
            if self._timer_for_imagecounter > 100:
                self._timer_for_imagecounter = 0
            screen.blit(self.image[self._curr_image], camera.apply(self))
        else:
            screen.blit(self.image, camera.apply(self))


class BGObject(WorldObject):
    def __init__(self, x, y, size, image):
        super().__init__(x, y, size, 'bg_object')
        self.image = image


class Tube(WorldObject):
    def __init__(self, x, y, texture, length):
        super().__init__(x, y, (64, length), 'tube')
        self.image = texture.subsurface((0, 0, 64, length))


class Flag(WorldObject):
    def __init__(self, x, y, texture, length):
        super().__init__(x, y, (96, length), 'flag')
        self.image = texture.subsurface((0, 0, 96, length))
