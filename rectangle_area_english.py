from manimlib.imports import *

# TODO: SCENE ORDER

# 0. ShowImageAndQuote
# 1. AreaThumbnail
# 1. ObjectifLecon
# 3. Proprietes
# 4. UnitSquare
# 5. AreaDecomposition
# 6. RectangleDefinition
# 7. RectangleDecomposition1
# 8. RectangleDecomposition2
# 9. ParticularRectangle
# 10. AreaFormula
# 11. SquareAreaFormula
# 12. Conclusion
# 13. Credits

class AreaThumbnail(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        # Préalable : Comprendre le concept d'aire.
        # But: Calculer l'aire d'un rectangle donné.
        line1 = TextMobject("Euclidean Geometry").scale(2.5).shift(2.25 * UP).set_color(BLUE)
        line2 = TextMobject(r"Rectangle Area").scale(3).next_to(line1, DOWN).set_color(BLUE)
        self.play(Write(line1), Write(line2))
        self.wait()

        # Define two squares (one yellow and one white, opacity allows to fill color in figure).
        left_rectangle, right_rectangle = Rectangle(fill_opacity=0.5, color=PINK), Rectangle()

        # Put the two squares next to another.
        VGroup(left_rectangle, right_rectangle) \
            .scale(self.square_scale) \
            .arrange_submobjects(RIGHT, buff=2).next_to(1.5*DOWN + 5*LEFT)

        self.play(*list(map(DrawBorderThenFill, [right_rectangle, left_rectangle])))
        self.wait(5)


class ShowImageAndQuote(Scene):
    def construct(self):
        quote = TextMobject(r"Ramener le problème à une situation déjà résolue.")
        quote.scale(0.7)
        quote.set_color(RED)
        quote.to_edge(UP)
        self.play(FadeIn(quote))

        path = r"C:/Users/Utilisateur/Desktop/CEGEP/"
        image = ImageMobject(path + "new_file")
        image.scale(2.75)
        image.to_edge(DOWN)
        self.play(FadeIn(image))
        self.wait(2)
        self.play(FadeOut(image))
        self.play(FadeOut(quote))


class ObjectifLecon(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Empowerement Promise}", color=WHITE).to_corner(UL)
        #definition = TextMobject(r"Connaître la formule de l'aire d'un rectangle et calculer l'aire d'un rectangle.")
        definition = TextMobject(r"""
        \begin{itemize}
        \item Learn the formula to calculate a rectangle's area,
        \item Be able to calculate the area of a rectangle.
        \end{itemize}
        """)
        definition.scale(0.7)
        definition.move_to(np.array([-1, 1, 0]))
        definition.set_color(BLUE)

        self.play(Write(title))
        self.wait(3)
        self.play(FadeIn(definition))

        path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/images/"
        #image_peinture = SVGMobject(path + "x-icon")
        image_peinture = ImageMobject(path + "objectif")
        image_peinture.next_to(1.5*DOWN+0.5*LEFT)
        self.play(ShowCreation(image_peinture))
        self.wait(10)


class RectangleDefinition(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW],
        "l_a": 5 / 5,
        "l_b": 12 / 5
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc What is a Rectangle?}", color=WHITE).to_corner(UL)
        definition = TextMobject(r"""
                    \RedBox[label=exsecond]{}{
                    In euclidean geometry, a rectangle is a quadrilateral whose four angles are right where
                    $l,w>0$ correspond to the length and the width respectively.
                    }      
                """
                )
        definition.scale(0.5)
        definition.next_to(1.5*UP+5.5*LEFT)

        rectangle = Rectangle(fill_opacity=0.5, color=PINK)
        rectangle.set_height(self.l_a)
        rectangle.set_height(self.l_b)
        rectangle.next_to(1.5*DOWN + 3.5*LEFT)

        drawed_coords = []
        for point in [DL, DR, UL, UR]:
            drawed_coords.append(rectangle.get_corner(point))
        dl, dr, ul, ur = drawed_coords
        # lin, liz, ls, ld = coords_sides

        vert_measure = MeasureDistance(Line(dl, dr), invertir=True, dashed=True, buff=-0.25).add_tips() \
            .add_tex("l", buff=-3.7, color=WHITE)
        hor_measure = MeasureDistance(Line(dl, ul), invertir=False, dashed=True, buff=0.5).add_tips() \
            .add_tex("w", buff=2, color=WHITE)
        hor_measure[-1].rotate(-PI/2)
        measures_1 = VGroup(hor_measure, vert_measure)

        self.title = VGroup(title)
        self.play(Write(title, run_time=1), FadeIn(definition), ShowCreation(rectangle, run_time=1),
                  *[GrowFromCenter(object) for object in [*measures_1]], run_time=1
                  )
        self.wait(26)


