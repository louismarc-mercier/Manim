
from big_ol_pile_of_manim_imports import *



class PlotQuadratic(GraphScene):
    """
    Quadratic function on interval [-10, 10]
    """
    CONFIG = {
        "y_max" : 100,
        "y_min" : 0,
        "x_max" : 10,
        "x_min" : -10,
        "y_tick_frequency" : 5,
        "x_tick_frequency" : 0.5,
        "axes_color" : BLUE,
        "y_labeled_nums": range(0,100,10),
        "x_labeled_nums": list(np.arange(-10, 10, 2)),
        "x_label_decimal":0,
        "y_label_decimal":0,
        "graph_origin": np.array((0, -2.5, 0))
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : x**2,
                                    color = GREEN,
                                    x_min = self.x_min,
                                    x_max = self.x_max
                                    )
        graph_lab = self.get_graph_label(graph, label="x^2")
        self.play(ShowCreation(graph), ShowCreation(graph_lab), run_time = 2)
        self.wait()


class PlotExponential(GraphScene):
    """
    Quadratic function on interval [-10, 10]
    """
    CONFIG = {
        "y_max" : 30,
        "y_min" : 0,
        "x_max" : 3,
        "x_min" : -3,
        "y_tick_frequency" : 5,
        "x_tick_frequency" : 0.5,
        "axes_color" : BLUE,
        "y_labeled_nums": range(0,30,5),
        "x_labeled_nums": list(np.arange(-3, 4, 1)),
        "x_label_decimal":0,
        "y_label_decimal":0,
        "graph_origin": np.array((0, -2.5, 0))
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : np.exp(x),
                                    color = RED,
                                    x_min = self.x_min,
                                    x_max = self.x_max
                                    )
        #graph_lab = self.get_graph_label(graph, label="e^x") \mathrm{e}
        graph_lab = self.get_graph_label(graph, label="\mathrm{e}^x")
        self.play(ShowCreation(graph), ShowCreation(graph_lab), run_time = 2)
        self.wait()


class PlotSinCos(GraphScene):
    CONFIG = {
        "y_max" : 1.5,
        "y_min" : -1.5,
        "x_max" : 3*PI/2,
        "x_min" : -3*PI/2,
        "axes_color": WHITE,
        "y_tick_frequency" : 0.5,
        "x_tick_frequency" : PI/2,
        "graph_origin" : ORIGIN,
        "y_axis_label": None, # Don't write y axis label
        "x_axis_label": None,
    }
    def construct(self):
        self.setup_axes()
        plotSin = self.get_graph(lambda x : np.sin(x),
                                    color = PINK,
                                    x_min=-1.5*np.pi,
                                    x_max=1.5*np.pi,
                                )
        plotCos = self.get_graph(lambda x : np.cos(x),
                                    color = YELLOW,
                                    x_min=-1.5*np.pi,
                                    x_max=1.5*np.pi,
                                )

        #xs_left = [-np.pi, -np.pi/2, 0, np.pi/2, np.pi]
        xs_left = np.arange(-np.pi, np.pi,0.05)
        xs_right = [x_left + np.pi/2 for x_left in xs_left]

        ys = [np.cos(x_left) for x_left in xs_left]

        xys_left = [self.coords_to_point(x_left, y) for x_left, y in zip(xs_left, ys)]
        xys_right = [self.coords_to_point(x_right, y) for x_right, y in zip(xs_right, ys)]

        horizontal_lines = []
        for xy_left, xy_right in zip(xys_left, xys_right):
            horizontal_line = Line(xy_left, xy_right, color=GREEN)
            horizontal_lines.append(horizontal_line)


        equation = TexMobject("\\sin(\\theta)",
                               "=",
                               "\\cos",
                               "(\\theta",
                               "-"
                               "\\frac{\\pi}{2}",
                               ")"
                               )

        equation[0].set_color(PINK)
        equation[2].set_color(YELLOW)
        equation[3].set_color(YELLOW)
        equation[4].set_color(GREEN)
        equation[5].set_color(YELLOW)

        equation.scale(0.75)
        equation.move_to(np.array([3, 3, 0]))

        graph_lab = self.get_graph_label(plotSin, label="\\sin(\\theta)")
        graph_lab2 = self.get_graph_label(plotCos, label="\\cos(\\theta)")


        plotSin.set_stroke(width=3) # width of line
        plotCos.set_stroke(width=2)

        # Animation
        for plot, graph_lab in ((plotSin, graph_lab), (plotCos, graph_lab2)):
            self.play(ShowCreation(plot), run_time = 2)
            self.play(ShowCreation(graph_lab))

        # Display the translation
        for i, horizontal_line in enumerate(horizontal_lines):
            if i==0:
                self.play(ShowCreation(horizontal_line))
                old_line = horizontal_line
            else:
                self.play(ReplacementTransform(old_line, horizontal_line), run_time = 0.025)
                old_line = horizontal_line

        self.play(Write(equation))
        self.wait(4)




    def setup_axes(self):
        def Range(in_val, end_val, step=1):
            return list(np.arange(in_val, end_val + step, step))

        GraphScene.setup_axes(self)

        # Width of edges
        self.x_axis.set_stroke(width=2)
        self.y_axis.set_stroke(width=2)

        # Color of edges
        self.x_axis.set_color(self.axes_color)
        self.y_axis.set_color(self.axes_color)

        # Add x,y labels
        func = TexMobject("f(\\theta)")
        var = TexMobject("\\theta")
        func.set_color(BLUE)
        var.set_color(BLUE)
        func.next_to(self.y_axis, UP)
        var.next_to(self.x_axis, RIGHT+UP)


        # Y labels
        self.y_axis.label_direction = LEFT*1.5
        self.y_axis.add_numbers(*[-1,1])

        #Parameters of x labels
        init_val_x, end_val_x = -3*PI/2, 3*PI/2
        step_x = PI/2

        # List of the positions of x labels
        values_decimal_x=Range(init_val_x,end_val_x,step_x)

        # List of tex objects
        list_x=TexMobject("-\\frac{3\\pi}{2}", #   -3pi/2
                            "-\\pi", #              -pi
                            "-\\frac{\\pi}{2}", #   -pi/2
                            "\\,", #                 0 (space)
                            "\\frac{\\pi}{2}", #     pi/2
                            "\\pi",#                 pi
                            "\\frac{3\\pi}{2}" #     3pi/2
                          )
        #List tuples (position,label)
        values_x = [(i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            x_tex.scale(0.7)
            if x_val == -PI or x_val == PI: #if x is equals -pi or pi
                x_tex.next_to(self.coords_to_point(x_val, 0), 2*DOWN) #Put 2*Down
            else: # In another case
                x_tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(x_tex)

        self.play(
            *[Write(objet)
            for objet in [
                    self.y_axis,
                    self.x_axis,
                    self.x_axis_labels,
                    func,var
                ]
            ],
            run_time=2
        )
