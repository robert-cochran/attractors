import os
#import pygame
from ode import ODE
import colour_scheme
import camera


# TODO - rename to view conf and move it to view section
# separate the other view and mODE. related configs too
# TODO REMOVE

######################################
## Atttractor 1 - Lorrenz Attractor ##
######################################
class Base_Lorrenz():
    TIME_STEP = 0.01 #0.009
    ODE = ODE.lorenz
    BETA = 8/3 #8/3
    RHO = 28 #28
    SIGMA = 10 #10
    ODE_PARAMETERS = [BETA, RHO, SIGMA]
    SCALE = 10
    ANGLE = 0 #-100
    COORDINATE_HISTORY_LIMIT = 10000 # min 2 (needs prev value to calc)
    NUMBER_OF_ATTRACTORS = 1
    ATTRACTOR_WIDTH = 4
    DISTANCE = 1 # changing distance moves how far apart or close together the
                 # x,y,z points start, for tom: 0.00001, for lorrenz: 0.1
    DYNAMIC_COLOUR = False # Flag sets whether colours change during runtime
    # Colour flag where colour changes by distance travelled, can also have the
    # distance travelled move other props like alpha value
    # this could show you visually how when all start at the same point with 
    # the same colour the change that occurs 
    COLOUR_SCHEME = colour_scheme.Static_White
    # c = 1
    # [[math.cos(angle)/c, 0, math.sin(angle)/c],
    # [0, 1, 0],
    # [-math.sin(angle)/c, 0, math.cos(angle)/c]]
    # AFTER_IMAGE



class Many_Rainbow_Lorrenz(Base_Lorrenz):
    COORDINATE_HISTORY_LIMIT = 3 # min 2
    NUMBER_OF_ATTRACTORS = 1000
    ATTRACTOR_WIDTH = 1
    COLOUR_SCHEME = colour_scheme.Rainbow


class Long_Lorrenz(Base_Lorrenz):
    COORDINATE_HISTORY_LIMIT = 100 # min 2
    NUMBER_OF_ATTRACTORS = 20

class Long_Blue_Lorrenz(Long_Lorrenz):
    COLOUR_SCHEME = colour_scheme.Static_Blue

class Long_Pink_Lorrenz(Long_Lorrenz):
    COLOUR_SCHEME = colour_scheme.Static_Pink

class Long_Violet_Blue_Lorrenz(Long_Lorrenz):
    COLOUR_SCHEME = colour_scheme.Static_Violet_Blue

class Wide_Distance(Many_Rainbow_Lorrenz):
    DISTANCE = 90
    TIME_STEP = 0.003

####################################################################
## Attractor 2 - Thomas' Cyclically Symmetric Attractor (aka Tom) ##
####################################################################
class Base_Tom():
    SET_CAPTION = "Thomas Attractor"
    TIME_STEP = 0.1
    ODE = ODE.tom
    SCALE = 100
    ANGLE = 0 #-100
    COORDINATE_HISTORY_LIMIT = 20 
    NUMBER_OF_ATTRACTORS = 100
    ODE_PARAMETERS = [0.1998]
    ATTRACTOR_WIDTH = 1
    DISTANCE = 0.05
    COLOUR_SCHEME = colour_scheme.Static_White
    # c = 1
    # [[math.cos(angle)/c, 0, math.sin(angle)/c],
    # [0, 1, 0],
    # [-math.sin(angle)/c, 0, math.cos(angle)/c]]


class Fast_Tom(Base_Tom):
    TIME_STEP = 0.4


####################################
## Attractor 3 - Aizawa Attractor ##
####################################
class Base_Aizawa():
    SET_CAPTION = "Aizawa Attractor"
    TIME_STEP = 0.05
    ODE = ODE.aizawa
    SCALE = 200
    ANGLE = 0 #-100
    COORDINATE_HISTORY_LIMIT = 200 
    NUMBER_OF_ATTRACTORS = 10
    ALPHA = 0.95
    BETA = 0.7
    GAMMA = 0.6
    DELTA = 3.5
    EPSILON = 0.25
    ZETA = 0.1
    ODE_PARAMETERS = [ALPHA, BETA, GAMMA, DELTA, EPSILON, ZETA]
    ATTRACTOR_WIDTH = 1
    DISTANCE = 0.001
    COLOUR_SCHEME = colour_scheme.Rainbow


####################################
## Attractor 4 - Bouali Attractor ##
####################################
class Base_Bouali():
    SET_CAPTION = "Bouali Attractor"
    TIME_STEP = 0.01
    ODE = ODE.bouali
    SCALE = 250
    ANGLE = 100
    COORDINATE_HISTORY_LIMIT = 2 
    NUMBER_OF_ATTRACTORS = 1000
    ALPHA = 0.95
    BETA = 0.7
    GAMMA = 0.6
    DELTA = 3.5
    EPSILON = 0.25
    ZETA = 0.1
    ODE_PARAMETERS = [ALPHA, BETA, GAMMA, DELTA, EPSILON, ZETA]
    ATTRACTOR_WIDTH = 1
    DISTANCE = 0.5
    COLOUR_SCHEME = colour_scheme.Rainbow
    ROTATION_TYPE=camera.Rotation.none
    # [[-1,0,0],
    # [0,c,0],
    # [0,0,c]]
