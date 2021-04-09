import random

class Attractor:
    previous = None
    def __init__(self, x, y, z, beta, rho, sigma, time, ode, color):
        self.x = x
        self.y = y
        self.z = z
        self.beta = beta
        self.rho = rho
        self.sigma = sigma
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
        x, y, z = self.ode(self.x, self.y, self.z, self.beta, self.rho, self.sigma, self.time)
        # x, y, z = self.ode(self.x, self.y, self.z, self.time)
        self.x = x
        self.y = y
        self.z = z
        self.points.append([[self.x], [self.y], [self.z]])
        # return x, y, z
        return self.points



class ODE(object):
    
    @staticmethod
    def lorenz(x, y, z, beta, rho, sigma, time):
        dx = (sigma * (y - x))*time
        dy = (x * (rho - z) - y)*time
        dz = (x * y - beta * z)*time
        return x+dx, y+dy, z+dz

    # @staticmethod
    # def tinkerbell(x,y,z,time):
    #     #a, b, c, d = 0.9, -0.6013, 2.0, 0.50
    #     a, b, c, d = 0.3, 0.6000, 2.0, 0.27
    #     dx = x*x - y*y + a*x + b*y
    #     dy = 2*x*y + c*x + d*y
    #     dz = 0
    #     return x+dx, y+dy, z+dz
    # def tinkerbell https://en.wikipedia.org/wiki/Tinkerbell_map
    # def ikeda https://en.wikipedia.org/wiki/Ikeda_map
    # def thomas https://en.wikipedia.org/wiki/Thomas%27_cyclically_symmetric_attractor
    # def standard https://en.wikipedia.org/wiki/Standard_map
    # def duffing https://en.wikipedia.org/wiki/Duffing_map
    # def Lotka–Volterra
    # def tongue https://en.wikipedia.org/wiki/Arnold_tongue
    # 

def generate_attractors(number, beta, rho, sigma, time, ode):
    attractors = []
    for n in range(number):
        r = random.random
        x, y, z = r()*10, r()*10, r()*10
        m, a = 255, 0
        c1, c2, c3 = int(r() * m) + a, int(r() * m) + a, int(r() * m) + a
        color = [c1, c2, c3]
        a = Attractor(x, y, z, beta, rho, sigma, time, ode, color)
        attractors.append(a)
    return attractors