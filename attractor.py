import random
import math

def generate_attractors(number_of_attractors, parameters, time, ode, distance, colour):
    attractors = []
    # beta, rho, sigma = parameters[0], parameters[1], parameters[2]
    for n in range(number_of_attractors):
        r = random.random
        d = distance 
        x, y, z = r()*d, r()*d, r()*d
            # m determines the range of color while a determines how white they are, for tom increse the constant white levels
        red = int(r() * colour.R_MULT) + colour.R_ADD
        green = int(r() * colour.G_MULT) + colour.G_ADD
        blue = int(r() * colour.B_MULT) + colour.B_ADD
        attractor_colour = [red, green, blue]
        # else:
        #     attractor_colour = [colour.RED, colour.GREEN, colour.BLUE]
        a = Attractor(x, y, z, parameters, time, ode, attractor_colour)
        attractors.append(a)
    return attractors

class Attractor:
    previous = None
    def __init__(self, x, y, z, parameters, time, ode, colour):
        self.parameters = parameters
        self.time = time
        self.ode = ode
        self.points = [
                        [
                            [x], 
                            [y], 
                            [z]
                        ]
                    ]
        self.colour = colour

    def next(self):
        p = self.points[-1]
        x = p[0][0]
        y = p[1][0]
        z = p[2][0]
        x, y, z = self.ode(x, y, z, self.parameters, self.time)
        self.points.append([[x], [y], [z]])
        return self.points


class ODE(object):
    
    @staticmethod
    def lorenz(x, y, z, parameters, time):
        beta, rho, sigma = parameters[0], parameters[1], parameters[2] 
        dx = (sigma * (y - x))*time
        dy = (x * (rho - z) - y)*time
        dz = (x * y - beta * z)*time
        return x+dx, y+dy, z+dz

    @staticmethod
    # def thomas https://en.wikipedia.org/wiki/Thomas%27_cyclically_symmetric_attractor
    def tom(x, y, z, parameters, time):
        b = parameters[0]
        dx = (math.sin(y) - b*x)*time
        dy = (math.sin(z) - b*y)*time
        dz = (math.sin(x) - b*z)*time
        return x+dx, y+dy, z+dz

    @staticmethod
    def aizawa(x, y, z, parameters, time):
        alpha = parameters[0]
        beta = parameters[1]

        dx = (z-beta)

    # Coupled Lorrenz https://softologyblog.wordpress.com/2018/01/21/line-based-3d-strange-attractors/

    # Sixwing Attractor https://hal.archives-ouvertes.fr/hal-02306636/document

    # @staticmethod
    # def tinkerbell https://en.wikipedia.org/wiki/Tinkerbell_map
    # def tinkerbell(x,y,z,time):
    #     #a, b, c, d = 0.9, -0.6013, 2.0, 0.50
    #     a, b, c, d = 0.3, 0.6000, 2.0, 0.27
    #     dx = x*x - y*y + a*x + b*y
    #     dy = 2*x*y + c*x + d*y
    #     dz = 0
    #     return x+dx, y+dy, z+dz

    #http://www.chaoscope.org/doc/attractors.htm
    #http://sprott.physics.wisc.edu/simplest.htm

    # def standard https://en.wikipedia.org/wiki/Standard_map
    # def duffing https://en.wikipedia.org/wiki/Duffing_map
    # def Lotka–Volterra
    # def tongue https://en.wikipedia.org/wiki/Arnold_tongue