class AreaFormula(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW],
        "l_a": 5 / 5,
        "l_b": 12 / 5
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Rectangle Area}", color=WHITE).to_corner(UL)
        definition = TextMobject(r"""
                    \RedBox[label=exsecond]{}{
                    Consider a rectangle of length $l>0$, of width $w>0$ and of area $A$. Its area is the product
                    between its length and its width.
                    \begin{equation}
                    A = l\times w
                    \end{equation}
                    }      
                """
                )
        definition.scale(0.5)
        definition.next_to(1.5*UP+5.5*LEFT)

        rectangle = Rectangle(fill_opacity=0.5, color=PINK)
        rectangle.set_height(self.l_a)
        rectangle.set_height(self.l_b)
        rectangle.next_to(1.5*DOWN + 3.5*LEFT)

        drawed_coords = []
        for point in [DL, DR, UL, UR]:
            drawed_coords.append(rectangle.get_corner(point))
        dl, dr, ul, ur = drawed_coords
        # lin, liz, ls, ld = coords_sides

        vert_measure = MeasureDistance(Line(dl, dr), invertir=True, dashed=True, buff=-0.25).add_tips() \
            .add_tex("l", buff=-3.7, color=WHITE)
        hor_measure = MeasureDistance(Line(dl, ul), invertir=False, dashed=True, buff=0.5).add_tips() \
            .add_tex("w", buff=2, color=WHITE)
        hor_measure[-1].rotate(-PI/2)
        measures_1 = VGroup(hor_measure, vert_measure)

        self.title = VGroup(title)
        self.play(Write(title, run_time=1), FadeIn(definition), ShowCreation(rectangle, run_time=1),
                  *[GrowFromCenter(object) for object in [*measures_1]], run_time=1
                  )
        self.wait(25)


class SquareAreaFormula(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW],
        "l_a": 5 / 5,
        "l_b": 12 / 5
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Square Area}", color=WHITE).to_corner(UL)
        definition = TextMobject(r"""
                    \RedBox[label=exsecond]{}{
                    Consider a square of side $c>0$. The area is equal to the square of the side.
                    \begin{equation}
                    A = c\times c=c^{2}
                    \end{equation}
                    }      
                """
                )
        definition.scale(0.5)
        definition.next_to(1.5*UP+5.5*LEFT)

        square = Square(side_length=3*(self.l_a+self.l_b)/4, fill_opacity=0.5, color=PINK)
        square.next_to(1.5*DOWN + 2.5*LEFT)

        drawed_coords = []
        for point in [DL, DR, UL, UR]:
            drawed_coords.append(square.get_corner(point))
        dl, dr, ul, ur = drawed_coords
        # lin, liz, ls, ld = coords_sides

        vert_measure = MeasureDistance(Line(dl, dr), invertir=True, dashed=True, buff=-0.25).add_tips() \
            .add_tex("c", buff=-3.7, color=WHITE)
        hor_measure = MeasureDistance(Line(dl, ul), invertir=False, dashed=True, buff=0.5).add_tips() \
            .add_tex("c", buff=2, color=WHITE)
        hor_measure[-1].rotate(-PI/2)
        measures_1 = VGroup(hor_measure, vert_measure)

        self.title = VGroup(title)
        self.wait(10)
        self.play(Write(title, run_time=1), FadeIn(definition), ShowCreation(square, run_time=1),
                  *[GrowFromCenter(object) for object in [*measures_1]], run_time=1
                  )
        self.wait(30)




