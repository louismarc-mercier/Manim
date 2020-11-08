from manimlib.imports import *
from manim_utils.slide_template import Warning, BoxedTitle, GenChannelLogo, YoutubeLogo

# 1. ThumbnailFrench
# 2. MiseContexte
# 3. PathAsCorners
# 4. ExempleFunction
# 5. Definition
# 6. SlopeInterp
# 7. SlopeVariation
# 8. TranslationVariation
# 9. FindTranslation
# 10. Application
# 11. Conclusion




class ThumbnailFrench(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        # Get images
        path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/images/Euclide/"
        euclide_img = ImageMobject(path + "perfect_euclide").scale(2)
        what_guy = ImageMobject(path + "What_meme_miroir").scale(2)

        # Quotes
        line_euclide = TextMobject(r"\sc{Conduire une droite d'un point}", r"\sc{quelconque à un point quelconque.}").scale(0.7).set_color([PINK])
        line_euclide[0].next_to(3 * UP + 0 * RIGHT)
        line_euclide[1].next_to(line_euclide[0], DOWN)
        # line_e[1].next_to(2 * UP + 7 * LEFT)

        line_guy = TextMobject(r"\sc{Quoi??}").scale(2).set_color([YELLOW])


        # Bubbles
        # Euclide
        right_rectangle = Rectangle(width=7, height=1.5, fill_opacity=0.05, color=PURPLE)
        right_rectangle.next_to(line_euclide, 0)

        TRANSLATION = np.array([2.75, 0, 0])
        right_triangle = Polygon(right_rectangle.get_corner(DR)-TRANSLATION,
                           right_rectangle.get_corner(DR)-TRANSLATION - np.array([0.5, 0, 0]),
                           right_rectangle.get_corner(DR)-TRANSLATION - np.array([0, 2, 0]),
                           color=PURPLE).set_fill(BLACK)

        right_black_line = Line(right_rectangle.get_corner(DR)-TRANSLATION - np.array([0.02, 0, 0]),
                          right_rectangle.get_corner(DR)-TRANSLATION - np.array([0.48, 0, 0]))
        right_black_line.set_color(BLACK)
        right_black_line.set_stroke(width=4.5)


        # Meme guy
        left_rectangle = Rectangle(width=4, height=1.5, fill_opacity=0.05, color=GOLD)
        left_rectangle.next_to(line_guy, 0)

        TRANSLATION = np.array([0, 0, 0])
        left_triangle = Polygon(left_rectangle.get_corner(UL) - TRANSLATION,
                           left_rectangle.get_corner(UL) - TRANSLATION - np.array([0.5, 0, 0]),
                           left_rectangle.get_corner(UL) - TRANSLATION - np.array([0, 1, 0]),
                           color=GOLD).set_fill(BLACK)

        left_black_line = Line(left_rectangle.get_corner(UL) - TRANSLATION - np.array([0, 0.02, 0]),
                          left_rectangle.get_corner(UL) - TRANSLATION - np.array([0, 2*0.465, 0]))
        left_black_line.set_color(BLACK)
        left_black_line.set_stroke(width=4.5)

        # Place images
        euclide_img.next_to(np.array([3,-1,0]))
        euclide_name_tag = TextMobject(r"\sc{Euclide (300 av. J.-C)}").scale(0.75).next_to(euclide_img, DOWN).set_color(PINK)

        what_guy.next_to(euclide_img, LEFT, buff=5*LARGE_BUFF)
        what_guy_name_tag =TextMobject(r"\sc{Vous}").scale(0.7).next_to(what_guy, DOWN).set_color(YELLOW)


        self.play(FadeIn(euclide_img))
        self.play(Write(euclide_name_tag))
        self.wait(3)
        self.play(Write(line_euclide))
        self.play(ShowCreation(right_rectangle), ShowCreation(right_triangle))
        self.play(ShowCreation(right_black_line))
        self.wait(5)
        self.play(FadeIn(what_guy))
        self.play(Write(what_guy_name_tag))
        self.wait(2)
        self.play(Write(line_guy))
        self.play(ShowCreation(left_rectangle), ShowCreation(left_triangle))
        self.play(ShowCreation(left_black_line))
        self.wait(5)


class MiseContexte(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Contexte", width=3, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        statement = TextMobject2(r"Soient $\mathbf{x}_{1},\mathbf{x}_{2}\in\mathbb{R}^{2}$. Par exemple, prenons:").scale(0.8)
        #statement[0].set_color(BLUE)
        statement.next_to(title, DOWN, buff=LARGE_BUFF)

        formulas = TextMobject(r"$\mathbf{x}_{1}=(x_{1},y_{1})=(-2,-2)$", r"$\mathbf{x}_{2}=(x_{2},y_{2})=(2,2)$")
        formulas[1].next_to(formulas[0], DOWN).align_to(formulas[0], LEFT)
        formulas.next_to(statement, DOWN, buff=LARGE_BUFF)

        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement))
        self.wait(5)
        self.play(Write(formulas))
        self.wait(20)


