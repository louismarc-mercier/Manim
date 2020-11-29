from manimlib.imports import *
from manim_utils.slide_template import Warning, BoxedTitle, GenChannelLogo, YoutubeLogo

# 1. ThumbnailFrench
# 2. Motivation
# 3. Definition
# 4. ParamA
# 5. ParamC
# 6. CanonForm
# 7. ParamH
# 8. ParamK
# 9. Symetrie
# 10. Transformation
# 11. Exo
# 11. Conclusion


class ThumbnailFrench(GraphScene):
    """
    Quadratic function on interval [-10, 10]
    """
    CONFIG = {
        "y_max" : 10,
        "y_min" : -10,
        "x_max" : 10,
        "x_min" : -10,
        "y_axis_label": "$f(x)$",
        "y_tick_frequency" : 1,
        "x_tick_frequency" : 1,
        "axes_color" : GRAY,
        "y_labeled_nums": range(-10,10,2),
        "x_labeled_nums": list(np.arange(-10, 10, 2)),
        "x_label_decimal":0,
        "y_label_decimal":0,
        "graph_origin": np.array((0, 0, 0))
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : x**2,
                                    color = GREEN,
                                    x_min = self.x_min,
                                    x_max = self.x_max
                                    )
        #graph.y_axis_label = TextMobject(r"$f(x)$")

        #graph_lab = TextMobject(r"\sc{Fonction}", r"\sc{quadratique}").set_color([YELLOW, PINK])
        graph_lab = BoxedTitle(text="Fonction quadratique", width=5, height=0.5, scale=0.7, text_color="#C70039",
                               box_split_color="#C70039")
        graph_lab.next_to(np.array([-3.5,-1.4,0])).rotate(PI/8).scale(2)
        self.play(ShowCreation(graph), ShowCreation(graph_lab), run_time = 2)
        self.wait(10)


class Motivation(GraphScene):
    """
    Quadratic function on interval [-10, 10]
    """
    CONFIG = {
        "y_max" : 10,
        "y_min" : -10,
        "x_max" : 10,
        "x_min" : -10,
        #"y_axis_label": "$f(x)$",
        "y_tick_frequency" : 10,
        "x_tick_frequency" : 10,
        "axes_color" : BLACK,
        "y_labeled_nums": range(-100,100,20),
        "x_labeled_nums": list(np.arange(-100, 100, 20)),
        "x_label_decimal":0,
        "y_label_decimal":0,
        "graph_origin": np.array((0, 0, 0))
    }
    def construct(self):
        self.setup_axes(animate=True)

        title = BoxedTitle(text="Motivation", width=3, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))
        self.play(ShowCreation(title))

        # Add the basket ball animation.
        path = r"C:/Users/Utilisateur/Desktop/CEGEP/Cours_maison/toastersman_videos/Revision_precalcul/Fonction_quadratique/partie_1/images/trajectory/"
        images = [ImageMobject("{}{}_balls.PNG".format(path, i)).scale(1.5) for i in range(1, 17)]
        for i, image in enumerate(images):
            if i == 0:
                self.play(ShowCreation(image))
            else:
                self.play(ReplacementTransform(old_image, image), run_time=0.5)
            old_image = image


        # Synonyms
        synonyms = ["- Fonction du second degré, ","- Fonction quadratique,",
                    "- Polynôme de degré deux."]
        synonyms_mbjs = [TextMobject(synonym).scale(0.85).set_color(BLUE) for synonym in synonyms]

        synonyms_mbjs[0].next_to(np.array([-7, 2, 0]))
        synonyms_mbjs[1].next_to(synonyms_mbjs[0], DOWN).align_to(synonyms_mbjs[0], LEFT)
        synonyms_mbjs[2].next_to(synonyms_mbjs[1], DOWN).align_to(synonyms_mbjs[1], LEFT)


        graph = self.get_graph(lambda x : (-1.05*x**2)+4.25,
                                    color = BLUE,
                                    x_min = self.x_min,
                                    x_max = self.x_max
                                    )

        self.play(ShowCreation(graph), run_time = 2)
        self.wait(3)
        self.play(Write(synonyms_mbjs[0]))
        self.wait(2)
        self.play(Write(synonyms_mbjs[1]))
        self.wait(2)
        self.play(Write(synonyms_mbjs[2]))
        self.wait(10)



