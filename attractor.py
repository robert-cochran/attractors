import random
import math

class Attractor:
    previous = None
    def __init__(self, x, y, z, parameters, time, ode, color):
        # self.x = x
        # self.y = y
        # self.z = z
        self.parameters = parameters
        # self.beta = beta
        # self.rho = rho
        # self.sigma = sigma
        self.time = time
        self.ode = ode
        self.points = [
                        [
                            [x], 
                            [y], 
                            [z]
                            ]
                        ]
        self.color = color


    def next(self):
        p = self.points[-1]
        x = p[0][0]
        y = p[1][0]
        z = p[2][0]
        x, y, z = self.ode(x, y, z, self.parameters, self.time)
        # x, y, z = self.ode(self.x, self.y, self.z, self.b, self.time)
        # self.x = x
        # self.y = y
        # self.z = z
        self.points.append([[x], [y], [z]])
        # return x, y, z
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
    def tom(x, y, z, parameters, time):
        b = parameters[0]
        dx = math.sin(y) - b*x
        dy = math.sin(z) - b*y
        dz = math.sin(x) - b*z
        return x+dx, y+dy, z+dz

    # @staticmethod
    # def tinkerbell https://en.wikipedia.org/wiki/Tinkerbell_map
    # def tinkerbell(x,y,z,time):
    #     #a, b, c, d = 0.9, -0.6013, 2.0, 0.50
    #     a, b, c, d = 0.3, 0.6000, 2.0, 0.27
    #     dx = x*x - y*y + a*x + b*y
    #     dy = 2*x*y + c*x + d*y
    #     dz = 0
    #     return x+dx, y+dy, z+dz

    # def thomas https://en.wikipedia.org/wiki/Thomas%27_cyclically_symmetric_attractor
    # def standard https://en.wikipedia.org/wiki/Standard_map
    # def duffing https://en.wikipedia.org/wiki/Duffing_map
    # def Lotka–Volterra
    # def tongue https://en.wikipedia.org/wiki/Arnold_tongue
    # 

def generate_attractors(number_of_attractors, parameters, time, ode):
    attractors = []
    # beta, rho, sigma = parameters[0], parameters[1], parameters[2]
    for n in range(number_of_attractors):
        r = random.random
        d = 0.5 # changing this moves how far apart or close together the x,y,z points start
        x, y, z = r()*d, r()*d, r()*d
        m, a = 255, 0 # m determines the range of color while a determines how white they are
        c1, c2, c3 = int(r() * m) + a, int(r() * m) + a, int(r() * m) + a
        color = [c1, c2, c3]
        a = Attractor(x, y, z, parameters, time, ode, color)
        attractors.append(a)
    return attractors