class ExempleFunction(GraphScene):
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
        "axes_color" : BLUE,
        "y_labeled_nums": range(-10,10,2),
        "x_labeled_nums": list(np.arange(-10, 10, 2)),
        "x_label_decimal":0,
        "y_label_decimal":0,
        "graph_origin": np.array((0, 0, 0))
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : x,
                                    color = GREEN,
                                    x_min = self.x_min,
                                    x_max = self.x_max
                                    )
        #graph.y_axis_label = TextMobject(r"$f(x)$")

        graph_lab = self.get_graph_label(graph, label="x")
        self.play(ShowCreation(graph), ShowCreation(graph_lab), run_time = 2)
        self.wait(10)



class Definition(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Définition", width=3, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        # Source: https://github.com/vivek3141/videos/blob/master/maxwell.py
        color_map = {
            r"m": YELLOW,
            r"b": PINK,
        }

        statement = TextMobject2(r"Soit $f:\mathbb{R}\rightarrow\mathbb{R}$, la fonction affine définie par").scale(0.8)
        statement.next_to(title, DOWN, buff=LARGE_BUFF)

        formula = TexMobject(r"f(x)=mx+b", tex_to_color_map=color_map)


        description_m = TexMobject(r"m\in", tex_to_color_map=color_map).next_to(formula, DOWN, buff=LARGE_BUFF)
        verbal_description_m = TextMobject(r"Pente", r":").next_to(description_m, LEFT, buff=LARGE_BUFF).align_to(statement, LEFT)
        verbal_description_m[0].set_color(YELLOW)
        description_m_cont = TextMobject(r"$\mathbb{R}$").next_to(description_m, RIGHT)


        description_b = TexMobject(r"b\in", tex_to_color_map=color_map).next_to(description_m, DOWN).align_to(description_m, RIGHT)
        verbal_description_b = TextMobject(r"Ordonnée à",  r":", r" l'origine")
        verbal_description_b[0].next_to(verbal_description_m, DOWN, buff=2*SMALL_BUFF).align_to(verbal_description_m, LEFT).set_color(PINK)
        verbal_description_b[1].next_to(verbal_description_b[0], RIGHT)
        verbal_description_m[1].next_to(verbal_description_b[1], UP)
        verbal_description_b[2].next_to(verbal_description_b[0], DOWN, buff=1*SMALL_BUFF).align_to(verbal_description_b[0], LEFT).set_color(PINK)


        description_b_cont = TextMobject(r"$\mathbb{R}$").next_to(description_b, RIGHT).align_to(description_m_cont, RIGHT)

        warning_desc = TexMobject(r"m,b", tex_to_color_map=color_map).next_to(description_m, RIGHT, buff=3*LARGE_BUFF)
        warning_desc_cont = TextMobject(r"$\bot x$").next_to(warning_desc, RIGHT, buff=0.1*SMALL_BUFF)
        warning_symbol = Warning().scale(0.3).next_to(warning_desc_cont, RIGHT)

        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement))
        self.wait(5)
        self.play(Write(formula))
        self.wait(5)
        self.play(Write(verbal_description_m))
        self.play(Write(description_m), Write(description_m_cont))
        self.wait(5)
        self.play(Write(verbal_description_b))
        self.play(Write(description_b), Write(description_b_cont))
        self.wait(5)
        self.play(WiggleOutThenIn(warning_symbol))
        self.wait(3)
        self.play(Write(warning_desc), Write(warning_desc_cont))
        self.wait(10)