class Definition(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Forme générale", width=4, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        # Source: https://github.com/vivek3141/videos/blob/master/maxwell.py
        color_map = {
            r"a": BLUE,
            r"b": ORANGE,
            r"c": PINK,
        }


        statement = TextMobject2(r"Soit $f:\mathbb{R}\rightarrow\mathbb{R}$, la fonction quadratique définie par").scale(0.8)
        statement.next_to(title, DOWN, buff=LARGE_BUFF)
        formula = TexMobject(r"f(x)=ax^{2}+bx+c", tex_to_color_map=color_map)


        description_m = TexMobject(r"a\neq 0", tex_to_color_map=color_map).next_to(formula, DOWN, buff=LARGE_BUFF)


        description_b = TexMobject(r"b,c\in", tex_to_color_map=color_map).next_to(description_m, DOWN).align_to(description_m, RIGHT)
        description_b_cont = TextMobject(r"$\mathbb{R}$").next_to(description_b, RIGHT)


        warning_desc = TexMobject(r"a,b,c", tex_to_color_map=color_map).next_to(description_m, RIGHT, buff=3*LARGE_BUFF)
        warning_desc_cont = TextMobject(r"$\bot x$").next_to(warning_desc, RIGHT, buff=0.1*SMALL_BUFF)
        warning_symbol = Warning().scale(0.3).next_to(warning_desc_cont, RIGHT)

        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement))
        self.wait(5)
        self.play(Write(formula))
        self.wait(5)
        self.play(Write(description_m))
        self.wait(5)
        self.play(Write(description_b), Write(description_b_cont))
        self.wait(5)
        self.play(WiggleOutThenIn(warning_symbol))
        self.wait(3)
        self.play(Write(warning_desc), Write(warning_desc_cont))
        self.wait(10)



class ParamA(GraphScene):
    """
    Quadratic function on interval [-10, 10]
    """
    CONFIG = {
        "y_max" : 10,
        "y_min" : -10,
        "x_max" : 10,
        "x_min" : -10,
        "y_axis_label": "$f(x)$",
        "y_tick_frequency" : 0.5,
        "x_tick_frequency" : 0.5,
        "axes_color" : GRAY,
        "y_labeled_nums": range(-10,10,2),
        "x_labeled_nums": list(np.arange(-10, 10, 2)),
        "x_label_decimal":0,
        "y_label_decimal":0,
        "graph_origin": np.array((0, 0, 0))
    }
    def construct(self):
        self.setup_axes(animate=True)

        color_map = {
            r"a": BLUE,
        }

        formula = TexMobject(r"f(x)=ax^{2}", tex_to_color_map=color_map).to_corner(UL)
        self.play(ShowCreation(formula))


        case_1 = BoxedTitle(text="", width=3, height=0.7, scale=0.7).to_corner(DR)
        case_1_ctd = TextMobject(r"Si ", r"$a$", r"$>0$").scale(0.7)
        case_1_ctd[0].set_color(BLACK).next_to(case_1.get_center() - np.array([1,0,0]))
        case_1_ctd[1].set_color(BLUE).next_to(case_1_ctd[0].get_center() + np.array([0, -0.05, 0]))
        case_1_ctd[2].set_color(BLACK).next_to(case_1_ctd[1].get_center() + np.array([-0.02, 0.03, 0]))

        case_2 = BoxedTitle(text="", width=3, height=0.7, scale=0.7).to_corner(UR)
        case_2_ctd = TextMobject(r"Si ", r"$a$", r"$<0$").scale(0.7)
        case_2_ctd[0].set_color(BLACK).next_to(case_2.get_center() - np.array([1, 0, 0]))
        case_2_ctd[1].set_color(BLUE).next_to(case_2_ctd[0].get_center() + np.array([0, -0.05, 0]))
        case_2_ctd[2].set_color(BLACK).next_to(case_2_ctd[1].get_center() + np.array([-0.02, 0.02, 0]))

        self.play(FadeIn(case_1), FadeIn(case_1_ctd))

        slopes = [0.25,1,3,9,-0.25,-1,-3,-9]
        for i, slope in enumerate(slopes):
            if i == 4:
                self.play(ReplacementTransform(case_1, case_2), ReplacementTransform(case_1_ctd, case_2_ctd))

            graph = self.get_graph(lambda x: slope*(x**2), color=WHITE, x_min=self.x_min, x_max=self.x_max)
            graph_lab = self.get_graph_label(graph, label="a").set_color(BLUE)
            graph_lab_ctd = TexMobject(r"={}".format(slope)).next_to(graph_lab.get_center() + np.array([0.1,0.05,0]))

            if i==0:
                self.play(ShowCreation(graph), ShowCreation(graph_lab), ShowCreation(graph_lab_ctd), run_time=2)
                self.wait(3)
                old_graph, old_graph_lab, old_graph_lab_ctd = graph, graph_lab, graph_lab_ctd
            else:
                self.play(ReplacementTransform(old_graph, graph), ReplacementTransform(old_graph_lab, graph_lab),
                          ReplacementTransform(old_graph_lab_ctd, graph_lab_ctd), run_time=2)
                self.wait(3)
                old_graph, old_graph_lab, old_graph_lab_ctd = graph, graph_lab, graph_lab_ctd

        self.wait(5)


