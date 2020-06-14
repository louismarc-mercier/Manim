from big_ol_pile_of_manim_imports import *



class MeasuredIdentity(Scene):
    CONFIG = {
        "color_triangle": YELLOW,
        "color_rect_c": RED,
        "color_rect_b": PURPLE,
        "color_rect_a": BLUE,
        "color_square_c": ORANGE,
        "opacity_triangles": 0.6,
        "opacity_square_a": 0.6,
        "opacity_square_b": 0.6,
        "opacity_square_c": 0.6,
        "line_width": 1,
        "l_a": 5 / 5,
        "l_b": 12 / 5,
        "l_c": 13 / 5,
    }

    def construct(self):
        self.pre_square()
        self.pos_square()
        self.transition_squares()

    def pre_square(self):
        square = Square(side_length=self.l_a + self.l_b, fill_opacity=0.5, color=ORANGE)
        drawed_coords = []
        for point in [DL, DR, UL, UR]:
            drawed_coords.append(square.get_corner(point))
        dl, dr, ul, ur = drawed_coords

        coords_sides = []
        for point in [dr + LEFT * self.l_b, dl + UP * self.l_a, ul + RIGHT * self.l_a, ur + DOWN * self.l_b]:
            coords_sides.append(point)
        lin, liz, ls, ld = coords_sides

        vert_measure = MeasureDistance(Line(dl, dr), invertir=True, dashed=True, buff=-0.25).add_tips()\
            .add_tex("a+b", buff=-3.7, color=WHITE)
        hor_measure = MeasureDistance(Line(dl, ul), invertir=False, dashed=True, buff=0.5).add_tips()\
            .add_tex("a+b", buff=2, color=WHITE)
        measures_1 = VGroup(hor_measure, vert_measure)


        title = TextMobject(r"\sc Preuve: Identit\'{e} remarquable $(a+b)^{2}=a^2+b^2+2ab$", color=WHITE).to_corner(UL)
        self.title = VGroup(title)
        self.play(Write(title, run_time=1), ShowCreation(square, run_time=1),
                  *[GrowFromCenter(object) for object in [*measures_1]], run_time=1
                  )


        joint_pre_square = VGroup(square)
        self.joint_pre_square = square
        self.joint_pre_square.add(hor_measure, vert_measure)
        self.play(joint_pre_square.to_edge, LEFT, {"buff": 1.7})
        self.square = square


    def pos_square(self):

        square = Square(side_length=self.l_a + self.l_b)
        drawed_coords = []
        for point in [DL, DR, UL, UR]:
            drawed_coords.append(square.get_corner(point))
        dl, dr, ul, ur = drawed_coords


        coords_sides = []
        for point in [dr + LEFT * self.l_b, dl + UP * self.l_a, ul + RIGHT * self.l_a, ur + DOWN * self.l_b]:
            coords_sides.append(point)
        lin, liz, ls, ld = coords_sides
        center_point = lin + UP * self.l_a


        rectangles = []
        rectangles_coords = [(ld, dr, lin, center_point), (lin, dl, liz, center_point), (liz, ul, ls, center_point),
                             (ls, ur, ld, center_point)]
        rectangles_colors = [GREEN, PURPLE, GREEN, BLUE]
        for rectangle_coords, rectangle_color in zip(rectangles_coords, rectangles_colors):
            rectangle = Polygon(rectangle_coords[0], rectangle_coords[1], rectangle_coords[2], rectangle_coords[3],
                                color=WHITE).set_fill(rectangle_color, self.opacity_triangles) \
                .set_stroke(None, self.line_width)
            rectangles.append(rectangle)


        hor_measure_a = MeasureDistance(Line(dl, lin), invertir=True, dashed=True, buff=-0.25).add_tips() \
            .add_tex("a", buff=-3.7, color=WHITE)
        hor_measure_b = MeasureDistance(Line(lin, dr), invertir=True, dashed=True, buff=-0.25).add_tips() \
            .add_tex("b", buff=-2.7, color=WHITE)
        vert_measure_b = MeasureDistance(Line(dl, liz), invertir=False, dashed=True, buff=0.5).add_tips() \
            .add_tex("a", buff=2, color=WHITE)
        vert_measure_a = MeasureDistance(Line(liz, ul), invertir=False, dashed=True, buff=0.5).add_tips() \
            .add_tex("b", buff=1, color=WHITE)
        vert_measure_a[-1].rotate(-PI / 2)
        vert_measure_b[-1].rotate(-PI / 2)
        measures_2 = VGroup(hor_measure_a, hor_measure_b, vert_measure_a, vert_measure_b)

        joint_pos_squares = VGroup(square, *rectangles, measures_2)
        joint_pos_squares.to_edge(RIGHT, buff=1.7)
        self.joint_pos_squares = joint_pos_squares

        self.measures_2 = measures_2

        self.rectangles = rectangles
        self.rect_ba = rectangles[0]
        self.square_a2 = rectangles[1]
        self.rect_ab = rectangles[2]
        self.square_b2 = rectangles[3]



    def transition_squares(self):

        self.play(*[GrowFromCenter(object) for object in [*self.measures_2]], run_time=1)
        self.play(DrawBorderThenFill(self.square_a2), DrawBorderThenFill(self.square_b2),
                  DrawBorderThenFill(self.rect_ba), DrawBorderThenFill(self.rect_ab),
                  run_time=1)

        #t_ab2 = TexMobject("(a+b)^2", color=WHITE).move_to(self.square)
        t_ab2 = TexMobject("(a+b)^2", color=WHITE).next_to(np.array([-3.5,0,0]))
        t_a2 = TexMobject("a^2", color=WHITE).move_to(self.square_a2)
        t_b2 = TexMobject("b^2", color=WHITE).move_to(self.square_b2)
        t_ab = TexMobject("ab", color=WHITE).move_to(self.rect_ab)
        t_ba = TexMobject("ba", color=WHITE).move_to(self.rect_ba)


        self.play(*[Write(t_) for t_ in [t_ab2, t_a2, t_b2, t_ab, t_ba]])

        theorem = TexMobject("(a+b)^2", "=", "a^2", "+", "b^2", "+", "2ab").to_edge(DOWN)
        [theorem[2 * i].set_color(theorem_color) for i, theorem_color in enumerate([ORANGE, PURPLE, BLUE, GREEN])]
        self.play(
            *[ReplacementTransform(
                t_.copy()[:], r_
            ) for t_, r_ in zip([t_ab2, t_a2, t_b2, t_ab, t_ba],
                                [theorem[0], theorem[2], theorem[4], theorem[6], theorem[6]])],
            Write(theorem[1]), Write(theorem[3]), Write(theorem[5]), run_time=2.5
        )
        self.wait()
        self.play(
            self.title.shift, UP * 3,
            theorem.shift, DOWN * 3,
            t_ab2.shift, LEFT * 7,
            self.joint_pre_square.shift, LEFT * 7,
            VGroup(t_a2, t_b2, t_ab, t_ba).shift, RIGHT * 7,
            VGroup(*self.rectangles).shift, RIGHT * 7,
            self.measures_2.shift, RIGHT * 7
        )



