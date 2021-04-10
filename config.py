import os
import pygame
from attractor import ODE
import colour_palette



class Base_Conf:
    WIDTH, HEIGHT = 1440, 900 
    SIZE = (WIDTH, HEIGHT)
    WHITE, BLACK = (200, 200, 200), (0, 0, 0)
    FPS = 100
    BACKGROUND = BLACK

######################################
## Atttractor 1 - Lorrenz Attractor ##
######################################
class Base_Lorrenz(Base_Conf):
    SET_CAPTION = "Lorenz Attractor"
    TIME = 0.01 #0.009
    ODE = ODE.lorenz
    BETA = 8/3 #8/3
    RHO = 28 #28
    SIGMA = 10 #10
    ODE_PARAMETERS = [BETA, RHO, SIGMA]
    SCALE = 10
    ANGLE = 0 #-100
    ATTRACTOR_LENGTH_LIMIT = 10000 #lowest is 2 as it needs the previous value to calculate
    NUMBER_OF_ATTRACTORS = 1
    ATTRACTOR_WIDTH = 4
    DISTANCE = 1 # changing distance moves how far apart or close together the x,y,z points start, for tom: 0.00001, for lorrenz: 0.1
    DYNAMIC_COLOUR = False # Flag sets whether colours change during runtime
    # Colour flag where colour changes by distance travelled, can also have the distance travelled move other props like alpha value
        # this could show you visually how when all start at the same point with the same colour the change that occurs 
    COLOUR_PALETTE = colour_palette.Static_White



class Many_Rainbow_Lorrenz(Base_Lorrenz):
    ATTRACTOR_LENGTH_LIMIT = 3 #lowest is 2 as it needs the previous value to calculate
    NUMBER_OF_ATTRACTORS = 1000
    ATTRACTOR_WIDTH = 1
    COLOUR_PALETTE = colour_palette.Rainbow_Col_Conf



class Long_Lorrenz(Base_Lorrenz):
    ATTRACTOR_LENGTH_LIMIT = 100 #lowest is 2 as it needs the previous value to calculate
    NUMBER_OF_ATTRACTORS = 20
class Long_Blue_Lorrenz(Long_Lorrenz):
    COLOUR_PALETTE = colour_palette.Static_Blue
class Long_Pink_Lorrenz(Long_Lorrenz):
    COLOUR_PALETTE = colour_palette.Static_Pink
class Long_Violet_Blue_Lorrenz(Long_Lorrenz):
    COLOUR_PALETTE = colour_palette.Static_Violet_Blue



####################################################################
## Attractor 2 - Thomas' Cyclically Symmetric Attractor (aka Tom) ##
####################################################################
class Base_Tom(Base_Conf):
    SET_CAPTION = "Thomas Attractor"
    TIME = 0.1
    ODE = ODE.tom
    SCALE = 100
    ANGLE = 0 #-100
    ATTRACTOR_LENGTH_LIMIT = 20 #lowest is 2 as it needs the previous value to calculate
    NUMBER_OF_ATTRACTORS = 100
    ODE_PARAMETERS = [0.1998]
    ATTRACTOR_WIDTH = 1
    DISTANCE = 0.05
    COLOUR_PALETTE = colour_palette.Static_White

class Fast_Tom(Base_Tom):
    TIME = 0.4


