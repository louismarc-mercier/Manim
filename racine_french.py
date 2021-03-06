from manimlib.imports import *


# 0. Thumbnail
# 1. Menu
# 2. CasParticuliers1
# 3. Avertissement
# 3. CasParticuliers2
# 4. RacineDef
# 5. ExpFrac
# 6. Proprietes
# 7. Exemples
# 8. Solutions
# 9. Conclusion


color_map = {
    r"{a}": BLUE,
    r"{x}": RED,
}

class ThumbnailFrench(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        line_e = TextMobject(r"{\sc Mon}", r"{\sc frère}", r"{\sc jumeau?}").scale(2.25).set_color(YELLOW)
        line_e[0].next_to(3 * UP + 7 * LEFT)
        line_e[1].next_to(2 * UP + 7 * LEFT)
        line_e[2].next_to(1 * UP + 7 * LEFT)
        line_pi = TextMobject(r"{\sc Je me suis}", r"{\sc pris dans}", r"{\sc une racine!}", r"*PLEURS*").scale(2.25).set_color(GOLD)
        line_pi[0].next_to(3 * UP + 0 * LEFT)
        line_pi[1].next_to(2 * UP + 0 * LEFT)
        line_pi[2].next_to(1 * UP + 0 * LEFT)
        line_pi[3].next_to(-0.5 * UP + 0 * LEFT)

        line2 = TextMobject("$x^{2}$","$x$")
        line2[0].scale(6).next_to(2.25 * DOWN + 6 * LEFT).set_color(BLUE)
        line2[1].scale(6).next_to(2.75 * DOWN + 2.5 * RIGHT).set_color(BLUE)
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
            *"""1) Rappel (racine carrée et cubique), 2) Définition de la racine, 3) Lien avec les exposants, 4) Propriétés des racines, 5) Exemples, 6) Conclusionnnnn"""
                .split(","), dot_color=BLUE
        )

        #l = NumberedList(*["Révision des axiomes", "Riemann Hypothesis", "P vs NP Problem"], dot_color=BLUE)
        l.scale(1)
        l.shift(0.5 * DOWN + 3*LEFT)
        self.play(FadeInFromDown(title))
        self.play(Write(l))

        #self.play(l.fade_all_but, 3)
        self.wait(25)


class CasParticuliers1(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\textbf{Cas particulier: racine carrée}}").to_corner(UL).scale(1).set_color(PURPLE)
        context = TextMobject2(r"Soit $a\geq 0$, alors l'équation $x^{2}=a$ admet deux solutions réeels opposées (i.e. $x=\pm\sqrt{a}$). "
                               r"Si $a=0$, alors $x^{2}=0$ admet une seule solution (i.e. $x=0$).").scale(0.75)
        context.next_to([-6.75, 1.5, 0])

        exemple_title = TextMobject2(r"\underline{Exemples:}").scale(1).set_color(YELLOW)
        exemple_title.next_to([-6.75, -0.5, 0])
        exemple_eq1 = TexMobject(r"\sqrt{2}=1.4142\dots")
        exemple_eq1.next_to(exemple_title, DOWN, buff=LARGE_BUFF).align_to(exemple_title, LEFT)

        exemple_eq2 = TexMobject(r"\sqrt{4}=2")
        exemple_eq2.next_to(exemple_eq1, RIGHT, buff=2*LARGE_BUFF)


        self.play(FadeInFromDown(title))
        self.play(Write(context))
        self.wait(30)
        self.play(Write(exemple_title))
        self.wait(5)
        self.play(Write(exemple_eq1), Write(exemple_eq2))
        self.wait(15)


class Avertissement(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\textbf{Mise en garde}}").to_corner(UL).scale(1).set_color(PURPLE)

        warning_symbol = Triangle(fill_opacity=0.75, color=YELLOW)
        warning_content = TexMobject("!", color=BLACK).scale(2.5).move_to(warning_symbol)

        explanation = TextMobject("Lorsqu'on applique la racine carrée, on prend seulement la solution positive (e.g. $\sqrt{9}=3$).").scale(0.75)
        explanation.next_to(warning_symbol, DOWN)
        explanation.set_color_by_gradient(RED, ORANGE, GOLD, ORANGE, RED)

        #COLOR_MAP
        self.play(FadeInFromDown(title))
        self.wait(5)
        self.play(ShowCreation(warning_symbol), ShowCreation(warning_content))
        self.play(ShowCreation(explanation))
        self.wait(15)