class ParamB(GraphScene):
    """
    Quadratic function on interval [-10, 10]
    """
    CONFIG = {
        "y_max" : 10,
        "y_min" : -10,
        "x_max" : 10,
        "x_min" : -10,
        "y_axis_label": "$f(x)$",
        "y_tick_frequency" : 0.5,
        "x_tick_frequency" : 0.5,
        "axes_color" : GRAY,
        "y_labeled_nums": range(-10,10,2),
        "x_labeled_nums": list(np.arange(-10, 10, 2)),
        "x_label_decimal":0,
        "y_label_decimal":0,
        "graph_origin": np.array((0, 0, 0))
    }
    def construct(self):
        self.setup_axes(animate=True)

        color_map = {
            r"a": BLUE,
            r"b": ORANGE,
        }

        formula = TexMobject(r"f(x)=x^{2}+bx+1", tex_to_color_map=color_map).to_corner(UL)
        self.play(ShowCreation(formula))

        warning_desc = TexMobject(r"a>0", tex_to_color_map=color_map).to_corner(UR)
        warning_symbol = Warning().scale(0.3).next_to(warning_desc, LEFT)
        self.play(WiggleOutThenIn(warning_symbol), ShowCreation(warning_desc))

        case_1 = BoxedTitle(text="", width=3, height=0.7, scale=0.7).to_corner(DR)
        case_1_ctd = TextMobject(r"Si ", r"$b$", r"$>0$").scale(0.7)
        case_1_ctd[0].set_color(BLACK).next_to(case_1.get_center() - np.array([1,0,0]))
        case_1_ctd[1].set_color(ORANGE).next_to(case_1_ctd[0].get_center() + np.array([0, 0, 0]))
        case_1_ctd[2].set_color(BLACK).next_to(case_1_ctd[1].get_center() + np.array([-0.02, 0.03, 0]))

        case_2 = BoxedTitle(text="", width=3, height=0.7, scale=0.7).to_corner(DL)
        case_2_ctd = TextMobject(r"Si ", r"$b$", r"$<0$").scale(0.7)
        case_2_ctd[0].set_color(BLACK).next_to(case_2.get_center() - np.array([1, 0, 0]))
        case_2_ctd[1].set_color(ORANGE).next_to(case_2_ctd[0].get_center() + np.array([0, 0, 0]))
        case_2_ctd[2].set_color(BLACK).next_to(case_2_ctd[1].get_center() + np.array([-0.02, 0.02, 0]))

        self.play(FadeIn(case_1), FadeIn(case_1_ctd))

        slopes = [0.5,1,3,6,-0.5,-1,-3,-6]
        for i, slope in enumerate(slopes):
            if i == 4:
                self.play(ReplacementTransform(case_1, case_2), ReplacementTransform(case_1_ctd, case_2_ctd))

            graph = self.get_graph(lambda x: (x**2)+slope*x+1, color=WHITE, x_min=self.x_min, x_max=self.x_max)
            graph_lab = self.get_graph_label(graph, label="b").set_color(ORANGE)
            graph_lab_ctd = TexMobject(r"={}".format(slope)).next_to(graph_lab.get_center() + np.array([0.1,0.05,0]))

            if i==0:
                self.play(ShowCreation(graph), ShowCreation(graph_lab), ShowCreation(graph_lab_ctd), run_time=2)
                self.wait(3)
                old_graph, old_graph_lab, old_graph_lab_ctd = graph, graph_lab, graph_lab_ctd
            else:
                self.play(ReplacementTransform(old_graph, graph), ReplacementTransform(old_graph_lab, graph_lab),
                          ReplacementTransform(old_graph_lab_ctd, graph_lab_ctd), run_time=2)
                self.wait(3)
                old_graph, old_graph_lab, old_graph_lab_ctd = graph, graph_lab, graph_lab_ctd
        self.wait(5)




class ParamC(GraphScene):
    """
    Quadratic function on interval [-10, 10]
    """
    CONFIG = {
        "y_max" : 10,
        "y_min" : -10,
        "x_max" : 10,
        "x_min" : -10,
        "y_axis_label": "$f(x)$",
        "y_tick_frequency" : 0.5,
        "x_tick_frequency" : 0.5,
        "axes_color" : GRAY,
        "y_labeled_nums": range(-10,10,2),
        "x_labeled_nums": list(np.arange(-10, 10, 2)),
        "x_label_decimal":0,
        "y_label_decimal":0,
        "graph_origin": np.array((0, 0, 0))
    }
    def construct(self):
        self.setup_axes(animate=True)

        color_map = {
            r"a": ORANGE,
            r"c": PINK,
        }

        formula = TexMobject(r"f(x)=x^{2}+c", tex_to_color_map=color_map).to_corner(UL)
        self.play(ShowCreation(formula))

        ordonnees_origine = [-9, -6, -3, 0, 3, 6, 9]
        y_0 = self.coords_to_point(0, 0)
        ys_coords = [self.coords_to_point(0, ordonnee) for ordonnee in ordonnees_origine]
        for i, (ordonnee_origine, y_coord) in enumerate(zip(ordonnees_origine, ys_coords)):

            graph = self.get_graph(lambda x: 1*(x**2) + ordonnee_origine, color=WHITE, x_min=self.x_min, x_max=self.x_max)
            horizontal_line = Line(y_0, y_coord, color=PINK)
            #graph_lab_ctd = TexMobject("b", "=", "{}".format(ordonnee_origine)).next_to(horizontal_line.get_center() - np.array([0.1,0.05,0]))
            graph_lab_ctd = TexMobject("b", "=", "{}".format(ordonnee_origine)).next_to(horizontal_line, LEFT, buff=MED_LARGE_BUFF)
            graph_lab_ctd[0].set_color(PINK)
            graph_lab_ctd[2].set_color(PINK)

            if i==0:
                self.play(ShowCreation(graph), ShowCreation(graph_lab_ctd), ShowCreation(horizontal_line), run_time=2)
                self.wait(3)
                old_graph, old_graph_lab_ctd, old_horizontal_line = graph, graph_lab_ctd, horizontal_line
            else:
                self.play(ReplacementTransform(old_graph, graph),
                          ReplacementTransform(old_graph_lab_ctd, graph_lab_ctd),
                          ReplacementTransform(old_horizontal_line, horizontal_line), run_time=2)
                self.wait(3)
                old_graph, old_graph_lab_ctd, old_horizontal_line = graph, graph_lab_ctd, horizontal_line

        self.wait(5)


