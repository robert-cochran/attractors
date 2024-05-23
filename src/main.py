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

if __name__ == "__main__":
    while run_attractor:
        # wipes previous animation, otherwise points stay on screen
        view.clear_screen()
        # An Attractor in this instance is a single point in space defined by
        # its cartesian coordinates. Attractors are the set of these points.
        for index, attractor in enumerate(attractors):
            attractor.generate_next_coordinate()
            for coord_index in range(len(attractor.coord_history)):
                coord_matrix = attractor.get_coord(coord_index)
                x_pos, y_pos = camera.translate_around_y_axis(coord_matrix)
                #if attractor.previous_translation is None:
                #    # NOTE: only printed when prev_coord_index == 0
                #    print("NONE " + str(index) + "  " + str(prev_coord_index))
                if attractor.previous_translation is not None: 
                    colour = model.get_colour_dict(index)
                    x_prev = attractor.previous_translation["x"]
                    y_prev = attractor.previous_translation["y"]
                    view.paint_line(colour["red"], 
                                    colour["green"],
                                    colour["blue"],
                                    x_pos, 
                                    y_pos, 
                                    x_prev, 
                                    y_prev, 
                                    model.get_width())
                # TODO make this method that sets prev coords (needed?)
                # TODO rename to previous_coords
                attractor.previous_translation={ "x": x_pos, "y": y_pos}
        camera.increase_angle(0.005)
        pygame.display.update()
        # ic((attractor.color[0]-1)%255)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_attractor = False
        #next(save_screen) 
    pygame.quit()

