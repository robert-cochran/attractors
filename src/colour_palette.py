import random


class Rainbow:
    R_MULT = 255
    R_ADD = 0
    G_MULT = 255
    G_ADD = 0
    B_MULT = 255
    B_ADD = 0
    ALPHA = 255

class Static_Pink:
    R_MULT = 1
    R_ADD = 166
    G_MULT = 1
    G_ADD = 47
    B_MULT = 1
    B_ADD = 87

class Diverse_Pink:
    R_MULT = 80
    R_ADD = 166
    G_MULT = 40
    G_ADD = 47
    B_MULT = 80
    B_ADD = 87

class Static_Blue:
    R_MULT = 1
    R_ADD = 47
    G_MULT = 1
    G_ADD = 87
    B_MULT = 1
    B_ADD = 166

class Static_Violet_Blue:
    R_MULT = 1
    R_ADD = 83
    G_MULT = 1
    G_ADD = 119
    B_MULT = 1
    B_ADD = 241

class Diverse_Blue:
    R_MULT = 50
    R_ADD = 83
    G_MULT = 80
    G_ADD = 119
    B_MULT = 40
    B_ADD = 201

class Static_White:
    R_MULT = 0
    R_ADD = 255
    G_MULT = 0
    G_ADD = 255
    B_MULT = 0
    B_ADD = 255
    ALPHA = 255

# Will be used for changing colours later. 
# These functions can generate a set of colours around some hue

# def blue_purple(color):
#     color = ( 
#             random.random()*255,
#             random.random()*255,
#             color[1]
#         )
#     return color

# def blue_white(color):
#     color = ( 
#             random.random()*255,
#             color[1],
#             color[2],
#         )
#     return color

# def yellow(color):
#     color = ( 
#             color[0],
#             color[1],
#             random.random()*255,
#         )
#     return color

#def new(color):
#    color = ( 
#            color[0],
#            random.random()*255,
#            random.random()*255,
#        )
#    return color


