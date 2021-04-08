import pygame
import os
from matrix import *
import math
import colorsys
from attractor import Attractor 
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


sigma = 10
rho = 28
beta = 8/3
x, y, z = 0.4, 0, 0
points = []
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




previous = (723,451)


while run:
    screen.fill(black)

    # tally = 0
    x, y, z = Attractor.lorenz(x, y, z, beta, rho, sigma, time)
    point = [[x], [y], [z]]
    points.append(point)
    # for p in range(int(len(points)/8),len(points)):
    for p in range(len(points)):
        x_pos, y_pos = generate_pos(angle, points, p)

        

        # if tally > 1:
        pygame.draw.line(screen, (255,255,255), (x_pos, y_pos), previous, 1) #(hsv2rgb(hue, 1, 1))
            # pygame.draw.circle(screen, (0,255,255) , (x_pos, y_pos), 3)
        previous = (x_pos, y_pos)
        # tally +=1
    angle += 0.0001
    pygame.display.update()
    # print(previous)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
