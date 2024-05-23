
    while run_attractor:
        # wipes previous animation, otherwise points stay on screen
        view.clear_screen()
        # An Attractor in this instance is a single point in space defined by
        # its cartesian coordinates. Attractors are the set of these points.
        for attractor_index, attractor in enumerate(attractors):
            # TODO - after image/trail effect by painting line of entire coord 
            # history before screen is wiped next round. as opposed to current 
            # approach which only paints newest prev coord
            coord_matrix_prv = attractor.get_current_coord_matrix()
            coord_matrix_cur = attractor.generate_next_coordinate()
            x_prv, y_prv = camera.translate_around_y_axis(coord_matrix_prv)
            x_cur, y_cur = camera.translate_around_y_axis(coord_matrix_cur)
            colour = model.get_colour_dict(attractor_index)
            view.paint_line(colour["red"],
                            colour["green"],
                            colour["blue"],
                            x_cur,
                            y_cur,
                            x_prv,
                            y_prv,
                            model.get_width())
            view.paint_circle(colour["red"],
                              colour["green"],
                              colour["blue"],
                              x_cur,
                              y_cur,
                              model.get_width()*2)
        camera.increase_angle(0.005)
        pygame.display.update()
        # ic((attractor.color[0]-1)%255)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_attractor = False
        #next(save_screen) 
    pygame.quit()

