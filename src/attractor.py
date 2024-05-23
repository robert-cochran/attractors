#import random
import math
#import config
from ode import ODE

# https://en.wikipedia.org/wiki/Attractor
# an attractor is a single 3d point whose behaviour is determined by ode arg

class Attractor:
    previous = None
    def __init__(self, x, y, z, ode_parameters, time_step, ode):
        self.ode_parameters = ode_parameters
        self.time_step = time_step
        self.ode = ode
        #Stores current and all previous coords as list
        # TODO change name to include 'history'
        # TODO update to include list of dict's to make less confusing
        self.cartesian_coords_matrix = [ [ [x], [y], [z] ] ]
        self.cartesian_coords = { "x": x, "y":y, "z":z }
        

    def next(self):
        p = self.cartesian_coords_matrix[-1]
        x = p[0][0]
        y = p[1][0]
        z = p[2][0]
        x, y, z = self.ode(x, y, z, self.ode_parameters, self.time_step)
        self.cartesian_coords_matrix.append([[x], [y], [z]])
        self.cartesian_coords = { "x": x, "y":y, "z":z }
        return self.cartesian_coords_matrix

    def dequeue_coord_history():
        coord_history.pop(0)



if __name__ == "__main__":
    number_of_attractors = 10
    lorenz_ode_parameters = [8/3,28,10]
    time_step = 0.1
    ode = ODE.lorenz
    distance = 0.1

    attractors = generate_attractors(number_of_attractors, \
                                     lorenz_ode_parameters, \
                                     time_step, \
                                     ode, \
                                     distance) 

    # A point in this instance is a single attractor that follows the path
    # defined by the ODE.
    attractor = attractors[0]


    print("-----attractor config-----")
    print("ode_parameter_beta:" + str(attractor.ode_parameters[0]))
    print("ode_parameter_rho:" + str(attractor.ode_parameters[1]))
    print("ode_parameter_sigma:" + str(attractor.ode_parameters[2]))
    print("time_step:" + str(attractor.time_step))
    print("ode_name:" + attractor.ode.__name__)
    
    print("-----initial coords-----")
    print("cartesian_coords:" + str(attractor.cartesian_coords_matrix))
    print("cartesian_coords[0][0][0]:" \
            + str(attractor.cartesian_coords_matrix[0][0][0]))
    print("cartesian_coords:" + str(attractor.cartesian_coords))
    print("cartesian_coords_x:" + str(attractor.cartesian_coords["x"]))
    print("cartesian_coords_y:" + str(attractor.cartesian_coords["y"]))
    print("cartesian_coords_z:" + str(attractor.cartesian_coords["z"]))

    attractors[0].next()

    print("-----next coords-----")
    print("cartesian_coords:" + str(attractor.cartesian_coords_matrix))
    print("cartesian_coords[0][0][0]:" \
            + str(attractor.cartesian_coords_matrix[0][0][0]))
    print("cartesian_coords_x:" + str(attractor.cartesian_coords["x"]))
    print("cartesian_coords_y:" + str(attractor.cartesian_coords["y"]))
    print("cartesian_coords_z:" + str(attractor.cartesian_coords["z"]))