class CanonForm(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Formes", width=3, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        # Source: https://github.com/vivek3141/videos/blob/master/maxwell.py
        color_map = {
            r"a": BLUE,
            r"b": ORANGE,
            r"c": PINK,
            r"h": RED,
            r"k": GREEN,
        }

        statement = TextMobject2(r"Soit $f:\mathbb{R}\rightarrow\mathbb{R}$, la fonction quadratique définie par").scale(0.8)
        statement.next_to(title, DOWN, buff=LARGE_BUFF)
        formula_general = TexMobject(r"f(x)=ax^{2}+bx+c", tex_to_color_map=color_map).align_to(statement, LEFT)
        description_general = TextMobject("(Forme générale)").next_to(formula_general, RIGHT, buff=LARGE_BUFF)
        checkmark = TexMobject("\\checkmark")
        checkmark.set_color(GREEN).scale(1.25)
        checkmark.next_to(description_general, RIGHT, buff=LARGE_BUFF)


        formula_canon = TexMobject(r"f(x)=a(x-h)^{2}+k", tex_to_color_map=color_map).next_to(formula_general, DOWN).align_to(formula_general, LEFT)
        description_canon = TextMobject("(Forme canonique)").next_to(formula_canon, RIGHT, buff=LARGE_BUFF).align_to(description_general, LEFT)


        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement))
        self.wait(5)
        self.play(Write(formula_general), Write(description_general), Write(checkmark))
        self.wait(5)
        self.play(Write(formula_canon), Write(description_canon))

        # Pause to think about it.
        circ = Arc(start_angle=PI / 2, angle=-2 * PI, radius=0.35).to_corner(DL)
        timers = [TexMobject(str(i)).move_to(circ) for i in range(10, -1, -1)]
        pause = TextMobject("À quoi ", r"(", r"$h$", r", ", r"$k$", r") ", r"correspond dans le forme canonique?").scale(0.9).next_to(circ, RIGHT)
        pause[2].set_color(RED)
        pause[4].set_color(GREEN)
        self.play(ShowCreation(circ), Write(pause))
        self.play(Write(timers[0]), run_time=0.5)
        for i in range(10):
            self.play(ReplacementTransform(timers[i], timers[i + 1]), run_time=0.5)
            self.wait(0.5)
        self.play(FadeOut(pause), FadeOut(timers[-1]), FadeOut(circ), run_time=2)
        #answer = TextMobject("Réponse: Au sommet de la fonction.").to_corner(DL)
        #self.play(Write(answer))

        self.wait(10)



