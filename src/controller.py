from view import View
from model import Model
from camera import Camera

class Controller(object):

    def __init__(self, model, view, camera):
        self.model = model
        self.view = view
        self.camera = camera

    def run(self):
        running = True
        while running:
            # wipes previous animation, otherwise points stay on screen
            self.view.clear_screen()
            # An Attractor in this instance is a single point in space defined 
            # by its cartesian coordinates. 
            # Attractors are the set of these points.
            for attractor_index, attractor in enumerate(self.model.attractors):
                # TODO - after image/trail effect by painting line of entire 
                # coord history before screen is wiped next round. as opposed to
                # current approach which only paints newest prev coord
                coord_matrix_prv = attractor.get_current_coord_matrix()
                coord_matrix_cur = attractor.generate_next_coordinate()
                x_prv, y_prv = \
                        self.camera.translate_around_y_axis(coord_matrix_prv)
                x_cur, y_cur = \
                        self.camera.translate_around_y_axis(coord_matrix_cur)
                colour = self.model.get_colour_dict(attractor_index)
                self.view.paint_line(colour["red"],
                                     colour["green"],
                                     colour["blue"],
                                     x_cur,
                                     y_cur,
                                     x_prv,
                                     y_prv,
                                     self.model.get_width())
                self.view.paint_circle(colour["red"],
                                       colour["green"],
                                       colour["blue"],
                                       x_cur,
                                       y_cur,
                                       self.model.get_width()*2)
            self.camera.increase_angle(0.005)
            self.view.update_display()
            # ic((attractor.color[0]-1)%255)
            running = not self.view.check_exit_signal()
            #next(save_screen) 
        self.view.quit()

