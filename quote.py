from big_ol_pile_of_manim_imports import *


class ShowImageAndQuote(Scene):
    def construct(self):
        quote = TextMobject(r"Une in\'egalit\'e exprime la domination d'un terme par rapport \`a un autre, d'une entit\'e par rapport \`a une autre.")
        quote.scale(0.7)
        quote.set_color(RED)
        quote.to_edge(UP)
        author = TextMobject(r"-C\'edric Villani")
        author.scale(0.7)
        author.next_to(quote.get_corner(DOWN + RIGHT), DOWN)
        self.play(FadeIn(quote))
        self.play(FadeIn(author))

        path = r"C:/Users/Utilisateur/Desktop/CEGEP/"
        image = ImageMobject(path + "new_file")
        image.scale(2.75)
        image.to_edge(DOWN)
        self.play(FadeIn(image))
        self.wait(2)
        self.play(FadeOut(image))
        self.play(FadeOut(author))
        self.play(FadeOut(quote))



class CauchySwartzInequality(Scene):
    def construct(self):
        Title = TextMobject(
            r"\underline{ In\'egalit\'e de Cauchy-Swartz}")
        Title.move_to(np.array([-3.75, 3, 0]))

        caption_string = r"Soit $\mathbf{x},\mathbf{y}\in\mathbb{R}^{n}$, alors "
        caption_property = TextMobject(caption_string)
        caption_property.scale(0.75)
        caption_property.move_to(np.array([-5, 2.1, 0]))

        inequality = TexMobject(
            "|\\mathbf{x}\\mathbf{y}|\leq",  # 0
            "\\norm{\\mathbf{x}}\\norm{\\mathbf{y}}",  # 1
        )

        self.play(Write(Title))
        self.play(FadeIn(caption_property))
        self.play(Write(inequality))
        self.wait()
        self.play(FadeOut(inequality))
        self.play(FadeOut(caption_property))
        self.play(FadeOut(Title))


class JensenInequality(Scene):
    def construct(self):
        Title = TextMobject(
            r"\underline{ In\'egalit\'e de Jensen}")
        Title.move_to(np.array([-4.75, 3, 0]))

        caption_string = r"Soient $f$ une fonction convexe, $\mathbf{x}\in\mathbb{R}^{n}$ appartenant \`a l'intervalle de d\'efinition de $f$ et " \
                         r" $\boldsymbol{\lambda}\in\mathbb{R}_{+}^{n}$ tels que $\sum_{i=1}^{n}\lambda_{i}=1$, alors"
        caption_property = TextMobject2(caption_string)
        caption_property.scale(0.7)
        caption_property.move_to(np.array([-0.75, 2.1, 0]))

        inequality = TexMobject(
            "f\Bigg(\sum_{i=1}^{n}\lambda_{i}x_{i}\Bigg)\leq",  # 0
            "\sum_{i=1}^{n}\lambda_{i}f(x_{i})",  # 1
        )

        self.play(Write(Title))
        self.play(FadeIn(caption_property))
        self.play(Write(inequality))
        self.wait()
        self.play(FadeOut(inequality))
        self.play(FadeOut(caption_property))
        self.play(FadeOut(Title))


class YoungInequality(Scene):
    def construct(self):
        Title = TextMobject(
            r"\underline{ In\'egalit\'e de Young}")
        Title.move_to(np.array([-4.75, 3, 0]))

        caption_string = r"Pour tous $a,b\in\mathbb{R}_{+}$ et $p,q\in\mathbb{R}_{+}\textbackslash\{0\}$ tels que $\frac{1}{p}+\frac{1}{q}=1$, on a "
        caption_property = TextMobject(caption_string)
        caption_property.scale(0.75)
        caption_property.move_to(np.array([-1.7,2.1,0]))

        inequality = TexMobject(
            "ab\leq",  # 0
            "\\frac{a^{p}}{p}",  # 1
            "+",
            "\\frac{b^{q}}{q}",  # 3
        )

        self.play(Write(Title))
        self.play(FadeIn(caption_property))
        self.play(Write(inequality))
        self.wait()
        self.play(FadeOut(inequality))
        self.play(FadeOut(caption_property))
        self.play(FadeOut(Title))


class GeoArithmInequality(Scene):
    def construct(self):
        Title = TextMobject(
            r"\underline{ In\'egalit\'e arithm\'etico-g\'eom\'etrique}")
        Title.move_to(np.array([-3.5, 3, 0]))

        caption_string = r"La moyenne g\'eom\'etrique de $x_{1},x_{2},\dots,x_{n}\in\mathbb{R}$ est inf\'erieure \`a leur moyenne arithm\'etique, i.e. "
        caption_property = TextMobject2(caption_string)
        caption_property.scale(0.75)
        caption_property.move_to(np.array([-0.65,2.1,0]))

        inequality = TexMobject(
            "\\sqrt[n]{x_{1}x_{2}\dots x_{n}} \leq",  # 0
            "\\frac{x_{1} + x_{2} +\dots + x_{n}}{n}",  # 1
        )

        self.play(Write(Title))
        self.play(FadeIn(caption_property))
        self.play(Write(inequality))
        self.wait(4)
        self.play(FadeOut(inequality))
        self.play(FadeOut(caption_property))
        self.play(FadeOut(Title))


class ShowInequalities(Scene):
    def construct(self):
        # Display image and quote.
        ShowImageAndQuote.construct(self)

        # TO DO:
        # 1) First inequality (Cauchy-Swartz Inequality)
        CauchySwartzInequality.construct(self)

        # 2) Second inequality (Jensen Inequality)
        JensenInequality.construct(self)

        # 3) Fourth inequality (Geometric-Arithmetic Inequality)
        GeoArithmInequality.construct(self)

        # 4) Third inequality (Young Inequality)
        YoungInequality.construct(self)


