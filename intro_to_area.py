from manimlib.imports import *
from scipy.special import factorial

# TODO: SCENE ORDER

# 0. AreaThumbnail
# 1. AreaDefinition
# 2. Applications
# 3. AreaProperties
# 4. ShrinkSquare (P1)
# 5. UnitSquare (P2)
# 6. SquareDecompositionP3 (P3)
# 7. TranslateRectangle (P4)
# 8. RotateRectangle (P4)
# 9. Conclusion
# 10. Credits

# Version: May 20th 2020


class AreaThumbnail(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        line1 = TextMobject("Géométrie Euclidienne").shift(2.25 * UP).set_color(BLUE)
        line2 = TextMobject(r"Aire d'une surface").scale(2).next_to(line1, DOWN).set_color(BLUE)
        #prob = TexMobject(r"\text{Find }T_n=A_n+B_n").scale(2).shift(2 * DOWN)
        self.play(Write(line1), Write(line2))
        self.wait()

        # Define two squares (one yellow and one white, opacity allows to fill color in figure).
        left_square, right_square = Square(fill_opacity=0.5, color=PINK), Square()

        # Put the two squares next to another.
        VGroup(left_square, right_square) \
            .scale(self.square_scale) \
            .arrange_submobjects(RIGHT, buff=2).next_to(1.5*DOWN + 3*LEFT)

        self.play(*list(map(DrawBorderThenFill, [right_square, left_square])))
        self.wait(5)


class AreaDefinition(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Définition}", color=WHITE).to_corner(UL)
        definition = TextMobject(r"L’aire est la surface occupée par un objet sur un plan de deux dimensions. L’aire se calcule en unités carrées.")
        definition.scale(0.7)
        definition.move_to(np.array([-1, 1, 0]))
        definition.set_color(BLUE)
        #definition.to_edge(UP)

        self.play(Write(title))
        self.wait(3)
        self.play(FadeIn(definition))

        # Define two squares (one yellow and one white, opacity allows to fill color in figure).
        left_square, right_square = Square(fill_opacity=0.5, color=PINK), Square()

        # Put the two squares next to another.
        VGroup(left_square, right_square) \
            .scale(self.square_scale) \
            .arrange_submobjects(RIGHT, buff=2).next_to(1.5 * DOWN + 3 * LEFT)

        self.play(*list(map(DrawBorderThenFill, [right_square, left_square])))
        self.wait(5)


class Conclusion(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc À retenir}", color=WHITE).to_corner(UL)

        compl_rules_str = [
            "",
            "L’aire est la surface occupée par un objet sur un plan de deux dimensions.",
            "L’aire se calcule en unités carrées.",
            "Les propriétés de l'aire. ",
        ]

        rules = [TextMobject("{}) {}".format(i, rule)) for i, rule in enumerate(compl_rules_str)]
        rules = [rule.scale(0.7) for rule in rules]

        for (i, rule) in enumerate(rules):
            if i != 0:
                rule.next_to(rules[0].get_center() - rule.get_center() + np.array([-6, -0.7 * i, 0]))
        rules = VGroup(*rules)
        rules.to_corner(LEFT + UP)

        self.play(Write(title))
        self.wait(3)
        self.play(Write(rules[1]))
        self.wait(3)
        self.play(Write(rules[2]))
        self.wait(3)
        self.play(Write(rules[3]))
        self.wait(3)



class Applications(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\sc Applications concrètes}", color=WHITE).to_corner(UL)

        compl_rules_str = [
            "",
            "Acheter des vitres (prix au centimètre carré).",
            "Peinturer (prix au litre de peinture).",
            "Installer de la tourbe (gazon) sur un terrain.",
        ]

        rules = [TextMobject("{}) {}".format(i, rule)) for i, rule in enumerate(compl_rules_str)]

        for (i, rule) in enumerate(rules):
            if i!=0:
                rule.next_to(rules[0].get_center() - rule.get_center() + np.array([-6, -0.7 * i, 0]))
        rules = VGroup(*rules)
        rules.to_corner(LEFT+UP)

        path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/images/"
        image_peinture = ImageMobject(path + "peinture")
        image_peinture.scale(1.25)
        image_peinture.to_edge(LEFT + DOWN)

        image_tourbe = ImageMobject(path + "tourbe")
        image_tourbe.scale(1.25)
        image_tourbe.to_edge(RIGHT + DOWN)

        self.play(Write(title))
        self.wait(3)
        self.play(Write(rules[1]))
        self.wait(3)
        self.play(Write(rules[2]))
        self.play(FadeIn(image_peinture))
        self.wait(3)
        self.play(Write(rules[3]))
        self.play(FadeIn(image_tourbe))
        self.wait(3)

        self.play(FadeOut(image_peinture))


class AreaProperties(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\sc Propriétés de l'aire}", color=WHITE).to_corner(UL)

        compl_rules_str = [
            "",
            "L'aire d'une surface plane bornée est un nombre positif ou nul.",
            "Une unité de longueur étant choisie, l'aire du carré de côté 1 est égale à 1.",
            "L'aire est additive.",
            "L'aire est invariante aux déplacements et aux rotations."
        ]

        rules = [TextMobject("P{}) {}".format(i, rule)) for i, rule in enumerate(compl_rules_str)]
        rules = [rule.scale(0.7) for rule in rules]

        for (i, rule) in enumerate(rules):
            if i!=0:
                rule.next_to(rules[0].get_center() - rule.get_center() + np.array([-6, -0.7 * i, 0]))
        rules = VGroup(*rules)
        rules.to_corner(LEFT+UP)


        self.play(Write(title))
        self.wait(3)
        self.play(Write(rules[1]))
        self.wait(3)
        self.play(Write(rules[2]))
        self.wait(3)
        self.play(Write(rules[3]))
        self.wait(3)
        self.play(Write(rules[4]))
        self.wait(3)




class SquareDecompositionP3(Scene):
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
        #lin, liz, ls, ld = coords_sides

        vert_measure = MeasureDistance(Line(dl, dr), invertir=True, dashed=True, buff=-0.25).add_tips()\
            .add_tex("3", buff=-3.7, color=WHITE)
        hor_measure = MeasureDistance(Line(dl, ul), invertir=False, dashed=True, buff=0.5).add_tips()\
            .add_tex("3", buff=2, color=WHITE)
        measures_1 = VGroup(hor_measure, vert_measure)


        title = TextMobject(r"\sc Example (P3): Additivité de l'aire (carré, $c=3$)", color=WHITE).to_corner(UL)
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

        square_length = self.l_a + self.l_b
        coords_sides = []
        for point in [dr + (LEFT * square_length / 3), dr + (LEFT * 2 * square_length / 3),
                      dl + (UP * square_length / 3), dl + (UP * 2 * square_length / 3),
                      ul + (RIGHT * square_length / 3), ul + (RIGHT * 2 * square_length / 3),
                      ur + (DOWN * square_length / 3), ur + (DOWN * 2 * square_length / 3)]:
            coords_sides.append(point)
        #for point in [dr + LEFT * self.l_b, dl + UP * self.l_a, ul + RIGHT * self.l_a, ur + DOWN * self.l_b]:
        #    coords_sides.append(point)
        DR_l1, DR_l2, DL_u1, DL_u2, UL_r1, UL_r2, UR_d1, UR_d2  = coords_sides



        rectangles = []
        rectangles_coords = [(dr, dl, DL_u1, UR_d2), (UR_d2, DL_u1, DL_u2, UR_d1), (UR_d1, DL_u2, ul, ur)]
        rectangles_colors = [ORANGE, ORANGE, ORANGE]

        for rectangle_coords, rectangle_color in zip(rectangles_coords, rectangles_colors):
            rectangle = Polygon(rectangle_coords[0], rectangle_coords[1], rectangle_coords[2], rectangle_coords[3],
                                color=WHITE).set_fill(rectangle_color, self.opacity_triangles) \
                .set_stroke(None, self.line_width)
            rectangles.append(rectangle)


        overlapping_rectangle = Polygon(DR_l1, DR_l2, UL_r1, UL_r2, color=WHITE).set_stroke(None, self.line_width)
        rectangles.append(overlapping_rectangle)


        hor_measure_a = MeasureDistance(Line(dr, DR_l1), invertir=True, dashed=True, buff=0.25).add_tips() \
            .add_tex("1", buff=3, color=WHITE)
        hor_measure_b = MeasureDistance(Line(DR_l1, DR_l2), invertir=True, dashed=True, buff=0.25).add_tips() \
            .add_tex("1", buff=3, color=WHITE)
        hor_measure_c = MeasureDistance(Line(DR_l2, dl), invertir=True, dashed=True, buff=0.25).add_tips() \
            .add_tex("1", buff=3, color=WHITE)


        vert_measure_a = MeasureDistance(Line(dl, DL_u1), invertir=False, dashed=True, buff=0.25).add_tips() \
            .add_tex("1", buff=2, color=WHITE)
        vert_measure_b = MeasureDistance(Line(DL_u1, DL_u2), invertir=False, dashed=True, buff=0.25).add_tips() \
            .add_tex("1", buff=2, color=WHITE)
        vert_measure_c = MeasureDistance(Line(DL_u2, ul), invertir=False, dashed=True, buff=0.25).add_tips() \
            .add_tex("1", buff=1, color=WHITE)
        hor_measure_a[-1].rotate(-PI)
        hor_measure_b[-1].rotate(-PI)
        hor_measure_c[-1].rotate(-PI)
        measures_2 = VGroup(hor_measure_a, hor_measure_b, hor_measure_c, vert_measure_a, vert_measure_b, vert_measure_c)

        joint_pos_squares = VGroup(square, *rectangles, measures_2)
        #joint_pos_squares = VGroup(square, *rectangles)
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

        self.wait()
        self.play(
            self.title.shift, UP * 3,
            self.joint_pre_square.shift, LEFT * 7,
            VGroup(*self.rectangles).shift, RIGHT * 7,
            self.measures_2.shift, RIGHT * 7
        )


class ExampleSquareArea(Scene):
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

    def pre_square(self):
        square = Square(side_length=self.l_a + self.l_b, fill_opacity=0.25, color=BLUE)
        drawed_coords = []
        for point in [DL, DR, UL, UR]:
            drawed_coords.append(square.get_corner(point))
        dl, dr, ul, ur = drawed_coords

        coords_sides = []
        for point in [dr + LEFT * self.l_b, dl + UP * self.l_a, ul + RIGHT * self.l_a, ur + DOWN * self.l_b]:
            coords_sides.append(point)
        lin, liz, ls, ld = coords_sides

        vert_measure = MeasureDistance(Line(dl, dr), invertir=True, dashed=True, buff=-0.25).add_tips()\
            .add_tex("3\\text{ unités}", buff=-3.7, color=WHITE)
        hor_measure = MeasureDistance(Line(dl, ul), invertir=False, dashed=True, buff=0.5).add_tips()\
            .add_tex("3\\text{ unité}", buff=2, color=WHITE)
        measures_1 = VGroup(hor_measure, vert_measure)


        title = TextMobject(r"\sc Example: Carré", color=WHITE).to_corner(UL)
        self.title = VGroup(title)
        self.play(Write(title, run_time=1), ShowCreation(square, run_time=1),
                  *[GrowFromCenter(object) for object in [*measures_1]], run_time=1
                  )
        self.wait()

        joint_square = VGroup(square)
        self.unit_square = square
        self.unit_square.add(hor_measure, vert_measure)
        self.play(joint_square.to_edge, LEFT, {"buff": 1.7})


        line1 = TextMobject(r"Aire","=","$3\\text{ unité} \\times 3\\text{ unité}$","=","$9\\text{ unité}^{2}$").\
            scale(0.75).move_to(2.5*RIGHT+1.2*UP).set_color(BLUE)
        self.play(Write(line1))
        self.wait()



class UnitSquare(Scene):
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
            .add_tex("1\\text{ unité}", buff=-3.7, color=WHITE)
        hor_measure = MeasureDistance(Line(dl, ul), invertir=False, dashed=True, buff=0.5).add_tips()\
            .add_tex("1\\text{ unité}", buff=2, color=WHITE)
        measures_1 = VGroup(hor_measure, vert_measure)


        title = TextMobject(r"\sc P2) Figure de base: Carré unité", color=WHITE).to_corner(UL)
        self.title = VGroup(title)
        self.play(Write(title, run_time=1), ShowCreation(square, run_time=1),
                  *[GrowFromCenter(object) for object in [*measures_1]], run_time=1
                  )
        self.wait()

        joint_square = VGroup(square)
        self.unit_square = square
        self.unit_square.add(hor_measure, vert_measure)
        self.play(joint_square.to_edge, LEFT, {"buff": 1.7})


        line1 = TextMobject(r"Aire","=","$1\\text{ unité}^{2}$").\
            scale(0.75).move_to(2.5*RIGHT+1.2*UP).set_color(ORANGE)
        self.play(Write(line1))
        self.wait()


class RotateSquare(Scene):
    def construct(self):
        #circle = Circle()
        title = TextMobject(r"\sc Exemple (P4): Invariance aux rotations (carré)", color=WHITE).to_corner(UL)
        circle = Square()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.set_fill(PINK, opacity=0.5)
        #square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)

        self.play(Write(title))
        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class RotateRectangle(Scene):
    def construct(self):
        title = TextMobject(r"\sc Exemple (P4): Invariance aux rotations ", color=WHITE).to_corner(UL)
        initial_rectangle = Rectangle()
        initial_rectangle.set_fill(PINK, opacity=0.5)

        rotated_rectangles = []
        for i in range(8):
            rotated_rectangle = Rectangle()
            rotated_rectangle.set_fill(PINK, opacity=0.5)
            rotated_rectangle.rotate(-3 * (i+1) * PI / 16)
            rotated_rectangles.append(rotated_rectangle)

        self.play(Write(title))
        self.play(ShowCreation(initial_rectangle))
        current_rectangle = initial_rectangle
        for rotated_rectangle in rotated_rectangles:
            self.play(Transform(current_rectangle, rotated_rectangle))
            self.wait(0.5)
            self.play(FadeOut(current_rectangle),run_time=0.05)
            current_rectangle = rotated_rectangle


class TranslateRectangle(Scene):
    def construct(self):
        title = TextMobject(r"\sc Exemple (P5): Invariance aux translations", color=WHITE).to_corner(UL)
        title.scale(0.95)
        initial_rectangle = Rectangle()
        initial_rectangle.next_to(5*LEFT)
        initial_rectangle.set_fill(PINK, opacity=0.5)

        translated_rectangles = []
        for i in range(10):
            translated_rectangle = Rectangle()
            translated_rectangle.set_fill(PINK, opacity=0.5)
            translated_rectangle.shift(5*LEFT + RIGHT*(i+1))
            translated_rectangles.append(translated_rectangle)

        self.play(Write(title))
        self.play(ShowCreation(initial_rectangle))
        current_rectangle = initial_rectangle
        for translated_rectangle in translated_rectangles:
            self.play(Transform(current_rectangle, translated_rectangle))
            self.wait(0.5)
            self.play(FadeOut(current_rectangle),run_time=0.05)
            current_rectangle = translated_rectangle


class ShrinkSquare(Scene):
    def construct(self):
        title = TextMobject(r"\sc Exemple (P1): Aire positive ou nulle (carré, $c>0$)", color=WHITE).to_corner(UL)
        initial_square = Square(side_length=2)
        #initial_square.next_to(5*LEFT)
        initial_square.set_fill(PINK, opacity=0.5)

        shrinked_squares = []
        for i in range(10):
            shrinked_square = Square(side_length=2/(i+1))
            shrinked_square.set_fill(PINK, opacity=0.5)
            #translated_rectangle.shift(5*LEFT + RIGHT*(i+1))
            shrinked_squares.append(shrinked_square)

        self.play(Write(title))
        self.play(ShowCreation(initial_square))
        current_rectangle = initial_square
        for shrinked_square in shrinked_squares:
            self.play(Transform(current_rectangle, shrinked_square))
            self.wait(0.5)
            self.play(FadeOut(current_rectangle),run_time=0.05)
            current_rectangle = shrinked_square




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


class CreditsDirectors(Scene):
    def wplay(self, *args, wait=1, run_time=1, rate_func=smooth):
        self.play(*args, run_time=run_time, rate_func=rate_func)
        if wait != 0:
            self.wait(wait)

    def construct(self):
        credits = TextMobject("Crédits").set_color(YELLOW).scale(1.7)
        thanks = TextMobject("Merci pour votre visionnement!").set_color(BLUE).scale(1.7)

        director1 = TexMobject(r"\text{Support moral}", r"\text{Bill Gates}")
        director2 = TexMobject(r"\text{Elon Musk}")
        instructor = TexMobject(r"\text{Enseignant}", r"\text{Louis-Marc Mercier}")
        viewer = TexMobject(r"\text{Spectacteur}", r"\text{Vous}")
        lines = [director1, director2, instructor, viewer]

        director1[0].align_to([-0.5, 0, 0], RIGHT).shift(8 * DOWN)
        director1[1].align_to([0.5, 0, 0], LEFT).shift(8 * DOWN)
        director2.next_to(director1, DOWN, buff=MED_SMALL_BUFF).align_to(director1[1], LEFT)
        instructor[0].next_to(director2, DOWN, buff=LARGE_BUFF).align_to(director1[0], RIGHT)
        instructor[1].next_to(director2, DOWN, buff=LARGE_BUFF).align_to(director1[1], LEFT)
        viewer[0].next_to(instructor, DOWN, buff=LARGE_BUFF).align_to(director1[0], RIGHT)
        viewer[1].next_to(instructor, DOWN, buff=LARGE_BUFF).align_to(director1[1], LEFT)

        credits.set_y(director1.get_top()[1] + 2 * LARGE_BUFF)
        thanks.set_y(-14.5)

        def half_start(t):
            # this rate function is great for gradually starting into a `linear` rate
            # it goes from 0 to 0.5 in value, and from 0 to 1 in slope (speed)
            return 1 / 2 * t ** 2

        everything_no_thanks = VGroup(credits, *lines)

        self.play(VGroup(*everything_no_thanks, thanks).shift, UP, rate_func=half_start)
        self.play(VGroup(*everything_no_thanks, thanks).shift, 14 * UP, rate_func=linear, run_time=14)
        self.play(everything_no_thanks.shift, 3 * UP, rate_func=linear, run_time=3)
        self.remove(*everything_no_thanks)
        self.wait(3)

        # all done :)
        self.wplay(FadeOut(thanks))


class Credits(Scene):
    def wplay(self, *args, wait=1, run_time=1, rate_func=smooth):
        self.play(*args, run_time=run_time, rate_func=rate_func)
        if wait != 0:
            self.wait(wait)

    def construct(self):
        credits = TextMobject("Crédits").set_color(YELLOW).scale(1.7)
        thanks = TextMobject("Merci pour votre visionnement!").set_color(ORANGE).scale(1.7)

        instructor = TexMobject(r"\text{Enseignant}", r"\text{Louis-Marc Mercier}")
        viewer = TexMobject(r"\text{Spectacteur}", r"\text{Vous}")
        lines = [instructor, viewer]

        instructor[0].align_to([-0.5, 0, 0], RIGHT).shift(8 * DOWN)
        instructor[1].align_to([0.5, 0, 0], LEFT).shift(8 * DOWN)

        viewer[0].next_to(instructor, DOWN, buff=LARGE_BUFF).align_to(instructor[0], RIGHT)
        viewer[1].next_to(instructor, DOWN, buff=LARGE_BUFF).align_to(instructor[1], LEFT)

        credits.set_y(instructor.get_top()[1] + 2 * LARGE_BUFF)
        thanks.set_y(-14.5)

        def half_start(t):
            # this rate function is great for gradually starting into a `linear` rate
            # it goes from 0 to 0.5 in value, and from 0 to 1 in slope (speed)
            return 1 / 2 * t ** 2

        everything_no_thanks = VGroup(credits, *lines)

        self.play(VGroup(*everything_no_thanks, thanks).shift, UP, rate_func=half_start)
        self.play(VGroup(*everything_no_thanks, thanks).shift, 14 * UP, rate_func=linear, run_time=14)
        self.play(everything_no_thanks.shift, 3 * UP, rate_func=linear, run_time=3)
        self.remove(*everything_no_thanks)
        self.wait(3)

        # all done :)
        self.wplay(FadeOut(thanks))
