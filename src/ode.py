
# Ordinary Differential Equations (not sure they're all Ordinary though)
# should change to DE (differential equations) instead to be more accurate
class ODE(object):

    @staticmethod
    def lorenz(x, y, z, parameters, time_step):
        beta, rho, sigma = parameters[0], parameters[1], parameters[2] 
        dx = (sigma * (y - x))*time_step
        dy = (x * (rho - z) - y)*time_step
        dz = (x * y - beta * z)*time_step
        return x+dx, y+dy, z+dz

    @staticmethod
    # https://en.wikipedia.org/wiki/Thomas%27_cyclically_symmetric_attractor
    def tom(x, y, z, parameters, time_step):
        b = parameters[0]
        dx = (math.sin(y) - b*x)*time_step
        dy = (math.sin(z) - b*y)*time_step
        dz = (math.sin(x) - b*z)*time_step
        return x+dx, y+dy, z+dz

    @staticmethod
    # https://www.behance.net/gallery/7618879/Strange-Attractors
    # http://www.3d-meier.de/tut19/Seite3.html
    def aizawa(x, y, z, parameters, time_step):
        alpha = parameters[0]
        beta = parameters[1]
        gamma = parameters[2]
        delta = parameters[3]
        epsilon = parameters[4]
        zeta = parameters[5]
        
        dx = ( (z-beta)*x - (delta*y) )*time_step
        dy = ( (delta*x) + (zeta-beta)*y )*time_step
        dz = ( (gamma) + (alpha*z) - ((z**3)/3) - \
                ( (x**2) + (y**2) ) * (1+(epsilon*z)) \
                + (zeta*z*(x**3)) )*time_step

        return x+dx, y+dy, z+dz

    @staticmethod
    # http://www.3d-meier.de/tut19/Seite5.html
    def bouali(x,y,z,parameters,time_step):
        a = parameters[0]
        s = parameters[1]

        dx = ( x*(4-y) + (a*z) )*time_step
        dy = ( (-1 * y) * (1-(x**2)) )*time_step
        dz = ( (-1*x) * (1.5-(s*z)) - (0.05*z) )*time_step

        return x+dx, y+dy, z+dz


    ##### 2D ATTRACTORS
    
    # Extending 2d to 3d http://paulbourke.net/fractals/sprott/
    # Python library of 2d attractors 
    # https://examples.pyviz.org/attractors/attractors.html

    @staticmethod
    # https://en.wikipedia.org/wiki/Tinkerbell_map
    def tinkerbell(x,y,z,time_step):
        #a, b, c, d = 0.9, -0.6013, 2.0, 0.50
        a, b, c, d = 0.3, 0.6000, 2.0, 0.27
        dx = x*x - y*y + a*x + b*y
        dy = 2*x*y + c*x + d*y
        dz = 0
        return x+dx, y+dy, z+dz

if __name__ == "__main__":

    x = 0.5
    y = 0.6
    z = 0.7
    lorrenz_parameters = [8/3,28,10]
    time_step = 0.1

    print(ODE.lorenz(x,y,z,lorrenz_parameters,time_step))
    print(ODE.tinkerbell(x,y,z,time_step))

