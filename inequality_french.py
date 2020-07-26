from manimlib.imports import *


# 0. ThumbnailFrench
# 1. ShowImageAndQuote
# 2. Application
# 3. Definition
# 4. Notation
# 5. ExampleInequality1
# 6. ExempleEquality
# 7. ExempleInequality2
# 8. Proprietes
# 9. RegleOr

# 9.4 RegleOrEx1
# 9.8 RegleOrEx2 (TO-DO)

# 10. RegleOrExemples
# 11. Inequation
# 12. InequationVerif
# 13. InequationEx
# 14. InequationSol
# 15. InequationExoSup
# 16. Conclusion


class ThumbnailEnglish(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/images/"
        image_peinture = ImageMobject(path + "Perfectly_balanced")
        image_peinture.scale(3.25)
        image_peinture.to_edge(DOWN)


        line_e = TextMobject(r"{\sc I am great!").scale(1.5).shift(1.25 * UP + 4 * LEFT).set_color(BLUE)
        line_pi = TextMobject(r"{\sc Haha! I am", r"\sc greater than you!").scale(1.5).set_color(YELLOW)
        line_pi[0].next_to(2.25 * UP + 0.5 * RIGHT)
        line_pi[1].next_to(1.25 * UP + 0.5 * LEFT)

        line2 = TextMobject("$e$", " $<$ ","$\pi$")
        line2[0].scale(6).next_to(1.5 * DOWN + 4 * LEFT).set_color(BLUE)
        line2[1].scale(8).next_to(1.5 * DOWN + 1.5 * LEFT).set_color(WHITE)
        line2[2].scale(12).next_to(1.5 * DOWN + 1.5 * RIGHT).set_color(YELLOW)
        #line2.next_to(0.5 * DOWN + 2 * LEFT)
        #prob = TexMobject(r"\text{Find }T_n=A_n+B_n").scale(2).shift(2 * DOWN)
        #self.play(FadeIn(image_peinture))
        self.play(Write(line2), Write(line_e), Write(line_pi))

        self.wait(5)

class ThumbnailFrench(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        line_e = TextMobject(r"{\sc Je suis grand!").scale(1.5).shift(1.25 * UP + 4 * LEFT).set_color(BLUE)
        line_pi = TextMobject(r"{\sc Haha! Pas ", r"\sc autant que moi!").scale(1.5).set_color(YELLOW)
        line_pi[0].next_to(2.25 * UP + 0.5 * RIGHT)
        line_pi[1].next_to(1.25 * UP + 0.5 * LEFT)

        line2 = TextMobject("$e$", " $<$ ","$\pi$")
        line2[0].scale(6).next_to(1.5 * DOWN + 4 * LEFT).set_color(BLUE)
        line2[1].scale(8).next_to(1.5 * DOWN + 1.5 * LEFT).set_color(WHITE)
        line2[2].scale(12).next_to(1.5 * DOWN + 1.5 * RIGHT).set_color(YELLOW)
        #line2.next_to(0.5 * DOWN + 2 * LEFT)
        #prob = TexMobject(r"\text{Find }T_n=A_n+B_n").scale(2).shift(2 * DOWN)
        #self.play(FadeIn(image_peinture))
        self.play(Write(line2), Write(line_e), Write(line_pi))

        self.wait(5)


class ShowImageAndQuote(Scene):
    def construct(self):
        quote = TextMobject(r"Une in\'egalit\'e exprime la domination d'un terme par rapport \`a un autre, d'une entit\'e par rapport \`a une autre.")
        quote.scale(0.7)
        quote.set_color(RED)
        quote.to_edge(UP)
        author = TextMobject(r"-Cédric Villani")
        author.scale(0.7)
        author.move_to(np.array([3.5, 2, 0]))
        self.play(FadeIn(quote))
        self.play(FadeIn(author))

        path = r"C:/Users/Utilisateur/Desktop/CEGEP/"
        image = ImageMobject(path + "new_file")
        image.scale(3)
        image.to_edge(DOWN)
        self.play(FadeIn(image))
        self.wait(2)
        self.play(FadeOut(image))
        self.play(FadeOut(author))
        self.play(FadeOut(quote))


class Application(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Applications}", color=WHITE).to_corner(UL)

        path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/images/"
        image_applications = ImageMobject(path + "selling_items")
        image_applications.scale(3)
        image_applications.to_edge(DOWN)

        self.play(Write(title))
        self.play(FadeIn(image_applications))
        self.wait(40)


class Definition(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW],
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Définition}", color=WHITE).to_corner(UL)
        definition = TextMobject(r"En mathématiques, une inégalité est un énoncé permettant de comparer la taille, ou l'ordre de deux objets.")
        definition.scale(0.7)
        definition.move_to(np.array([0, 2, 0]))
        definition.set_color(BLUE)

        # DRAW A REAL NUMBER LINE
        line = NumberLine(color=BLUE)
        line.add_numbers()
        set_number = TexMobject("\\mathbb{R}")
        set_number.next_to(line.n2p(1)+np.array([0,1,0]), RIGHT, buff=5.5)


        self.play(Write(title))
        self.play(FadeIn(definition))
        self.add(line)
        self.play(Write(set_number))
        #self.play(Write(number_line), Write(set_number))
        self.wait(35)


class Notation(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Apprendre à lire}", color=WHITE).to_corner(UL)

        compl_rules_str = [
            "",
            " $a<b$ signifie que $a$ est strictement inférieur à $b$;",
            " $a>b$ signifie que $a$ est strictement supérieur à $b$;",
            " $a\leq b$ signifie que $a$ est inférieur ou égal à $b$;",
            " $a\geq b$ signifie que $a$ est supérieur ou égal à $b$;"
        ]

        def choose_color(i):
            color = BLUE if i<=2 else YELLOW
            return color

        rules = [TextMobject("{}) {}".format(i, rule), color=choose_color(i)) for i, rule in enumerate(compl_rules_str)]
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
        self.wait(5)
        self.play(Write(rules[3]))
        self.wait(5)
        self.play(Write(rules[4]))
        self.wait(10)


class ExampleEquality(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\sc Exemple: $a=b$}", color=WHITE).to_corner(UL)
        self.play(Write(title))

        a = TextMobject("$a=3$",color=GREEN)
        a.next_to(2 * UP + 7 * LEFT)
        b = TextMobject("$b=3$", color=RED)
        b.next_to(1.5 * UP + 7 * LEFT)
        self.play(Write(a), Write(b))


        line = NumberLine(color=BLUE)
        line.add_numbers()
        self.add(line)
        set_number = TexMobject("\\mathbb{R}")
        set_number.next_to(line.n2p(1) + np.array([0, 1, 0]), RIGHT, buff=5.5)
        self.play(Write(set_number))


        arrow_2 = Vector([3, 0, 0])
        desc_2 = line.numbers[7 + 3].copy()
        desc_2_target = TexMobject('3')
        arrow_3 = Vector([3, 0, 0])
        desc_3 = line.numbers[7 + 3].copy()
        desc_3_target = TexMobject('3')

        VGroup(arrow_2, desc_2_target).set_color(GREEN)
        VGroup(arrow_3, desc_3_target).set_color(RED)

        arrow_2.shift([0, 0.1, 0])
        desc_2_target.next_to(arrow_2, UP)
        arrow_3.shift([0, -0.1, 0])
        desc_3_target.next_to(arrow_3, DOWN)

        self.wait(3) # 4.3
        self.play(
            ShowCreation(arrow_2),
            Transform(desc_2, desc_2_target)
            )
        green_dot = Dot([3, 0, 0])
        green_dot.set_color(GREEN)
        self.play(ShowCreation(green_dot))
        self.wait(5)

        self.play(
            ShowCreation(arrow_3),
            Transform(desc_3, desc_3_target)
        )
        red_dot = Dot([3, 0, 0])
        red_dot.set_color(RED)
        self.play(ShowCreation(red_dot))
        self.wait(5)

        #inequality = TextMobject("$2=a<b=3$")
        inequality = TextMobject("$3=a$",
                                 " $=$ ",
                                 "$b=3$")
        inequality[0].set_color(GREEN)
        inequality[2].set_color(RED)
        inequality.next_to(3 * DOWN + 2 * LEFT)
        self.play(Write(inequality))
        self.wait(10)



class ExampleInequality1(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\sc Exemple: $a<b$}", color=WHITE).to_corner(UL)
        self.play(Write(title))

        a = TextMobject("$a=2$",color=GREEN)
        a.next_to(2 * UP + 7 * LEFT)
        b = TextMobject("$b=3$", color=RED)
        b.next_to(1.5 * UP + 7 * LEFT)
        self.play(Write(a), Write(b))


        line = NumberLine(color=BLUE)
        line.add_numbers()
        self.add(line)
        set_number = TexMobject("\\mathbb{R}")
        set_number.next_to(line.n2p(1) + np.array([0, 1, 0]), RIGHT, buff=5.5)
        self.play(Write(set_number))


        arrow_2 = Vector([2, 0, 0])
        desc_2 = line.numbers[7 + 2].copy()
        desc_2_target = TexMobject('2')
        arrow_3 = Vector([3, 0, 0])
        desc_3 = line.numbers[7 + 3].copy()
        desc_3_target = TexMobject('3')

        VGroup(arrow_2, desc_2_target).set_color(GREEN)
        VGroup(arrow_3, desc_3_target).set_color(RED)

        arrow_2.shift([0, 0.1, 0])
        desc_2_target.next_to(arrow_2, UP)
        arrow_3.shift([0, -0.1, 0])
        desc_3_target.next_to(arrow_3, DOWN)

        self.wait(3) # 4.3
        self.play(
            ShowCreation(arrow_2),
            Transform(desc_2, desc_2_target)
            )
        green_dot = Dot([2, 0, 0])
        green_dot.set_color(GREEN)
        self.play(ShowCreation(green_dot))
        self.wait(5)

        self.play(
            ShowCreation(arrow_3),
            Transform(desc_3, desc_3_target)
        )
        red_dot = Dot([3, 0, 0])
        red_dot.set_color(RED)
        self.play(ShowCreation(red_dot))
        self.wait(5)

        #inequality = TextMobject("$2=a<b=3$")
        inequality = TextMobject("$2=a$",
                                 " $<$ ",
                                 "$b=3$")
        inequality[0].set_color(GREEN)
        inequality[2].set_color(RED)
        inequality.next_to(3 * DOWN + 2 * LEFT)
        self.play(Write(inequality))
        self.wait(10)


class ExampleInequality2(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\sc Exemple: $a>b$}", color=WHITE).to_corner(UL)
        self.play(Write(title))

        a = TextMobject("$a=3$",color=GREEN)
        a.next_to(2 * UP + 7 * LEFT)
        b = TextMobject("$b=2$", color=RED)
        b.next_to(1.5 * UP + 7 * LEFT)
        self.play(Write(a), Write(b))


        line = NumberLine(color=BLUE)
        line.add_numbers()
        self.add(line)


        arrow_2 = Vector([3, 0, 0])
        desc_2 = line.numbers[7 + 3].copy()
        desc_2_target = TexMobject('3')
        arrow_3 = Vector([2, 0, 0])
        desc_3 = line.numbers[7 + 2].copy()
        desc_3_target = TexMobject('2')

        VGroup(arrow_2, desc_2_target).set_color(GREEN)
        VGroup(arrow_3, desc_3_target).set_color(RED)

        arrow_2.shift([0, 0.1, 0])
        desc_2_target.next_to(arrow_2, UP)
        arrow_3.shift([0, -0.1, 0])
        desc_3_target.next_to(arrow_3, DOWN)

        self.wait(3) # 4.3
        self.play(
            ShowCreation(arrow_2),
            Transform(desc_2, desc_2_target)
            )
        green_dot = Dot([3, 0, 0])
        green_dot.set_color(GREEN)
        self.play(ShowCreation(green_dot))
        self.wait(5)

        self.play(
            ShowCreation(arrow_3),
            Transform(desc_3, desc_3_target)
        )

        red_dot = Dot([2, 0, 0])
        red_dot.set_color(RED)
        self.play(ShowCreation(red_dot))
        self.wait(5)

        #inequality = TextMobject("$2=a<b=3$")
        inequality = TextMobject("$3=a$",
                                 " $>$ ",
                                 "$b=2$")
        inequality[0].set_color(GREEN)
        inequality[2].set_color(RED)
        inequality.next_to(3 * DOWN + 2 * LEFT)
        self.play(Write(inequality))
        self.wait(10)


class Proprietes(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Propriétés des inégalités}", color=WHITE).to_corner(UL)

        compl_rules_str = [
            "",
            " Quels que soient $x, y \in\mathbb{R}$, une et une seule des trois possibilités suivantes est réalisée : $x > y$, $x = y$, $x < y$;",
            " Quels que soient $x, y$ et $z\in\mathbb{R}$, $x > y$ et $y > z$ entraînent $x > z$.",
            " Quels que soient $x, y$ et $z\in\mathbb{R}$, $x > y$ entraîne $x + z > y + z$;",
            " Quels que soient $x, y$ et $z\in\mathbb{R}$, $x > y$ et $z > 0$ entraînent $xz > yz$."
        ]

        def choose_color(i):
            color = BLUE if i<=1 else YELLOW
            return color

        rules = [TextMobject("P{}) {}".format(i, rule), color=choose_color(i)) for i, rule in enumerate(compl_rules_str)]
        rules = [rule.scale(0.7) for rule in rules]

        for (i, rule) in enumerate(rules):
            if i != 0:
                rule.next_to(rules[0].get_center() - rule.get_center() + np.array([-6, -0.5 + -0.7 * i, 0]))
        rules = VGroup(*rules)
        rules.to_corner(LEFT + UP)

        self.play(Write(title))
        self.wait(10)
        self.play(Write(rules[1]))
        self.wait(10)
        self.play(Write(rules[2]))
        self.wait(10)
        self.play(Write(rules[3]))
        self.wait(10)
        self.play(Write(rules[4]))
        self.wait(20)



class Proprietes1(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Propriétés des inégalités}", color=WHITE).to_corner(UL)

        compl_rules_str = [
            "",
            " Quels que soient $x, y \in\mathbb{R}$, une et une seule des trois possibilités suivantes est réalisée : $x > y$, $x = y$, $x < y$;",
            " Quels que soient $x, y$ et $z\in\mathbb{R}$, $x > y$ et $y > z$ entraînent $x > z$.",
            " Quels que soient $x, y$ et $z\in\mathbb{R}$, $x > y$ entraîne $x + z > y + z$;",
            " Quels que soient $x, y$ et $z\in\mathbb{R}$, $x > y$ et $z > 0$ entraînent $xz > yz$."
        ]

        def choose_color(i):
            color = BLUE if i<=10 else YELLOW
            return color

        rules = [TextMobject("P{}) {}".format(i, rule), color=choose_color(i)) for i, rule in enumerate(compl_rules_str)]
        rules = [rule.scale(0.7) for rule in rules]

        for (i, rule) in enumerate(rules):
            if i != 0:
                rule.next_to(rules[0].get_center() - rule.get_center() + np.array([-6, -0.5 + -0.7 * i, 0]))
        rules = VGroup(*rules)
        rules.to_corner(LEFT + UP)

        self.play(Write(title))
        self.wait(10)
        self.play(Write(rules[1]))
        self.wait(5)
        self.play(Write(rules[2]))
        self.wait(5)
        self.play(Write(rules[3]))
        self.wait(5)
        self.play(Write(rules[4]))
        self.wait(10)


class RegleOr(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Fonction et Inégalité}", color=GOLD).to_corner(UL)

        definition = TextMobject(r"""
                            \RedBox[label=exsecond]{}{
                            Toute fonction $f:\mathbb{R}\rightarrow\mathbb{R}$ strictement croissante peut être appliquée aux deux termes d'une inégalité tout en la conservant. 
                            \begin{equation}
                            a > b \Rightarrow f(a) > f(b)
                            \end{equation}
                            Si on applique une fonction $f:\mathbb{R}\rightarrow\mathbb{R}$ strictement décroissante, il faut alors changer le signe de l'inégalité en son opposé.
                            \begin{equation}
                            a > b \Rightarrow f(a) < f(b)
                            \end{equation} 
                            }      
                        """
                                 )
        definition.scale(0.5)
        definition.next_to(0 * UP + 5.5 * LEFT)

        self.play(Write(title))
        self.wait(10)
        self.play(FadeIn(definition))
        self.wait(45)
        self.play(FadeOut(definition))
        self.play(FadeOut(title))



class RegleOrEx1(GraphScene):
    """
    Linear function on interval [-10, 10]
    """
    CONFIG = {
        "y_max" : 5,
        "y_min" : 0,
        "x_max" : 5,
        "x_min" : -5,
        "y_tick_frequency" : 1,
        "x_tick_frequency" : 0.5,
        "axes_color" : BLUE,
        "y_labeled_nums": range(0,6,1),
        "x_labeled_nums": list(np.arange(-5, 6, 1)),
        "x_label_decimal":0,
        "y_label_decimal":0,
        "graph_origin": np.array((0, -2.5, 0))
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : x,
                                    color = WHITE,
                                    x_min = self.x_min,
                                    x_max = self.x_max
                                    )

        # Vertical line (for a=1)
        fa1_coords = self.coords_to_point(1, 0)
        fa2_coords = self.coords_to_point(1, 1)
        vertical_line_a = Line(fa1_coords, fa2_coords, color=RED)
        a_value = TextMobject(r"$a$", color=RED)
        a_value.scale(0.8)
        a_value.move_to(self.coords_to_point(1.25, 0.5))

        # Horizontal line (for f(a)=1)
        a1, f_a1 = 0, 1
        a2, f_a2 = 1, 1
        fa1_coords = self.coords_to_point(a1, f_a1)
        fa2_coords = self.coords_to_point(a2, f_a2)
        horizontal_line_a = Line(fa1_coords, fa2_coords, color=RED)
        fa_value = TextMobject(r"$f(a)$", color=RED)
        fa_value.scale(0.8)
        fa_value.move_to(self.coords_to_point(0.5, 1.25))

        # Animated horizontal lines and vertical lines.
        xs_left = np.arange(-np.pi, np.pi, 0.05)
        xs_right = [x_left + np.pi / 2 for x_left in xs_left]
        ys = [np.cos(x_left) for x_left in xs_left]

        xys_left = [self.coords_to_point(x_left, y) for x_left, y in zip(xs_left, ys)]
        xys_right = [self.coords_to_point(x_right, y) for x_right, y in zip(xs_right, ys)]

        horizontal_lines = []
        for xy_left, xy_right in zip(xys_left, xys_right):
            horizontal_line = Line(xy_left, xy_right, color=GREEN)
            horizontal_lines.append(horizontal_line)

        # a = 1 et b>a
        a_eq = TextMobject(r"$a=1$")
        a_eq.move_to(3*UP + 6*LEFT).set_color(RED)
        a_b_ineq = TextMobject(r"$b$", r" $>$ ", r"$a$")
        a_b_ineq[0].set_color(GREEN)
        a_b_ineq[2].set_color(RED)
        a_b_ineq.move_to(2.5 * UP + 6 * LEFT)

        # Horizontal line (for f(b)=3)
        fb1_coords = self.coords_to_point(0, 1.5)
        fb2_coords = self.coords_to_point(1.5, 1.5)
        horizontal_line_b = Line(fb1_coords, fb2_coords, color=GREEN)
        fb_value = TextMobject(r"$f(b)$", color=GREEN)
        fb_value.scale(0.8)
        fb_value.move_to(self.coords_to_point(0.5, 1.75))

        # Vertical line (for b=3)
        fb1_coords = self.coords_to_point(1.5, 0)
        fb2_coords = self.coords_to_point(1.5, 1.5)
        vertical_line_b = Line(fb1_coords, fb2_coords, color=GREEN)
        b_value = TextMobject(r"$b$", color=GREEN)
        b_value.scale(0.8)
        b_value.move_to(self.coords_to_point(1.75, 0.5))

        graph_lab = self.get_graph_label(graph, label="f(x)=x")
        self.play(ShowCreation(graph), ShowCreation(graph_lab), run_time = 2)
        self.wait(10)
        self.play(ShowCreation(a_eq))
        self.play(ShowCreation(a_b_ineq))
        self.wait(10)
        self.play(ShowCreation(a_value), ShowCreation(vertical_line_a)) #ShowCreation(horizontal_line_a)
        self.play(ShowCreation(b_value), ShowCreation(vertical_line_b))
        self.wait(10)
        self.play(ShowCreation(horizontal_line_a), ShowCreation(fa_value))
        self.play(ShowCreation(horizontal_line_b), ShowCreation(fb_value))

        values = np.arange(1.5, 5, 0.1)
        x_values = [self.coords_to_point(0, value) for value in values]
        y_values = [self.coords_to_point(value, 0) for value in values]
        images_values = [self.coords_to_point(value, value) for value in values]

        horizontal_lines, vertical_lines, new_fb_values, new_b_values = [], [], [], []
        for i, (x_value, y_value, image_value) in enumerate(zip(x_values, y_values, images_values)):
            horizontal_line = Line(x_value, image_value, color=GREEN)
            horizontal_lines.append(horizontal_line)

            vertical_line = Line(y_value, image_value, color=GREEN)
            vertical_lines.append(vertical_line)

            new_b_value = TextMobject(r"$b$", color=GREEN)
            new_b_value.scale(0.8)
            new_b_value.move_to(self.coords_to_point(1.75 + 0.10*i, 0.5+ 0.10*i))
            new_b_values.append(new_b_value)

            new_fb_value = TextMobject(r"$f(b)$", color=GREEN)
            new_fb_value.scale(0.8)
            new_fb_value.move_to(self.coords_to_point(0.5 + 0.10 * i, 1.75 + 0.10 * i))
            new_fb_values.append(new_fb_value)


        for i, (horizontal_line, vertical_line, new_fb_value, new_b_value) in enumerate(zip(horizontal_lines, vertical_lines, new_fb_values, new_b_values)):
            if i==0:
                self.play(ReplacementTransform(horizontal_line_b, horizontal_line), run_time = 0.025)
                self.play(ReplacementTransform(vertical_line_b, vertical_line), run_time=0.025)
                self.play(ReplacementTransform(b_value, new_b_value), run_time=0.025)
                self.play(ReplacementTransform(fb_value, new_fb_value), run_time=0.025)
                old_horizontal_line = horizontal_line
                old_vertical_line = vertical_line
                old_fb_value = new_fb_value
                old_b_value = new_b_value
            else:
                self.play(ReplacementTransform(old_horizontal_line, horizontal_line), run_time = 0.025)
                self.play(ReplacementTransform(old_vertical_line, vertical_line), run_time=0.025)
                self.play(ReplacementTransform(old_b_value, new_b_value), run_time=0.025)
                self.play(ReplacementTransform(old_fb_value, new_fb_value), run_time=0.025)
                old_horizontal_line = horizontal_line
                old_vertical_line = vertical_line
                old_fb_value = new_fb_value
                old_b_value = new_b_value


        #self.play(ShowCreation(b_value), ShowCreation(vertical_line_b), ShowCreation(horizontal_line_b))
        self.wait(25)



class RegleOrExemples(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Cas particuliers}", color=GOLD).to_corner(UL)

        definition = TextMobject(r"""
                \begin{itemize}
                \item \underline{$f(x)=x + c$}: Soient $a, b, c\in\mathbb{R}$, si $a > b$ alors $f(a) = a + c > b + c = f(b)$,
                \item \underline{$f(x)=x - c$}: Soient $a, b, c\in\mathbb{R}$, si $a > b$ alors $f(a) = a - c > b - c = f(b)$,
                \item \underline{$f(x)=cx$}: 
                    \begin{itemize}
                    \item Soient $a, b\in\mathbb{R}$ et $c>0$, si $a > b$ alors $f(a) = ca > cb = f(b)$;
                    \item Soient $a, b\in\mathbb{R}$ et $c<0$, si $a > b$ alors $f(a) = ca < cb = f(b)$
                    \end{itemize} 
                \end{itemize}
                """)
        definition.scale(0.7)
        definition.move_to(np.array([-1, 1, 0]))
        definition.set_color(BLUE)

        self.play(Write(title))
        self.wait(10)
        self.play(FadeIn(definition))

        self.wait(55)
        self.play(FadeOut(definition))
        self.play(FadeOut(title))



class Inequation(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Définition: Inéquation}", color=GOLD).to_corner(UL)
        definition = TextMobject(
            r"Une inéquation est une inégalité qui devient vraie ou fausse selon la valeur de la(ou les) variable(s).")
        definition.scale(0.8)
        definition.move_to(np.array([0, 2, 0]))
        definition.set_color(BLUE)

        self.play(Write(title))
        self.wait(7)
        self.play(FadeIn(definition))

        self.wait(20)
        self.play(FadeOut(definition))
        self.play(FadeOut(title))


class InequationVerif(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    # TO-DO :
    # Time limit. Find the answers.
    # Put the solution on both sides.
    def construct(self):
        title = TextMobject(r"\underline{\sc Exemple: Inéquation}").to_corner(UL)
        definition = TextMobject(
            r"Soit l'inéquation ",
            r" $3x$", r" $>$ ", r"$2x-3$. ",
            "Est-ce que cette inéquation est respectée pour $x=-4$? Et pour $x=0$?")
        definition[1].set_color(BLUE)
        definition[3].set_color(YELLOW)
        definition.scale(0.7)
        definition.move_to(np.array([0, 2, 0]))
        #definition.set_color(BLUE)


        # Question 1
        question_1 = TextMobject(r"\underline{Si $x=-4$?}")
        answer_1_p1 = TextMobject(r"$3(-4)=-12$").set_color(BLUE)
        answer_1_p2 = TextMobject(r"$2(-4)-3=-11$").set_color(YELLOW)
        answer_1_p3 = TextMobject(r"$-12$ ", r"$\ngtr$",r" $-11$")
        final_answer_1 = TextMobject(r"Non").set_color(RED)
        answer_1_p3[0].set_color(BLUE)
        answer_1_p3[2].set_color(YELLOW)
        #question_1.scale(0.8)
        question_1.move_to(np.array([-4.75, 1, 0]))
        answer_1_p1.move_to(np.array([-4.5, 0.25, 0]))
        answer_1_p2.move_to(np.array([-4.1, -0.5, 0]))
        answer_1_p3.move_to(np.array([-4.95, -1.25, 0]))
        final_answer_1.move_to(np.array([-4.95, -2.25, 0]))

        # Question 2
        question_2 = TextMobject(r"\underline{Si $x=0$?}")
        answer_2_p1 = TextMobject(r"$3(0)=0$").set_color(BLUE)
        answer_2_p2 = TextMobject(r"$2(0)-3=-3$").set_color(YELLOW)
        answer_2_p3 = TextMobject(r"$0$ ", r"$>$", r" $-3$")
        final_answer_2 = TextMobject(r"Oui").set_color(GREEN)
        answer_2_p3[0].set_color(BLUE)
        answer_2_p3[2].set_color(YELLOW)
        #question_2.scale(0.8)
        question_2.move_to(np.array([1.5, 1, 0]))
        answer_2_p1.move_to(np.array([1.25, 0.25, 0]))
        answer_2_p2.move_to(np.array([1.9, -0.5, 0]))
        answer_2_p3.move_to(np.array([1.25, -1.25, 0]))
        final_answer_2.move_to(np.array([1.15, -2.25, 0]))


        self.play(Write(title))
        self.wait(5)
        self.play(FadeIn(definition))

        # Question 1 and 2
        self.wait(10)
        self.play(Write(question_1))
        self.wait(5)
        self.play(Write(question_2))
        self.wait(5)


        self.wait(5)
        self.play(Write(answer_1_p1))
        self.wait(5)
        self.play(Write(answer_1_p2))
        self.wait(5)
        self.play(Write(answer_1_p3))
        self.play(Write(final_answer_1))
        self.wait(5)

        # Question 2
        #self.play(Write(question_2))
        self.wait(5)
        self.play(Write(answer_2_p1))
        self.wait(5)
        self.play(Write(answer_2_p2))
        self.wait(5)
        self.play(Write(answer_2_p3))
        self.play(Write(final_answer_2))
        self.wait(15)

        self.play(FadeOut(definition))
        self.play(FadeOut(title))



class InequationEx(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    # TO-DO :
    # Time limit. Find the answers.
    # Put the solution on both sides.
    def construct(self):
        title = TextMobject(r"\underline{\sc Résoudre une Inéquation}").to_corner(UL)
        eq_0_str = r" $3-2x<x+9$"
        definition = TextMobject(
            r"Trouvez les solutions de l'inéquation: ",
            eq_0_str)
        #definition.scale(0.7)
        definition.move_to(np.array([0, 2, 0]))


        self.play(Write(title))
        self.wait(5)
        self.play(FadeIn(definition))
        self.wait(5)

        # Pause to think about it.
        circ = Arc(start_angle=PI / 2, angle=-2 * PI, radius=0.35).to_corner(DL)
        timers = [TexMobject(str(i)).move_to(circ) for i in range(5, -1, -1)]
        pause = TextMobject("Faites pause et trouvez la solution.").next_to(circ, RIGHT)
        self.play(ShowCreation(circ), Write(pause))
        self.play(Write(timers[0]), run_time=0.5)
        for i in range(5):
            self.play(ReplacementTransform(timers[i], timers[i + 1]), run_time=0.5)
            self.wait(0.5)
        self.play(FadeOut(pause), FadeOut(timers[-1]), FadeOut(circ), run_time=2)

        answer = TextMobject("Solution: $x>-2$").to_corner(DL)
        self.play(Write(answer))
        self.wait(10)
        self.play(FadeOut(definition))
        self.play(FadeOut(title))



class InequationSol(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }

    def construct(self):
        title = TextMobject(r"\underline{\sc Solution de l'inéquation}").to_corner(UL)
        eq_0_str = r"$3-2x<x+9$"
        eq_1_str = r" $-x-2x<9-3$"
        eq_2_str = r" $-3x<6$"
        eq_3_str = r" $x>-2$"
        exercise_description = TextMobject(
            r"Trouvez les solutions de l'inéquation: ",
            r"$3$", r"$-2$", r"$x$", r" $<$ ", r"$x$","$+$","$9$")
        exercise_description[3].set_color(YELLOW)
        exercise_description[5].set_color(YELLOW)
        #exercise_description.scale(0.7)
        exercise_description.move_to(np.array([0, 2, 0]))

        # Solution: Line 1
        exercise_solution_line_1 = TextMobject(r"$3$", r"$-2$", r"$x$", r" $<$ ", r"$x$","$+$","$9$",
                                        r" $\Leftrightarrow$ ",
                                        r"$-$", r"$x$", r"$-$", r"2", r"x", r" $<$ ", r"$9-3$")
        exercise_solution_line_1[2].set_color(YELLOW)
        exercise_solution_line_1[4].set_color(YELLOW)
        exercise_solution_line_1[9].set_color(YELLOW)
        exercise_solution_line_1[12].set_color(YELLOW)
        exercise_solution_line_1.move_to(np.array([-3, 1, 0]))

        # Solution: Line 2
        exercise_solution_line_2 = TextMobject(r" $\Leftrightarrow$ ",
                                               r"$-3$", r"$x$", r" $<$ ", r"$6$")
        exercise_solution_line_2[2].set_color(YELLOW)
        exercise_solution_line_2.move_to(np.array([-2.25, 0, 0]))

        # Solution: Line 3
        exercise_solution_line_3 = TextMobject(r" $\Leftrightarrow$ ",
                                               r"$x$", r" $>$ ", r"$-2$")
        exercise_solution_line_3[1].set_color(YELLOW)
        exercise_solution_line_3.move_to(np.array([-2.36, -1, 0]))

        # Les notations
        notation_ensemble = TextMobject(r" Ensemble : $\{x\in\mathbb{R} \ |\ x>2\}$")
        notation_ensemble.move_to(np.array([-3.75, -2, 0]))
        notation_intervalle = TextMobject(r" Intervalle : $x \in\ ]2,\infty[$")
        notation_intervalle.move_to(np.array([-4.3, -3, 0]))


        self.play(Write(title))
        self.wait(10)
        self.play(FadeIn(exercise_description))
        self.wait(10)

        self.play(Write(exercise_solution_line_1))
        self.wait(5)
        self.play(Write(exercise_solution_line_2))
        self.wait(5)
        self.play(Write(exercise_solution_line_3))
        self.wait(15)

        self.play(Write(notation_ensemble))
        self.play(Write(notation_intervalle))
        self.wait(10)



class InequationInt(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }

    def construct(self):
        title = TextMobject(r"\underline{\sc Interprétaton visuelle}").to_corner(UL)
        exercise_description = TextMobject(r"Soit les solutions $x<-2$: ")
        exercise_description.move_to(np.array([0, 2, 0]))

        # DRAW A REAL NUMBER LINE
        line = NumberLine(color=BLUE)
        line.add_numbers()
        set_number = TexMobject("\\mathbb{R}")
        set_number.next_to(line.n2p(1) + np.array([0, 1, 0]), RIGHT, buff=5.5)

        #green_dot = Dot([-2, 0, 0])
        white_dot = Circle(radius=0.1).move_to([-2, 0, 0])
        white_dot.set_color(WHITE)


        # Region of Solution
        horizontal_line = Line(np.array([-7.5, 0, 0]), np.array([-2, 0, 0]), color=WHITE)


        self.play(Write(title))
        self.wait(10)
        self.play(FadeIn(exercise_description))
        self.wait(5)
        self.add(line)
        self.play(Write(set_number))
        self.play(ShowCreation(white_dot))
        self.wait(5)
        self.play(ShowCreation(horizontal_line))
        self.wait(15)



class InequationExoSup(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    # TO-DO :
    # Time limit. Find the answers.
    # Put the solution on both sides.
    def construct(self):
        title = TextMobject(r"\underline{\sc Exercices supplémentaires}").to_corner(UL)
        exos = TextMobject(r" Trouvez les ensembles de solutions des inéquations:",
        r"""
        \begin{enumerate}
        \item $3(x-2)-2(x-5)>16+x$,
        \item $-4\leq \frac{x-11}{4} \leq 7$,
        \end{enumerate}
        """)
        #definition.scale(0.7)
        exos[0].move_to(np.array([-1, 2, 0]))


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

        answer = TextMobject("Solutions (respectivement): $x\in \emptyset$, $-5\leq x\leq 39$").to_corner(DL)
        self.play(Write(answer))
        self.wait(10)
        self.play(FadeOut(exos))
        self.play(FadeOut(title))



class Credits(Scene):
    def wplay(self, *args, wait=1, run_time=1, rate_func=smooth):
        self.play(*args, run_time=run_time, rate_func=rate_func)
        if wait != 0:
            self.wait(wait)

    def construct(self):
        credits = TextMobject("Crédits").set_color(YELLOW).scale(1.7)
        thanks = TextMobject("Merci pour votre visionnement!!").set_color(ORANGE).scale(1.7)

        instructor = TexMobject(r"\text{Enseignant}", r"\text{Louis-Marc Mercier}")
        viewer = TexMobject(r"\text{Spectateur}", r"\text{Vous}")
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
