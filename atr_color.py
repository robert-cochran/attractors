import random

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

def shiny_blue_purple(color):
    color = ( 
            random.random()*255,
            random.random()*255,
            color[1]
        )
    return color

def shiny_blue_white(color):
    color = ( 
            random.random()*255,
            color[1],
            color[2],
        )
    return color

def shiny_yellow(color):
    color = ( 
            color[0],
            color[1],
            random.random()*255,
        )
    return color

def new(color):
    color = ( 
            color[0],
            random.random()*255,
            random.random()*255,
        )
    return color