class ParamH(GraphScene):
    """
    Quadratic function on interval [-10, 10]
    """
    CONFIG = {
        "y_max" : 10,
        "y_min" : -10,
        "x_max" : 10,
        "x_min" : -10,
        "y_axis_label": "$f(x)$",
        "y_tick_frequency" : 0.5,
        "x_tick_frequency" : 0.5,
        "axes_color" : GRAY,
        "y_labeled_nums": range(-10,12,2),
        "x_labeled_nums": list(np.arange(-10, 12, 2)),
        "x_label_decimal":0,
        "y_label_decimal":0,
        "graph_origin": np.array((0, 0, 0))
    }
    def construct(self):
        self.setup_axes(animate=True)

        color_map = {
            r"h": RED,
        }

        formula = TexMobject(r"f(x)=(x-h)^{2}", tex_to_color_map=color_map).to_corner(UR)
        self.play(ShowCreation(formula))


        case_1 = BoxedTitle(text="", width=3, height=0.7, scale=0.7).to_corner(DR)
        case_1_ctd = TextMobject(r"Si ", r"$h$", r"$<0$").scale(0.7)
        case_1_ctd[0].set_color(BLACK).next_to(case_1.get_center() - np.array([1,0,0]))
        case_1_ctd[1].set_color(RED).next_to(case_1_ctd[0].get_center() + np.array([0, 0, 0]))
        case_1_ctd[2].set_color(BLACK).next_to(case_1_ctd[1].get_center() + np.array([-0.02, 0, 0]))

        case_2 = BoxedTitle(text="", width=3, height=0.7, scale=0.7).to_corner(DL)
        case_2_ctd = TextMobject(r"Si ", r"$h$", r"$>0$").scale(0.7)
        case_2_ctd[0].set_color(BLACK).next_to(case_2.get_center() - np.array([1, 0, 0]))
        case_2_ctd[1].set_color(RED).next_to(case_2_ctd[0].get_center() + np.array([0, 0, 0]))
        case_2_ctd[2].set_color(BLACK).next_to(case_2_ctd[1].get_center() + np.array([-0.02, 0, 0]))

        self.play(FadeIn(case_1), FadeIn(case_1_ctd))

        hs = [-6,-4,-2,0,2,4,6]
        for i, h in enumerate(hs):
            if i == 4:
                self.play(ReplacementTransform(case_1, case_2), ReplacementTransform(case_1_ctd, case_2_ctd))
                formula.to_corner(UL)

            graph = self.get_graph(lambda x: (x-h)**2, color=WHITE, x_min=self.x_min, x_max=self.x_max)
            graph_lab = self.get_graph_label(graph, label="h").set_color(RED)
            graph_lab_ctd = TexMobject(r"={}".format(h)).next_to(graph_lab.get_center() + np.array([0.1,0.05,0]))
            line = Line(self.coords_to_point(h, -10), self.coords_to_point(h, 10), color=RED)

            if i==0:
                self.play(ShowCreation(graph), ShowCreation(graph_lab), ShowCreation(graph_lab_ctd), ShowCreation(line), run_time=2)
                self.wait(3)
                old_graph, old_graph_lab, old_graph_lab_ctd, old_line = graph, graph_lab, graph_lab_ctd, line
            else:
                self.play(ReplacementTransform(old_graph, graph), ReplacementTransform(old_graph_lab, graph_lab),
                          ReplacementTransform(old_graph_lab_ctd, graph_lab_ctd), ReplacementTransform(old_line, line),
                          run_time=2)
                self.wait(3)
                old_graph, old_graph_lab, old_graph_lab_ctd, old_line = graph, graph_lab, graph_lab_ctd, line

        self.wait(5)