class CasParticuliers2(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\textbf{Cas particulier: racine cubique}}").to_corner(UL).scale(1).set_color(PURPLE)
        context = TextMobject2(r"La racine cubique de $a\in\mathbb{R}$ (i.e. $\sqrt[3]{a}$) est l'unique racine réelle de l'équation").scale(0.75)
        context.next_to([-6.75, 2, 0])

        eq = TextMobject(r"$x^{3}=a$").to_corner(UL).scale(1)
        eq.next_to(context, DOWN)

        exemple_title = TextMobject2(r"\underline{Exemples:}").scale(1).set_color(YELLOW)
        exemple_title.next_to([-6.75, -0.5, 0])
        exemple_eq1 = TexMobject(r"\sqrt{-8}=-2")
        exemple_eq1.next_to(exemple_title, DOWN, buff=LARGE_BUFF).align_to(exemple_title, LEFT)

        exemple_eq2 = TexMobject(r"\sqrt{27}=3")
        exemple_eq2.next_to(exemple_eq1, RIGHT, buff=2*LARGE_BUFF)


        self.play(FadeInFromDown(title))
        self.play(Write(context))
        self.wait(5)
        self.play(Write(eq))
        self.wait(5)
        self.play(Write(exemple_title))
        self.play( Write(exemple_eq1), Write(exemple_eq2))
        self.wait(20)


class RacineDef(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\textbf{Définition: Racine}}").scale(1).set_color(PURPLE)
        context = TextMobject(r"Pour $a\geq 0$, il existe un $x\geq 0$ tel que $x^{n}=a$."
                              r" Ce réel est appelé la racine $n$-ième de $a$ et est noté $\sqrt[n]{a}$.").scale(0.7)
        context.next_to([-7, 1.5, 0])
        title.next_to([-2.75, 3, 0])

        eq_1 = TexMobject(
        "\\sqrt",
        "{a}"
        ).scale(1.1)
        eq_1[0].set_color(BLUE)
        eq_1[1].set_color(YELLOW)

        order_sqrt = TexMobject("n")
        order_sqrt.set_color(RED)
        order_sqrt.next_to(np.array([-0.5,0.3,0])).scale(0.6)

        l = NumberedList(
            *"""1) indice, 2) radical, 3) radicant""".split(
                ","), dot_color=BLUE
        )
        l[0].set_color(RED)
        l[1].set_color(BLUE)
        l[2].set_color(YELLOW)
        l.next_to(np.array([2, -2, 0]))

        interpretation = TextMobject(r"""
                        \begin{itemize}
                        \item Si $n$ est pair, alors $\sqrt[n]{a}=x$ si $a,x\geq 0$,
                        \item Si $n$ est impair, alors $\sqrt[n]{a}=x$ si $a\in\mathbb{R}$.
                        \end{itemize}
                        """).scale(0.7)
        interpretation.next_to(np.array([-7,-2,0]))

        self.play(FadeInFromDown(title))
        self.play(Write(context))
        self.wait(20)
        self.play(Write(eq_1), Write(order_sqrt))
        self.wait(5)
        self.play(Write(l))
        self.wait(12)
        self.play(Write(interpretation))
        self.wait(35)