class ParticularRectangle(Scene):
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
        rectangle = Rectangle(fill_opacity=0.5, color=ORANGE)
        drawed_coords = []
        for point in [DL, DR, UL, UR]:
            drawed_coords.append(rectangle.get_corner(point))
        dl, dr, ul, ur = drawed_coords

        coords_sides = []
        for point in [dr + LEFT * self.l_b, dl + UP * self.l_a, ul + RIGHT * self.l_a, ur + DOWN * self.l_b]:
            coords_sides.append(point)
        lin, liz, ls, ld = coords_sides

        hor_measure = MeasureDistance(Line(dl, dr), invertir=True, dashed=True, buff=-0.25).add_tips()\
            .add_tex("4.1", buff=-3.7, color=GREEN)
        vert_measure = MeasureDistance(Line(dl, ul), invertir=False, dashed=True, buff=0.5).add_tips()\
            .add_tex("2.2", buff=2, color=BLUE)
        vert_measure[-1].rotate(-PI/2)
        measures_1 = VGroup(vert_measure, hor_measure)


        title = TextMobject(r"\sc Area Calculation (Rectangle, $l=4.1$, $w=2.2$)", color=WHITE).to_corner(UL)
        self.wait(5)
        self.title = VGroup(title)
        self.play(Write(title, run_time=1), ShowCreation(rectangle, run_time=1),
                  *[GrowFromCenter(object) for object in [*measures_1]], run_time=1
                  )
        self.wait(5)

        joint_square = VGroup(rectangle)
        self.unit_square = rectangle
        self.unit_square.add(hor_measure, vert_measure)
        #self.play(joint_square.to_edge, LEFT, {"buff": 1.7})
        #self.play(ShowCreation(joint_square))
        self.wait(15)

        # Pause to think about it.
        circ = Arc(start_angle=PI / 2, angle=-2 * PI, radius=0.35).to_corner(DL)
        timers = [TexMobject(str(i)).move_to(circ) for i in range(5, -1, -1)]
        pause = TextMobject("Pause the video and find the area of the rectangle.").next_to(circ, RIGHT)
        self.play(ShowCreation(circ), Write(pause))
        self.play(Write(timers[0]), run_time=0.5)
        for i in range(5):
            self.play(ReplacementTransform(timers[i], timers[i + 1]), run_time=0.5)
            self.wait(0.5)
        self.play(FadeOut(pause), FadeOut(timers[-1]), FadeOut(circ), run_time=2)

        #line1 = TextMobject(r"Aire", " = ", "$4.1\\times 2.2=9.02$"). \
        #    scale(0.75).move_to(5 * LEFT + 2 * UP).set_color(ORANGE)
        line1 = TextMobject(r"Area", " = ", "4.1", "$\\times$", "2.2", " = ", "{}".format(4.1*2.2)). \
            scale(0.75).move_to(5 * LEFT + 2 * UP)
        line1[0].set_color(ORANGE)
        line1[2].set_color(GREEN)
        line1[4].set_color(BLUE)
        line1[6].set_color(ORANGE)
        self.play(Write(line1))

        answer = TextMobject("The area of the rectangle is $9.02$ squared units.").to_corner(DL)
        self.play(Write(answer))
        self.wait(20)


class SquareExample(Scene):
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
        rectangle = Square(fill_opacity=0.5, color=ORANGE)
        drawed_coords = []
        for point in [DL, DR, UL, UR]:
            drawed_coords.append(rectangle.get_corner(point))
        dl, dr, ul, ur = drawed_coords

        coords_sides = []
        for point in [dr + LEFT * self.l_b, dl + UP * self.l_a, ul + RIGHT * self.l_a, ur + DOWN * self.l_b]:
            coords_sides.append(point)
        lin, liz, ls, ld = coords_sides

        hor_measure = MeasureDistance(Line(dl, dr), invertir=True, dashed=True, buff=-0.25).add_tips()\
            .add_tex("4.1", buff=-3.7, color=GREEN)
        vert_measure = MeasureDistance(Line(dl, ul), invertir=False, dashed=True, buff=0.5).add_tips()\
            .add_tex("4.1", buff=2, color=BLUE)
        measures_1 = VGroup(vert_measure, hor_measure)
        vert_measure[-1].rotate(-PI/2)
        #vert_measure.rotate(PI/2)


        title = TextMobject(r"\sc Calcul d'aire (carré, $c=4.1$)", color=WHITE).to_corner(UL)
        self.title = VGroup(title)
        self.play(Write(title, run_time=1), ShowCreation(rectangle, run_time=1),
                  *[GrowFromCenter(object) for object in [*measures_1]], run_time=1
                  )
        self.wait(5)

        joint_square = VGroup(rectangle)
        self.unit_square = rectangle
        self.unit_square.add(hor_measure, vert_measure)
        #self.play(joint_square.to_edge, LEFT, {"buff": 1.7})
        self.play(ShowCreation(joint_square))
        self.wait(5)

        # Pause to think about it.
        circ = Arc(start_angle=PI / 2, angle=-2 * PI, radius=0.35).to_corner(DL)
        timers = [TexMobject(str(i)).move_to(circ) for i in range(5, -1, -1)]
        pause = TextMobject("Faites pause et trouvez l'aire du carré.").next_to(circ, RIGHT)
        self.play(ShowCreation(circ), Write(pause))
        self.play(Write(timers[0]), run_time=0.5)
        for i in range(5):
            self.play(ReplacementTransform(timers[i], timers[i + 1]), run_time=0.5)
            self.wait(0.5)
        self.play(FadeOut(pause), FadeOut(timers[-1]), FadeOut(circ), run_time=2)

        area_value = 4.1*4.1
        line1 = TextMobject(r"Aire", " = ", "4.1", "$\\times$", "4.1", " = ", "{}".format(area_value)). \
            scale(0.75).move_to(5 * LEFT + 2 * UP)
        line1[0].set_color(ORANGE)
        line1[2].set_color(GREEN)
        line1[4].set_color(BLUE)
        line1[6].set_color(ORANGE)
        self.play(Write(line1))

        answer = TextMobject("L'aire du carré est de {} unités carrés.".format(area_value)).to_corner(DL)
        self.play(Write(answer))
        self.wait(15)