class ParamK(GraphScene):
    """
    Quadratic function on interval [-10, 10]
    """
    CONFIG = {
        "y_max" : 10,
        "y_min" : -10,
        "x_max" : 10,
        "x_min" : -10,
        "y_axis_label": "$f(x)$",
        "y_tick_frequency" : 0.5,
        "x_tick_frequency" : 0.5,
        "axes_color" : GRAY,
        "y_labeled_nums": range(-10,12,2),
        "x_labeled_nums": list(np.arange(-10, 12, 2)),
        "x_label_decimal":0,
        "y_label_decimal":0,
        "graph_origin": np.array((0, 0, 0))
    }
    def construct(self):
        self.setup_axes(animate=True)

        color_map = {
            r"k": GREEN,
        }

        formula = TexMobject(r"f(x)=x^{2}+k", tex_to_color_map=color_map).to_corner(UL)
        self.play(ShowCreation(formula))


        case_1 = BoxedTitle(text="", width=3, height=0.7, scale=0.7).to_corner(DL)
        case_1_ctd = TextMobject(r"Si ", r"$k$", r"$<0$").scale(0.7)
        case_1_ctd[0].set_color(BLACK).next_to(case_1.get_center() - np.array([1,0,0]))
        case_1_ctd[1].set_color(GREEN).next_to(case_1_ctd[0].get_center() + np.array([0, 0, 0]))
        case_1_ctd[2].set_color(BLACK).next_to(case_1_ctd[1].get_center() + np.array([-0.02, 0, 0]))

        case_2 = BoxedTitle(text="", width=3, height=0.7, scale=0.7).to_corner(DL)
        case_2_ctd = TextMobject(r"Si ", r"$k$", r"$>0$").scale(0.7)
        case_2_ctd[0].set_color(BLACK).next_to(case_2.get_center() - np.array([1, 0, 0]))
        case_2_ctd[1].set_color(GREEN).next_to(case_2_ctd[0].get_center() + np.array([0, 0, 0]))
        case_2_ctd[2].set_color(BLACK).next_to(case_2_ctd[1].get_center() + np.array([-0.02, 0, 0]))

        self.play(FadeIn(case_1), FadeIn(case_1_ctd))

        ks = [-6,-4,-2,0,2,4,6]
        for i, k in enumerate(ks):
            if i == 4:
                self.play(ReplacementTransform(case_1, case_2), ReplacementTransform(case_1_ctd, case_2_ctd))
                formula.to_corner(UL)

            graph = self.get_graph(lambda x: (x**2)+k, color=WHITE, x_min=self.x_min, x_max=self.x_max)
            graph_lab = self.get_graph_label(graph, label="k").set_color(GREEN)
            graph_lab_ctd = TexMobject(r"={}".format(k)).next_to(graph_lab.get_center() + np.array([0.1,0.05,0]))
            line = self.get_graph(lambda x: k, color=GREEN, x_min=self.x_min, x_max=self.x_max)

            if i==0:
                self.play(ShowCreation(graph), ShowCreation(graph_lab), ShowCreation(graph_lab_ctd), ShowCreation(line), run_time=2)
                self.wait(3)
                old_graph, old_graph_lab, old_graph_lab_ctd, old_line = graph, graph_lab, graph_lab_ctd, line
            else:
                self.play(ReplacementTransform(old_graph, graph), ReplacementTransform(old_graph_lab, graph_lab),
                          ReplacementTransform(old_graph_lab_ctd, graph_lab_ctd), ReplacementTransform(old_line, line),
                          run_time=2)
                self.wait(3)
                old_graph, old_graph_lab, old_graph_lab_ctd, old_line = graph, graph_lab, graph_lab_ctd, line

        self.wait(5)
        self.play(FadeOut(graph), FadeOut(graph_lab), FadeOut(graph_lab_ctd), FadeOut(line))
        self.play(FadeOut(case_2), FadeOut(case_2_ctd), FadeOut(formula))
        self.play(self.axes.shift, UP * 10)

        # Pause to think about it.
        circ = Arc(start_angle=PI / 2, angle=-2 * PI, radius=0.35).to_corner(DL)
        timers = [TexMobject(str(i)).move_to(circ) for i in range(10, -1, -1)]
        pause = TextMobject("À quoi ", r"(", r"$h$", r", ", r"$k$", r") ",
                            r"correspond dans le forme canonique?").scale(0.9).next_to(circ, RIGHT)
        pause[2].set_color(RED)
        pause[4].set_color(GREEN)
        self.play(ShowCreation(circ), Write(pause))
        self.play(Write(timers[0]), run_time=0.5)
        for i in range(10):
            self.play(ReplacementTransform(timers[i], timers[i + 1]), run_time=0.5)
            self.wait(0.5)
        self.play(FadeOut(pause), FadeOut(timers[-1]), FadeOut(circ), run_time=2)
        answer = TextMobject2("Réponse: Au sommet de la fonction (i.e. le minimum (si $a>0$) ou le maximum (si $a<0$)).")
        answer.next_to(np.array([-9,-3,0]))
        answer.scale(0.75)
        self.wait(10)
        self.play(Write(answer))
        self.wait(5)

        # Titles (a<0 and a>0)
        #title_1 = BoxedTitle(text="$a>0$", width=1.5, height=0.7, scale=0.7)
        #title_1.move_to(np.array([-4, 3.25, 0]))

        case_1 = BoxedTitle(text="", width=1.5, height=0.7, scale=0.7).move_to(np.array([-4, 3.25, 0]))
        case_1_ctd = TextMobject(r"Si ", r"$a$", r"$>0$").scale(0.7)
        case_1_ctd[0].set_color(BLACK).next_to(case_1.get_center() - np.array([1, 0, 0]))
        case_1_ctd[1].set_color(BLUE).next_to(case_1_ctd[0].get_center() + np.array([0, -0.05, 0]))
        case_1_ctd[2].set_color(BLACK).next_to(case_1_ctd[1].get_center() + np.array([-0.02, 0.03, 0]))
        self.play(ShowCreation(case_1), ShowCreation(case_1_ctd))


        case_2 = BoxedTitle(text="", width=1.5, height=0.7, scale=0.7).move_to(np.array([4, 3.25, 0]))
        case_2_ctd = TextMobject(r"Si ", r"$a$", r"$<0$").scale(0.7)
        case_2_ctd[0].set_color(BLACK).next_to(case_2.get_center() - np.array([1, 0, 0]))
        case_2_ctd[1].set_color(BLUE).next_to(case_2_ctd[0].get_center() + np.array([0, -0.05, 0]))
        case_2_ctd[2].set_color(BLACK).next_to(case_2_ctd[1].get_center() + np.array([-0.02, 0.03, 0]))
        self.play(ShowCreation(case_2), ShowCreation(case_2_ctd))


        # Put images of curvature
        path = r"C:/Users/Utilisateur/Desktop/CEGEP/Cours_maison/toastersman_videos/Revision_precalcul/Fonction_quadratique/partie_1/images/"
        image_1_name, image_2_name = "a_positif","a_negatif"
        image_1, image_2 = ImageMobject("{}{}.PNG".format(path, image_1_name)).scale(1.5) ,\
                           ImageMobject("{}{}.PNG".format(path, image_2_name)).scale(1.5)
        image_1.next_to(case_1, DOWN, buff=MED_LARGE_BUFF)
        image_2.next_to(case_2, DOWN, buff=MED_LARGE_BUFF)
        self.play(FadeIn(image_1), FadeIn(image_2))
        self.wait(20)




