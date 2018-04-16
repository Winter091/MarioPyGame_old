VERSION = 'BETA_0.1.1'

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
HALF_WIDTH = 640
HALF_HEIGHT = 360

GRAVITY = 0.20
MAX_FALL_SPEED = 8
MAX_X_SPEED = 2.5

WORLD_GROUND_HEIGHT = 2

JUMP_POWER = 8
SPEED_INCREASE_RATE = 0.1
SPEED_DECREASE_RATE = 0.1

STAY = 0
RUN = 1
JUMP = 2
STOPPING = 3

RIGHT = 0
LEFT = 1

DIRECTION_DICT = {
    0: 'Right',
    1: 'Left'
}

STATE_DICT = {
    0: 'Stay',
    1: 'Run',
    2: 'Jump',
    3: 'Stopping'
}

# ---------------------TEXTURES---------------------
MARIO_TEXTURE = r'lib\img\mario.png'
GROUND_TEXTURE = r'lib\img\ground.png'
SKY_TEXTURE = r'lib\img\sky.png'
BRICK_TEXTURE = r'lib\img\brick.png'
CLOUD1_TEXTURE = r'lib\img\cloud1.png'
CLOUD2_TEXTURE = r'lib\img\cloud2.png'
MOUNTAIN1_TEXTURE = r'lib\img\mountain1.png'
MOUNTAIN2_TEXTURE = r'lib\img\mountain2.png'
SHRUB1_TEXTURE = r'lib\img\bush1.png'
SHRUB2_TEXTURE = r'lib\img\bush2.png'
QUESTION_ACTIVATED_TEXTURE = r'lib\img\question_activated.png'
QUESTION1_TEXTURE = r'lib\img\question1.png'
QUESTION2_TEXTURE = r'lib\img\question2.png'
QUESTION3_TEXTURE = r'lib\img\question3.png'
TUBE_TEXTURE = r'lib\img\tube.png'
STAIR_TEXTURE = r'lib\img\stair.png'
FLAG_TEXTURE = r'lib\img\flag.png'

CLOUD1_SIZE = (60, 41)
CLOUD2_SIZE = (120, 41)
MOUNTAIN1_SIZE = (145, 75)
MOUNTAIN2_SIZE = (95, 50)
SHRUB1_SIZE = (60, 41)
SHRUB2_SIZE = (120, 41)

# ---------------------SOUNDS---------------------
SURFACE_MELODY = r'lib\snd\on_surface.wav'