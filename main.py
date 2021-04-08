import pygame
import os
from matrix import *
import math
import colorsys
from attractor import Attractor, ODE
from rotation import Rotation
from icecream import ic

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
points1 = []
x2, y2, z2 = 10, 0.2, 50
points2 = []
colors = []
scale = 15
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




a1 = Attractor(x1, y1, z1, beta, rho, sigma, time, ode)

while run:
    screen.fill(black)
    tally = 0
    points1 = a1.next()


    # for p in range(int(len(points1)/8),len(points1)):
    for p in range(len(points1)):
        x_pos1, y_pos1 = generate_pos(angle, points1, p)
        # x_pos2, y_pos2 = generate_pos(angle, points2, p)

        if p > 0:
            pygame.draw.line(screen, (255,255,255), (x_pos1, y_pos1), previous1, 1) #(hsv2rgb(hue, 1, 1))
            # pygame.draw.line(screen, (255,140,0), (x_pos2, y_pos2), previous2, 1) #(hsv2rgb(hue, 1, 1))

            # pygame.draw.circle(screen, (0,255,255) , (x_pos1, y_pos1), 3)
        previous1 = (x_pos1, y_pos1)
        # previous2 = (x_pos2, y_pos2)
        tally +=1

    angle += 0.00001
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
