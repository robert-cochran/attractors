import os
import pygame
import setup

class View(object):
    def __init__(self, config):
        self.conf = config
        self.background_colour = self.conf.BACKGROUND_COLOUR
        self.screen, self.pygame = self.setup()

    # TODO - why does classmethod make this
    #@classmethod
    # creates screen and pygame
    def setup(self):
        os.environ["SDL_VIDEO_CENTERED"]='1'
        pygame.init()
        pygame.display.set_caption(self.conf.SET_CAPTION)
        screen = pygame.display.set_mode(self.conf.SIZE)
        pygame.time.Clock().tick(self.conf.FPS)
        screen.fill(self.conf.BLACK)
        return screen, pygame
    
    # difference between setup and make_video?
    # does make video acutally create a hard copy?
    #@classmethod
    def make_video(self):
        _image_num = 0
        while True:
            _image_num += 1
            str_num = "0000" + str(_image_num)
            file_name = "./image/img" + str_num[-5:] + ".jpg"
            self.pygame.image.save(self.screen, file_name)
            print("In generator ", file_name)  # delete, just for demonstration
            self.pygame.time.wait(1000)  # delete, just for demonstration
            yield

    #@classmethod
    def clear_screen(self):
        # needs access to screen object
        self.screen.fill(self.background_colour)

    #@classmethod
    def paint_line(self, red, green, blue, x, y, x_prev, y_prev, width):
        colour = (red, green, blue)
        coords = (x, y)
        prev_coords = (x_prev, y_prev)
        self.pygame.draw.line(self.screen, colour, coords, prev_coords, width)

    # TODO what is class method and why does it inhibit self usage?
    #@classmethod
    def paint_circle(self, red, green, blue, x, y, paint_width):
        colour = (red, green, blue)
        coordinates = (x, y)
        pygame.draw.circle(self.screen, colour, coordinates, paint_width)

    def update_display(self):
        self.pygame.display.update()

    def check_exit_signal(self):
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                return True
    
    def quit(self):
        self.pygame.quit

if __name__ == "__main__":
    class Test_Conf:
        SET_CAPTION = "attractor"
        WIDTH, HEIGHT = 1440,900 #QHD2560,1440 #MAC1440,900
        SIZE = (WIDTH, HEIGHT)
        WHITE = (200, 200, 200)
        BLACK = (0, 0, 0)
        FPS = 100
        BACKGROUND_COLOUR = BLACK
        #ROTATION_TYPE = camera.Rotation.y

    view = View(Test_Conf)
    red=255
    green=0
    blue=0
    x=0
    y=50
    step=0.1
    paint_width = 100
    run_video = True
    view.setup()
    view.make_video()
    while run_video:
        x=x+step
        y=y+step
        view.paint_circle(red, green, blue, x, y, paint_width)
        view.update_display()
        if view.check_exit_signal():
            run_video=False
        view.clear_screen()
    view.quit()