class Conclusion(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Important Elements}", color=WHITE).to_corner(UL)

        compl_rules_str = [
            "",
            "The area of a rectangle is equal to the product of its length and its width.",
            "The area of a square is the square of its side.",
        ]


        rules = [TextMobject("{}) {}".format(i, rule), color=WHITE) for i, rule in enumerate(compl_rules_str)]
        rules = [rule.scale(0.7) for rule in rules]

        for (i, rule) in enumerate(rules):
            if i != 0:
                rule.next_to(rules[0].get_center() - rule.get_center() + np.array([-6, -0.7 * i, 0]))
        rules = VGroup(*rules)
        rules.to_corner(LEFT + UP)

        self.play(Write(title))
        self.wait(10)
        self.play(Write(rules[1]))
        self.wait(5)
        self.play(Write(rules[2]))
        self.wait(10)

        # Define two squares (one yellow and one white, opacity allows to fill color in figure).
        left_rectangle, right_rectangle = Rectangle(fill_opacity=0.5, color=PINK), Square(fill_opacity=0.5, color=BLUE)

        # Put the two squares next to another.
        VGroup(left_rectangle, right_rectangle) \
            .scale(self.square_scale) \
            .arrange_submobjects(RIGHT, buff=2).next_to(1.5 * DOWN + 5 * LEFT)

        self.play(*list(map(DrawBorderThenFill, [right_rectangle, left_rectangle])))
        t_a2 = TexMobject("A=l\\times w", color=WHITE).move_to(left_rectangle)
        t_b2 = TexMobject("A=c^{2}", color=WHITE).move_to(right_rectangle)
        self.play(*[Write(t_) for t_ in [t_a2, t_b2]])
        self.wait(10)


class Credits(Scene):
    def wplay(self, *args, wait=1, run_time=1, rate_func=smooth):
        self.play(*args, run_time=run_time, rate_func=rate_func)
        if wait != 0:
            self.wait(wait)

    def construct(self):
        credits = TextMobject("Credits").set_color(YELLOW).scale(1.7)
        thanks = TextMobject("Thanks for watching!!").set_color(ORANGE).scale(1.7)

        instructor = TexMobject(r"\text{Teacher}", r"\text{Louis-Marc Mercier}")
        viewer = TexMobject(r"\text{Viewer}", r"\text{You}")
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
            .add_tex("1\\text{ unit}", buff=-3.7, color=WHITE)
        hor_measure = MeasureDistance(Line(dl, ul), invertir=False, dashed=True, buff=0.5).add_tips()\
            .add_tex("1\\text{ unit}", buff=2, color=WHITE)
        measures_1 = VGroup(hor_measure, vert_measure)


        title = TextMobject(r"\sc Reminder: Unit Square ($c=1$)", color=WHITE).to_corner(UL)
        self.title = VGroup(title)
        self.play(Write(title, run_time=1), ShowCreation(square, run_time=1),
                  *[GrowFromCenter(object) for object in [*measures_1]], run_time=1
                  )
        self.wait(5)

        joint_square = VGroup(square)
        self.unit_square = square
        self.unit_square.add(hor_measure, vert_measure)
        self.play(joint_square.to_edge, LEFT, {"buff": 1.7})
        self.wait(4)

        line1 = TextMobject(r"Area"," = ","$1\\text{ unit}^{2}$").\
            scale(0.75).move_to(2.5*RIGHT+1.2*UP).set_color(ORANGE)
        self.play(Write(line1))
        self.wait(15)


