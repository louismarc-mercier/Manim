from manimlib.imports import *


# 0. Thumbnail
# 1. Menu
# 2. Applications
# 3. Application_reg (regression polynomiale)
# 4. ExposantDef
# 5. CasParticuliers
# 6. ExtensionExpNegatifs
# 7. Proprietes
# 8. Exemples
# 9. Solutions
# 8. Conclusion (TO-DO)


color_map = {
    r"{a}": BLUE,
    r"{b}": YELLOW,
}

class ThumbnailFrench(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        line_e = TextMobject(r"\sc{Comment}", r"\sc{es-tu}", r"\sc{toujours}", r"\sc{positif?}").scale(2.5).shift(2.25 * UP + 4 * LEFT).set_color(PINK)
        line_e[0].next_to(3 * UP + 7 * LEFT)
        line_e[1].next_to(2 * UP + 7 * LEFT)
        line_e[2].next_to(1 * UP + 7 * LEFT)
        line_e[3].next_to(0 * UP + 7 * LEFT)
        line_pi = TextMobject(r"{\sc C'est dans }", r"{\sc ma nature!}").scale(2.5).set_color(YELLOW)
        line_pi[0].next_to(3 * UP + 0 * LEFT)
        line_pi[1].next_to(2 * UP + 0 * LEFT)

        line2 = TextMobject("$x$","$x^{2}$")
        line2[0].scale(8).next_to(2.5 * DOWN + 4 * LEFT).set_color(PINK)
        line2[1].scale(8).next_to(1.75 * DOWN + 1.5 * RIGHT).set_color(YELLOW)
        self.play(FadeIn(line2))
        self.wait(2)
        self.play(FadeIn(line_e))
        self.wait(2)
        self.play(FadeIn(line_pi))
        self.wait(5)


class Menu(Scene):
    def construct(self):
        title = TextMobject(r"\underline{ \textbf{Menu}}", color=PURPLE).to_corner(UL).scale(1.25)

        l = NumberedList(
            *"""1) Applications mathématiques, 2) Définition de l'exposant, 3) Propriétés des exposants, 3) Exemplesssss""".split(","), dot_color=BLUE
        )

        #l = NumberedList(*["Révision des axiomes", "Riemann Hypothesis", "P vs NP Problem"], dot_color=BLUE)
        l.scale(1)
        l.shift(0.5 * DOWN + 3*LEFT)
        self.play(FadeInFromDown(title))
        self.play(Write(l))
        self.wait()

        #self.play(l.fade_all_but, 3)
        self.wait(15)


class Applications(Scene):
    def construct(self):
        title = TextMobject(r"\underline{ \textbf{Applications}}", color=PURPLE).to_corner(UL).scale(1.25)

        l = NumberedList(
            *"""1) Matrices (produit de matrices), 2) Fonctions (pour la composition), 3) Ensembles (pour le produit cartésien)e""".split(","), dot_color=BLUE
        )

        #l = NumberedList(*["Révision des axiomes", "Riemann Hypothesis", "P vs NP Problem"], dot_color=BLUE)
        l.scale(1)
        l.shift(0.5 * DOWN + 1*LEFT)
        self.play(FadeInFromDown(title))
        self.play(Write(l))
        self.wait()

        #self.play(l.fade_all_but, 3)
        self.wait(25)


class Application_reg(Scene):
    def construct(self):
        title = TextMobject(r"\underline{ \textbf{Application: Régression polynomiale}}", color=PURPLE).scale(1.25)
        title.next_to(3*UP + 6.5*LEFT)

        path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/images/"
        nuage_points = ImageMobject(path + "small_fr_points")
        nuage_points.scale(2.5)
        nuage_points.next_to(7*LEFT + 0.75*DOWN)

        reg_lin_points = ImageMobject(path + "small_lin_reg.png")
        reg_lin_points.scale(2.5)
        reg_lin_points.next_to(7 * LEFT + 0.75 * DOWN)

        poly_reg_points = ImageMobject(path + "small_fr_poly_reg.png")
        poly_reg_points.scale(2.5)
        poly_reg_points.next_to(7 * LEFT + 0.75 * DOWN)

        legende_1 = TextMobject(r"$y$", ": ",  r"Salaire").scale(1)
        legende_1[0].set_color(BLUE)
        legende_1.next_to(1.5*RIGHT + 1.5*UP)

        legende_2 = TextMobject(r"$x$", ": ",  r"Expérience").scale(1)
        legende_2.next_to(legende_1, DOWN, buff=0.25).align_to(legende_1, LEFT)
        legende_2[0].set_color(PINK)

        eq_1 = TextMobject(r"$y$", " $=$ ",  r"$\beta_{0}$", r" $+$ ", r"$\beta_{1}$",r"$x$").scale(1)
        eq_1[0].set_color(BLUE)
        eq_1[-1].set_color(PINK)
        eq_1.next_to(legende_2, DOWN, buff=0.25).align_to(legende_2, LEFT)

        eq_1_params = TextMobject(r"$\beta_{0},\beta_{1}\in\mathbb{R}$").scale(1)
        eq_1_params.next_to(eq_1, DOWN, buff=1.5).align_to(eq_1, LEFT)

        #eq_2 = TextMobject(r"$y$", " $=$ ", r"$\beta_{0}$", r" $+$ ", r"$\sum_{i=1}^{p}\beta_{i}$", r"$x^{i}$").scale(1)
        eq_2 = TexMobject(r"y", "=", r"\beta_{0}", r"+", r"\sum_{i=1}^{p}\beta_{i}", r"x^", r"i").scale(1)
        eq_2[0].set_color(BLUE)
        eq_2[-2].set_color(PINK)
        eq_2[-1].set_color(YELLOW)
        eq_2.next_to(eq_1, DOWN, buff=0).align_to(legende_2, LEFT)

        eq_2_params_1 = TextMobject(r"$\beta_{0},\beta_{1},\dots,\beta_{p}\in\mathbb{R}$").scale(1)
        eq_2_params_1.next_to(eq_1, DOWN, buff=1.5).align_to(eq_1, LEFT)

        eq_2_params_2 = TextMobject(r"$p\in\mathbb{N}\setminus\{0,1\}$").scale(1)
        eq_2_params_2.next_to(eq_2_params_1, DOWN, buff=0.5).align_to(eq_2_params_1, LEFT)

        self.play(FadeInFromDown(title))
        self.wait(10)
        self.play(FadeIn(nuage_points))
        self.wait(10)
        self.play(Write(legende_1), Write(legende_2))
        self.wait(15)
        self.play(Write(eq_1))
        self.play(Write(eq_1_params))
        self.wait(10)
        self.play(ShowCreation(reg_lin_points))
        self.play(FadeOut(nuage_points))
        self.wait(15)

        self.play(FadeOut(reg_lin_points))
        self.play(FadeOut(eq_1))
        self.play(FadeOut(eq_1_params))
        self.play(FadeIn(nuage_points))
        self.wait(10)
        self.play(Write(eq_2))
        self.wait(10)
        self.play(FadeIn(eq_2_params_1))
        self.wait(3)
        self.play(FadeIn(eq_2_params_2))
        self.wait(15)
        self.play(FadeIn(poly_reg_points))
        self.wait(15)


class ExposantDef(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\textbf{Les Exposants}}").scale(1).set_color(PURPLE)
        context = TextMobject(r"L'opération puissance consiste à multiplier un élément $a$ par lui-même "
                              r"plusieurs fois. Le nombre de facteurs intervenant dans cette opération est appelé ",
                              r"exposant ",
                              r"de l'élément $a$. Soit $a\in\mathbb{R}$, alors on a ").scale(0.7)
        context[1].set_color(YELLOW)
        context.next_to([-7, 1.5, 0])
        title.next_to([-2.75, 3, 0])

        eq_1 = TexMobject(r"a^", r"n", r"=", r"a\times a\times \dots \times a").scale(1.1)
        eq_1[1].set_color(YELLOW)
        brace1 = Brace(eq_1[3], DOWN, buff=SMALL_BUFF)
        brace_txt = TextMobject(r"$n$", " fois").scale(1.1)
        brace_txt[0].set_color(YELLOW)
        brace_txt.next_to(brace1,DOWN)

        interpretation = TextMobject(r"""
                        \begin{itemize}
                        \item $a$ puissance $n$,
                        \item $a$ exposant $n$. 
                        \end{itemize}
                        """).scale(0.7)
        interpretation.next_to(np.array([-7,-2,0]))

        self.play(FadeInFromDown(title))
        self.play(Write(context))
        self.wait(10)
        self.play(Write(eq_1), Write(brace1), Write(brace_txt))
        self.wait(5)
        self.play(Write(interpretation))
        self.wait(25)


class CasParticuliers(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\textbf{Cas Particuliers}}").to_corner(UL).scale(1).set_color(PURPLE)
        context = TextMobject(r"Soit $a\in\mathbb{R}$, alors on a ")
        context.next_to([-6.75, 2.5, 0])

        eq_1 = TextMobject(r"1) ", r"$a^{2}=a\times a$").scale(1)
        eq_2 = TextMobject(r"2) ", r"$a^{3}=a\times a\times a$").scale(1)
        eq_3 = TextMobject(r"3) ", r"$a^{1}=a$").scale(1)
        eq_4 = TextMobject(r"3) ", r"$a^{0}=1$").scale(1)

        nom_1 = TextMobject(r"", r"(Aire carré)").scale(1).set_color(RED)
        nom_2 = TextMobject(r"", r"(Volume cube)").scale(1).set_color(BLUE)
        nom_3 = TextMobject(r"", r"(Convention)").scale(1).set_color(YELLOW)
        nom_4 = TextMobject(r"", r"(Si $a$ est inversible)").scale(1).set_color(GREEN)

        eq_1[1].set_color(RED)
        eq_2[1].set_color(BLUE)
        eq_3[1].set_color(YELLOW)
        eq_4[1].set_color(GREEN)

        eq_1.next_to([-6, 1.5, 0], RIGHT)


        eq_2.next_to(eq_1, DOWN, buff=LARGE_BUFF).align_to(eq_1, LEFT)
        eq_3.next_to(eq_2, DOWN, buff=LARGE_BUFF).align_to(eq_2, LEFT)
        eq_4.next_to(eq_3, DOWN, buff=LARGE_BUFF).align_to(eq_3, LEFT)

        nom_2.next_to(eq_2, RIGHT, buff=LARGE_BUFF)
        nom_1.next_to(eq_1, RIGHT, buff=LARGE_BUFF).align_to(nom_2, LEFT)
        nom_3.next_to(eq_3, RIGHT, buff=LARGE_BUFF).align_to(nom_2, LEFT)
        nom_4.next_to(eq_4, RIGHT, buff=LARGE_BUFF).align_to(nom_2, LEFT)

        self.play(FadeInFromDown(title))
        self.play(Write(context))
        self.wait(5)
        self.play(Write(eq_1), Write(nom_1))
        self.wait(5)
        self.play(Write(eq_2), Write(nom_2))
        self.wait(5)
        self.play(Write(eq_3), Write(nom_3))
        self.wait(5)
        self.play(Write(eq_4), Write(nom_4))
        self.wait(25)



class ExtensionExpNegatifs(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\textbf{Extension aux exposants négatifs}}").to_corner(UL).scale(1).set_color(PURPLE)
        context = TextMobject(r"Si $a$ est un élément inversible, on note $a^{-1}$ son inverse.").scale(0.75)
        context.next_to([-6.75, 2.5, 0])

        context_2 = TextMobject2(r"Si en outre $n$ est un entier naturel, alors $a^{n}$ est aussi inversible, et l'on note $a^{-n}$ son inverse.").scale(0.75)
        context_2.next_to(context, DOWN, buff=LARGE_BUFF).align_to(context, LEFT)

        exemple_title = TextMobject2(r"\underline{Exemple:}").scale(1)
        exemple_title.next_to([-6.75, -0.5, 0])
        exemple_eq = TexMobject(r"2^{-2}=\frac{1}{2^{2}}=\frac{1}{4}")
        exemple_eq.next_to(exemple_title, DOWN, buff=LARGE_BUFF).align_to(exemple_title, LEFT)

        self.play(FadeInFromDown(title))
        self.play(Write(context))
        self.wait(5)
        self.play(Write(context_2))
        self.wait(8)
        self.play(Write(exemple_title), Write(exemple_eq))
        self.wait(12)


class Proprietes(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\textbf{Propriétés des exposants}}").to_corner(UL).scale(1).set_color(PURPLE)
        context = TextMobject(r"Soit $a,b\in\mathbb{R}$ (qui sont inversibles) et $m,n\in\mathbb{N}_{\star}$, alors on a ")
        context.next_to([-6.75, 2.5, 0])

        eq_1 = TextMobject(r"1) ", r"$a^{n+m}=a^{n}\times a^{m}$").scale(1)
        eq_2 = TextMobject(r"2) ", r"$a^{n-m}=\frac{a^{n}}{a^{m}}$").scale(1)
        eq_3 = TextMobject(r"3) ", r"$(a^{n})^{m}=a^{n\times m}$").scale(1)
        eq_4 = TextMobject(r"4) ", r"$(a\times b)^{n}=a^{n}\times b^{n}$").scale(1)

        eq_1[1].set_color(RED)
        eq_2[1].set_color(BLUE)
        eq_3[1].set_color(YELLOW)
        eq_4[1].set_color(GREEN)

        eq_1.next_to([-6, 1.5, 0], RIGHT)
        eq_2.next_to(eq_1, DOWN, buff=LARGE_BUFF).align_to(eq_1, LEFT)
        eq_3.next_to(eq_2, DOWN, buff=LARGE_BUFF).align_to(eq_2, LEFT)
        eq_4.next_to(eq_3, DOWN, buff=LARGE_BUFF).align_to(eq_3, LEFT)


        self.play(FadeInFromDown(title))
        self.play(Write(context))
        self.wait(10)
        self.play(Write(eq_1))
        self.wait(8)
        self.play(Write(eq_2))
        self.wait(8)
        self.play(Write(eq_3))
        self.wait(8)
        self.play(Write(eq_4))
        self.wait(25)



class Exemples(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\textbf{Exemples}}").to_corner(UL).scale(1).set_color(PURPLE)
        context = TextMobject(r"Simplifiez chacune des expressions suivantes: ")
        context.next_to([-6.75, 2.5, 0])

        eq_1 = TextMobject(r"1) ", r"$2^{2}\times 2^{3}$").scale(1)
        eq_2 = TextMobject(r"3) ", r"$9^{2}\times 2^{-3}$").scale(1)
        eq_3 = TextMobject(r"2) ", r"$(7^{2})^{3}$").scale(1)
        eq_4 = TextMobject(r"4) ", r"$\frac{(7\times 6)^{2}}{7\times 6^{3}}$").scale(1)

        eq_1.next_to([-6, 1.5, 0], RIGHT)
        eq_2.next_to(eq_1, DOWN, buff=LARGE_BUFF).align_to(eq_1, LEFT)
        eq_3.next_to(eq_1, RIGHT, buff=3*LARGE_BUFF)
        eq_4.next_to(eq_2, RIGHT, buff=3*LARGE_BUFF).align_to(eq_3, LEFT)


        self.play(FadeInFromDown(title))
        self.play(Write(context))
        self.wait(6)
        self.play(Write(eq_1))
        self.play(Write(eq_2))
        self.play(Write(eq_3))
        self.play(Write(eq_4))

        # Pause to think about it.
        circ = Arc(start_angle=PI / 2, angle=-2 * PI, radius=0.35).to_corner(DL)
        timers = [TexMobject(str(i)).move_to(circ) for i in range(5, -1, -1)]
        pause = TextMobject("Faites pause et trouvez les solutions.").next_to(circ, RIGHT)
        self.play(ShowCreation(circ), Write(pause))
        self.play(Write(timers[0]), run_time=0.5)
        for i in range(5):
            self.play(ReplacementTransform(timers[i], timers[i + 1]), run_time=0.5)
            self.wait(0.5)
        self.play(FadeOut(pause), FadeOut(timers[-1]), FadeOut(circ), run_time=2)
        answers = TextMobject("Solutions (respectivement): $2^{5}$, $7^{6}$, $\\frac{81}{8}$, $\\frac{7}{6}$").to_corner(DL)
        self.play(Write(answers))
        self.wait(15)



class Solutions(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\textbf{Solutions}}").to_corner(UL).scale(1).set_color(PURPLE)
        context = TextMobject(r"Simplifiez chacune des expressions suivantes: ")
        context.next_to([-6.75, 2.5, 0])

        eq_1 = TextMobject(r"1) ", r"$2^{2}\times 2^{3}=2^{2+3}=2^{5}$").scale(1)
        eq_2 = TextMobject(r"3) ", r"$9^{2}\times 2^{-3}=\frac{9^{2}}{2^{3}}=\frac{81}{8}$").scale(1)
        eq_3 = TextMobject(r"2) ", r"$(7^{2})^{3}=7^{2\times 3}=7^{6}$").scale(1)
        eq_4 = TextMobject(r"4) ", r"$\frac{(7\times 6)^{2}}{7\times 6^{3}}=\frac{7\times (7\times 6^{2})}{6\times (7\times 6^{2})}=\frac{7}{6}$").scale(1)

        eq_1.next_to([-6, 1.5, 0], RIGHT)
        eq_3.next_to(eq_1, DOWN, buff=0.75*LARGE_BUFF).align_to(eq_1, LEFT)
        eq_2.next_to(eq_3, DOWN, buff=0.75*LARGE_BUFF).align_to(eq_1, LEFT)
        eq_4.next_to(eq_2, DOWN, buff=0.75*LARGE_BUFF).align_to(eq_1, LEFT)


        self.play(FadeInFromDown(title))
        self.play(Write(context))
        self.wait(5)
        self.play(Write(eq_1))
        self.wait(7)
        self.play(Write(eq_3))
        self.wait(7)
        self.play(Write(eq_2))
        self.wait(7)
        self.play(Write(eq_4))
        self.wait(19)





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
        self.wait(3)
        self.pre_square()
        self.wait(10)
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


        title = TextMobject(r"\sc Preuve (géométrique): ", color=WHITE).to_corner(UL)
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

        self.wait(15)
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
        self.wait(10)
        #self.play(
        #    self.title.shift, UP * 3,
        #    theorem.shift, DOWN * 3,
        #    t_ab2.shift, LEFT * 7,
        #    self.joint_pre_square.shift, LEFT * 7,
        #    VGroup(t_a2, t_b2, t_ab, t_ba).shift, RIGHT * 7,
        #    VGroup(*self.rectangles).shift, RIGHT * 7,
        #    self.measures_2.shift, RIGHT * 7
        #)



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
        Title = TextMobject(r"\underline{Preuve (géométrique):}")
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


class Exercises1(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    # TO-DO :
    # Time limit. Find the answers.
    # Put the solution on both sides.
    def construct(self):
        title = TextMobject(r"\underline{\sc Exercices supplémentaires}").to_corner(UL).set_color(PURPLE).scale(1.15)
        exos = TextMobject(r" Factoriser les expressions suivantes à l'aide des identités remarquables:",
        r"""
        \begin{enumerate}
        \item $a-2\sqrt{a}\sqrt{b}+b$,
        \item $16y^{2}-4x^{2}$.
        \end{enumerate}
        """)
        #definition.scale(0.7)
        exos[0].move_to(np.array([-0.75, 2, 0]))
        exos.scale(0.8)


        self.play(Write(title))
        self.wait(10)
        self.play(FadeIn(exos))
        self.wait(5)

        # Pause to think about it.
        circ = Arc(start_angle=PI / 2, angle=-2 * PI, radius=0.35).to_corner(DL)
        timers = [TexMobject(str(i)).move_to(circ) for i in range(5, -1, -1)]
        pause = TextMobject("Faites pause et trouvez les solutions.").next_to(circ, RIGHT)
        self.play(ShowCreation(circ), Write(pause))
        self.play(Write(timers[0]), run_time=0.5)
        for i in range(5):
            self.play(ReplacementTransform(timers[i], timers[i + 1]), run_time=0.5)
            self.wait(0.5)
        self.play(FadeOut(pause), FadeOut(timers[-1]), FadeOut(circ), run_time=2)

        answer = TextMobject("Solutions (respectivement): $(\sqrt{a}-\sqrt{b})^{2}$, $(4y-2x)(4y+2x)$").to_corner(DL)
        self.play(Write(answer))
        self.wait(10)
        self.play(FadeOut(exos))
        self.play(FadeOut(title))


class Conclusion(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\textbf{À retenir}}", color=PURPLE).to_corner(UL).scale(1)

        compl_rules_str = [
            "",
            "Définition de la puissance,",
            "Propriétés des exposants entiers,",
            "Être en mesure de simplifier des expressions avec les propriétés des exposants.",
        ]

        def choose_color(i):
            color = WHITE if i<=2 else YELLOW
            return color

        rules = [TextMobject2("{}) {}".format(i, rule), color=choose_color(i)) for i, rule in enumerate(compl_rules_str)]
        rules = [rule.scale(0.7) for rule in rules]

        for (i, rule) in enumerate(rules):
            if i != 0:
                rule.next_to(rules[0].get_center() - rule.get_center() + np.array([-6, -0.7 * i, 0]))
        rules = VGroup(*rules)
        rules.to_corner(LEFT + UP)

        self.play(Write(title))
        self.wait(5)
        self.play(Write(rules[1]))
        self.wait(4)
        self.play(Write(rules[2]))
        self.wait(4)
        self.play(Write(rules[3]))
        self.wait(15)


class NumberedList(BulletedList):
    CONFIG = {
        "dot_scale_factor": 1,
        "num_color": BLUE,
    }

    def __init__(self, *items, **kwargs):
        line_separated_items = [s + "\\\\" for s in items]
        TextMobject.__init__(self, *line_separated_items, **kwargs)

