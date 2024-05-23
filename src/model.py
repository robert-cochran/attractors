from attractor import Attractor, ODE
import colour_scheme
import random

# TODO - an after image effect using previous generated points that fade out
# based on how long theyve been around. would tie opacity to time step. but also
# seriously increase the amount of memory needed to run?

class Model:

    def __init__(self, config):
        self.attractor_width = config.ATTRACTOR_WIDTH
        self.number_of_attractors = config.NUMBER_OF_ATTRACTORS
        self.coordinate_history_limit = config.ATTRACTOR_LENGTH_LIMIT
        self.attractors = []
        self.colour_sets = []
        r = random.random
        d = config.DISTANCE 
        for x in range(self.number_of_attractors):
            x, y, z = r()*d, r()*d, r()*d
            attractor = Attractor(x, 
                                  y, 
                                  z, \
                                  config.ODE_PARAMETERS, \
                                  config.TIME_STEP, \
                                  config.ODE, \
                                  self.coordinate_history_limit)
            self.attractors.append(attractor)
            colours = colour_scheme.generate_colour_set(config.COLOUR_SCHEME)
            self.colour_sets.append(colours)

    #@classmethod
    def load_config(self, config):
        # does this require also updating config set inside self.attractors?
        print("todo")


    def get_colour_set(self, index):
        colour_set = self.colour_sets[index]
        return (colour_set["red"], 
                colour_set["green"], 
                colour_set["blue"], 
                255)

    def get_colour_dict(self, index):
        colour_set = self.colour_sets[index]
        return  { "red": colour_set["red"], \
                  "green": colour_set["green"], \
                  "blue": colour_set["blue"] }

    def get_width(self):
        return self.attractor_width

if __name__ == "__main__":
    class Test_Conf:
        TIME_STEP = 0.01 #0.009
        ODE = ODE.lorenz
        BETA = 8/3 #8/3
        RHO = 28 #28
        SIGMA = 10 #10
        ODE_PARAMETERS = [BETA, RHO, SIGMA]
        SCALE = 10
        ANGLE = 0 #-100
        ATTRACTOR_LENGTH_LIMIT = 10000 # min 2 (needs prev value to calc)
        NUMBER_OF_ATTRACTORS = 1
        ATTRACTOR_WIDTH = 4
        COLOUR_SCHEME = colour_scheme.Static_White
        DISTANCE = 1


    model = Model(Test_Conf)
    attractor0 = model.attractors[0]

    print("-----attractor0 config-----")
    print("ode_parameter_beta:" + str(attractor0.ode_parameters[0]))
    print("ode_parameter_rho:" + str(attractor0.ode_parameters[1]))
    print("ode_parameter_sigma:" + str(attractor0.ode_parameters[2]))
    print("time_step:" + str(attractor0.time_step))
    print("ode_name:" + attractor0.ode.__name__)
    print("colour_sets[0].red:" + str(model.colour_sets[0]["red"]))
    print("colour_sets[0].green:" + str(model.colour_sets[0]["green"]))
    print("colour_sets[0].blue:" + str(model.colour_sets[0]["blue"]))

    
    print("-----attractor0 initial coords-----")
    print("cartesian_coords:" + str(attractor0.cartesian_coords_matrix))
    print("cartesian_coords[0][0][0]:" \
            + str(attractor0.cartesian_coords_matrix[0][0][0]))
    print("cartesian_coords:" + str(attractor0.cartesian_coords))
    print("cartesian_coords_x:" + str(attractor0.cartesian_coords["x"]))
    print("cartesian_coords_y:" + str(attractor0.cartesian_coords["y"]))
    print("cartesian_coords_z:" + str(attractor0.cartesian_coords["z"]))


