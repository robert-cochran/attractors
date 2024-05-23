import random
import math
from ode import ODE

# https://en.wikipedia.org/wiki/Attractor
# an attractor is a single 3d point whose behaviour is determined by ode arg

class Attractor:

    def __init__(self, x, y, z, ode_parameters, time_step, ode, history_limit):
        self.ode_parameters = ode_parameters
        self.time_step = time_step
        self.ode = ode
        # Stores limited range of previous coords as list
        self.coord_history = []
        self.coord_history_limit = history_limit
        self.cartesian_coords = { "x": x, "y": y, "z": z }
        self.coord_history.append(self.cartesian_coords)
        self.generate_next_coordinate()
        

    def generate_next_coordinate(self):
        x, y, z = self.ode(self.cartesian_coords["x"], 
                           self.cartesian_coords["y"],
                           self.cartesian_coords["z"],
                           self.ode_parameters, 
                           self.time_step)
        self.cartesian_coords = { "x": x, "y": y, "z": z }
        self.coord_history.append(self.cartesian_coords)
        if len(self.coord_history) == self.coord_history_limit:
            # cleaning coord_history massively increases speed
            self.dequeue_coord_history()
        return [ [x], [y], [z] ]

    def dequeue_coord_history(self):
        self.coord_history.pop(0)

    def get_current_coord_matrix(self):
        x = self.cartesian_coords["x"]
        y = self.cartesian_coords["y"]
        z = self.cartesian_coords["z"]
        return [ [x], [y], [z] ]

    def get_current_coord_dict(self):
        return self.cartesian_coords

    def get_coord(self, index):
        return self.coord_history[index]

    def get_ode_params(self):
        return self.ode_parameters

    def get_config(self):
        return { "ode_name:": self.ode.__name__,
                 "ode_params: ": str(self.ode_parameters),
                 "time_step: ": str(self.time_step) }

if __name__ == "__main__":
    number_of_attractors = 10
    lorenz_ode_parameters = [8/3,28,10]
    time_step = 0.1
    ode = ODE.lorenz
    distance = 0.1

    # A point in this instance is a single attractor that follows the path
    # defined by the ODE.
    x = random.random()*distance
    y = random.random()*distance
    z = random.random()*distance
    attractor = Attractor(x, y, z, lorenz_ode_parameters, time_step, ode, 3) 

    print(attractor.get_config())
    
    print("-----initial coords-----")
    print("cartesian_coords:" + str(attractor.get_current_coord_dict()))

    attractor.generate_next_coordinate()

    print("-----next coords-----")
    print("cartesian_coords:" + str(attractor.get_current_coord_dict()))

