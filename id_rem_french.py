from manimlib.imports import *


# 0. Thumbnail
# 1. Menu
# 2. Motivation (Distributivite)
# 3. IdentitesRemarquables
# 4. IdRem1 (preuve algebrique: (a+b)^2)
# 5. MeasuredIdentity (preuve geometrique: (a+b)^2 = a^2 + b^2 + 2ab)
# 6. IdRem2 (preuve algebrique: (a-b)^2)
# 7. IdRem3 (preuve algebrique: (a-b)(a+b))
# 8. Exercises1 (1 de chaque) (TO-DO)
# 9. Exercises2 supp. (TO-DO)


color_map = {
    r"{a}": BLUE,
    r"{b}": YELLOW,
}

class Thumbnail(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/images/"
        image_peinture = ImageMobject(path + "kondo_id_rem")
        image_peinture.scale(4)
        #image_peinture.to_edge(DOWN)

        line_expand = TextMobject("$a^{2}+b^{2}$").set_color(BLACK).scale(1.5)
        line_expand.next_to(4.9*LEFT + 3.65*UP)

        line_factor = TextMobject(r"$a^{2}-b^{2}$").set_color(BLACK).scale(1.65)
        line_factor.next_to(2.1*RIGHT + 3.65*UP)

        self.play(FadeIn(image_peinture))
        self.play(Write(line_expand), Write(line_factor))
        self.wait(5)


class Menu(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\sc Menu}", color=PURPLE).to_corner(UL).scale(1.5)

        l = NumberedList(
            *"""1) Motivation, 2) Identités remarquabless""".split(","), dot_color=BLUE
        )

        #l = NumberedList(*["Révision des axiomes", "Riemann Hypothesis", "P vs NP Problem"], dot_color=BLUE)
        l.scale(1)
        l.shift(0.5 * DOWN + 3*LEFT)
        self.play(FadeInFromDown(title))
        self.play(Write(l))
        self.wait()

        #self.play(l.fade_all_but, 3)
        self.wait(15)



class Motivation(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\sc Motivation}", color=PURPLE).to_corner(UL).scale(1.25)

        l = NumberedList(
            *"""1) Accélérer des calculs, 2) Factoriser, 3) Développer des expressionssss""".split(","), dot_color=BLUE
        )

        #l = NumberedList(*["Révision des axiomes", "Riemann Hypothesis", "P vs NP Problem"], dot_color=BLUE)
        l.scale(1)
        l.shift(0.5 * DOWN + 3*LEFT)
        self.play(FadeInFromDown(title))
        self.play(Write(l))
        self.wait()

        #self.play(l.fade_all_but, 3)
        self.wait(15)


class IdentitesRemarquables(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\sc Les Identités Remarquables}").to_corner(UL).scale(1)
        context = TextMobject(r"Soit $a,b\in\mathbb{R}$, alors on a }")
        context.next_to([-6.75, 2, 0])

        eq_1 = TextMobject(r"1) ", r"$(a+b)^{2}=a^{2}+2ab+b^{2}$").scale(1)
        eq_2 = TextMobject(r"2) ", r"$(a-b)^{2}=a^{2}-2ab+b^{2}$").scale(1)
        eq_3 = TextMobject(r"3) ", r"$(a-b)(a+b)=a^{2}-b^{2}$").scale(1)

        nom_1 = TextMobject(r"", r"IR1").scale(1).set_color(RED)
        nom_2 = TextMobject(r"", r"IR2").scale(1).set_color(BLUE)
        nom_3 = TextMobject(r"", r"IR3").scale(1).set_color(YELLOW)

        eq_1[1].set_color(RED)
        eq_2[1].set_color(BLUE)
        eq_3[1].set_color(YELLOW)

        eq_1.next_to([-6, 0.75, 0], RIGHT)
        nom_1.next_to(eq_1, RIGHT, buff=LARGE_BUFF)
        eq_2.next_to(eq_1, DOWN, buff=LARGE_BUFF)
        nom_2.next_to(eq_2, RIGHT, buff=LARGE_BUFF).align_to(nom_1, LEFT)
        eq_3.next_to(eq_2, DOWN, buff=LARGE_BUFF)
        nom_3.next_to(eq_3, RIGHT, buff=LARGE_BUFF).align_to(nom_2, LEFT)

        self.play(FadeInFromDown(title))
        self.play(Write(context))
        self.wait(5)
        self.play(Write(eq_1), Write(nom_1))
        self.wait(3)
        self.play(Write(eq_2), Write(nom_2))
        self.wait(3)
        self.play(Write(eq_3), Write(nom_3))
        self.wait(25)


class IdRem1(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\sc Preuve de IR1}", color=RED).to_corner(UL).scale(1)

        eq_1 = TextMobject(r"$(a+b)^{2}$", r" $=$", r" $(a+b)(a+b)$").scale(1.1)
        justification_1 = TextMobject(r"(Par définition)").scale(0.9)
        eq_1.next_to([-6, 1.5, 0], RIGHT)
        justification_1.next_to([2.75, 1.35, 0])

        eq_2 = TextMobject(r" $=$",r"$a^{2}+ab+ba+b^{2}$").scale(1.1)
        justification_2 = TextMobject(r"(Par distributivité)").scale(0.9)
        eq_2[0].next_to(eq_1, DOWN, buff=LARGE_BUFF).align_to(eq_1[1], LEFT)
        eq_2[1].next_to(eq_2[0], RIGHT, buff=LARGE_BUFF).align_to(eq_1[2], LEFT)
        justification_2.next_to(eq_2[1], RIGHT, buff=LARGE_BUFF).align_to(justification_1, RIGHT)

        eq_3 = TextMobject(r" $=$", r"$a^{2}+ab+ab+b^{2}$").scale(1.1)
        justification_3 = TextMobject(r"(Par commutativité)").scale(0.9)
        eq_3[0].next_to(eq_2, DOWN, buff=LARGE_BUFF).align_to(eq_2[0], LEFT)
        eq_3[1].next_to(eq_3[0], RIGHT, buff=LARGE_BUFF).align_to(eq_2[1], LEFT)
        justification_3.next_to(eq_3[1], RIGHT, buff=LARGE_BUFF).align_to(justification_2, RIGHT)

        eq_4 = TextMobject(r" $=$", r"$a^{2}+2ab+b^{2}$").scale(1.1)
        eq_4[0].next_to(eq_3, DOWN, buff=LARGE_BUFF).align_to(eq_3[0], LEFT)
        eq_4[1].next_to(eq_4[0], RIGHT, buff=LARGE_BUFF).align_to(eq_3[1], LEFT)

        square = Square(side_length=0.25, fill_color=GOLD, fill_opacity=1, color=ORANGE)
        square.move_to(5 * RIGHT + 3 * DOWN)


        self.play(Write(title))
        self.wait(5)
        self.play(Write(eq_1))
        self.wait(5)
        self.play(Write(justification_1))
        self.wait(3)
        self.play(Write(eq_2))
        self.wait(5)
        self.play(Write(justification_2))
        self.wait(3)
        self.play(Write(eq_3))
        self.wait(5)
        self.play(Write(justification_3))
        self.wait(5)
        self.play(Write(eq_4))
        self.wait(3)
        self.play(Write(square))
        self.wait(15)



class IdRem2(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\sc Preuve de IR2}", color=BLUE).to_corner(UL).scale(1)

        eq_1 = TextMobject(r"$(a-b)^{2}$", r" $=$", r" $(a+c)^{2}$").scale(1.1)
        justification_1 = TextMobject(r"(Posons $c=-b$)").scale(0.9)
        eq_1.next_to([-6, 1.5, 0], RIGHT)
        justification_1.next_to([2.75, 1.35, 0])

        eq_2 = TextMobject(r" $=$",r"$a^{2}+2ac+c^{2}$").scale(1.1)
        justification_2 = TextMobject(r"(Par IR1)").scale(0.9).set_color(RED)
        eq_2[0].next_to(eq_1, DOWN, buff=LARGE_BUFF).align_to(eq_1[1], LEFT)
        eq_2[1].next_to(eq_2[0], RIGHT, buff=LARGE_BUFF).align_to(eq_1[2], LEFT)
        justification_2.next_to(eq_2[1], RIGHT, buff=LARGE_BUFF).align_to(justification_1, RIGHT)

        eq_3 = TextMobject(r" $=$", r"$a^{2}+2a(-b)+(-b)^{2}$").scale(1.1)
        justification_3 = TextMobject(r"(Par définition)").scale(0.9)
        eq_3[0].next_to(eq_2, DOWN, buff=LARGE_BUFF).align_to(eq_2[0], LEFT)
        eq_3[1].next_to(eq_3[0], RIGHT, buff=LARGE_BUFF).align_to(eq_2[1], LEFT)
        justification_3.next_to(eq_3[1], RIGHT, buff=LARGE_BUFF).align_to(justification_2, RIGHT)

        eq_4 = TextMobject(r" $=$", r"$a^{2}-2ab+b^{2}$").scale(1.1)
        eq_4[0].next_to(eq_3, DOWN, buff=LARGE_BUFF).align_to(eq_3[0], LEFT)
        eq_4[1].next_to(eq_4[0], RIGHT, buff=LARGE_BUFF).align_to(eq_3[1], LEFT)

        square = Square(side_length=0.25, fill_color=GOLD, fill_opacity=1, color=ORANGE)
        square.move_to(5 * RIGHT + 3 * DOWN)


        self.play(Write(title))
        self.wait(5)
        self.play(Write(eq_1))
        self.wait(5)
        self.play(Write(justification_1))
        self.wait(3)
        self.play(Write(justification_2))
        self.wait(5)
        self.play(Write(eq_2))
        self.wait(3)
        self.play(Write(justification_3))
        self.wait(5)
        self.play(Write(eq_3))
        self.wait(5)
        self.play(Write(eq_4))
        self.wait(3)
        self.play(Write(square))
        self.wait(15)


class IdRem3(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\sc Preuve de IR3:}", color=YELLOW).to_corner(UL).scale(1)

        eq_1 = TextMobject(r"$(a-b)(a+b)$", r" $=$", r" $a^{2}+ab-ba-b^{2}$").scale(1.1)
        justification_1 = TextMobject(r"(Distributivité)").scale(0.8)
        eq_1.next_to([-6, 1.5, 0], RIGHT)
        justification_1.next_to([2.75, 1.35, 0])

        eq_2 = TextMobject(r" $=$ ", r"$a^{2}$", r" $+$ ", r"$(ab$", r" $-$ ", r"$ab)$", r" $-$ ", r"$b^{2}$").scale(1.1)
        justification_2 = TextMobject(r"(Commutativité)").scale(0.8)
        eq_2.next_to([-2.6,0,0])
        justification_2.next_to(eq_2[1], RIGHT, buff=LARGE_BUFF).align_to(justification_1, RIGHT)

        cancel_ab = Cancel(eq_2[0])

        eq_3 = TextMobject(r" $=$", r"$a^{2}-b^{2}$").scale(1.1)
        eq_3[0].next_to(eq_2, DOWN, buff=LARGE_BUFF).align_to(eq_2[0], LEFT)
        eq_3[1].next_to(eq_3[0], RIGHT, buff=LARGE_BUFF).align_to(eq_2[1], LEFT)

        square = Square(side_length=0.25, fill_color=GOLD, fill_opacity=1, color=ORANGE)
        square.move_to(5 * RIGHT + 3 * DOWN)


        self.play(Write(title))
        self.wait(5)
        self.play(Write(eq_1))
        self.wait(5)
        #self.play(Write(justification_1))
        self.play(Write(eq_2))
        self.wait(5)
        self.add(eq_2, cancel_ab)
        self.wait(5)
        #self.play(Write(justification_2))
        self.play(Write(eq_3))
        self.wait(5)
        self.play(Write(square))
        self.wait(15)



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



class Cancel(VGroup):
    CONFIG = {
        "line_kwargs": {"color":RED},
        "buff_text": None,
        "buff_line": 0.9,
    }
    def __init__(self,text,**kwargs):
        digest_config(self,kwargs)
        VGroup.__init__(self,**kwargs)

        pre_coord_dl = text.get_corner(DL)
        pre_coord_ur = text.get_corner(UR)
        reference_line = Line(pre_coord_dl,pre_coord_ur)
        reference_unit_vector = reference_line.get_unit_vector()
        coord_dl = text.get_corner(DL) - text.get_center() - reference_unit_vector*self.buff_line
        coord_ur = text.get_corner(UR) - text.get_center() + reference_unit_vector*self.buff_line

        line = Line(coord_dl+np.array([0.65,0,0]), coord_ur+np.array([0.65,0,0]),**self.line_kwargs)
        self.add(line)


class CancelTerms(Scene):
    def construct(self):
        formula = TexMobject("f(x)",height=1)
        cancel_formula = Cancel(formula)
        self.play(Write(formula),Write(cancel_formula))


class CreditsFr(Scene):
    def wplay(self, *args, wait=1, run_time=1, rate_func=smooth):
        self.play(*args, run_time=run_time, rate_func=rate_func)
        if wait != 0:
            self.wait(wait)

    def construct(self):
        credits = TextMobject("Crédits").set_color(YELLOW).scale(1.7)
        thanks = TextMobject("Merci pour votre visionnement!!").set_color(ORANGE).scale(1.7)

        instructor = TexMobject(r"\text{Enseignant}", r"\text{Louis-Marc Mercier}")
        viewer = TexMobject(r"\text{Spectateur}", r"\text{Vous}")
        chanson = TexMobject(r"\text{Chanson (artiste)}", r"\text{Prophecy (Adrian von Ziegler)}")
        lines = [instructor, viewer, chanson]

        instructor[0].align_to([-1, 0, 0], RIGHT).shift(8 * DOWN)
        instructor[1].align_to([0, 0, 0], LEFT).shift(8 * DOWN)

        viewer[0].next_to(instructor, DOWN, buff=LARGE_BUFF).align_to(instructor[0], RIGHT)
        viewer[1].next_to(instructor, DOWN, buff=LARGE_BUFF).align_to(instructor[1], LEFT)

        chanson[0].next_to(viewer, DOWN, buff=LARGE_BUFF).align_to(viewer[0], RIGHT)
        chanson[1].next_to(viewer, DOWN, buff=LARGE_BUFF).align_to(viewer[1], LEFT)


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



class CreditsEng(Scene):
    def wplay(self, *args, wait=1, run_time=1, rate_func=smooth):
        self.play(*args, run_time=run_time, rate_func=rate_func)
        if wait != 0:
            self.wait(wait)

    def construct(self):
        credits = TextMobject("Credits").set_color(YELLOW).scale(1.7)
        thanks = TextMobject("Thanks for watching!!").set_color(ORANGE).scale(1.7)

        instructor = TexMobject(r"\text{Teacher}", r"\text{Louis-Marc Mercier}")
        viewer = TexMobject(r"\text{Viewer}", r"\text{You}")
        chanson = TexMobject(r"\text{Song (artist)}", r"\text{Prophecy (Adrian von Ziegler)}")
        lines = [instructor, viewer, chanson]

        instructor[0].align_to([-1, 0, 0], RIGHT).shift(8 * DOWN)
        instructor[1].align_to([0, 0, 0], LEFT).shift(8 * DOWN)

        viewer[0].next_to(instructor, DOWN, buff=LARGE_BUFF).align_to(instructor[0], RIGHT)
        viewer[1].next_to(instructor, DOWN, buff=LARGE_BUFF).align_to(instructor[1], LEFT)

        chanson[0].next_to(viewer, DOWN, buff=LARGE_BUFF).align_to(viewer[0], RIGHT)
        chanson[1].next_to(viewer, DOWN, buff=LARGE_BUFF).align_to(viewer[1], LEFT)


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






class NumberedList(BulletedList):
    CONFIG = {
        "dot_scale_factor": 1,
        "num_color": BLUE,
    }

    def __init__(self, *items, **kwargs):
        line_separated_items = [s + "\\\\" for s in items]
        TextMobject.__init__(self, *line_separated_items, **kwargs)