class SlopeInterpretation(GraphScene):
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
        "axes_color" : BLUE,
        "y_labeled_nums": range(-10,10,2),
        "x_labeled_nums": list(np.arange(-10, 10, 2)),
        "x_label_decimal":0,
        "y_label_decimal":0,
        "graph_origin": np.array((0, 0, 0))
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : x,
                                    color = WHITE,
                                    x_min = self.x_min,
                                    x_max = self.x_max
                                    )
        # Plot function

        self.play(ShowCreation(graph), run_time = 2)

        graph_lab = TexMobject(r"f(x)", "=", "1", "x","=x").to_corner(UL)
        graph_lab[2].set_color(YELLOW)

        point_x1 = TexMobject(r"\mathbf{x}_{1}=(", "x_{1}", ",", "f(x_{1})", ")=(4,4)")
        point_x1_label = TexMobject(r"\mathbf{x}_{1}")
        point_x1.scale(0.85).next_to(graph_lab, DOWN).align_to(graph_lab, LEFT)
        point_x1[1].set_color(GREEN)
        point_x1[3].set_color(RED)

        point_x2 = TexMobject(r"\mathbf{x}_{2}=(", "x_{2}", ",", "f(x_{2})", ")=(8,8)")
        point_x2_label = TexMobject(r"\mathbf{x}_{2}")
        point_x2.scale(0.85).next_to(point_x1, DOWN).align_to(point_x1, LEFT)
        point_x2[1].set_color(GREEN)
        point_x2[3].set_color(RED)

        self.play(Write(graph_lab))
        self.play(Write(point_x1), Write(point_x2))
        self.wait(10)


        # Draw points for slope calculation
        raw_x1, raw_x2, raw_x3 = (8, 8), (8, 4), (4, 4)
        x1_, x2_, x3_ = self.coords_to_point(raw_x1[0], raw_x1[1]), self.coords_to_point(raw_x2[0], raw_x2[1]), \
                        self.coords_to_point(raw_x3[0], raw_x3[1])
        x1, x2, x3 = Dot().next_to(x1_, 0), Dot().next_to(x2_, 0), Dot().next_to(x3_, 0)
        point_x1_label.next_to(x3, UP)
        point_x2_label.next_to(x1, UP)
        self.add(x1)
        self.add(point_x1_label)
        self.add(x3)
        self.add(point_x2_label)
        self.wait(10)
        self.play(FadeOut(graph_lab), FadeOut(graph))
        self.wait(10)

        # Draw point for slope calculation
        self.add(x2)

        # Draw triangle of slope
        vertical_line = Line(x1, x2, color=RED)
        delta_y = TextMobject(r"$\Delta y$").set_color(RED).next_to(vertical_line, RIGHT)

        horizontal_line = Line(x3, x2, color=GREEN)
        delta_x = TextMobject(r"$\Delta x$").set_color(GREEN).next_to(horizontal_line, DOWN)

        slope_equation = TexMobject("m","=", "{\Delta{y}", "\over", "\Delta{x}}", "=",
                                    "{f(x_{2})-f(x_{1})", "\over", "x_{2}-x_{1}}",).next_to(np.array([0.5,-1.5,0]))
        slope_equation[0].set_color(YELLOW)
        slope_equation[2].set_color(RED)
        slope_equation[4].set_color(GREEN)
        slope_equation[6].set_color(RED)
        slope_equation[8].set_color(GREEN)

        slope_value = TexMobject("=", "{8-4", "\over", "8-4}", "=1").next_to(slope_equation, DOWN).align_to(slope_equation[1], LEFT)
        slope_value[1].set_color(RED)
        slope_value[3].set_color(GREEN)

        self.play(ShowCreation(vertical_line), ShowCreation(delta_y))
        self.wait(5)
        self.play(ShowCreation(horizontal_line), ShowCreation(delta_x))
        self.wait(10)
        self.play(ShowCreation(slope_equation))
        self.wait(10)
        self.play(ShowCreation(slope_value))
        self.wait(10)



