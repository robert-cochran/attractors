from model import Model
import config_model


def lorenz():
    model = Model(config_model.Rainbow_Lorenz)
    return model



if __name__ == "__main__":
    lorenz_model = lorenz()

    attractor0coords = lorenz_model.get_attractor_coords(0)
    print(str(attractor0coords))

    coords = lorenz_model.get_all_attractors_coords()
    print(str(coords))
