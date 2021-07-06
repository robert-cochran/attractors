import pygame
import os
from attractor import Attractor, ODE, generate_attractors
from camera import Rotation, generate_pos, matrix_multiplication
# from atr_colour import colour_gen
from icecream import ic
import random
import config
from setup import setup

# To Do
## Have a bunch of configs i can quickly enter in and cycle through
###### Check how to make rotation.y rotate in place instead of in a large circle 
### Add in changing colours
### Add in options to add circles drawn
    ### maybe add circles only at beginning of line?
### Allow for specified number of central points (atm its just one where all atr's emerge, allow for more)
### Option for selfdrawing (doesnt seem to do it with Lorrenz_Conf, but it does do it with Long_Attractors)
    ### need to figure out why selfdrawing occurs
### Afterimage effect (https://www.youtube.com/watch?v=idpOunnpKTo / https://github.com/xMissingno/Coding-Projects)
### Test Opacitity (Alpha)
### Will C++ impl allow for much greater atr number?
### Format with Black Linter


def make_video(screen):

    _image_num = 0

    while True:
        _image_num += 1
        str_num = "0000" + str(_image_num)
        file_name = "./image/img" + str_num[-5:] + ".jpg"
        pygame.image.save(screen, file_name)
        # print("In generator ", file_name)  # delete, just for demonstration
        # pygame.time.wait(1000)  # delete, just for demonstration
        yield


conf = config.Many_Rainbow_Lorrenz
screen = setup(conf)
attractors = generate_attractors(conf.NUMBER_OF_ATTRACTORS, conf.ODE_PARAMETERS, conf.TIME, conf.ODE, conf.DISTANCE, conf.COLOUR_PALETTE)
run = True

save_screen = make_video(screen)  # initiate the video generator


while run:
    screen.fill(conf.BACKGROUND)
    for attractor in attractors:
        if len(attractor.points) == conf.ATTRACTOR_LENGTH_LIMIT:
            attractor.points.pop(0)
        attractor.next()
        for p in range(len(attractor.points)):
            x_pos, y_pos = generate_pos(conf.ANGLE, attractor.points, p, conf.SCALE, conf.SIZE, conf.ROTATION_TYPE)
            # if attractor.previous is not None: # include this line instead of p>0 to view closed attractors "self drawing"
            if p>0:
                # color = atr_color.new(attractor.color)
                # pygame.draw.line(screen, color, (x_pos, y_pos), attractor.previous, 1) #white
                # pygame.draw.circle(screen, color, (x_pos, y_pos), 2)
                # pygame.draw.circle(screen, (attractor.colour[0], attractor.colour[1], attractor.colour[2]), (x_pos, y_pos), 1)
                pygame.draw.line(screen, (attractor.colour[0], attractor.colour[1], attractor.colour[2], 255), (x_pos, y_pos), attractor.previous, conf.ATTRACTOR_WIDTH)
            attractor.previous=[x_pos, y_pos]
    conf.ANGLE += 0.005
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #next(save_screen) 
pygame.quit()