class Ab_sqrt_proof(Scene):
    CONFIG = {
        "square_scale": 2,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):

        # Define two squares (one yellow and one white, opacity allows to fill color in figure).
        left_square, right_square = Square(fill_opacity=0.5, color=ORANGE), Square()

        # Put the two squares next to another.
        VGroup(left_square, right_square)\
                .scale(self.square_scale)\
                .arrange_submobjects(RIGHT,buff=2)


        # RIGHT SQUARE SETTINGS
        ## Configure dots to draw triangles inside right square.
        dots2 = [right_square.point_from_proportion(i * 1 / 4 + j * 1 / 16) for i, j in zip(range(4), [1, 3, 3, 1])]
        dots_corners2 = [right_square.point_from_proportion(i * 1 / 4) for i in range(4)]
        middle = np.array([dots2[0][0], dots2[1][1], 0])


        def get_color(i):
            if i == 0 or i == 2:
                return GREEN
            elif i == 1:
                return BLUE
            else:
                return PURPLE


        # Generate the rectangles and squares in which to place the triangles.
        all_rectangles = VGroup(*[Polygon(dots_corners2[i], dots2[i], middle, dots2[i - 1],
                fill_opacity=0.7, color=get_color(i)) for i in range(4)])
        rectangles = all_rectangles[0::2]   # Rectangles: rectangles of the triangles
        squares = all_rectangles[1::2]      # Big and small squares

        # Generate the title
        Title = TextMobject(r"\underline{Preuve de l'identit\'e remarquable $(a+b)^{2}=a^{2}+b^{2}+2ab$}")
        Title.to_edge(UP + LEFT)

        # Latex formula (located at the bottom of screen).
        theorem_colors = [ORANGE, BLUE, PURPLE, GREEN]
        theorem = TexMobject("(a+b)^2", "=", "a^2", "+", "b^2", "+", "2ab").to_edge(DOWN)
        [theorem[2*i].set_color(theorem_color) for i, theorem_color in enumerate(theorem_colors)]

        # Create tex formula expressions to the new locations (in the Figure (for visualization))
        parts_theorem = VGroup(
            TexMobject("(a+b)^2").move_to(left_square),
            TexMobject("a^2").move_to(squares[0]),
            TexMobject("b^2").move_to(squares[1]),
            TexMobject("ab").move_to(rectangles[0]),
            TexMobject("ba").move_to(rectangles[1])
        )

        # Display title
        self.play(Write(Title))

        # Draw borders of the squares and fill them (if opacity is defined).
        self.play(*list(map(DrawBorderThenFill, [left_square, right_square])))

        # Display the left square, the small right squares and the expressions of the theorem (in small squares).
        self.play(ShowCreation(squares), ShowCreation(rectangles), Write(parts_theorem))

        # Replace the elements of the bottom formula by the colored one associated to the figure.
        self.play(*[ReplacementTransform(t_.copy()[:], r_, run_time=4)
                for t_, r_ in zip(parts_theorem, [theorem[0], theorem[2], theorem[4], theorem[6], theorem[6]])],
            Write(theorem[1]), Write(theorem[3]), Write(theorem[5])
        )
        self.wait(3)



