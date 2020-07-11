from manimlib.imports import *


# 0. Thumbnail
# 1. Thumbnail2
# 2. ObjectifLecon
# 3. History
# 4. DefIntuition
# 5. Utilisation
# 7. ExempleAffirmation
# 8. ExempleDefinition
# 9. ExempleEquation
# 10. RegleOr
# 11. RegleOrExemples
# 12. ZeroDivision
# 13. ExempleElem
# 13. ExempleElemSol
# 13. ExempleComplexe
# 13. ExempleComplexeSol


class Thumbnail(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/images/"
        image_peinture = ImageMobject(path + "Perfectly_balanced")
        image_peinture.scale(3.25)
        image_peinture.to_edge(DOWN)


        line1 = TextMobject(r"{\sc Perfectly balanced").scale(2).shift(2.25 * UP).set_color(WHITE)
        line2 = TextMobject(r"=").scale(4).next_to(0.5*DOWN+2*LEFT).set_color(WHITE)
        #prob = TexMobject(r"\text{Find }T_n=A_n+B_n").scale(2).shift(2 * DOWN)
        self.play(FadeIn(image_peinture))
        self.play(Write(line1), Write(line2))

        self.wait(5)


class Thumbnail2(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/images/"
        image_peinture = ImageMobject(path + "Perfectly_balanced_robert")
        image_peinture.scale(3.25)
        image_peinture.to_edge(DOWN)


        line = TextMobject(r"{\sc ...as all things should be").scale(1.5).shift(2.5 * DOWN).set_color(WHITE)
        #prob = TexMobject(r"\text{Find }T_n=A_n+B_n").scale(2).shift(2 * DOWN)
        self.play(FadeIn(image_peinture))
        self.play(Write(line))
        self.wait(5)


class ObjectifLecon(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Objectifs d'apprentissage}", color=WHITE).to_corner(UL)
        #definition = TextMobject(r"Connaître la formule de l'aire d'un rectangle et calculer l'aire d'un rectangle.")
        definition = TextMobject(r"""
        \begin{itemize}
        \item Connaître la règle de substitution.
        \item Résoudre des problèmes d'algèbre nécessitant l'isolation d'un (ou des) inconnu(s).
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


class History(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Histoire}", color=WHITE).to_corner(UL)
        #definition = TextMobject(r"L’aire est la surface occupée par un objet sur un plan de deux dimensions. L’aire se calcule en unités carrées.")
        definition = TextMobject(r"Le signe $=$ a été introduit par Robert Recorde en 1557, dans Whetstone of Witte pour épargner à tous ceux qui "
                                 r"effectuaient des calculs (lui, en particulier) d'avoir à écrire est égal en toutes lettres.")
        definition.scale(0.7)
        definition.move_to(np.array([0, 2, 0]))
        definition.set_color(BLUE)
        #definition.to_edge(UP)

        path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/images/"
        image_robert = ImageMobject(path + "robert_recorde")
        image_robert.scale(1.75)
        image_robert.to_edge(DOWN)
        self.play(FadeIn(image_robert))

        self.play(Write(title))
        self.play(FadeIn(definition))
        self.wait(35)


class DefIntuition(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Définition (intuitive)}", color=WHITE).to_corner(UL)
        #definition = TextMobject(r"L’aire est la surface occupée par un objet sur un plan de deux dimensions. L’aire se calcule en unités carrées.")
        definition = TextMobject(r"Une égalité exprime l'équivalence entre deux termes, d'une entité par rapport à une autre.")
        definition.scale(0.7)
        definition.move_to(np.array([0, 2, 0]))
        definition.set_color(BLUE)
        #definition.to_edge(UP)

        self.play(Write(title))
        self.play(FadeIn(definition))
        self.wait(25)


class Utilisation(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Usages}", color=WHITE).to_corner(UL)
        #definition = TextMobject(r"L’aire est la surface occupée par un objet sur un plan de deux dimensions. L’aire se calcule en unités carrées.")
        definition = TextMobject(r"Une égalité peut apparaître comme :")
        definition.scale(0.7)
        definition.move_to(np.array([-4, 2, 0]))
        definition.set_color(BLUE)

        compl_rules_str = [
            "",
            "une affirmation,",
            " une définition de notation ou",
            "une équation.",
        ]

        rules = [TextMobject("{}) {}".format(i, rule), color=WHITE) for i, rule in enumerate(compl_rules_str)]
        rules = [rule.scale(0.7) for rule in rules]

        for (i, rule) in enumerate(rules):
            if i != 0:
                rule.next_to(rules[0].get_center() - rule.get_center() + np.array([-6, -2 - (0.7 * i), 0]))
        rules = VGroup(*rules)
        rules.to_corner(LEFT + UP)

        self.play(Write(title))
        self.play(FadeIn(definition))
        self.wait(3)
        self.play(Write(rules[1]))
        self.wait(3)
        self.play(Write(rules[2]))
        self.wait(3)
        self.play(Write(rules[3]))
        self.wait(10)


class ExempleAffirmation(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Exemple: Affirmation}", color=WHITE).to_corner(UL)

        title.move_to(np.array([-4.25, 3, 0]))
        caption_string = r"Soient $a,b\in\mathbb{R}$, alors on a que:"
        caption_property = TextMobject2(caption_string)
        caption_property.scale(0.7)
        caption_property.move_to(np.array([-4.5, 2.1, 0]))

        equality = TexMobject(
            "(a+b)^{2}",  # 0
            "=", # 1
            "a^{2}+b^{2}+2ab",  # 2
        )
        brace1 = Brace(equality[0], UP, buff=SMALL_BUFF)
        brace2 = Brace(equality[2], UP, buff=SMALL_BUFF)
        t1 = brace1.get_text("Côté gauche")
        t2 = brace2.get_text("Côté droit")

        self.play(Write(title))
        self.play(FadeIn(caption_property))
        self.play(FadeIn(equality))
        self.play(
            GrowFromCenter(brace1),
            FadeIn(t1),
        )
        self.wait(15)
        self.play(
            ReplacementTransform(brace1, brace2),
            ReplacementTransform(t1, t2)
        )
        self.wait(15)
        self.play(FadeOut(equality))
        self.play(FadeOut(caption_property))
        self.play(FadeOut(title))


class ExempleDefinition(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Exemple: Définition de notation}", color=WHITE).to_corner(UL)
        title.move_to(np.array([-2.75, 3, 0]))
        caption_string = r"Soit $f:\mathbb{R}\rightarrow\mathbb{R}$, la fonction définie par $f(x)=ax^{2}+bx+c$ où $a,b,c\in\mathbb{R}$. " \
                         r"La fonction possède au moins un zéro si $\Delta=b^{2}-4ac \geq 0$."
        caption_property = TextMobject2(caption_string)
        caption_property.scale(0.7)
        caption_property.move_to(np.array([-1, 2.1, 0]))

        equality = TexMobject(
            "x",  # 0
            "=", # 1
            "\\frac{-b\pm\sqrt{\Delta}}{2a}",
            "=",
            "\\frac{-b\pm\sqrt{b^{2}-4ac}}{2a}",  # 2
        )

        self.play(Write(title))
        self.play(FadeIn(caption_property))
        self.wait(22)
        self.play(Write(equality))
        self.wait(25)
        self.play(FadeOut(equality))
        self.play(FadeOut(caption_property))
        self.play(FadeOut(title))


class ExempleEquation(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Exemple: Équation}", color=WHITE).to_corner(UL)

        title.move_to(np.array([-4.5, 3, 0]))
        caption_string = r"La première équation connue sous la notation de Recorde est: "
        caption_property = TextMobject2(caption_string)
        caption_property.scale(0.7)
        caption_property.move_to(np.array([-2.25, 2.1, 0]))

        equality = TexMobject(
            "14x + 15 ",  # 0
            "=", # 1
            "71"
        )

        self.play(Write(title))
        self.play(FadeIn(caption_property))
        self.wait(10)
        self.play(Write(equality))
        self.wait(15)
        self.play(FadeOut(equality))
        self.play(FadeOut(caption_property))
        self.play(FadeOut(title))


class RegleOr(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc La règle de substitution}", color=GOLD).to_corner(UL)

        definition = TextMobject(r"""
                            \RedBox[label=exsecond]{}{
                            Pour toutes quantités $a$ et $b$, et pour toute expression $F(x)$, si $a = b$ alors : 
                            \begin{equation}
                            F(a) = F(b)
                            \end{equation}
                            }      
                        """
                                 )
        definition.scale(0.5)
        definition.next_to(1.5 * UP + 5.5 * LEFT)

        self.play(Write(title))
        self.play(FadeIn(definition))
        self.wait(35)
        self.play(FadeOut(definition))
        self.play(FadeOut(title))


class RegleOrExemples(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = TextMobject(r"\underline{\sc Cas particuliers de la règle d'or}", color=GOLD).to_corner(UL)

        definition = TextMobject(r"""
                \begin{itemize}
                \item \underline{$F(x)=x + c$}: Soient $a, b, c\in\mathbb{R}$, si $a = b$ alors $F(a) = a + c = b + c = F(b)$,
                \item \underline{$F(x)=x - c$}: Soient $a, b, c\in\mathbb{R}$, si $a = b$ alors $F(a) = a - c = b - c = F(b)$,
                \item \underline{$F(x)=cx$}: Soient $a, b, c\in\mathbb{R}$, si $a = b$ alors $F(a) = ca = cb = F(b)$,
                \item \underline{$F(x)=\frac{x}{c}$}: Soient $a, b\in\mathbb{R}$ et $c\neq 0$, si $a = b$ alors $F(a) = \frac{a}{c} = \frac{b}{c} = F(b)$,
                \end{itemize}
                """)
        definition.scale(0.7)
        definition.move_to(np.array([-1, 1, 0]))
        definition.set_color(BLUE)

        self.play(Write(title))
        self.wait(7)
        self.play(FadeIn(definition))

        self.wait(45)
        self.play(FadeOut(definition))
        self.play(FadeOut(title))


class ZeroDivision(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }

    def construct(self):
        path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/images/"
        image_peinture = ImageMobject(path + "divide_by_zero")
        image_peinture.scale(3.25)
        image_peinture.to_edge(DOWN)

        # prob = TexMobject(r"\text{Find }T_n=A_n+B_n").scale(2).shift(2 * DOWN)
        self.play(FadeIn(image_peinture))
        self.wait(15)


class ExempleElem(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }

    def construct(self):
        title = TextMobject(r"\underline{\sc Exercice: $1$ équation, $1$ inconnu}", color=WHITE).to_corner(UL)

        title.move_to(np.array([-2.5, 3, 0]))
        caption_string = r"Trouver la solution de l'équations suivante: "
        caption_property = TextMobject2(caption_string)
        caption_property.scale(0.7)
        caption_property.move_to(np.array([-2.25, 2.1, 0]))

        equality = TexMobject(
            "14x + 15 ",  # 0
            "=",  # 1
            "71"
        )

        self.play(Write(title))
        self.wait(5)
        self.play(Write(equality))

        # Pause to think about it.
        circ = Arc(start_angle=PI / 2, angle=-2 * PI, radius=0.35).to_corner(DL)
        timers = [TexMobject(str(i)).move_to(circ) for i in range(5, -1, -1)]
        pause = TextMobject("Faites pause et trouvez la valeur de $x$.").next_to(circ, RIGHT)
        self.play(ShowCreation(circ), Write(pause))
        self.play(Write(timers[0]), run_time=0.5)
        for i in range(5):
            self.play(ReplacementTransform(timers[i], timers[i + 1]), run_time=0.5)
            self.wait(0.5)
        self.play(FadeOut(pause), FadeOut(timers[-1]), FadeOut(circ), run_time=2)

        answer = TextMobject("Solution: $x=4$").to_corner(DL)
        self.play(Write(answer))
        self.wait(10)



class ExempleElemSol(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }

    def construct(self):
        title = TextMobject(r"\underline{\sc Solution: $1$ équation, $1$ inconnu}", color=WHITE).to_corner(UL)

        equation1 = TexMobject("14x+15", "=", "71")
        equation2 = TexMobject("14x", "=", "71-15")
        equation3 = TexMobject("14x", "=", "56")
        equation4 = TexMobject("x", "=", "\\frac{56}{14}","=","4")

        self.play(Write(title))
        self.wait(5)
        self.play(Write(equation1))
        self.wait(5)
        self.play(ReplacementTransform(equation1, equation2))
        self.wait(5)
        self.play(ReplacementTransform(equation2, equation3))
        self.wait(5)
        self.play(ReplacementTransform(equation3, equation4))
        self.wait(15)


class ExempleComplexe(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }

    def construct(self):
        title = TextMobject(r"\underline{\sc Exercice: $2$ équations, $2$ inconnus}", color=WHITE).to_corner(UL)

        title.move_to(np.array([-2.5, 3, 0]))
        definition1 = TextMobject(r"""
                        \systeme{3x-4y=32, 7x-6y=58}
                        """)
        definition1.scale(1.25)
        definition1.move_to(np.array([-1, 1, 0]))
        definition1.set_color(BLUE)

        #definition2 = TextMobject(r"""
        ##                        \systeme{-9x+12y=-96, 14x-12y=116}
        #                        """)
        #definition2.scale(0.7)
        #definition2.move_to(np.array([-1, 1, 0]))
        #definition2.set_color(BLUE)

        self.play(Write(title))
        self.play(FadeIn(definition1))


        # Pause to think about it.
        circ = Arc(start_angle=PI / 2, angle=-2 * PI, radius=0.35).to_corner(DL)
        timers = [TexMobject(str(i)).move_to(circ) for i in range(5, -1, -1)]
        pause = TextMobject("Faites pause et trouvez la valeur de $x$ et de $y$.").next_to(circ, RIGHT)
        self.play(ShowCreation(circ), Write(pause))
        self.play(Write(timers[0]), run_time=0.5)
        for i in range(5):
            self.play(ReplacementTransform(timers[i], timers[i + 1]), run_time=0.5)
            self.wait(0.5)
        self.play(FadeOut(pause), FadeOut(timers[-1]), FadeOut(circ), run_time=2)

        answer = TextMobject("Solution: $x=4$ et $y=-5$").to_corner(DL)
        self.play(Write(answer))
        self.wait(20)


class ExempleComplexeSol(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }

    def construct(self):
        title = TextMobject(r"\underline{\sc Solution: $2$ équations, $2$ inconnus}", color=WHITE).to_corner(UL)

        title.move_to(np.array([-2.5, 3, 0]))
        system0 = TextMobject(r"""\systeme{3x-4y=32, 7x-6y=58}""")
        system0.scale(0.7)
        system0.move_to(np.array([-1, 2, 0]))
        system0.set_color(BLUE)

        sytem0_copy = system0.copy()

        system1 = TextMobject(r"""\systeme{-9x+12y=-96, 7x-6y=58}""")
        system1.scale(0.7)
        system1.move_to(np.array([-1, 2, 0]))
        system1.set_color(BLUE)

        system2 = TextMobject(r"""\systeme{-9x+12y=-96, 14x-12y=116}""")
        system2.scale(0.7)
        system2.move_to(np.array([-1, 2, 0]))
        system2.set_color(BLUE)



        operations1 = TextMobject(r"""
                        \begin{enumerate}
                        \item $E_{1}\leftarrow -3 E_{1}$,
                        \end{enumerate}
                        """)
        operations1.scale(0.7)
        operations1.move_to(np.array([-5, -2, 0]))
        operations1.set_color(BLUE)

        operations2 = TextMobject(r"""
                                \begin{enumerate}
                                \item $E_{1}\leftarrow -3 E_{1}$,
                                \item $E_{2}\leftarrow 2 E_{2}$,
                                \end{enumerate}
                                """)
        operations2.scale(0.7)
        operations2.move_to(np.array([-5, -2, 0]))
        operations2.set_color(BLUE)


        operations3 = TextMobject(r"""
                                                \begin{enumerate}
                                                \item $E_{1}\leftarrow -3 E_{1}$,
                                                \item $E_{2}\leftarrow 2 E_{2}$,
                                                \item $E_{1}+E_{2}$.
                                                \end{enumerate}
                                                """)
        operations3.scale(0.7)
        operations3.move_to(np.array([-5, -2, 0]))
        operations3.set_color(BLUE)

        operations4 = TextMobject(r"""
                                                        \begin{enumerate}
                                                        \item $E_{1}\leftarrow -3 E_{1}$,
                                                        \item $E_{2}\leftarrow 2 E_{2}$,
                                                        \item $E_{1}+E_{2}$,
                                                        \item Substituez $x$ dans $E_{1}$ ou $E_{2}$.
                                                        \end{enumerate}
                                                        """)
        operations4.scale(0.7)
        operations4.move_to(np.array([-4, -2, 0]))
        operations4.set_color(BLUE)

        simplified_equation = TexMobject("5x+0y", "=", "20")
        simplified_equation.scale(0.7)
        simplified_equation.next_to(np.array([-2,0.75,0]))

        subsitution_equation = TexMobject("3(4)-4y=32","\Leftrightarrow", "-4y=20")
        subsitution_equation.scale(0.7)
        subsitution_equation.next_to(np.array([-3, 0.75, 0]))

        solution_x = TexMobject("x=4", color=BLUE)
        solution_x.scale(1)
        solution_x.next_to(np.array([1, -2, 0]))
        frameBox_x = SurroundingRectangle(solution_x, buff=0.75 * SMALL_BUFF)
        frameBox_x.set_stroke(RED, 2)

        solution_y = TexMobject("y=-5", color=BLUE)
        solution_y.scale(1)
        solution_y.next_to(np.array([4, -2, 0]))
        frameBox_y = SurroundingRectangle(solution_y, buff=0.75 * SMALL_BUFF)
        frameBox_y.set_stroke(RED, 2)

        horizontal_line = Line(np.array([-3.25,1.25,0]), np.array([1.5,1.25,0]), color=GREEN)

        self.play(Write(title))
        self.wait(5)
        self.play(Write(system0))
        self.wait(5)
        self.play(Write(operations1))
        self.wait(5)
        self.play(ReplacementTransform(system0, system1))
        self.wait(5)
        self.play(ReplacementTransform(operations1, operations2))
        self.wait(5)
        self.play(ReplacementTransform(system1, system2))
        self.wait(5)
        self.play(ShowCreation(horizontal_line))
        self.wait(5)
        self.play(ReplacementTransform(operations2, operations3))
        self.wait(5)
        self.play(ShowCreation(simplified_equation))
        self.wait(5)
        self.play(Write(solution_x))
        self.play(ShowCreation(frameBox_x))
        self.wait(5)
        self.play(FadeOut(simplified_equation))
        self.play(FadeOut(horizontal_line))
        self.play(ReplacementTransform(system2, sytem0_copy))
        self.wait(5)
        self.play(ReplacementTransform(operations3, operations4))
        self.wait(5)
        self.play(FadeIn(subsitution_equation))
        self.play(Write(solution_y))
        self.play(ShowCreation(frameBox_y))
        self.wait(10)


class Credits(Scene):
    def wplay(self, *args, wait=1, run_time=1, rate_func=smooth):
        self.play(*args, run_time=run_time, rate_func=rate_func)
        if wait != 0:
            self.wait(wait)

    def construct(self):
        credits = TextMobject("Crédits").set_color(YELLOW).scale(1.7)
        thanks = TextMobject("Merci d'avoir visionné le vidéo!!").set_color(ORANGE).scale(1.7)

        instructor = TexMobject(r"\text{Enseignant}", r"\text{Louis-Marc Mercier}")
        viewer = TexMobject(r"\text{Spectateur}", r"\text{You}")
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