class SlopeVariation(GraphScene):
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
        "axes_color" : BLUE,
        "y_labeled_nums": range(-10,10,2),
        "x_labeled_nums": list(np.arange(-10, 10, 2)),
        "x_label_decimal":0,
        "y_label_decimal":0,
        "graph_origin": np.array((0, 0, 0))
    }
    def construct(self):
        self.setup_axes(animate=True)

        color_map = {
            r"m": YELLOW,
            r"b": PINK,
        }

        formula = TexMobject(r"f(x)=mx", tex_to_color_map=color_map).to_corner(UL)
        self.play(ShowCreation(formula))


        case_1 = BoxedTitle(text="", width=3, height=0.7, scale=0.7).to_corner(DR)
        case_1_ctd = TextMobject(r"Si ", r"$m$", r"$>0$").scale(0.7)
        case_1_ctd[0].set_color(BLACK).next_to(case_1.get_center() - np.array([1,0,0]))
        case_1_ctd[1].set_color(YELLOW).next_to(case_1_ctd[0].get_center() + np.array([0, -0.05, 0]))
        case_1_ctd[2].set_color(BLACK).next_to(case_1_ctd[1].get_center() + np.array([-0.02, 0.03, 0]))

        case_2 = BoxedTitle(text="", width=3, height=0.7, scale=0.7).to_corner(DL)
        case_2_ctd = TextMobject(r"Si ", r"$m$", r"$<0$").scale(0.7)
        case_2_ctd[0].set_color(BLACK).next_to(case_2.get_center() - np.array([1, 0, 0]))
        case_2_ctd[1].set_color(YELLOW).next_to(case_2_ctd[0].get_center() + np.array([0, -0.05, 0]))
        case_2_ctd[2].set_color(BLACK).next_to(case_2_ctd[1].get_center() + np.array([-0.02, 0.02, 0]))

        self.play(FadeIn(case_1), FadeIn(case_1_ctd))

        slopes = [0.25,1,3,9,-9,-3,-1,-0.25]
        for i, slope in enumerate(slopes):
            if i == 4:
                self.play(ReplacementTransform(case_1, case_2), ReplacementTransform(case_1_ctd, case_2_ctd))

            graph = self.get_graph(lambda x: slope*x, color=WHITE, x_min=self.x_min, x_max=self.x_max)
            graph_lab = self.get_graph_label(graph, label="m").set_color(YELLOW)
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



class TranslationVariation(GraphScene):
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
        "axes_color" : BLUE,
        "y_labeled_nums": range(-10,10,2),
        "x_labeled_nums": list(np.arange(-10, 10, 2)),
        "x_label_decimal":0,
        "y_label_decimal":0,
        "graph_origin": np.array((0, 0, 0))
    }
    def construct(self):
        self.setup_axes(animate=True)

        color_map = {
            r"m": YELLOW,
            r"b": PINK,
        }

        formula = TexMobject(r"f(x)=x+b", tex_to_color_map=color_map).to_corner(UL)
        self.play(ShowCreation(formula))

        ordonnees_origine = [-9, -6, -3, 0, 3, 6, 9]
        y_0 = self.coords_to_point(0, 0)
        ys_coords = [self.coords_to_point(0, ordonnee) for ordonnee in ordonnees_origine]
        for i, (ordonnee_origine, y_coord) in enumerate(zip(ordonnees_origine, ys_coords)):

            graph = self.get_graph(lambda x: x + ordonnee_origine, color=WHITE, x_min=self.x_min, x_max=self.x_max)
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



