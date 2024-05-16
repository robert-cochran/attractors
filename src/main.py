import pygame
import os
from attractor import Attractor, ODE, generate_attractors
from camera import Rotation, generate_pos, matrix_multiplication
#from colour_palette import new
import colour_palette
from icecream import ic
import random
import config
from setup import setup

def make_video(screen):
    _image_num = 0
    while True:
        _image_num += 1
        str_num = "0000" + str(_image_num)
        file_name = "./image/img" + str_num[-5:] + ".jpg"
        pygame.image.save(screen, file_name)
        print("In generator ", file_name)  # delete, just for demonstration
        pygame.time.wait(1000)  # delete, just for demonstration
        yield


conf = config.Many_Rainbow_Lorrenz
#conf = config.Fast_Tom

screen = setup(conf)
attractors = generate_attractors(\
        conf.NUMBER_OF_ATTRACTORS, \
        conf.ODE_PARAMETERS, \
        conf.TIME, \
        conf.ODE, \
        conf.DISTANCE, \
        conf.COLOUR_PALETTE)
run = True

save_screen = make_video(screen)  # initiate the video generator


while run:
    screen.fill(conf.BACKGROUND)
    for attractor in attractors:
        if len(attractor.points) == conf.ATTRACTOR_LENGTH_LIMIT:
            attractor.points.pop(0)
        attractor.next()
        for p in range(len(attractor.points)):
            x_pos, y_pos = generate_pos(conf.ANGLE, \
                                        attractor.points, \
                                        p, \
                                        conf.SCALE, \
                                        conf.SIZE, \
                                        conf.ROTATION_TYPE)
            # if attractor.previous is not None: 
            # ^ include this line instead of p>0 to view closed attractors 
            # "self drawing"
            if p>0:
                #color = atr_color.blue_purple(attractor.color)
                #color = colour_palette.new(attractor.color)
                #pygame.draw.line(screen, \
                #                 color, \
                #                 (x_pos, y_pos), \
                #                 attractor.previous, \
                #                 1) #white
                #pygame.draw.circle(screen, color, (x_pos, y_pos), 2)
                #pygame.draw.circle(screen, \
                #                   (attractor.colour[0], \
                #                      attractor.colour[1], \
                #                      attractor.colour[2]), \
                #                   (x_pos, y_pos), \
                #                   1)
                new_colour_tuple = (attractor.colour[0], \
                                    attractor.colour[1], \
                                    attractor.colour[2], \
                                    255)
                pygame.draw.line(screen, \
                                 new_colour_tuple, \
                                 (x_pos, y_pos), \
                                 attractor.previous, \
                                 conf.ATTRACTOR_WIDTH)
            attractor.previous=[x_pos, y_pos]
    conf.ANGLE += 0.005
    pygame.display.update()
    # ic((attractor.color[0]-1)%255)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #next(save_screen) 
pygame.quit()
