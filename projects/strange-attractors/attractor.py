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
    # https://en.wikipedia.org/wiki/Thomas%27_cyclically_symmetric_attractor
    def tom(x, y, z, parameters, time):
        b = parameters[0]
        dx = (math.sin(y) - b*x)*time
        dy = (math.sin(z) - b*y)*time
        dz = (math.sin(x) - b*z)*time
        return x+dx, y+dy, z+dz

    @staticmethod
    # https://www.behance.net/gallery/7618879/Strange-Attractors
    # http://www.3d-meier.de/tut19/Seite3.html
    def aizawa(x, y, z, parameters, time):
        alpha = parameters[0]
        beta = parameters[1]
        gamma = parameters[2]
        delta = parameters[3]
        epsilon = parameters[4]
        zeta = parameters[5]
        
        dx = ( (z-beta)*x - (delta*y) )*time
        dy = ( (delta*x) + (zeta-beta)*y )*time
        dz = ( (gamma) + (alpha*z) - ((z**3)/3) - ( (x**2) + (y**2) ) * (1+(epsilon*z)) + (zeta*z*(x**3)) )*time

        return x+dx, y+dy, z+dz

    @staticmethod
    # http://www.3d-meier.de/tut19/Seite5.html
    def bouali(x,y,z,parameters,time):
        a = parameters[0]
        s = parameters[1]

        dx = ( x*(4-y) + (a*z) )*time
        dy = ( (-1 * y) * (1-(x**2)) )*time
        dz = ( (-1*x) * (1.5-(s*z)) - (0.05*z) )*time

        return x+dx, y+dy, z+dz

    ##### SINGLE ATTRACTORS
    # Coupled Lorrenz https://softologyblog.wordpress.com/2018/01/21/line-based-3d-strange-attractors/
    # Sixwing Attractor https://hal.archives-ouvertes.fr/hal-02306636/document
    # Newton-Leipnik http://www.3d-meier.de/tut19/Seite0.html
    # Nose-Hoover http://www.3d-meier.de/tut19/Seite0.html
    # Halvorsen http://www.3d-meier.de/tut19/Seite0.html
    # Chen-Lee http://www.3d-meier.de/tut19/Seite0.html
    # 3Cells CNN http://www.3d-meier.de/tut19/Seite0.html
    # Bouali http://www.3d-meier.de/tut19/Seite0.html
    # Finance http://www.3d-meier.de/tut19/Seite0.html
    # Automatic generation of strange attractors  JC Sprott http://paulbourke.net/fractals/sprott/paper203.pdf
    # def standard https://en.wikipedia.org/wiki/Standard_map
    # def duffing https://en.wikipedia.org/wiki/Duffing_map
    # def Lotka–Volterra
    # def tongue https://en.wikipedia.org/wiki/Arnold_tongue
    # Magnetic https://www.michelemorrone.eu/glchaosp/Magnetic.html - https://www.reddit.com/r/creativecoding/comments/e4t1kx/magnetic_attractor_in_glchaosp_3d_strange/
    # Mirrored lorrenz https://arxiv.org/pdf/1311.6128.pdf
    # Halvorsen model https://iopscience.iop.org/article/10.1088/1742-6596/1286/1/012028/pdf
    # De-Jong http://www.3d-meier.de/Galerie/Attraktor/De-Jong.html
    # Mikael Christensons examples https://syntopia.github.io/StrangeAttractors/

    ### LISTS
    # Library of 3d atttractors https://www.michelemorrone.eu/glchaosp/RampeClass.html   
    # Another Library of 3D attractors https://chaos-equations.glitch.me/?p=RCMEZN
    # List of missingno's 3D attractors https://www.youtube.com/watch?v=idpOunnpKTo&ab_channel=OrfeasLiossatos
    # List of 3d attractors http://www.chaoscope.org/doc/attractors.htm
    # List of simple 3d attractors http://sprott.physics.wisc.edu/simplest.htm / http://sprott.physics.wisc.edu/pubs/paper212.pdf



    ##### 2D ATTRACTORS
    
    # Extending 2d to 3d http://paulbourke.net/fractals/sprott/
    # Python library of 2d attractors https://examples.pyviz.org/attractors/attractors.html

    # @staticmethod
    # def tinkerbell https://en.wikipedia.org/wiki/Tinkerbell_map
    # def tinkerbell(x,y,z,time):
    #     #a, b, c, d = 0.9, -0.6013, 2.0, 0.50
    #     a, b, c, d = 0.3, 0.6000, 2.0, 0.27
    #     dx = x*x - y*y + a*x + b*y
    #     dy = 2*x*y + c*x + d*y
    #     dz = 0
    #     return x+dx, y+dy, z+dz


    ##### MATH 
    # https://en.wikipedia.org/wiki/Attractor
