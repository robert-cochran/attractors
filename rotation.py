import math

# The rotation matrix used to take the x,y,z points and 
# rotate them through space - further reading:
# https://en.wikipedia.org/wiki/Rotation_matrix 

class Rotation:
    def x(angle):
        return [[1, 0, 0],
                [0, math.cos(angle), -math.sin(angle)],
                [0, math.sin(angle), math.cos(angle)]]
    
    def y(angle): 
        return [[math.cos(angle), 0, math.sin(angle)],
                [0, 1, 0],
                [-math.sin(angle), 0, math.cos(angle)]]

    def z(angle):
        return [[math.cos(angle), -math.sin(angle), 0],
                [math.sin(angle), math.cos(angle), 0 ],
                [0, 0, 1]]
    def none():
        return [[1,0,0],
                [0,1,0],
                [0,0,1]]