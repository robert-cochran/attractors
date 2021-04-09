import math
from atr_math import matrix_multiplication

# The rotation matrix used to take the x,y,z points and 
# rotate them through space - further reading:
# https://en.wikipedia.org/wiki/Rotation_matrix 

class Rotation:
    def x(angle):
        return [[1, 0, 0],
                [0, math.cos(angle)/2, -math.sin(angle)/2],
                [0, math.sin(angle)/2, math.cos(angle)/2]]
    
    def y(angle): 
        c = 1
        return [[math.cos(angle)/c, 0, math.sin(angle)/c],
                [0, 1, 0],
                [-math.sin(angle)/c, 0, math.cos(angle)/c]]

    def z(angle):
        return [[math.cos(angle), -math.sin(angle), 0],
                [math.sin(angle), math.cos(angle), 0 ],
                [0, 0, 1]]
    def none():
        return [[1,0,0],
                [0,1,0],
                [0,0,1]]

def generate_pos(angle, points, p, scale, size):
    width = size[0]
    height = size[1]
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


