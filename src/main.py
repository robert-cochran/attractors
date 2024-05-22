import pygame
import os
from camera import Rotation, generate_pos, matrix_multiplication
from model import Model
from view import View
from icecream import ic
import random
import config_model
import config_view
from setup import setup

#TODO check for parameters passed in to load new config, otherwise load default



conf_view = config_view.Base_Conf
conf_model = config_model.Many_Rainbow_Lorrenz
screen = setup(conf_view)
model = Model(conf_model)
attractors = model.attractors
view = View(conf_view)
run_attractor = True
#save_screen = view.make_video(screen)  # initiate the video generator
coord_history_limit = model.conf.ATTRACTOR_LENGTH_LIMIT

if __name__ == "__main__":
    while run_attractor:
        # wipes previous animation, otherwise points stay on screen
        #screen.fill(conf_view.BACKGROUND_COLOUR)
        view.clear_screen()
        # An attractor in this instance is a single point in space defined by
        # its cartesian coordinates. Attractors are the set of these points.
        for index, attractor in enumerate(attractors):
            # I think this is limit history kept
            if len(attractor.cartesian_coords_matrix) == coord_history_limit:
                # if history limit reached, remove oldest coords
                attractor.cartesian_coords_matrix.pop(0)
            attractor.next()
            # p is x, y, z points?
            for p in range(len(attractor.cartesian_coords_matrix)):
                x_pos, y_pos = generate_pos(conf_model.ANGLE, \
                                            attractor.cartesian_coords_matrix, \
                                            p, \
                                            conf_model.SCALE, \
                                            conf_view.SIZE, \
                                            conf_view.ROTATION_TYPE)
                # if attractor.previous is not None: 
                # replace p>0 w/above to view closed attractors "self drawing"
                if p>0:
                    colour = (model.colour_sets[index]["red"], \
                              model.colour_sets[index]["green"], \
                              model.colour_sets[index]["blue"], \
                              255)
                    pygame.draw.line(screen, \
                                     colour, \
                                     (x_pos, y_pos), \
                                     attractor.previous, \
                                     conf_model.ATTRACTOR_WIDTH)
                # TODO make this method that sets prev coords (needed?)
                # TODO rename to previous_coords
                attractor.previous=[x_pos, y_pos]
        conf_model.ANGLE += 0.005
        pygame.display.update()
        # ic((attractor.color[0]-1)%255)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_attractor = False
        #next(save_screen) 
    pygame.quit()