class ExpFrac(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\textbf{Les exposants fractionnaires}}").to_corner(UL).scale(1).set_color(PURPLE)
        context = TextMobject(r"Soit $a\in\mathbb{R}$. Le nombre qui, élevé à la puissance $n\in\mathbb{N}_{\star}$, donne $a$ est noté $\sqrt[n]{a}$.").scale(0.75)
        context.next_to([-6.75, 2.5, 0])

        context_2 = TextMobject2(r"But: Trouver un exposant $p$ tel que ", "$(a^{p})^{n}$", " $=$ ", "$a$.").scale(0.75)
        context_2.next_to(context, DOWN, buff=LARGE_BUFF).align_to(context, LEFT)
        context_2[1].set_color(RED)
        context_2[3].set_color(BLUE)

        exemple_title = TextMobject2(r"\underline{Démarche:}").scale(1)
        exemple_title.next_to([-6.75, -0.5, 0])
        solution_p1 = TexMobject(r"(a^{p})^{n}", r"=", r"a^{pn}", "=", "a^{1}")
        solution_p1.next_to(exemple_title, DOWN, buff=LARGE_BUFF).align_to(exemple_title, LEFT)

        solution_p1[0].set_color(RED)
        solution_p1[2].set_color(RED)
        solution_p1[4].set_color(BLUE)

        solution_p2 = TexMobject("\Rightarrow\quad", "pn", "=", "1")
        solution_p2.next_to(solution_p1, RIGHT, buff=LARGE_BUFF)
        solution_p2[1].set_color(RED)
        solution_p2[3].set_color(BLUE)

        solution_p3 = TexMobject("\Leftrightarrow\quad", "p", "=", "{1\\over n}")
        solution_p3.next_to(solution_p2, RIGHT, buff=LARGE_BUFF)


        self.play(FadeInFromDown(title))
        self.play(Write(context))
        self.wait(5)
        self.play(Write(context_2))
        self.wait(15)
        self.play(Write(exemple_title))
        self.wait(5)
        self.play(Write(solution_p1))
        self.wait(10)
        self.play(Write(solution_p2))
        self.wait(8)
        self.play(Write(solution_p3))
        self.wait(12)


class Proprietes(Scene):
    def construct(self):
        ###################
        ### OLD CONTENT ###
        ###################
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

        ###################
        ### NEW CONTENT ###
        ###################
        new_title = TextMobject(r"\underline{\textbf{Propriétés des racines}}").to_corner(UL).scale(1).set_color(PURPLE)
        new_context = TextMobject(r"Soit $a,b> 0$ et $m,n\in\mathbb{N}_{\star}$, alors on a ")
        new_context.next_to([-6.75, 2.5, 0])

        new_eq_1 = TextMobject(r"P1) ", r"$(\sqrt[n]{a})^{m}=a^{\frac{m}{n}}=\big(\sqrt[n]{a^{m}}\big)$").scale(1)
        new_eq_2 = TextMobject(r"P2) ", r"$\frac{\sqrt[n]{a}}{\sqrt[n]{b}}=\sqrt[n]{\frac{a}{b}}$").scale(1)
        new_eq_3 = TextMobject(r"P3) ", r"$\sqrt[m]{\sqrt[n]{a}}=\sqrt[mn]{a}$").scale(1)
        new_eq_4 = TextMobject(r"P4) ", r"$\sqrt[n]{ab}=\sqrt[n]{a}\sqrt[n]{b}$").scale(1)

        new_eq_1[1].set_color(RED)
        new_eq_2[1].set_color(BLUE)
        new_eq_3[1].set_color(YELLOW)
        new_eq_4[1].set_color(GREEN)

        new_eq_1.next_to([-6, 1.5, 0], RIGHT)
        new_eq_2.next_to(eq_1, DOWN, buff=LARGE_BUFF).align_to(new_eq_1, LEFT)
        new_eq_3.next_to(eq_2, DOWN, buff=LARGE_BUFF).align_to(new_eq_2, LEFT)
        new_eq_4.next_to(eq_3, DOWN, buff=LARGE_BUFF).align_to(new_eq_3, LEFT)

        example_1 = TextMobject(r"$\sqrt[2]{2^{10}}=2^{\frac{10}{2}}=2^{5}$").scale(1)
        example_1.next_to(new_eq_1, RIGHT, buff=1.5*LARGE_BUFF)

        example_2 = TextMobject(r"$\frac{\sqrt[3]{200}}{\sqrt[3]{25}}=\sqrt[3]{\frac{200}{25}}=2$").scale(1)
        example_2.next_to(new_eq_2, RIGHT, buff=1.5*LARGE_BUFF).align_to(example_1, LEFT)

        example_3 = TextMobject(r"$\sqrt[2]{\sqrt[3]{16}}=\sqrt[3]{2}$").scale(1)
        example_3.next_to(new_eq_3, RIGHT, buff=1.5*LARGE_BUFF).align_to(example_1, LEFT)

        example_4 = TextMobject(r"$\sqrt[2]{18}=\sqrt[2]{9}\sqrt[2]{2}=3\sqrt[2]{2}$").scale(1)
        example_4.next_to(new_eq_4, RIGHT, buff=1.5*LARGE_BUFF).align_to(example_1, LEFT)


        # Old play
        self.play(FadeInFromDown(title))
        self.play(Write(context))
        self.play(Write(eq_1), Write(eq_2), Write(eq_3), Write(eq_4))
        self.wait(15)

        # New play
        self.play(ReplacementTransform(title, new_title), run_time=0.5)
        self.play(ReplacementTransform(context, new_context), run_time=0.5)
        self.play(ReplacementTransform(eq_1, new_eq_1), run_time=0.5)
        self.play(ReplacementTransform(eq_2, new_eq_2), run_time=0.5)
        self.play(ReplacementTransform(eq_3, new_eq_3), run_time=0.5)
        self.play(ReplacementTransform(eq_4, new_eq_4), run_time=0.5)
        self.wait(15)

        self.play(Write(example_1))
        self.wait(12)
        self.play(Write(example_2))
        self.wait(12)
        self.play(Write(example_3))
        self.wait(12)
        self.play(Write(example_4))
        self.wait(12)