class Proprietes(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Reminder: Area Properties}", color=WHITE).to_corner(UL)

        compl_rules_str = [
            "",
            "Given a unit length, the area of a square of side 1 is equal to 1.",
            "The area is additive.",
        ]

        rules = [TextMobject("{}) {}".format(i, rule), color=YELLOW) for i, rule in enumerate(compl_rules_str)]
        rules = [rule.scale(0.7) for rule in rules]

        for (i, rule) in enumerate(rules):
            if i != 0:
                rule.next_to(rules[0].get_center() - rule.get_center() + np.array([-6, -0.7 * i, 0]))
        rules = VGroup(*rules)
        rules.to_corner(LEFT + UP)

        self.play(Write(title))
        self.wait(6)
        self.play(Write(rules[1]))
        self.wait(7)
        self.play(Write(rules[2]))
        self.wait(15)



class AreaDecomposition(Scene):
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
        self.wait(5)
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


        title = TextMobject(r"\sc Reminder (cont'd): Area Additivity", color=WHITE).to_corner(UL)
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
        self.wait(10)
        self.wait()
        self.play(
            self.title.shift, UP * 3,
            self.joint_pre_square.shift, LEFT * 7,
            VGroup(*self.rectangles).shift, RIGHT * 7,
            self.measures_2.shift, RIGHT * 7
        )


class RectangleDecomposition1(Scene):
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
        self.wait(5)
        self.pos_square()
        self.transition_squares()

    def pre_square(self):
        rectangle = Rectangle(fill_opacity=0.5, color=ORANGE)
        rectangle.set_width(self.l_a/2)
        rectangle.set_height(self.l_b/2)
        #rectangle = Square(side_length=self.l_a + self.l_b, fill_opacity=0.5, color=ORANGE)
        drawed_coords = []
        for point in [DL, DR, UL, UR]:
            drawed_coords.append(rectangle.get_corner(point))
        dl, dr, ul, ur = drawed_coords
        #lin, liz, ls, ld = coords_sides

        horizontal_measure = MeasureDistance(Line(dl, dr), invertir=True, dashed=True, buff=-0.25).add_tips()\
            .add_tex("2", buff=-3.7, color=GREEN)
        vertical_measure = MeasureDistance(Line(dl, ul), invertir=False, dashed=True, buff=0.5).add_tips()\
            .add_tex("1", buff=2, color=BLUE)
        vertical_measure[-1].rotate(-PI/2)
        measures_1 = VGroup(vertical_measure, horizontal_measure)


        title = TextMobject(r"\sc Example: Area Calculation (Rectangle, $l=2$, $w=1$)", color=WHITE).to_corner(UL)
        self.title = VGroup(title)
        self.play(Write(title, run_time=1), ShowCreation(rectangle, run_time=1),
                  *[GrowFromCenter(object) for object in [*measures_1]], run_time=1
                  )


        joint_pre_square = VGroup(rectangle)
        self.joint_pre_square = rectangle
        self.joint_pre_square.add(vertical_measure, horizontal_measure)
        self.play(joint_pre_square.to_edge, LEFT, {"buff": 1.7})
        self.square = rectangle

        # Pause to think about it.
        circ = Arc(start_angle=PI / 2, angle=-2 * PI, radius=0.35).to_corner(DL)
        timers = [TexMobject(str(i)).move_to(circ) for i in range(5, -1, -1)]
        pause = TextMobject("Pause the video and find the area of the rectangle.").next_to(circ, RIGHT)
        self.wait(10)
        self.play(ShowCreation(circ), Write(pause))
        self.play(Write(timers[0]), run_time=0.5)
        for i in range(5):
            self.play(ReplacementTransform(timers[i], timers[i + 1]), run_time=0.5)
            self.wait(0.5)
        self.play(FadeOut(pause), FadeOut(timers[-1]), FadeOut(circ), run_time=2)


    def pos_square(self):
        rectangle = Rectangle(fill_opacity=0.5, color=ORANGE)
        rectangle.set_width(self.l_a/2)
        rectangle.set_height(self.l_b/2)
        drawed_coords = []
        for point in [DL, DR, UL, UR]:
            drawed_coords.append(rectangle.get_corner(point))
        dl, dr, ul, ur = drawed_coords

        rectangle_width, rectangle_height = self.l_a/2, self.l_b/2
        coords_sides = []
        for point in [dr + (LEFT * rectangle_height), ul + (RIGHT * rectangle_height)]:
            coords_sides.append(point)
        DR_l1, UL_r1  = coords_sides


        rectangles = []
        rectangles_coords = [(dr, DR_l1, UL_r1, ur), (DR_l1, dl, ul, UL_r1)]
        rectangles_colors = [ORANGE, ORANGE]

        for rectangle_coords, rectangle_color in zip(rectangles_coords, rectangles_colors):
            rectangle = Polygon(rectangle_coords[0], rectangle_coords[1], rectangle_coords[2], rectangle_coords[3],
                                color=WHITE).set_fill(rectangle_color, self.opacity_triangles) \
                .set_stroke(None, self.line_width)
            rectangles.append(rectangle)


        hor_measure_a = MeasureDistance(Line(dr, DR_l1), invertir=True, dashed=True, buff=0.25).add_tips() \
            .add_tex("1", buff=3, color=GREEN)
        hor_measure_b = MeasureDistance(Line(DR_l1, dl), invertir=True, dashed=True, buff=0.25).add_tips() \
            .add_tex("1", buff=3, color=GREEN)


        vert_measure_a = MeasureDistance(Line(dl, ul), invertir=False, dashed=True, buff=0.25).add_tips() \
            .add_tex("1", buff=2, color=BLUE)
        vert_measure_a[-1].rotate(-PI / 2)
        hor_measure_a[-1].rotate(-PI)
        hor_measure_b[-1].rotate(-PI)
        measures_2 = VGroup(hor_measure_a, hor_measure_b, vert_measure_a)

        joint_pos_squares = VGroup(rectangle, *rectangles, measures_2)
        joint_pos_squares.to_edge(RIGHT, buff=1.7)
        self.joint_pos_squares = joint_pos_squares

        self.measures_2 = measures_2
        self.rectangles = rectangles
        self.rect_ba = rectangles[0]
        self.square_a2 = rectangles[1]

        # Pause to think about it.
        answer = TextMobject("The area of the rectangle is $2$ squared units.").to_corner(DL)
        self.play(Write(answer))
        self.wait(6)
        self.play(FadeOut(answer), run_time=5)


    def transition_squares(self):

        self.play(*[GrowFromCenter(object) for object in [*self.measures_2]], run_time=1)
        self.play(DrawBorderThenFill(self.square_a2), DrawBorderThenFill(self.rect_ba), run_time=1)
        line1 = TextMobject(r"Area", " = ", "2", "$\\times$", "1", " = ", "{}".format(2 * 1)). \
            scale(0.75).move_to(2 * UP)
        line1[0].set_color(ORANGE)
        line1[2].set_color(GREEN)
        line1[4].set_color(BLUE)
        line1[6].set_color(ORANGE)
        self.play(Write(line1))
        self.wait(20)
        self.wait()
        self.play(
            self.title.shift, UP * 3,
            self.joint_pre_square.shift, LEFT * 7,
            VGroup(*self.rectangles).shift, RIGHT * 7,
            self.measures_2.shift, RIGHT * 7
        )



