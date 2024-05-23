import math
from matrix import matrix_multiplication

class Camera(object):
    previous_translation = None

    def __init__(self, config_model, config_view):
        self.angle = config_model.ANGLE
        self.scale = config_model.SCALE
        self.size = config_view.SIZE
        self.width = config_view.SIZE[0]
        self.height = config_view.SIZE[1]
    
    # translates the coordinates rotaionally around the y axis
    def translate_around_y_axis(self, coordinates):
        rotated_2d = matrix_multiplication(Rotation.y(self.angle), coordinates) 
        # distance = 1 #0.01
        # val = 1/(distance - rotated_2d[2][0])#z value
        projection_matrix = [[1, 0, 0],
                            [0, 1, 0]]
        projected2d = matrix_multiplication(projection_matrix, rotated_2d)
        projected2d = rotated_2d # ????
        x_pos = int(projected2d[0][0] * self.scale) + self.width//2 #+ 100
        y_pos = int(projected2d[1][0] * self.scale) + self.height//2
        return x_pos, y_pos
    
    def increase_angle(self, step):
        self.angle += step

# The rotation matrix used to take the x,y,z points and 
# rotate them through space - further reading:
# https://en.wikipedia.org/wiki/Rotation_matrix 
class Rotation:
    def x(angle):
        c = 5
        return [[1, 0, 0],
                [0, math.cos(angle)/c, -math.sin(angle)/c],
                [0, math.sin(angle)/c, math.cos(angle)/c]]
    
    def y(angle): 
        c = 1
        return [[math.cos(angle)/c, 0, math.sin(angle)/c],
                [0, 1, 0],
                [-math.sin(angle)/c, 0, math.cos(angle)/c]]

    def z(angle):
        return [[math.cos(angle), -math.sin(angle), 0],
                [math.sin(angle), math.cos(angle), 0 ],
                [0, 0, 1]]

    def none(angle):
        c = 0.1
        return [[-1,0,0],
                [0,c,0],
                [0,0,c]]




