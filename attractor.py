class Attractor:
    def __init__(self, x, y, z, beta, rho, sigma, time, ode):
        self.x = x
        self.y = y
        self.z = z
        self.beta = beta
        self.rho = rho
        self.sigma = sigma
        self.time = time
        self.ode = ode
        self.points = [[[x], [y], [z]]]
    
    # https://en.wikipedia.org/wiki/Lorenz_system
    # def lorenz(x, y, z, beta, rho, sigma, time):
    #     dx = (sigma * (y - x))*time
    #     dy = (x * (rho - z) - y)*time
    #     dz = (x * y - beta * z)*time
    #     return x+dx, y+dy, z+dz
    def next(self):
        p = self.points[-1]
        x = p[0][0]
        y = p[1][0]
        z = p[2][0]
        print(p, x, y, z)
        x, y, z = self.ode(self.x, self.y, self.z, self.beta, self.rho, self.sigma, self.time)
        self.x = x
        self.y = y
        self.z = z
        self.points.append([[self.x], [self.y], [self.z]])
        # return x, y, z
        return self.points
    
    # def lorenz(self):
    #     dx = (self.sigma * (self.y - self.x))*self.time
    #     dy = (self.x * (self.rho - self.z) - self.y)*self.time
    #     dz = (self.x * self.y - self.beta * self.z)*self.time
    #     self.x = self.x + dx
    #     self.y = self.y + dy
    #     self.z = self.z + dz
    #     return self.x, self.y, self.z


class ODE(object):
    
    @staticmethod
    def lorenz(x, y, z, beta, rho, sigma, time):
        dx = (sigma * (y - x))*time
        dy = (x * (rho - z) - y)*time
        dz = (x * y - beta * z)*time
        return x+dx, y+dy, z+dz
    # def tinkerbell https://en.wikipedia.org/wiki/Tinkerbell_map
    # def ikeda https://en.wikipedia.org/wiki/Ikeda_map
    # def thomas https://en.wikipedia.org/wiki/Thomas%27_cyclically_symmetric_attractor
    # def standard https://en.wikipedia.org/wiki/Standard_map
    # def duffing https://en.wikipedia.org/wiki/Duffing_map
    # def Lotka–Volterra
    # def tongue https://en.wikipedia.org/wiki/Arnold_tongue
    # 