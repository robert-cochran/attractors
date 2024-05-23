import pygame
import os
from camera import Camera
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
camera = Camera(conf_model, conf_view)
run_attractor = True
#save_screen = view.make_video(screen)  # initiate the video generator
coord_history_limit = model.coordinate_history_limit

if __name__ == "__main__":
    while run_attractor:
        # wipes previous animation, otherwise points stay on screen
        view.clear_screen()
        # An attractor in this instance is a single point in space defined by
        # its cartesian coordinates. Attractors are the set of these points.
        for index, attractor in enumerate(attractors):
            # I think this is limit history kept
            if len(attractor.cartesian_coords_matrix) == coord_history_limit:
                # keep no more than coord_history_limit amount of coords 
                attractor.cartesian_coords_matrix.pop(0)
                #attractor.cartesian_coords_matrix.pop(0)
            attractor.generate_next_coordinates()
            # p is x, y, z points?
            for p in range(len(attractor.cartesian_coords_matrix)):
                coords = attractor.cartesian_coords_matrix[p]
                x_pos, y_pos = camera.translate_around_y_axis(coords)
                if attractor.previous is not None: 
                    pygame.draw.line(screen, \
                                     model.get_colour_set(index), \
                                     (x_pos, y_pos), \
                                     attractor.previous, \
                                     conf_model.ATTRACTOR_WIDTH)
                # TODO make this method that sets prev coords (needed?)
                # TODO rename to previous_coords
                attractor.previous=[x_pos, y_pos]
        camera.increase_angle(0.005)
        pygame.display.update()
        # ic((attractor.color[0]-1)%255)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_attractor = False
        #next(save_screen) 
    pygame.quit()