class Symetrie(GraphScene):
    """
    Quadratic function on interval [-10, 10]
    """
    CONFIG = {
        "y_max" : 10,
        "y_min" : -10,
        "x_max" : 10,
        "x_min" : -10,
        "y_axis_label": "$f(x)$",
        "y_tick_frequency" : 0.5,
        "x_tick_frequency" : 0.5,
        "axes_color" : GRAY,
        "y_labeled_nums": range(-10,10,2),
        "x_labeled_nums": list(np.arange(-10, 10, 2)),
        "x_label_decimal":0,
        "y_label_decimal":0,
        "graph_origin": np.array((0, 0, 0))
    }
    def construct(self):
        self.setup_axes(animate=True)

        formula = TexMobject(r"f(x)=x^{2}").to_corner(UL)
        optimum = TexMobject(r"(h,k)=(0,0)").to_corner(UL).next_to(formula, DOWN).align_to(formula, LEFT)
        self.play(ShowCreation(formula), ShowCreation(optimum))

        a = 0.25
        graph = self.get_graph(lambda x: a*x**2, color=WHITE, x_min=self.x_min, x_max=self.x_max)
        self.play(ShowCreation(graph))

        epsilons = [3, 4, 5, 6]
        for i, epsilon in enumerate(epsilons):

            vertical_line_left = Line(self.coords_to_point(-epsilon, 0), self.coords_to_point(-epsilon, a*epsilon**2))
            left_margin = Brace(Line(self.coords_to_point(-epsilon, a*epsilon**2), self.coords_to_point(0, a*epsilon**2)), UP)
            left_margin_txt = left_margin.get_text("${}$".format(epsilon)).scale(0.75)

            vertical_line_right = Line(self.coords_to_point(epsilon, 0), self.coords_to_point(epsilon, a*epsilon**2))
            right_margin = Brace(Line(self.coords_to_point(0, a*epsilon**2), self.coords_to_point(epsilon, a*epsilon**2)), UP)
            right_margin_txt = right_margin.get_text("${}$".format(epsilon)).scale(0.75)

            image_value = Line(self.coords_to_point(-epsilon, a*epsilon**2), self.coords_to_point(epsilon, a*epsilon**2),
                               color=BLUE)

            if i==0:
                self.play(ShowCreation(vertical_line_left), ShowCreation(vertical_line_right),
                          ShowCreation(left_margin), ShowCreation(right_margin),
                          ShowCreation(left_margin_txt), ShowCreation(right_margin_txt),
                          ShowCreation(image_value),  run_time=1.5)
                self.wait(3)
            else:
                self.play(ReplacementTransform(old_vertical_line_left, vertical_line_left),
                          ReplacementTransform(old_vertical_line_right, vertical_line_right),
                          ReplacementTransform(old_left_margin, left_margin),
                          ReplacementTransform(old_right_margin, right_margin),
                          ReplacementTransform(old_left_margin_txt, left_margin_txt),
                          ReplacementTransform(old_right_margin_txt, right_margin_txt),
                          ReplacementTransform(old_image_value, image_value), run_time=2)
                self.wait(3)
            old_vertical_line_left, old_vertical_line_right, old_image_value = vertical_line_left, vertical_line_right, image_value
            old_left_margin, old_right_margin = left_margin, right_margin
            old_left_margin_txt, old_right_margin_txt = left_margin_txt, right_margin_txt

        self.wait(5)


class Transformation(Scene):
    def construct(self):
        #title = TextMobject(r"\underline{\sc Preuve de IR3:}", color=YELLOW).to_corner(UL).scale(1)
        title = BoxedTitle(text="Canonique à général", width=5, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))
        self.play(ShowCreation(title))

        color_map = {
            r"a": BLUE,
            r"h": RED,
            r"k": GREEN
        }

        color_map_2 = {
            r"a": BLUE,
            r"b": ORANGE,
            r"c": PINK,
        }

        eq_1 = TexMobject(r"a(x-h)^{2}+k", r" =", r" a(x^{2}-2xh+h^{2})+k", tex_to_color_map=color_map).scale(1.1)
        justification_1 = TextMobject(r"(Distributivité)").scale(0.8)
        eq_1.next_to([-6, 1.5, 0], RIGHT)
        justification_1.next_to([2.75, 1.35, 0])

        eq_2 = TexMobject(r"=", r"ax^{2} - 2ahx + ah^{2} + k", tex_to_color_map=color_map).scale(1.1)
        eq_2.next_to([-2.6,0,0])
        justification_2 = TextMobject(r"(Commutativité)").scale(0.8)
        justification_2.next_to(eq_2, RIGHT, buff=LARGE_BUFF).align_to(justification_1, RIGHT)

        eq_3 = TexMobject(r"=", r"a", r"x^{2}", r"+", r"(-2ah)", r"x", r"+", r"(ah^{2}+k)").scale(1.1)
        eq_3.next_to(eq_2, DOWN, buff=LARGE_BUFF).align_to(eq_2[0], LEFT)
        eq_3[1].set_color(BLUE)
        eq_3[4].set_color(ORANGE)
        eq_3[7].set_color(PINK)

        eq_4 = TexMobject(r"=", r"ax^{2}+bx+c", tex_to_color_map=color_map_2)
        eq_4.next_to(eq_3, DOWN, buff=LARGE_BUFF).align_to(eq_3[0], LEFT)
        formulas = TextMobject(r"\Big($h=-\frac{b}{2a},\quad$", r"$k=c-\frac{b^{2}}{4a}$\Big)")
        formulas.next_to(eq_4, RIGHT, buff=LARGE_BUFF)

        #square = Square(side_length=0.25, fill_color=GOLD, fill_opacity=1, color=ORANGE)
        #square.next_to(eq_4, RIGHT, buff=4*LARGE_BUFF)


        self.wait(5)
        self.play(Write(eq_1))
        self.wait(5)
        #self.play(Write(justification_1))
        self.play(Write(eq_2))
        self.wait(5)
        self.add(eq_2)
        self.wait(5)
        #self.play(Write(justification_2))
        self.play(Write(eq_3))
        self.wait(5)
        self.play(Write(eq_4))
        self.wait(5)
        self.play(Write(formulas))
        self.wait(15)