class FindTranslation(GraphScene):
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
        "axes_color" : BLUE,
        "y_labeled_nums": range(-10,10,2),
        "x_labeled_nums": list(np.arange(-10, 10, 2)),
        "x_label_decimal":0,
        "y_label_decimal":0,
        "graph_origin": np.array((0, 0, 0))
    }
    def construct(self):
        self.setup_axes(animate=True)

        formula = TexMobject(r"f(x)", "=", "x", "+", "b").to_corner(UL)
        point_x1 = TexMobject(r"\mathbf{x}_{1}=(", "x_{1}", ",", "f(x_{1})", ")=(2,4)").next_to(formula, DOWN).align_to(
            formula, LEFT)
        point_x1[1].set_color(GREEN)
        point_x1[3].set_color(RED)
        self.play(Write(formula), Write(point_x1))
        self.wait(5)


        point_x1_label = TexMobject(r"\mathbf{x}_{1}").scale(0.85)
        raw_x1 = (2, 4)
        x1_ = self.coords_to_point(raw_x1[0], raw_x1[1])
        x1 = Dot().next_to(x1_, 0)
        point_x1_label.next_to(x1, RIGHT)
        self.add(x1)
        self.play(ShowCreation(point_x1_label))

        # Pause to think about it.
        circ = Arc(start_angle=PI / 2, angle=-2 * PI, radius=0.35).to_corner(DL)
        timers = [TexMobject(str(i)).move_to(circ) for i in range(5, -1, -1)]
        pause = TextMobject("Trouvez la valeur de $b$.").scale(0.9).next_to(circ, RIGHT)
        self.play(ShowCreation(circ), Write(pause))
        self.play(Write(timers[0]), run_time=0.5)
        for i in range(5):
            self.play(ReplacementTransform(timers[i], timers[i + 1]), run_time=0.5)
            self.wait(0.5)
        self.play(FadeOut(pause), FadeOut(timers[-1]), FadeOut(circ), run_time=2)

        answer = TextMobject("Réponse: $b=2$").to_corner(DL)
        self.play(Write(answer))
        self.wait(5)
        self.play(FadeOut(answer))
        self.wait(10)


        ordonnees_origine = [-6, -4, -2, 0, 2]
        ordonnees_strings = ["-6", "-4", "-2","+0","+2"]
        ys_coords = [self.coords_to_point(0, ordonnee) for ordonnee in ordonnees_origine]
        for i, (ordonnee_origine, y_coord) in enumerate(zip(ordonnees_origine, ys_coords)):
            graph = self.get_graph(lambda x: x + ordonnee_origine, color=WHITE, x_min=self.x_min, x_max=self.x_max)
            graph_lab = self.get_graph_label(graph, label="x{}".format(ordonnees_strings[i]))
            if i==0:
                self.play(ShowCreation(graph), ShowCreation(graph_lab), run_time=1)
                self.wait(3)
            else:
                self.play(ReplacementTransform(old_graph, graph), run_time=1)
                self.play(ReplacementTransform(old_graph_lab, graph_lab), run_time=1)
                self.wait(3)
            old_graph, old_graph_lab = graph, graph_lab
        self.wait(10)

        intersection_equation = TexMobject("f(x_{1})", "=", "f(x_{1})").next_to(np.array([0.5, -1, 0]))
        intersection_equation[2].set_color(RED)
        self.play(Write(intersection_equation))
        self.wait(5)

        intersection_cont_equation = TexMobject("2+b", "=", "4").next_to(intersection_equation, DOWN).align_to(intersection_equation, LEFT)
        intersection_cont_equation[2].set_color(RED)
        self.play(Write(intersection_cont_equation))
        self.wait(5)

        intersection_cont2_equation = TexMobject(r"\Rightarrow", "b=4-2=2").next_to(intersection_cont_equation, DOWN).align_to(intersection_cont_equation, LEFT)
        self.play(Write(intersection_cont2_equation))
        self.wait(5)



class Application(Scene):
    def construct(self):
        title = BoxedTitle(text="Application concrète", width=5, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        description = TextMobject2(r"Le prix de l'abonnement mensuel est $A$ et le prix d'une communication à la minute "
                                   r"est de $0.10$\$/min. Exprimez une fonction pour calculer le prix à payer en fonction du nombre de minutes.").scale(0.7)
        description.next_to(title, DOWN, buff=MED_LARGE_BUFF)

        # Get images
        path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/images/Euclide/"
        phone_img = ImageMobject(path + "telephone").scale(1.5)
        phone_img.next_to(description, DOWN, buff=LARGE_BUFF).align_to(description, LEFT)

        # Answer
        answer_p1 = TexMobject(r"f:\mathbb{R}_{+}\rightarrow\mathbb{R}_{+}").next_to(phone_img, RIGHT, buff=2*LARGE_BUFF)
        answer_p2 = TexMobject(r"f(x)", "=", "0.1", "x", "+", "A", ).next_to(answer_p1, DOWN).align_to(answer_p1, LEFT)
        answer_p2[2].set_color(YELLOW)
        answer_p2[5].set_color(PINK)

        self.play(Write(title))
        self.wait(5)
        self.play(ShowCreation(phone_img))
        self.wait(5)
        self.play(Write(description))
        self.wait(15)
        self.play(Write(answer_p1))
        self.wait(5)
        self.play(Write(answer_p2))
        self.wait(10)



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
            "Formuler l'équation de la fonction affine.",
            "Interpréter les concepts de la pente et de l'ordonnée à l'origine ($m$ et $b$).",
            "Trouver la pente à l'aide de deux points donnés.",
            "Trouver l'ordonnée à l'origine à l'aide de la pente et d'un point donné.",
            "Formuler une problématique mathématique concrète  à l'aide d'une fonction affine.",
        ]

        def choose_color(i):
            color = WHITE if i<5 else YELLOW
            return color

        rules = [TextMobject2("{}) {}".format(i, rule), color=choose_color(i)) for i, rule in enumerate(compl_rules_str)]
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
        self.wait(5)
        self.play(Write(rules[5]))
        self.wait(15)






