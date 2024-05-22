import os
import camera

class Base_Conf:
    SET_CAPTION = "attractor"
    WIDTH, HEIGHT = 1440,900 #QHD2560,1440 #MAC1440,900
    SIZE = (WIDTH, HEIGHT)
    WHITE = (200, 200, 200)
    BLACK = (0, 0, 0)
    FPS = 100
    BACKGROUND_COLOUR = BLACK
    ROTATION_TYPE = camera.Rotation.y