class RectangleDecomposition2(Scene):
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
        "l_a": 3 / 5,
        "l_b": 7 / 5,
        "l_c": 13 / 5,
    }

    def construct(self):
        self.pre_square()
        self.wait(5)
        self.pos_square()
        self.transition_squares()

    def pre_square(self):
        rectangle = Rectangle(fill_opacity=0.5, color=ORANGE)
        rectangle.set_width(self.l_a)
        rectangle.set_height(self.l_b)

        drawed_coords = []
        for point in [DL, DR, UL, UR]:
            drawed_coords.append(rectangle.get_corner(point))
        dl, dr, ul, ur = drawed_coords
        #lin, liz, ls, ld = coords_sides

        horizontal_measure = MeasureDistance(Line(dl, dr), invertir=True, dashed=True, buff=-0.25).add_tips()\
            .add_tex("4", buff=-3.7, color=GREEN)
        vertical_measure = MeasureDistance(Line(dl, ul), invertir=False, dashed=True, buff=0.5).add_tips()\
            .add_tex("2", buff=2, color=BLUE)
        vertical_measure[-1].rotate(-PI/2)
        measures_1 = VGroup(vertical_measure, horizontal_measure)


        title = TextMobject(r"\sc Example: Area Calculation (rectangle, $l=4$, $w=2$)", color=WHITE).to_corner(UL)
        self.title = VGroup(title)
        self.play(Write(title, run_time=1), ShowCreation(rectangle, run_time=1),
                  *[GrowFromCenter(object) for object in [*measures_1]], run_time=1
                  )


        joint_pre_square = VGroup(rectangle)
        self.joint_pre_square = rectangle
        self.joint_pre_square.add(vertical_measure, horizontal_measure)
        self.play(joint_pre_square.to_edge, LEFT, {"buff": 1.7})
        self.square = rectangle

        # Pause to think about it.
        circ = Arc(start_angle=PI / 2, angle=-2 * PI, radius=0.35).to_corner(DL)
        timers = [TexMobject(str(i)).move_to(circ) for i in range(5, -1, -1)]
        pause = TextMobject("Pause the video and find the area of the rectangle.").next_to(circ, RIGHT)
        self.play(ShowCreation(circ), Write(pause))
        self.play(Write(timers[0]), run_time=0.5)
        for i in range(5):
            self.play(ReplacementTransform(timers[i], timers[i + 1]), run_time=0.5)
            self.wait(0.5)
        self.play(FadeOut(pause), FadeOut(timers[-1]), FadeOut(circ), run_time=2)


    def pos_square(self):
        rectangle = Rectangle(fill_opacity=0.5, color=ORANGE)
        rectangle.set_width(self.l_a)
        rectangle.set_height(self.l_b)
        drawed_coords = []
        for point in [DL, DR, UL, UR]:
            drawed_coords.append(rectangle.get_corner(point))
        dl, dr, ul, ur = drawed_coords

        #rectangle_width, rectangle_height = self.l_a, self.l_b
        rectangle_height, rectangle_width = np.sum(dr - dl), np.sum(ul - dl)
        #print("Rectangle width:", self.l_a, rectangle.width, rectangle_width)
        #print("Rectangle height:", self.l_b, rectangle.height, rectangle_height)

        coords_sides = []
        for point in [dr + (0.25* LEFT * rectangle_height),   # DR_l1
                      dr + (0.5* LEFT * rectangle_height),    # DR_l2
                      dr + (0.75* LEFT * rectangle_height),   # DR_l3
                      dl + (0.5 * UP * rectangle_width),      # DL_u1
                      ul + (0.25 * RIGHT * rectangle_height), # UL_r1
                      ul + (0.5 * RIGHT * rectangle_height),       # UL_r2
                      ul + (0.75 * RIGHT * rectangle_height),      # UL_r3
                      ur + (0.5 * DOWN * rectangle_width)     # UR_d1
                      ]:
            coords_sides.append(point)
        #print("HERE", dr-dl)
        DR_l1, DR_l2, DR_l3, DL_u1, UL_r1, UL_r2, UL_r3, UR_d1 = coords_sides

        interior_points = [down_height_point + (0.5 * UP * rectangle_width) for down_height_point in [DR_l1, DR_l2, DR_l3]]


        #|--------------------------------------------------|
        #|  R1    |    R2      |     R3       |     R4      |
        #|--------------------------------------------------|
        #|  R5    |    R6      |     R7       |     R8      |
        #|--------------------------------------------------|
        rectangles = []
        rectangles_coords = [(dr, DR_l1, interior_points[0], UR_d1),  # R8
                             (DR_l1, DR_l2, interior_points[1], interior_points[0]), # R7
                             (DR_l2, DR_l3, interior_points[2], interior_points[1]), # R6
                             (DR_l3, dl, DL_u1, interior_points[2]), # R5

                             (interior_points[2], DL_u1, ul, UL_r1), # R4
                             (interior_points[1], interior_points[2], UL_r1, UL_r2), # R3
                             (interior_points[0], interior_points[1], UL_r2, UL_r3), # R2
                             (UR_d1, interior_points[0], UL_r3, ur) # R1
                             ]
        rectangles_colors = [ORANGE for _ in rectangles_coords]


        for rectangle_coords, rectangle_color in zip(rectangles_coords, rectangles_colors):
            rectangle = Polygon(rectangle_coords[0], rectangle_coords[1], rectangle_coords[2], rectangle_coords[3],
                                color=WHITE).set_fill(rectangle_color, self.opacity_triangles) \
                .set_stroke(None, self.line_width)
            rectangles.append(rectangle)


        hor_measure_a = MeasureDistance(Line(dr, DR_l1), invertir=True, dashed=True, buff=0.25).add_tips() \
            .add_tex("1", buff=3, color=GREEN)
        hor_measure_b = MeasureDistance(Line(DR_l1, DR_l2), invertir=True, dashed=True, buff=0.25).add_tips() \
            .add_tex("1", buff=3, color=GREEN)
        hor_measure_c = MeasureDistance(Line(DR_l2, DR_l3), invertir=True, dashed=True, buff=0.25).add_tips() \
            .add_tex("1", buff=3, color=GREEN)
        hor_measure_d = MeasureDistance(Line(DR_l3, dl), invertir=True, dashed=True, buff=0.25).add_tips() \
            .add_tex("1", buff=3, color=GREEN)

        vert_measure_a = MeasureDistance(Line(dl, DL_u1), invertir=False, dashed=True, buff=0.25).add_tips() \
            .add_tex("1", buff=2, color=BLUE)
        vert_measure_b = MeasureDistance(Line(DL_u1, ul), invertir=False, dashed=True, buff=0.25).add_tips() \
            .add_tex("1", buff=2, color=BLUE)
        vert_measure_a[-1].rotate(-PI / 2)
        vert_measure_b[-1].rotate(-PI / 2)

        hor_measure_a[-1].rotate(-PI)
        hor_measure_b[-1].rotate(-PI)
        hor_measure_c[-1].rotate(-PI)
        hor_measure_d[-1].rotate(-PI)
        measures_2 = VGroup(vert_measure_a, vert_measure_b, hor_measure_a, hor_measure_b, hor_measure_c,
                            hor_measure_d)

        joint_pos_squares = VGroup(rectangle, *rectangles, measures_2)
        joint_pos_squares.to_edge(RIGHT, buff=1.7)
        self.joint_pos_squares = joint_pos_squares

        self.measures_2 = measures_2
        self.rectangles = rectangles

        # Pause to think about it.
        answer = TextMobject("The area of the rectangle is $8$ squared units.").to_corner(DL)
        self.play(Write(answer))
        self.wait(10)
        self.play(FadeOut(answer), run_time=5)



    def transition_squares(self):

        self.play(*[GrowFromCenter(object) for object in [*self.measures_2]], run_time=1)
        self.play(DrawBorderThenFill(self.rectangles[0]), DrawBorderThenFill(self.rectangles[1]),
                  DrawBorderThenFill(self.rectangles[2]), DrawBorderThenFill(self.rectangles[3]),
                  DrawBorderThenFill(self.rectangles[4]), DrawBorderThenFill(self.rectangles[5]),
                  DrawBorderThenFill(self.rectangles[6]), DrawBorderThenFill(self.rectangles[7]),
                  run_time=1)
        line1 = TextMobject(r"Area", " = ", "4", "$\\times$", "2", " = ", "{}".format(4 * 2)). \
            scale(0.75).move_to(2 * UP)
        line1[0].set_color(ORANGE)
        line1[2].set_color(GREEN)
        line1[4].set_color(BLUE)
        line1[6].set_color(ORANGE)
        self.play(Write(line1))

        self.wait(20)
        self.wait()
        self.play(
            self.title.shift, UP * 3,
            self.joint_pre_square.shift, LEFT * 7,
            VGroup(*self.rectangles).shift, RIGHT * 7,
            self.measures_2.shift, RIGHT * 7
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


########################
### OUTSIDE PROJECT ####
########################

class TheoremBox(Scene):
    def construct(self):
        circuit = TextMobject(r"""
        \begin{tcolorbox}
        \begin{theorem}
        Considerons cela.
        \end{theorem}
        \end{tcolorbox}
            """, color=ORANGE
            )
        circuit.scale(0.75)
        #circuit.set_color(RED)
        #circuit.set_fill(BLUE)
        self.play(Write(circuit))
        self.wait()


class TheoremColoredBox(Scene):
    def construct(self):
        circuit = TextMobject(r"""
            \BlueBox[label=exsecond]{}{\lipsum[2]}      
        """
        )
        circuit.scale(0.55)
        self.play(Write(circuit))
        self.wait()


class TheoremExample(Scene):
    def construct(self):
        circuit = TextMobject(r"""
            \begin{theorem}
            Let $f$ be a function whose derivative exists in every point, then $f$ 
            is a continuous function.
            \end{theorem}
            """
            )
        circuit.scale(0.75)
        self.play(Write(circuit))
        self.wait()


class DefinitionExample(Scene):
    def construct(self):
        circuit = TextMobject(r"""
            \begin{definition}
            Let $f$ be a function whose derivative exists in every point, then $f$ 
            is a continuous function.
            \end{definition}
            """
            )
        circuit.scale(0.75)
        self.play(Write(circuit))
        self.wait()