class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))


class ScreenGrid(VGroup):
    CONFIG = {
        "rows": 8,
        "columns": 14,
        "height": FRAME_Y_RADIUS * 2,
        "width": 14,
        "grid_stroke": 0.5,
        "grid_color": WHITE,
        "axis_color": RED,
        "axis_stroke": 2,
        "labels_scale": 0.5,
        "labels_buff": 0,
        "number_decimals": 2
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        vector_ii = ORIGIN + np.array((- self.width / 2, - self.height / 2, 0))
        vector_si = ORIGIN + np.array((- self.width / 2, self.height / 2, 0))
        vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))

        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)

        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

        divisions_x = self.width / columns
        divisions_y = self.height / rows

        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip([columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff)
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = TextMobject(f"{coord_point}").scale(self.labels_scale)
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes, labels)


def coord(x,y,z=0):
    return np.array([x,y,z])

def getX(mob):
    return mob.get_center()[0]

def getY(mob):
    return mob.get_center()[1]



class PathScene(Scene):
    CONFIG = {
        #"x_coords":[0,  1, 3,  -2, -3],
        #"y_coords":[3, -2, 1, 2.5, -1]
        "x_coords": [-2, 2],
        "y_coords": [-2, 2]
    }
    """
    The setup method it is executed before the construct method, 
    so whatever they write in the setup method will be executed 
    before the construct method
    """
    def setup(self):
        self.screen_grid = ScreenGrid()
        # tuples = [(0,3),(1,-2)...]
        self.tuples = list(zip(self.x_coords,self.y_coords))

        dots,labels,numbers = self.get_all_mobs()
        self.add(self.screen_grid,dots,labels,numbers)

    def get_dots(self,coords):
        # This is called list comprehension, learn to use it here:
        # https://www.youtube.com/watch?v=AhSvKGTh28Q
        dots = VGroup(*[Dot(coord(x,y)) for x,y in coords])
        return dots

    def get_dot_labels(self,dots,direction=RIGHT):
        labels = VGroup(*[
            # This is called f-strings, learn to use it here:
            # https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
            TexMobject(f"({getX(dot)},{getY(dot)})",height=0.3)\
                      .next_to(dot,direction,buff=SMALL_BUFF)
                      # This is called Multi-line statement, learn how to use it here:
                      # https://www.programiz.com/python-programming/statement-indentation-comments
            for dot in dots
            ])
        return labels

    def get_dot_numbers(self,dots):
        numbers = VGroup(*[
            TextMobject(f"$x_{n}$",height=0.2).next_to(dot,DOWN,buff=SMALL_BUFF)
            for n,dot in zip(range(1,len(dots)+1),dots)
            ])
        return numbers

    def get_all_mobs(self):
        dots = self.get_dots(self.tuples)
        labels = self.get_dot_labels(dots)
        numbers = self.get_dot_numbers(dots)
        return dots,labels,numbers



class PathAsCorners(PathScene):
    def construct(self):
        path = VMobject()
        path.set_points_as_corners([*[coord(x,y) for x,y in self.tuples]])
        self.add(path)
        self.wait(10)


class TransformPathStyle(PathScene):
    def construct(self):
        path = VMobject()
        path.set_points_as_corners([*[coord(x,y) for x,y in self.tuples]])
        self.add(path)
        self.play(path.make_smooth)
        self.wait()
        """
        There are 3 methods:
            path.make_smooth()
            path.make_jagged()
            path.change_anchor_mode()
        """
