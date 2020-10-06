from manimlib.imports import *
from manim_utils.slide_template import BoxedTitle, GenChannelLogo, YoutubeLogo
from MyAnim.RevisionSecondaire.id_rem_french import MeasureDistance
from scipy.special import factorial

# TODO: SCENE ORDER

# 0. IntroCEGEP
# 1. ThumbnailFrench
# 2. Applications
# 3. MES
# 4. Definition
# 5. Ensembles
# 6. LesEnsembles
# 7. Notation
# 8. NotationSuite
# 9. HierarchieEnsembles
# 10. Exercices


# Version: May 20th 2020


class ThumbnailFrench(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        line_e = TextMobject(r"\sc{Deviens}", r"\sc{réel!}").scale(2.5).shift(2.25 * UP + 4 * LEFT).set_color(PINK)
        line_e[0].next_to(3 * UP + 7 * LEFT)
        line_e[1].next_to(2 * UP + 7 * LEFT)
        line_pi = TextMobject(r"{\sc Sois }", r"{\sc rationnel!}").scale(2.5).set_color(YELLOW)
        line_pi[0].next_to(3 * UP + 0 * LEFT)
        line_pi[1].next_to(2 * UP + 0 * LEFT)

        line2 = TextMobject("$\pi$",r"$i$")
        line2[0].scale(10).next_to(2.5 * DOWN + 6 * LEFT).set_color(PINK)
        line2[1].scale(10).next_to(1.75 * DOWN + 1.5 * RIGHT).set_color(YELLOW)
        self.play(FadeIn(line2))
        self.wait(2)
        self.play(FadeIn(line_e))
        self.wait(2)
        self.play(FadeIn(line_pi))
        self.wait(5)



class Applications(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        #title = TextMobject(r"\underline{\sc À retenir}", color=WHITE).to_corner(UL)
        title = BoxedTitle(text="Applications", width=4, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))


        compl_rules_str = [
            "",
            "Compter sa monnaie pour payer quelqu'un.",
            "Évaluer la performance d'un appareil.",
            "Comparer les classements de films sur Imdb."
        ]

        def choose_color(i):
            color = WHITE if i<=5 else YELLOW
            return color

        rules = [TextMobject("- {}".format(rule), color=choose_color(i)) for i, rule in enumerate(compl_rules_str)]
        rules = [rule.scale(0.8) for rule in rules]

        for (i, rule) in enumerate(rules):
            if i != 0:
                rule.next_to(rules[0].get_center() - rule.get_center() + np.array([-6, -1.4 * i, 0]))
        rules = VGroup(*rules)
        rules.to_corner(LEFT + UP)

        self.play(Write(title))
        self.wait(10)
        self.play(Write(rules[1]))
        self.wait(5)
        self.play(Write(rules[2]))
        self.wait(5)
        self.play(Write(rules[3]))
        self.wait(7)


class MES(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Quel film choisir?", width=5, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        title_1 = TextMobject("Dragonball Evolution")
        rating_1 = TextMobject("$\star\star$", color="#d9bf87").next_to(title_1, LEFT)

        title_2 = TextMobject("Frozen").next_to(title_1, DOWN, buff=MED_LARGE_BUFF).align_to(title_1, LEFT)
        rating_2 = TextMobject("$\star\star\star\star$", color="#d9bf87").next_to(title_2, LEFT)

        title_3 = TextMobject("Toys Story").next_to(title_2, DOWN, buff=MED_LARGE_BUFF).align_to(title_2, LEFT)
        rating_3 = TextMobject("$\star\star\star\star\star$", color="#d9bf87").next_to(title_3, LEFT)

        self.play(Write(title))
        self.wait(5)
        self.play(Write(title_1), DrawBorderThenFill(rating_1))
        self.wait(5)
        self.play(Write(title_2), DrawBorderThenFill(rating_2))
        self.wait(5)
        self.play(Write(title_3), DrawBorderThenFill(rating_3))
        self.wait(5)


class Definition(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Définition", width=3, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        title_1 = TextMobject("Un nombre est un concept mathématique servant à compter, évaluer, comparer ou mesurer des grandeurs. "
                              "Les nombres sont définis à l'aide de chiffres.")
        title_1.scale(0.7)

        self.play(Write(title))
        self.wait(5)
        self.play(Write(title_1))
        self.wait(10)


class Ensembles(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Ensembles de nombres", width=6, height=0.7, scale=0.8)
        title.move_to(np.array([0, 3.25, 0]))

        compl_rules_str = [
            "",
            "nombres complexes ($\mathbb{C}$),",
            "nombres réels ($\mathbb{R}$),",
            "nombres rationnels ($\mathbb{Q}$)",
            "nombres irrationnels ($\mathbb{Q}^{c}$),",
            "nombres entiers ($\mathbb{Z}$),",
            "nombres naturels ($\mathbb{N}$),"
        ]

        def choose_color(i):
            color = WHITE if i <= 10 else YELLOW
            return color

        rules = [TextMobject("- {}".format(rule), color=choose_color(i)) for i, rule in enumerate(compl_rules_str)]
        rules = [rule.scale(0.8) for rule in rules]

        for (i, rule) in enumerate(rules):
            if i != 0:
                rule.next_to(rules[0].get_center() + np.array([-3, -0.7, 0]) + np.array([-6, -0.7 * i, 0]))
        rules = VGroup(*rules)
        rules.to_corner(LEFT + UP)

        self.play(Write(title))
        self.wait(7)
        self.play(Write(rules[1]))
        self.wait(3)
        self.play(Write(rules[2]))
        self.wait(3)
        self.play(Write(rules[3]))
        self.wait(3)
        self.play(Write(rules[4]))
        self.wait(3)
        self.play(Write(rules[5]))
        self.wait(3)
        self.play(Write(rules[6]))
        self.wait(3)


def get_sets_symbols():
    naturals = TextMobject(r"$\mathbb{N}$")
    integers = TextMobject(r"$\mathbb{Z}$")
    rationals = TextMobject(r"$\mathbb{Q}$")
    irrationals = TextMobject(r"$\mathbb{Q}^{c}$")
    real = TextMobject(r"$\mathbb{R}$")
    empty = TextMobject(r"$\mathbb{R}$").set_color(BLACK)
    return [naturals, integers, rationals, irrationals, real, empty]

def get_descriptions():
    naturals = TextMobject(r"Dénombrer")
    integers = TextMobject(r"Naturels et opposés")
    rationals = TextMobject(r"Exprimable en fraction")
    irrationals = TextMobject(r"Pas rationnel")
    real = TextMobject(r"Rationnel et irrationnel")
    return [naturals, integers, rationals, irrationals, real]

def get_examples():
    naturals = TextMobject(r"$0,1,2,100$")
    integers = TextMobject(r"$-5,-1,110$")
    rationals = TextMobject(r"$\frac{3}{4},-\frac{1}{3},5$")
    irrationals = TextMobject(r"$\sqrt{2},\pi$")
    real = TextMobject(r"$-20,\frac{3}{8}\sqrt{3}$")
    return [naturals, integers, rationals, irrationals, real]


class LesEnsembles(Scene):
    def wplay(self, *args, wait=1, run_time=1, rate_func=smooth):
        self.play(*args, run_time=run_time, rate_func=rate_func)
        if wait != 0:
            self.wait(wait)

    def construct(self):
        horiz = Line([-FRAME_X_RADIUS + MED_LARGE_BUFF, 2.75, 0],
                     [FRAME_X_RADIUS - MED_LARGE_BUFF, 2.75, 0])

        headers = TexMobject(r"\textbf{Nombres}", r"\textbf{Description}", r"\textbf{Exemples}").next_to(horiz, UP)
        headers[0].set_x(horiz.get_start()[0] + headers[0].get_width() / 2 + MED_LARGE_BUFF)
        vert_1 = Line([headers[0].get_right()[0] + MED_LARGE_BUFF, FRAME_Y_RADIUS - MED_LARGE_BUFF, 0],
                    [headers[0].get_right()[0] + MED_LARGE_BUFF, -FRAME_Y_RADIUS + MED_LARGE_BUFF, 0])
        vert_2 = Line([headers[1].get_right()[0] + MED_LARGE_BUFF, FRAME_Y_RADIUS - MED_LARGE_BUFF, 0],
                      [headers[1].get_right()[0] + MED_LARGE_BUFF, -FRAME_Y_RADIUS + MED_LARGE_BUFF, 0])
        remaining_space = horiz.get_right()[0] - vert_1.get_x()
        spacing = remaining_space / 4

        headers[1].set_x(vert_1.get_x() + headers[1].get_width() / 2 + spacing / 2).set_color(YELLOW)
        headers[2].set_x(headers[1].get_x() + 2 * spacing)
        headers[2].set_color(BLUE)

        sets_symbols = VGroup(*get_sets_symbols()).arrange(DOWN,buff=0.45).next_to(horiz, DOWN).set_x(headers[0].get_x())

        rows = VGroup(*[horiz.copy().set_stroke(width=1)
                      .set_y((sets_symbols[i].get_y() + sets_symbols[i + 1].get_y()) / 2) for i in range(5)])

        descriptions = VGroup(*get_descriptions()).arrange(DOWN, buff=0.45) \
            .next_to(horiz, DOWN).set_x(headers[1].get_x()).set_color(YELLOW)

        examples = VGroup(*get_examples()).arrange(DOWN, buff=0.3) \
            .next_to(horiz, DOWN).set_x(headers[2].get_x()).set_color(BLUE)

        self.play(ShowCreation(horiz), ShowCreation(vert_1), ShowCreation(vert_2))
        self.play(Write(headers[0]), Write(headers[1]), Write(headers[2]))
        for set_symbol, description, example, row in zip(sets_symbols[0:-1], descriptions, examples, rows):
            self.play(ShowCreation(set_symbol))
            self.wait(3)
            self.play(ShowCreation(description))
            self.wait(6)
            self.play(ShowCreation(example))
            self.wait(3)
            self.play(ShowCreation(row))
        self.wait(5)



def get_notation():
    naturals = TextMobject(r"$\{,\}$")
    integers = TextMobject(r"$\in$")
    rationals = TextMobject(r"$\notin$")
    irrationals = TextMobject(r"$\subset$")
    real = TextMobject(r"$\cup$")
    empty = TextMobject(r"$\mathbb{R}$").set_color(BLACK)
    return [naturals, integers, rationals, irrationals, real, empty]

def get_notation_descriptions():
    naturals = TextMobject(r"Énumération")
    integers = TextMobject(r"Appartient à")
    rationals = TextMobject(r"N'appartient pas")
    irrationals = TextMobject(r"Sous-ensemble de")
    real = TextMobject(r"Union d'ensembles")
    return [naturals, integers, rationals, irrationals, real]

def get_notation_examples():
    naturals = TextMobject(r"$\{0,1,2,\dots\}$")
    integers = TextMobject(r"$1\in\mathbb{N}$")
    rationals = TextMobject(r"$-3\notin\mathbb{N}$")
    irrationals = TextMobject(r"$\{0,1\}\subset\mathbb{N}$")
    real = TextMobject(r"$\mathbb{R}=\mathbb{Q}\cup\mathbb{Q}^{c}$")
    return [naturals, integers, rationals, irrationals, real]


class Notation(Scene):
    def wplay(self, *args, wait=1, run_time=1, rate_func=smooth):
        self.play(*args, run_time=run_time, rate_func=rate_func)
        if wait != 0:
            self.wait(wait)

    def construct(self):
        horiz = Line([-FRAME_X_RADIUS + MED_LARGE_BUFF, 2.75, 0],
                     [FRAME_X_RADIUS - MED_LARGE_BUFF, 2.75, 0])

        headers = TexMobject(r"\textbf{Symboles}", r"\textbf{Définition}", r"\textbf{Exemples}").next_to(horiz, UP)
        headers[0].set_x(horiz.get_start()[0] + headers[0].get_width() / 2 + MED_LARGE_BUFF)
        vert_1 = Line([headers[0].get_right()[0] + MED_LARGE_BUFF, FRAME_Y_RADIUS - MED_LARGE_BUFF, 0],
                    [headers[0].get_right()[0] + MED_LARGE_BUFF, -FRAME_Y_RADIUS + MED_LARGE_BUFF, 0])
        vert_2 = Line([headers[1].get_right()[0] + MED_LARGE_BUFF, FRAME_Y_RADIUS - MED_LARGE_BUFF, 0],
                      [headers[1].get_right()[0] + MED_LARGE_BUFF, -FRAME_Y_RADIUS + MED_LARGE_BUFF, 0])
        remaining_space = horiz.get_right()[0] - vert_1.get_x()
        spacing = remaining_space / 4

        headers[1].set_x(vert_1.get_x() + headers[1].get_width() / 2 + spacing / 2).set_color(YELLOW)
        headers[2].set_x(headers[1].get_x() + 2 * spacing)
        headers[2].set_color(BLUE)

        sets_symbols = VGroup(*get_notation()).arrange(DOWN,buff=0.45).next_to(horiz, DOWN).set_x(headers[0].get_x())

        rows = VGroup(*[horiz.copy().set_stroke(width=1)
                      .set_y((sets_symbols[i].get_y() + sets_symbols[i + 1].get_y()) / 2) for i in range(5)])

        descriptions = VGroup(*get_notation_descriptions()).arrange(DOWN, buff=0.45) \
            .next_to(horiz, DOWN).set_x(headers[1].get_x()).set_color(YELLOW)

        examples = VGroup(*get_notation_examples()).arrange(DOWN, buff=0.4) \
            .next_to(horiz, DOWN).set_x(headers[2].get_x()).set_color(BLUE)

        self.play(ShowCreation(horiz), ShowCreation(vert_1), ShowCreation(vert_2))
        self.play(Write(headers[0]), Write(headers[1]), Write(headers[2]))
        for set_symbol, description, example, row in zip(sets_symbols[0:-1], descriptions, examples, rows):
            self.play(ShowCreation(set_symbol))
            self.wait(3)
            self.play(ShowCreation(description))
            self.wait(6)
            self.play(ShowCreation(example))
            self.wait(3)
            self.play(ShowCreation(row))
        self.wait(5)


def get_notation_suite():
    naturals = TextMobject(r"$\cap$")
    integers = TextMobject(r"$\backslash$")
    rationals = TextMobject(r"$+$")
    irrationals = TextMobject(r"$-$")
    real = TextMobject(r"$\star$")
    empty = TextMobject(r"$\mathbb{R}$").set_color(BLACK)
    return [naturals, integers, rationals, irrationals, real, empty]

def get_notation_descriptions_suite():
    naturals = TextMobject(r"Intersection")
    integers = TextMobject(r"Exclusion")
    rationals = TextMobject(r"Éléments positifs")
    irrationals = TextMobject(r"Éléments négatifs")
    real = TextMobject(r"Sans zéro")
    return [naturals, integers, rationals, irrationals, real]

def get_notation_examples_suite():
    naturals = TextMobject(r"$\mathbb{Z}\cap\mathbb{N}=\mathbb{N}$")
    integers = TextMobject(r"$\mathbb{N}\backslash\{0,1\}$")
    rationals = TextMobject(r"$\mathbb{Z}_{+}$")
    irrationals = TextMobject(r"$\mathbb{Z}_{-}$")
    real = TextMobject(r"$\mathbb{N}_{\star}$")
    return [naturals, integers, rationals, irrationals, real]


class NotationSuite(Scene):
    def wplay(self, *args, wait=1, run_time=1, rate_func=smooth):
        self.play(*args, run_time=run_time, rate_func=rate_func)
        if wait != 0:
            self.wait(wait)

    def construct(self):
        horiz = Line([-FRAME_X_RADIUS + MED_LARGE_BUFF, 2.75, 0],
                     [FRAME_X_RADIUS - MED_LARGE_BUFF, 2.75, 0])

        headers = TexMobject(r"\textbf{Symboles}", r"\textbf{Définition}", r"\textbf{Exemples}").next_to(horiz, UP)
        headers[0].set_x(horiz.get_start()[0] + headers[0].get_width() / 2 + MED_LARGE_BUFF)
        vert_1 = Line([headers[0].get_right()[0] + MED_LARGE_BUFF, FRAME_Y_RADIUS - MED_LARGE_BUFF, 0],
                    [headers[0].get_right()[0] + MED_LARGE_BUFF, -FRAME_Y_RADIUS + MED_LARGE_BUFF, 0])
        vert_2 = Line([headers[1].get_right()[0] + MED_LARGE_BUFF, FRAME_Y_RADIUS - MED_LARGE_BUFF, 0],
                      [headers[1].get_right()[0] + MED_LARGE_BUFF, -FRAME_Y_RADIUS + MED_LARGE_BUFF, 0])
        remaining_space = horiz.get_right()[0] - vert_1.get_x()
        spacing = remaining_space / 4

        headers[1].set_x(vert_1.get_x() + headers[1].get_width() / 2 + spacing / 2).set_color(YELLOW)
        headers[2].set_x(headers[1].get_x() + 2 * spacing)
        headers[2].set_color(BLUE)

        sets_symbols = VGroup(*get_notation_suite()).arrange(DOWN,buff=0.45).next_to(horiz, DOWN).set_x(headers[0].get_x())

        rows = VGroup(*[horiz.copy().set_stroke(width=1)
                      .set_y((sets_symbols[i].get_y() + sets_symbols[i + 1].get_y()) / 2) for i in range(5)])

        descriptions = VGroup(*get_notation_descriptions_suite()).arrange(DOWN, buff=0.35) \
            .next_to(horiz, DOWN).set_x(headers[1].get_x()).set_color(YELLOW)

        examples = VGroup(*get_notation_examples_suite()).arrange(DOWN, buff=0.35) \
            .next_to(horiz, DOWN).set_x(headers[2].get_x()).set_color(BLUE)

        self.play(ShowCreation(horiz), ShowCreation(vert_1), ShowCreation(vert_2))
        self.play(Write(headers[0]), Write(headers[1]), Write(headers[2]))
        for i, (set_symbol, description, example, row) in enumerate(zip(sets_symbols[0:-1], descriptions, examples, rows)):
            self.play(ShowCreation(set_symbol))
            self.wait(3)
            self.play(ShowCreation(description))
            self.wait(6)
            self.play(ShowCreation(example))
            self.wait(3)
            if i!=4:
                self.play(ShowCreation(row))
        self.wait(5)


class HierarchieEnsembles(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Structure Ensembles", width=5, height=0.7, scale=0.7)
        title.move_to(np.array([-0.6, 3.25, 0]))

        # Natural numbers
        natural_circle = Circle(radius=0.4)
        natural_def = TextMobject(r"$\mathbb{N}$").next_to(natural_circle, 0)

        # Integers numbers
        integers_ellipse = Ellipse().next_to(np.array([-1.5,0,0]))
        integers_def = TextMobject(r"$\mathbb{Z}$").next_to(natural_def, LEFT-np.array([1,0,0]))

        # Rational numbers
        rational_ellipse = Ellipse(width=3, height=1.5).next_to(np.array([-2.25, 0, 0]))
        rational_def = TextMobject(r"$\mathbb{Q}$").next_to(integers_def, LEFT - np.array([1, 0, 0]))

        # Real numbers
        real_ellipse = Ellipse(width=4.25, height=1.75).next_to(np.array([-3.25, 0, 0]))
        real_def = TextMobject(r"$\mathbb{R}$").next_to(rational_def, LEFT - np.array([1, 0, 0]))

        self.play(ShowCreation(title))
        self.play(ShowCreation(natural_circle), ShowCreation(natural_def))
        self.wait(2)
        self.play(ShowCreation(integers_ellipse), ShowCreation(integers_def))
        self.wait(3)
        self.play(ShowCreation(rational_ellipse), ShowCreation(rational_def))
        self.wait(3)
        self.play(ShowCreation(real_ellipse), ShowCreation(real_def))
        self.wait(7)



class Exercices(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        #title = TextMobject(r"\underline{\textbf{À retenir}}", color=PURPLE).to_corner(UL).scale(1)
        title = BoxedTitle(text="Exercice", width=3.5, height=0.8, scale=0.9)
        title.move_to(np.array([-0.6, 3.25, 0]))

        # Integers numbers
        A_ellipse = Ellipse(width=3, height=1.5).next_to(np.array([-3.5, -1, 0])).set_color(BLUE)
        A_def = TextMobject(r"$\mathbf{A}$").next_to(A_ellipse, LEFT + np.array([1, 0, 0]))

        # Rational numbers
        B_ellipse = Ellipse(width=3, height=1.5).next_to(np.array([-1.25,-1,0])).set_color(YELLOW)
        B_def = TextMobject(r"$\mathbf{B}$").next_to(B_ellipse, RIGHT - np.array([1, 0, 0]))

        B_ellipse.set_fill(opacity=0.5)
        A_ellipse.set_fill(opacity=0.5)

        self.play(Write(title))
        self.wait(5)
        self.play(Write(A_ellipse), Write(A_def))
        self.wait(3)
        self.play(Write(B_ellipse), Write(B_def))
        self.wait(3)

        context = TextMobject(r"Exprimer les ensembles suivants : ")
        context_elements = TextMobject(r"- $\mathbf{A}$ sans $\mathbf{B}$, ", r"- $\mathbf{A}$ et $\mathbf{B}$, ",
                                       "- $\mathbf{A}$ ou $\mathbf{B}$")

        context.next_to(np.array([-7,2,0])).scale(0.85)
        context_elements[0].set_color(BLUE).next_to(context, RIGHT)
        context_elements[1].set_color("#95a630").next_to(context_elements[0], DOWN).align_to(context_elements[0], LEFT)
        context_elements[2].set_color(YELLOW).next_to(context_elements[1], DOWN).align_to(context_elements[1], LEFT)

        self.play(Write(context))
        self.play(Write(context_elements))
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
        answers = TextMobject(
            r"Solutions (respectivement): $\mathbf{A}\backslash \mathbf{B}$, $\mathbf{A}\cap \mathbf{B}$, $\mathbf{A}\cup \mathbf{B}$").to_corner(DL)
        self.play(Write(answers))
        self.wait(15)




class Conclusion(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        #title = TextMobject(r"\underline{\textbf{À retenir}}", color=PURPLE).to_corner(UL).scale(1)
        title = BoxedTitle(text="Conclusion", width=3.5, height=0.5, scale=0.7)
        title.move_to(np.array([-0.6, 3.25, 0]))

        compl_rules_str = [
            "",
            "Les ensembles de nombres,",
            "La notation des ensembles,",
            "Bonus: Définir des ensembles avec la notation des ensembles.",
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




class IntroCEGEP(Scene):
    CONFIG = {
        "x_start": 3,
        "x_end": 7,
        "axes_config": {
            "center_point": [-6,-3,0],
            "x_axis_config": {
                "unit_size": 0.6,
                "x_min": 0,
                "x_max": 10,
                "include_numbers": True
            },
            "y_axis_config": {
                "unit_size": 0.65,
                "label_direction": UP,
                "x_min": -0.5,
                "x_max": 6,
                "include_numbers": True
            },
        },
        "func": lambda x: 0.1 * (x - 2) * (x - 8) * (x - 5) + 3,
        "func_config": {
            "color": BLUE_C,
            "x_min": 0.8,
            "x_max": 9,
        },
        "dot_radius": 0.1,
        "line_config": {}
    }
    def construct(self):
        # Channel logo and name (UP LEFT CORNER)
        path = r"C:/Users/Utilisateur/Desktop/CEGEP/Cours_maison/"
        image = ImageMobject(path + "very_light_phoenix").next_to(np.array([4, -2.25, 0]))
        image.scale(1.25)

        channel_name = TextMobject(r"Louis-Math")
        channel_name.next_to(np.array([4.1, -3.5, 0]))
        channel_name.scale(1)
        channel_name.set_color_by_gradient(RED, ORANGE, GOLD, ORANGE, RED)

        youtube_logo = YoutubeLogo().scale(0.4)
        youtube_logo.next_to(image, LEFT)

        # Title and subtitle of the trailer
        trailer_title = TextMobject(r"\sc{\textbf{Pré-calcul}}")
        trailer_title.set_color_by_gradient(PINK, RED, ORANGE, YELLOW, GREEN, BLUE)
        trailer_title.next_to(np.array([-5.5, 3.25, 0]))
        trailer_title.scale(1.75)

        trailer_subtitle = TextMobject(r"\sc{\textbf{Les ensembles}}")
        trailer_subtitle.set_color(WHITE)
        trailer_subtitle.next_to(trailer_title, DOWN, buff=0.2 * LARGE_BUFF).align_to(trailer_title, LEFT)
        trailer_subtitle.scale(1)

        #trailer_subtitle_2 = TextMobject(r"\sc{\textbf{et double}}")
        #trailer_subtitle_2.set_color(WHITE)
        #trailer_subtitle_2.next_to(trailer_subtitle, DOWN, buff=0.2 * LARGE_BUFF).align_to(trailer_subtitle, LEFT)
        #trailer_subtitle_2.scale(1)

        ubiquit = BoxedTitle(text="Projet Ubiquit", width=3.75, scale=0.75).to_corner(UR)

        # Displaying everything
        self.play(FadeIn(image))
        self.play(FadeIn(channel_name))
        self.play(DrawBorderThenFill(youtube_logo))
        self.play(ShowCreation(ubiquit))
        self.play(FadeIn(trailer_title), FadeIn(trailer_subtitle))
        #self.play(FadeIn(trailer_subtitle_2))

        # Plot
        axes = self.get_axes()
        func = self.get_graph(self.func,**self.func_config)
        dot_start = self.get_dot_from_x_coord(self.x_start)
        dot_end = self.get_dot_from_x_coord(self.x_end)
        line = VMobject()
        line.add_updater(self.get_line_updater(dot_start,dot_end))
        # self.add(axes,func,dot_start,dot_end,line)
        x_axis = TextMobject(r"$x$", color=WHITE)
        y_axis = TextMobject(r"$f(x)$", color=WHITE)

        y_axis.next_to(axes[1], UP)
        x_axis.next_to(axes[0], RIGHT)

        self.play(
            Write(axes),
            Write(x_axis), Write(y_axis),
            ShowCreation(func),
            *list(map(GrowFromCenter,[dot_start,dot_end]))
        )


        self.play(ShowCreation(line))
        self.wait(3)

    def get_axes(self):
        self.axes = Axes(**self.axes_config)
        print(self.axes)
        # FIX Y LABELS
        y_labels = self.axes.get_y_axis().numbers
        for label in y_labels:
            label.rotate(-PI/2)
        return self.axes

    def get_graph(self,func,**kwargs):
        return self.axes.get_graph(
                                    func,
                                    **kwargs
                                )

    def get_f(self,x_coord):
        return self.axes.c2p(x_coord, self.func(x_coord))

    def get_dot_from_x_coord(self,x_coord,**kwargs):
        return Dot(
            self.get_f(x_coord),
            radius=self.dot_radius,
            **kwargs
        )

    def get_dot_updater(self, start, end):
        def updater(mob,alpha):
            x = interpolate(start, end, alpha)
            coord = self.get_f(x)
            mob.move_to(coord)
        return updater

    def get_line_across_points(self,d1,d2,buff):
        reference_line = Line(d1.get_center(),d2.get_center())
        vector = reference_line.get_unit_vector()
        return Line(
            d1.get_center() - vector * buff,
            d2.get_center() + vector * buff,
            **self.line_config
        )

    def get_line_updater(self,d1,d2,buff=3,**kwargs):
        def updater(mob):
            mob.become(
                self.get_line_across_points(d1,d2,buff)
            )
        return updater

    def move_dot(self,dot,start,end,*args,**kwargs):
        self.play(
            UpdateFromAlphaFunc(
                dot, self.get_dot_updater(start,end),
                *args,
                **kwargs
            )
        )

    def get_derivative_updater(self, dot, length=6):
        def updater(mob):
            derivative = Line(
                dot.get_center(),
                self.get_dot_from_x_coord(
                    self.axes.p2c(dot.get_center())[0] + 0.0001
                ).get_center(),
                **self.line_config
            )
            derivative.set_length(length)
            derivative.move_to(dot)
            mob.become(derivative)
        return updater