class Exo(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    # TO-DO :
    # Time limit. Find the answers.
    # Put the solution on both sides.
    def construct(self):
        title = BoxedTitle(text="Exercices supplémentaires", width=6, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))
        exos = TextMobject(r"Changer la forme des fonctions quadratiques suivantes:",
        r"""
        \begin{enumerate}
        \item $f(x)=3(x+2)^{2}+2$,
        \item $g(x)=3x^{2}+12x+12$.
        \end{enumerate}
        """)
        #definition.scale(0.7)
        exos[0].move_to(np.array([-1, 2, 0]))
        exos.scale(0.8)


        self.play(Write(title))
        self.wait(10)
        self.play(FadeIn(exos))
        self.wait(5)

        # Pause to think about it.
        circ = Arc(start_angle=PI / 2, angle=-2 * PI, radius=0.35).to_corner(DL)
        timers = [TexMobject(str(i)).move_to(circ) for i in range(10, -1, -1)]
        pause = TextMobject("Faites pause et trouvez les solutions.").next_to(circ, RIGHT)
        self.play(ShowCreation(circ), Write(pause))
        self.play(Write(timers[0]), run_time=0.5)
        for i in range(10):
            self.play(ReplacementTransform(timers[i], timers[i + 1]), run_time=0.5)
            self.wait(0.5)
        self.play(FadeOut(pause), FadeOut(timers[-1]), FadeOut(circ), run_time=2)

        answer = TextMobject("Solutions (respectivement): $f(x)=3x^{2}+12x+14$, $g(x)=3(x+2)^{2}$").next_to(np.array([-7.5,-3,0]))
        answer.scale(0.85)
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
        title = BoxedTitle(text="Conclusion", width=3, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        compl_rules_str = [
            "",
            "Formuler les formes générale et canonique de la fonction quadratique.",
            "Comprendre l'interprétation des paramètres $a,b$ et $c$ de la forme générale.",
            "Comprendre l'interprétation des paramètres $h$ et $k$ de la forme canonique.",
            "Pouvoir passer de la forme canonique à la forme générale et vice versa."
        ]


        rules = [TextMobject2("{}) {}".format(i, rule), color=WHITE) for i, rule in enumerate(compl_rules_str)]
        rules = [rule.scale(0.7) for rule in rules]

        for (i, rule) in enumerate(rules):
            if i != 0:
                rule.next_to(rules[0].get_center() - rule.get_center() + np.array([-6, -1-0.7 * i, 0]))
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
        self.wait(25)



class Courbes(GraphScene):
    """
    Quadratic function on interval [-10, 10]
    """
    CONFIG = {
        "y_max" : 10,
        "y_min" : -10,
        "x_max" : 10,
        "x_min" : -10,
        #"y_axis_label": "$f(x)$",
        "y_tick_frequency" : 10,
        "x_tick_frequency" : 10,
        "axes_color" : BLACK,
        "y_labeled_nums": range(-100,100,20),
        "x_labeled_nums": list(np.arange(-100, 100, 20)),
        "x_label_decimal":0,
        "y_label_decimal":0,
        "graph_origin": np.array((0, 0, 0))
    }
    def construct(self):
        self.setup_axes(animate=True)

        #title = BoxedTitle(text="Motivation", width=3, height=0.7, scale=0.7)
        #title.move_to(np.array([0, 3.25, 0]))
        #self.play(ShowCreation(title))

        color_map = {
            r"h": RED,
            r"k": GREEN,
        }


        graph = self.get_graph(lambda x : -1*(x**2),
                                    color = BLUE,
                                    x_min = self.x_min,
                                    x_max = self.x_max
                                    )

        self.play(ShowCreation(graph), run_time = 2)

        # Draw points for slope calculation
        raw_x1 = (0, 0)
        x1_ = self.coords_to_point(raw_x1[0], raw_x1[1])
        x1 = Dot().next_to(x1_, 0)
        point_x1_label = TexMobject(r"(h,k)", tex_to_color_map = color_map)
        point_x1_label.next_to(x1, UP)
        self.add(x1)
        self.add(point_x1_label)

        self.wait(10)