class Exemples(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\textbf{Exemples}}").to_corner(UL).scale(1).set_color(PURPLE)
        context = TextMobject(r"Simplifiez chacune des expressions suivantes: ")
        context.next_to([-6.75, 2.5, 0])

        eq_1 = TextMobject(r"a) ", r"$\sqrt{17-3}$").scale(1)
        eq_2 = TextMobject(r"c) ", r"$\sqrt[3]{100}\sqrt[4]{100}$").scale(1)
        eq_3 = TextMobject(r"b) ", r"$\frac{3\sqrt{20}+2\sqrt{80}}{\sqrt{20}}$").scale(1)
        eq_4 = TextMobject(r"d) ", r"$4^{-\frac{3}{2}}$").scale(1)

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
        answers = TextMobject("Solutions (respectivement): $\sqrt{14}$, $7$, $100^{\\frac{7}{12}}$, $\\frac{1}{8}$").to_corner(DL)
        self.play(Write(answers))
        self.wait(15)



class Solutions(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\textbf{Solutions}}").to_corner(UL).scale(1).set_color(PURPLE)
        context = TextMobject(r"Simplifiez chacune des expressions suivantes: ")
        context.next_to([-6.75, 2.5, 0])

        eq_1 = TextMobject(r"a) ", r"$\sqrt{17-3}=\sqrt{14}$").scale(1)
        eq_2 = TextMobject(r"c) ", r"$\sqrt[3]{100}\sqrt[4]{100}=100^{\frac{1}{3}}100^{\frac{1}{4}}=100^{\frac{1}{3}+\frac{1}{4}}=100^{\frac{7}{12}}$").scale(1)
        eq_3 = TextMobject(r"b) ", r"$\frac{3\sqrt{20}+2\sqrt{80}}{\sqrt{20}}=3+\frac{2\sqrt{4\times 20}}{\sqrt{20}}=3+\frac{2\times2\sqrt{20}}{\sqrt{20}}=7$").scale(1)
        eq_4 = TextMobject(r"d) ", r"$4^{-\frac{3}{2}}=(\frac{1}{\sqrt{4}})^{3}=(\frac{1}{2})^{3}=\frac{1}{8}$").scale(1)

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
        self.wait(23)
        self.play(Write(eq_2))
        self.wait(13)
        self.play(Write(eq_4))
        self.wait(12)


class Conclusion(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\textbf{À retenir}}", color=PURPLE).to_corner(UL).scale(1)

        compl_rules_str = [
            "",
            "Définition de la racine,",
            "Lien entre les exposants et les racines,",
            "Propriétés des racines,",
            "Être en mesure de simplifier des expressions avec les propriétés des racines.",
        ]

        def choose_color(i):
            color = WHITE if i<=3 else YELLOW
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
        self.wait(5)
        self.play(Write(rules[4]))
        self.wait(15)


class NumberedList(BulletedList):
    CONFIG = {
        "dot_scale_factor": 1,
        "num_color": BLUE,
    }

    def __init__(self, *items, **kwargs):
        line_separated_items = [s + "\\\\" for s in items]
        TextMobject.__init__(self, *line_separated_items, **kwargs)

