from lib.Entity import *
from lib.World import *

from lib.Constants import *


class Player(Entity):
    def __init__(self, hp, spawn_coords: tuple):
        super().__init__()

        self.x_vel = 0
        self.y_vel = 0
        self.hp = hp
        self.state = STAY
        self.direction = RIGHT
        self.coins = 0

        self.gravity = GRAVITY

        self.spawn_coords = spawn_coords

        self.right = self.down = self.left = self.up = 0
        self.onground = False

        self.size = (32, 32)
        self.rect = pg.Rect(spawn_coords, self.size)
        self.image = pg.image.load(r'lib\img\dmitry.png').convert()

        self.images = []
        self.__load_images(MARIO_TEXTURE)
        self.__image_index = 0
        self.__image_timer = 0

    def __load_images(self, texture):
        texture = pg.image.load(texture).convert_alpha()

        # Right
        direction = list()
        # STAY
        state = list()
        state.append(texture.subsurface(0, 4, 32, 32))
        direction.append(state)
        # RUN
        state = list()
        state.append(texture.subsurface(35, 4, 32, 32))
        state.append(texture.subsurface(69, 4, 32, 32))
        direction.append(state)
        # JUMP
        state = list()
        state.append(texture.subsurface(108, 4, 32, 32))
        direction.append(state)
        # STOPPING
        state = list()
        state.append(texture.subsurface(189, 4, 32, 32))
        direction.append(state)

        self.images.append(direction)

        # Left
        direction = list()
        # STAY
        state = list()
        state.append(pg.transform.flip(self.images[0][0][0], 180, 0))
        direction.append(state)
        # RUN
        state = list()
        state.append(pg.transform.flip(self.images[0][1][0], 180, 0))
        state.append(pg.transform.flip(self.images[0][1][1], 180, 0))
        direction.append(state)
        # JUMP
        state = list()
        state.append(pg.transform.flip(self.images[0][2][0], 180, 0))
        direction.append(state)
        # STOPPING
        state = list()
        state.append(pg.transform.flip(self.images[0][3][0], 180, 0))
        direction.append(state)

        self.images.append(direction)
        del texture, state, direction

    def __check_collisions(self, objects, direction, world):
        for obj in objects:
            if pg.Rect.colliderect(self.rect, obj.rect):

                if direction == 'X':
                    if self.x_vel > 0:
                        self.rect.right = obj.rect.left
                        self.x_vel = 0
                    if self.x_vel < 0:
                        self.rect.left = obj.rect.right
                        self.x_vel = 0

                elif direction == 'Y':
                    if self.y_vel > 0:
                        self.onground = True
                        self.rect.bottom = obj.rect.top
                        self.y_vel = 0
                    if self.y_vel < 0:
                        self.rect.top = obj.rect.bottom
                        self.y_vel = - self.y_vel / 2
                        if obj.type == 'brick_platform':
                            obj.destroy(world)
                        elif obj.type == 'question_platform':
                            obj.activate()

            if pg.Rect.colliderect(pg.Rect(self.rect[0] + 1, self.rect[1], self.rect[2], self.rect[3]),
                                   obj.rect) and direction == 'X':
                self.x_vel = 0

    # Вся физика игрока, обработка его движений
    def move(self, objects, world):
        if self.right:
            self.x_vel += SPEED_INCREASE_RATE
        if self.left:
            self.x_vel -= SPEED_INCREASE_RATE
        if self.up:
            if self.onground:
                self.y_vel = - JUMP_POWER

        # Плавная остановка и ограничение максим. скорости
        if not (self.right or self.left):
            if self.x_vel > 0:
                self.x_vel -= SPEED_DECREASE_RATE
            if self.x_vel < 0:
                self.x_vel += SPEED_DECREASE_RATE
        else:
            if self.x_vel > 0 and self.x_vel > MAX_X_SPEED:
                self.x_vel = MAX_X_SPEED
            if self.x_vel < 0 and - self.x_vel > MAX_X_SPEED:
                self.x_vel = - MAX_X_SPEED

        # Убираем погрешность
        if 0 < self.x_vel < SPEED_DECREASE_RATE:
            self.x_vel = 0
        if 0 > self.x_vel > -SPEED_DECREASE_RATE:
            self.x_vel = 0

        # Ограничение макс. скорости падения
        if not self.onground:
            self.y_vel += self.gravity
            if self.y_vel > MAX_FALL_SPEED:
                self.y_vel = MAX_FALL_SPEED

        """ Тут баг самой библиотеки pygame. self.rect работает с целыми числами,
        и если отнимать у x-координаты, например, 0.01, то он будет изменяться на -1,
        а если прибавлять те же самые 0.01, то прибавляться на 1 координата не будет."""
        if self.x_vel > 0:
            self.rect.left += (self.x_vel + 1)
        else:
            self.rect.left += self.x_vel
        self.__check_collisions(objects, 'X', world)

        self.rect.top += self.y_vel
        self.onground = False
        self.__check_collisions(objects, 'Y', world)

        # Если этого не будет, то стоя на земле, onground будет не всегда True, и y_vel будет расти
        for obj in objects:
            if pg.Rect(self.rect.x, self.rect.y + 1, self.size[0], self.size[1]).colliderect(obj.rect):
                self.onground = True
                self.y_vel = 0

    # Обработка вида спрайта игрока
    def control_image(self):
        if self.x_vel == 0:
            self.state = STAY
            self.__image_index = 0
            self.__image_timer = 0
        else:
            self.state = RUN
            if self.x_vel > 0:
                self.direction = RIGHT
            else:
                self.direction = LEFT

            if (self.x_vel > 0 and self.left and not self.right) or (self.x_vel < 0 and self.right and not self.left):
                self.__image_index, self.__image_timer = 0, 0
                self.state = STOPPING


        if self.y_vel != 0:
            self.state = JUMP
            self.__image_timer = 0
            self.__image_index = 0

        if self.state == RUN:
            self.__image_timer += 1
            if self.__image_timer > 20:
                self.__image_timer = 0
            self.__image_index = 1 if self.__image_timer >= 10 else 0



    def render(self, screen, camera):
        screen.blit(self.images[self.direction][self.state][self.__image_index], camera.apply(self))

