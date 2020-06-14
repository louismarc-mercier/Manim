from big_ol_pile_of_manim_imports import *


class PythagoreanProof(Scene):
    CONFIG = {
        "color_triangle": YELLOW,
        "color_rect_c": RED,
        "color_rect_b": PURPLE,
        "color_rect_a": BLUE,
        "color_square_c": ORANGE,
        "opacidad_triangulos": 0.6,
        "opacidad_cuadradro_a": 0.6,
        "opacidad_cuadradro_b": 0.6,
        "opacidad_cuadradro_c": 0.6,
        "grosor_lineas": 1,
        "l_a": 5 / 5,
        "l_b": 12 / 5,
        "l_c": 13 / 5,
    }

    def construct(self):
        self.pre_square()
        self.pos_square()
        self.transition_squares()

    def pre_square(self):
        cuadro = Square(side_length=self.l_a + self.l_b)
        drawed_coords = []
        for point in [DL, DR, UL, UR]:
            drawed_coords.append(cuadro.get_corner(point))
        dl, dr, ul, ur = drawed_coords

        coords_sides = []
        #               lin 			liz					ls 				   ld
        for point in [dr + LEFT * self.l_b, dl + UP * self.l_b, ul + RIGHT * self.l_b, ur + DOWN * self.l_b]:
            coords_sides.append(point)
        lin, liz, ls, ld = coords_sides


        triangles = []
        triangles_coords = [(lin, dr, ld), (lin, dl, liz), (liz, ul, ls), (ld, ur, ls)]
        for triangle_coords in triangles_coords:
            triangle = Polygon(triangle_coords[0], triangle_coords[1], triangle_coords[2], color=self.color_triangle)\
                .set_fill(self.color_triangle, self.opacidad_triangulos)\
                .set_stroke(None, self.grosor_lineas)
            triangles.append(triangle)


        square_c = Polygon(*coords_sides, color=self.color_square_c).set_fill(self.color_square_c,
                                                                                       self.opacidad_cuadradro_c)

        self.cuadrado_c = square_c

        hor_measure_a = MeasureDistance(Line(dl, lin), invertir=True, dashed=True, buff=-0.25).add_tips()\
            .add_tex("a", buff=-3.7, color=WHITE)
        hor_measure_b = MeasureDistance(Line(lin, dr), invertir=True, dashed=True, buff=-0.25).add_tips()\
            .add_tex("b", buff=-2.7, color=WHITE)
        vert_measure_b = MeasureDistance(Line(dl, liz), invertir=False, dashed=True, buff=0.5).add_tips()\
            .add_tex("b", buff=1, color=WHITE)
        vert_measure_a = MeasureDistance(Line(liz, ul), invertir=False, dashed=True, buff=0.5).add_tips()\
            .add_tex("a", buff=2, color=WHITE)
        vert_measure_a[-1].rotate(-PI / 2)
        vert_measure_b[-1].rotate(-PI / 2)
        mediciones_1 = VGroup(hor_measure_a, hor_measure_b, vert_measure_a, vert_measure_b)

        titulo = TextMobject(r"\sc Preuve: Th\'{e}or\`{e}me de Pythagore.", color=WHITE).to_corner(UL)
        self.titulo = VGroup(titulo)
        self.play(Write(titulo, run_time=1), ShowCreation(cuadro, run_time=1),
                  *[DrawBorderThenFill(triangulo) for triangulo in triangles],
                  *[GrowFromCenter(objeto) for objeto in [*mediciones_1]], run_time=1
                  )

        conjunto_pre_cuadrado = VGroup(cuadro, *triangles)
        self.conjunto_pre_cuadrado = conjunto_pre_cuadrado
        self.conjunto_pre_cuadrado.add(hor_measure_a, hor_measure_b, vert_measure_a, vert_measure_b)
        self.play(conjunto_pre_cuadrado.to_edge, LEFT, {"buff": 1.7})
        square_c.move_to(cuadro)

    def pos_square(self):
        square = Square(side_length=self.l_a + self.l_b)
        coordenadas_esquinas = []
        for punto in [DL, DR, UL, UR]:
            coordenadas_esquinas.append(square.get_corner(punto))
        eii, eid, esi, esd = coordenadas_esquinas

        coords_sides = []
        #               lin 				liz					ls 				   ld
        for punto in [eid + LEFT * self.l_b, eii + UP * self.l_a, esi + RIGHT * self.l_a, esd + DOWN * self.l_b,
                      eii + self.l_a * (UP + RIGHT)]:
            coords_sides.append(punto)
        lin, liz, ls, ld, center = coords_sides
        p_lin, p_liz, p_ls, p_ld = Dot(lin), Dot(liz), Dot(ls), Dot(ld)
        p_center = Dot(center)

        triangles = []
        triangles_coords = [(lin, eid, ld), (lin, center, ld), (esi, liz, center), (center, ls, esi)]
        for triangle_coords in triangles_coords:
            triangle = Polygon(triangle_coords[0], triangle_coords[1], triangle_coords[2], color=self.color_triangle) \
                .set_fill(self.color_triangle, self.opacidad_triangulos) \
                .set_stroke(None, self.grosor_lineas)
            triangles.append(triangle)


        cuadrado_a = Polygon(*[eii, liz, center, lin], color=self.color_rect_a).set_fill(self.color_rect_a,
                                                                                         self.opacidad_cuadradro_a)
        cuadrado_b = Polygon(*[center, ls, esd, ld], color=self.color_rect_b).set_fill(self.color_rect_b,
                                                                                       self.opacidad_cuadradro_b)

        med_ia = MeasureDistance(Line(eii, lin), invertir=True, dashed=True, buff=-0.25).add_tips().add_tex("a", buff=-3.7,
                                                                                                   color=WHITE)
        med_ib = MeasureDistance(Line(lin, eid), invertir=True, dashed=True, buff=-0.25).add_tips().add_tex("b", buff=-2.7,
                                                                                                   color=WHITE)
        med_iza = MeasureDistance(Line(eii, liz), invertir=False, dashed=True, buff=0.5).add_tips().add_tex("a", buff=1.8,
                                                                                                     color=WHITE)
        med_izb = MeasureDistance(Line(liz, esi), invertir=False, dashed=True, buff=0.5).add_tips().add_tex("b", buff=1,
                                                                                                     color=WHITE)
        med_iza[-1].rotate(-PI / 2)
        med_izb[-1].rotate(-PI / 2)
        mediciones_2 = VGroup(med_ia, med_ib, med_iza, med_izb)

        conjunto_pos_cuadrado = VGroup(square, *triangles, cuadrado_a, cuadrado_b, mediciones_2)
        conjunto_pos_cuadrado.to_edge(RIGHT, buff=1.7)
        self.conjunto_pos_cuadrado = conjunto_pos_cuadrado

        self.mediciones_2 = mediciones_2

        self.cuadrado_a = cuadrado_a
        self.cuadrado_b = cuadrado_b


    def transition_squares(self):
        self.play(
            ReplacementTransform(
                self.conjunto_pre_cuadrado[0].copy(), self.conjunto_pos_cuadrado[0],
            ), run_time=1
        )
        self.play(
            *[ReplacementTransform(
                self.conjunto_pre_cuadrado[i].copy(), self.conjunto_pos_cuadrado[i],
            ) for i in range(1, 5)], run_time=1
        )
        self.play(*[GrowFromCenter(objeto) for objeto in [*self.mediciones_2]], run_time=1)
        self.play(DrawBorderThenFill(self.cuadrado_c), DrawBorderThenFill(self.conjunto_pos_cuadrado[-3]),
                  DrawBorderThenFill(self.conjunto_pos_cuadrado[-2]), run_time=1)

        t_a2 = TexMobject("a^2", color=WHITE).move_to(self.cuadrado_a)
        t_b2 = TexMobject("b^2", color=WHITE).move_to(self.cuadrado_b)
        t_c2 = TexMobject("c^2", color=WHITE).move_to(self.cuadrado_c)

        self.play(*[Write(t_) for t_ in [t_a2, t_b2, t_c2]])

        theorem = TexMobject("c^2", "=", "a^2", "+", "b^2").to_edge(DOWN)
        [theorem[2 * i].set_color(theorem_color) for i, theorem_color in enumerate([ORANGE, BLUE, PURPLE])]
        self.play(
            *[ReplacementTransform(
                t_.copy()[:], r_
            ) for t_, r_ in zip([t_a2, t_b2, t_c2], [theorem[2], theorem[-1], theorem[0]])],
            Write(theorem[1]), Write(theorem[-2]), run_time=1
        )
        self.wait()
        self.play(
            self.titulo.shift, UP * 3,
            theorem.shift, DOWN * 3,
            self.conjunto_pos_cuadrado.shift, RIGHT * 7,
            self.conjunto_pre_cuadrado.shift, LEFT * 7,
            VGroup(t_a2, t_b2).shift, RIGHT * 7,
            t_c2.shift, LEFT * 5,
            self.cuadrado_c.shift, LEFT * 7,
        )






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