class MeasureObject1(Scene):
    def construct(self):
        square=Square()
        measure_line=Line(square.get_corner(DL),square.get_corner(UL))
        # MeasureDistance: my_objects.py - line 143
        measure=MeasureDistance(measure_line).add_tips()
        measure_tex=measure.get_tex("x")
        self.add(square,measure,measure_tex)
        self.wait(2)


class MeasureDistance(VGroup):
    CONFIG = {
        "color": RED_B,
        "buff": 0.3,
        "lateral": 0.3,
        "invert": False,
        "dashed_segment_length": 0.09,
        "dashed": True,
        "ang_arrows": 30 * DEGREES,
        "size_arrows": 0.2,
        "stroke": 2.4,
    }

    def __init__(self, mob, **kwargs):
        VGroup.__init__(self, **kwargs)
        if self.dashed == True:
            medicion = DashedLine(ORIGIN, mob.get_length() * RIGHT,
                                  dashed_segment_length=self.dashed_segment_length).set_color(self.color)
        else:
            medicion = Line(ORIGIN, mob.get_length() * RIGHT)

        medicion.set_stroke(None, self.stroke)

        pre_medicion = Line(ORIGIN, self.lateral * RIGHT).rotate(PI / 2).set_stroke(None, self.stroke)
        pos_medicion = pre_medicion.copy()

        pre_medicion.move_to(medicion.get_start())
        pos_medicion.move_to(medicion.get_end())

        angulo = mob.get_angle()
        matriz_rotacion = rotation_matrix(PI / 2, OUT)
        vector_unitario = mob.get_unit_vector()
        direccion = np.matmul(matriz_rotacion, vector_unitario)
        self.direccion = direccion

        self.add(medicion, pre_medicion, pos_medicion)
        self.rotate(angulo)
        self.move_to(mob)

        if self.invert == True:
            self.shift(-direccion * self.buff)
        else:
            self.shift(direccion * self.buff)
        self.set_color(self.color)
        self.tip_point_index = -np.argmin(self.get_all_points()[-1, :])

    def add_tips(self):
        linea_referencia = Line(self[0][0].get_start(), self[0][-1].get_end())
        vector_unitario = linea_referencia.get_unit_vector()

        punto_final1 = self[0][-1].get_end()
        punto_inicial1 = punto_final1 - vector_unitario * self.size_arrows

        punto_inicial2 = self[0][0].get_start()
        punto_final2 = punto_inicial2 + vector_unitario * self.size_arrows

        lin1_1 = Line(punto_inicial1, punto_final1).set_color(self[0].get_color()).set_stroke(None, self.stroke)
        lin1_2 = lin1_1.copy()
        lin2_1 = Line(punto_inicial2, punto_final2).set_color(self[0].get_color()).set_stroke(None, self.stroke)
        lin2_2 = lin2_1.copy()

        lin1_1.rotate(self.ang_arrows, about_point=punto_final1, about_edge=punto_final1)
        lin1_2.rotate(-self.ang_arrows, about_point=punto_final1, about_edge=punto_final1)

        lin2_1.rotate(self.ang_arrows, about_point=punto_inicial2, about_edge=punto_inicial2)
        lin2_2.rotate(-self.ang_arrows, about_point=punto_inicial2, about_edge=punto_inicial2)

        return self.add(lin1_1, lin1_2, lin2_1, lin2_2)

    def add_tex(self, text, scale=1, buff=-1, **moreargs):
        linea_referencia = Line(self[0][0].get_start(), self[0][-1].get_end())
        texto = TexMobject(text, **moreargs)
        ancho = texto.get_height() / 2
        texto.rotate(linea_referencia.get_angle()).scale(scale).move_to(self)
        texto.shift(self.direccion * (buff + 1) * ancho)
        return self.add(texto)

    def add_text(self, text, scale=1, buff=0.1, **moreargs):
        linea_referencia = Line(self[0][0].get_start(), self[0][-1].get_end())
        texto = TextMobject(text, **moreargs)
        ancho = texto.get_height() / 2
        texto.rotate(linea_referencia.get_angle()).scale(scale).move_to(self)
        texto.shift(self.direccion * (buff + 1) * ancho)
        return self.add(texto)

    def add_size(self, text, scale=1, buff=0.1, **moreargs):
        linea_referencia = Line(self[0][0].get_start(), self[0][-1].get_end())
        texto = TextMobject(text, **moreargs)
        ancho = texto.get_height() / 2
        texto.rotate(linea_referencia.get_angle())
        texto.shift(self.direccion * (buff + 1) * ancho)
        return self.add(texto)

    def add_letter(self, text, scale=1, buff=0.1, **moreargs):
        linea_referencia = Line(self[0][0].get_start(), self[0][-1].get_end())
        texto = TexMobject(text, **moreargs).scale(scale).move_to(self)
        ancho = texto.get_height() / 2
        texto.shift(self.direccion * (buff + 1) * ancho)
        return self.add(texto)

    def get_text(self, text, scale=1, buff=0.1, invert_dir=False, invert_texto=False, remove_rot=False, **moreargs):
        linea_referencia = Line(self[0][0].get_start(), self[0][-1].get_end())
        texto = TextMobject(text, **moreargs)
        ancho = texto.get_height() / 2
        if invert_texto:
            inv = PI
        else:
            inv = 0
        if remove_rot:
            texto.scale(scale).move_to(self)
        else:
            texto.rotate(linea_referencia.get_angle()).scale(scale).move_to(self)
            texto.rotate(inv)
        if invert_dir:
            inv = -1
        else:
            inv = 1
        texto.shift(self.direccion * (buff + 1) * ancho * inv)
        return texto

    def get_tex(self, tex, scale=1, buff=1, invert_dir=False, invert_texto=False, remove_rot=True, **moreargs):
        linea_referencia = Line(self[0][0].get_start(), self[0][-1].get_end())
        texto = TexMobject(tex, **moreargs)
        ancho = texto.get_height() / 2
        if invert_texto:
            inv = PI
        else:
            inv = 0
        if remove_rot:
            texto.scale(scale).move_to(self)
        else:
            texto.rotate(linea_referencia.get_angle()).scale(scale).move_to(self)
            texto.rotate(inv)
        if invert_dir:
            inv = -1
        else:
            inv = 1
        texto.shift(self.direccion * (buff + 1) * ancho)
        return texto