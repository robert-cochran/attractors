class Attractor:
    # https://en.wikipedia.org/wiki/Lorenz_system
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