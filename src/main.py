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
from controller import Controller

#TODO check for parameters passed in to load new config, otherwise load default

conf_view = config_view.Base_Conf
conf_model = config_model.Rainbow_Lorenz
#conf_model = config_model.Dense_Tom
screen = setup(conf_view)
model = Model(conf_model)
attractors = model.attractors
view = View(conf_view)
camera = Camera(conf_model, conf_view)
run_attractor = True
#save_screen = view.make_video(screen)  # initiate the video generator

if __name__ == "__main__":
    controller = Controller(model, view, camera)
    controller.run()
