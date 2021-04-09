import pygame
import os
from matrix import *
import math
import colorsys
from attractor import Attractor, ODE
from camera import Rotation, matrix_multiplication
from icecream import ic
import random

#--- Constants ------

os.environ["SDL_VIDEO_CENTERED"]='1'
width, height = 1440, 900 
size = (width, height)
white, black = (200, 200, 200), (0, 0, 0)
pygame.init()
pygame.display.set_caption("Lorenz Attractor")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 200
screen.fill(black)
clock.tick(fps)
time = 0.009 #0.009

ode = ODE.lorenz
sigma = 10
rho = 28
beta = 8/3
x1, y1, z1 = 0.4, 0, 0
x2, y2, z2 = 10, 0.2, 50
x3, y3, z3 = 5, 5, 3
x4, y4, z4 = 1, 5, 5
points1 = []
points2 = []
points3 = []
points4 = []
colors = []
scale = 10
angle = -100
previous = None
run = True


def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))


def generate_pos(angle, points, p):
    rotated_2d = matrix_multiplication(Rotation.y(angle), points[p]) 
    # distance = 1 #0.01
    # val = 1/(distance - rotated_2d[2][0])#z value
    projection_matrix = [[1, 0, 0],
                        [0, 1, 0]]
    projected2d = matrix_multiplication(projection_matrix, rotated_2d)
    projected2d = rotated_2d
    x_pos = int(projected2d[0][0] * scale) + width//2 #+ 100
    y_pos = int(projected2d[1][0] * scale) + height//2
    return x_pos, y_pos

def generate_attractors(number, beta, rho, sigma, time, ode):
    attractors = []
    for n in range(number):
        r = random.random
        x, y, z = r(), r(), r()
        c1, c2, c3 = int(r() * 255), int(r() * 255), int(r() * 255)
        color = [c1, c2, c3]
        a = Attractor(x, y, z, beta, rho, sigma, time, ode, color)
        attractors.append(a)
    return attractors

def draw_attractor(attractor, attractor_limit):
    if len(attractor.points) == attractor_limit:
        attractor.points.pop(0)
    attractor.next()
    for p in range(len(attractor.points)):
        x_pos, y_pos = generate_pos(angle, attractor.points, p)
        # if attractor.previous is not None: # include this line to view closed attractors "self drawing"
        if p>0:
            pygame.draw.line(screen, (attractor.color[0], attractor.color[1], attractor.color[2]), (x_pos, y_pos), attractor.previous, 1) #white
        attractor.previous=[x_pos, y_pos]

attractors = generate_attractors(30, beta, rho, sigma, time, ode)


while run:
    screen.fill(black)
    for attractor in attractors:
        draw_attractor(attractor, 30)
        #attractor = attractors[a]


    angle += 0.005
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
