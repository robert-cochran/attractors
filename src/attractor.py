#import random
import math
#import config
from ode import ODE

# https://en.wikipedia.org/wiki/Attractor
# an attractor is a single 3d point whose behaviour is determined by ode arg

class Attractor:

    previous_translation = None

    def __init__(self, x, y, z, ode_parameters, time_step, ode, history_limit):
        self.ode_parameters = ode_parameters
        self.time_step = time_step
        self.ode = ode
        #Stores current and all previous coords as list
        # TODO change name to include 'history'
        # TODO update to include list of dict's to make less confusing
        self.coord_history = []
        self.coord_history_limit = history_limit
        self.cartesian_coords_matrix = [ [x], [y], [z] ]
        self.cartesian_coords = { "x": x, "y":y, "z":z }
        self.coord_history.append(self.cartesian_coords_matrix)
        self.generate_next_coordinate()
        

    def generate_next_coordinate(self):
        x = self.cartesian_coords["x"]
        y = self.cartesian_coords["y"]
        z = self.cartesian_coords["z"]
        x, y, z = self.ode(x, y, z, self.ode_parameters, self.time_step)
        self.cartesian_coords_matrix = [ [x], [y], [z] ]
        self.coord_history.append(self.cartesian_coords_matrix)
        self.cartesian_coords = { "x": x, "y":y, "z":z }
        if len(self.coord_history) == self.coord_history_limit:
            # cleaning coord_history massively increases speed
            self.dequeue_coord_history()
        return self.cartesian_coords_matrix

    def dequeue_coord_history(self):
        self.coord_history.pop(0)

    def get_previous_coord(self):
        return self.coord_history[-2]

    def get_current_coord(self):
        return self.coord_history[-1]

    def get_coord(self, index):
        return self.coord_history[index]


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


