from manimlib.imports import *
from manim_utils.slide_template import Warning, BoxedTitle, GenChannelLogo, YoutubeLogo
import math


# 1. IntroCEGEP
# 2. MES
# 3. mandat
# 4. vitesse_moyenne
# 5. graphique
# 6. def_limite
# 7. exemple
# 8. Conclusion



class conclusion(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Conclusion", width=3, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        compl_rules_str = [
            "",
            "Connaître la définition de la dérivée en un point.",
            "Calculer la dérivée en un point.",
            "Interpréter la dérivée en un point."
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
        self.wait(3)
        self.play(Write(rules[2]))
        self.wait(3)
        self.play(Write(rules[3]))
        self.wait(10)


class exemple(Scene):
    def construct(self):
        title = BoxedTitle(text="Exercice", width=2, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        path = r"C:/Users/Utilisateur/Desktop/CEGEP/Ahunstic-Hiver2021/video/images/"
        image_name = "x_carre_parfait"
        fonction_image = ImageMobject("{}{}.PNG".format(path, image_name)).scale(2.25).move_to(np.array([-3,0,0]))

        exo = TextMobject(r"Soit $f:\mathbb{R}\rightarrow\mathbb{R}$, la fonction $f(x)=x^{2}$.").scale(0.7)
        exo.next_to(title.get_center() + np.array([0.5,-2,0]))

        exo_a = TextMobject2(r"a) Trouver $f'(0)$ à l'aide du graphique.").scale(0.7)
        exo_a.next_to(exo, DOWN).align_to(exo, LEFT)

        exo_b = TextMobject(r"b) Calculer $f'(0)$ avec la définition.").scale(0.7)
        exo_b.next_to(exo_a, DOWN).align_to(exo_a, LEFT)

        indice = TexMobject(
            "f'(0)=",
            r"\lim_{h\to 0}",
            r"\frac{f(0+h)-f(0)}{h}",
            r"=",
            r"\lim_{h\to 0}",
            r"\frac{h^{2}-0^{2}}{h}",
            r"=",
            r"\lim_{h\to 0}",
            r"h",
            r"=",
            r"0",
        ).move_to(np.array([-1.75,-2.75,0])).scale(0.7)

        self.play(Write(title))
        self.play(FadeIn(fonction_image))
        self.wait(5)
        self.play(FadeIn(exo))
        self.wait(3)
        self.play(FadeIn(exo_a))
        self.wait(3)
        self.play(FadeIn(exo_b))
        self.wait(15)
        self.play(FadeIn(indice))
        # To-do: algebraic computation
        self.wait(15)









class def_limite(Scene):
    def construct(self):
        title = BoxedTitle(text="Définition de la dérivée en un point", width=7.75, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        caption_string = r"Si $f(x)$ est une fonction continue, la dérivée de $f$ en $a$ est donnée par:"
        caption_property = TextMobject(caption_string)
        caption_property.scale(0.75)
        caption_property.move_to(np.array([-1,2.1,0]))

        definition_limite = TexMobject(
            "f'(a)=",  # 0
            r"\lim_{h\to 0}",  # 1
            r"\frac{f(a+h)-f(a)}{h}",
        )

        info_sup = TextMobject(r"- $f'(a)$ indique si la fonction croît ($f'(a)>0$) ou décroît ($f'(a)<0$).").scale(0.75)
        info_sup.next_to(caption_property, DOWN, buff=3.5*LARGE_BUFF).align_to(caption_property, LEFT)

        info_sup_2 = TextMobject(r"- $f'(a)$ correspond à \underline{\textbf{la pente de la tangente}} de $f(x)$ en $x=a$.").scale(0.75)
        info_sup_2.next_to(info_sup, DOWN).align_to(info_sup, LEFT)

        info_sup_3 = TextMobject(r"- $f'(a)$ est aussi appelé le \underline{\textbf{taux de variation instantané}} de $f(x)$ en $x=a$.").scale(0.75)
        info_sup_3.next_to(info_sup_2, DOWN).align_to(info_sup_2, LEFT)

        self.play(Write(title))
        self.play(FadeIn(caption_property))
        self.wait(5)
        self.play(Write(definition_limite))
        self.wait(15)
        self.play(FadeIn(info_sup))
        self.wait(8)
        self.play(FadeIn(info_sup_2))
        self.wait(8)
        self.play(FadeIn(info_sup_3))
        self.wait(10)




class graphique(GraphScene):
    """
    Quadratic function on interval [-10, 10]
    """
    CONFIG = {
        "y_min" : 0,
        "y_max": 1,
        "x_min" : 0,
        "x_max": 10,
        "y_tick_frequency" : 0.1,
        "x_tick_frequency" : 0.5,
        "axes_color" : WHITE,
        "y_labeled_nums": list(np.arange(0, 2, 1)),
        "x_labeled_nums": list(np.arange(0, 11, 1)),
        "x_label_decimal":0,
        #"y_label_decimal":0,
        "graph_origin": np.array((-6, -2.75, 0))
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : 1/(1+math.exp(1-x)) - 1/(1+math.exp(1)),
                                    color = BLUE,
                                    x_min = self.x_min,
                                    x_max = self.x_max
                                    )
        graph_lab = self.get_graph_label(graph, label="s(t)")

        def position_function(x):
            return 1/(1+math.exp(1-x)) - 1/(1+math.exp(1))

        def round_number(number, digit_param=2):
            return round(number, digit_param - int(math.floor(math.log10(number))) - 1)

        def get_slope(point_1, point_2):
            delta_y = point_2[1] - point_1[1]
            delta_x = point_2[0] - point_1[0]
            return delta_y/delta_x

        def get_intercept(point, slope):
            return point[1] - slope*point[0]

        def get_linear_function_params(point_1, point_2):
            slope = get_slope(point_1, point_2)
            intercept = get_intercept(point_1, slope)
            return (slope, intercept)

        y_values = [i*0.1 for i in range(1,10,1)]
        y_positions = [self.coords_to_point(0, y_value) for y_value in y_values]
        y_values_labels = [TexMobject("{}".format(round_number(y_value))).next_to(y_position + np.array([-1,0,0])).scale(0.75) for y_value, y_position in zip(y_values, y_positions)]

        for y_value_label in y_values_labels:
            self.play(ShowCreation(y_value_label), run_time=0.1)

        self.play(ShowCreation(graph), ShowCreation(graph_lab), run_time=2)

        # Graph labels
        x_label = TexMobject(r"\text{Position (km)}").move_to(np.array([-4.75,3.5,0])).scale(0.75)
        y_label = TexMobject(r"\text{Temps}").move_to(np.array([3,-1.75,0])).scale(0.75)
        y_label_ctnd = TexMobject(r"\text{écoulé (sec.)}").next_to(y_label, DOWN, buff=SMALL_BUFF).scale(0.75)
        self.play(ShowCreation(x_label))
        self.play(ShowCreation(y_label), ShowCreation(y_label_ctnd))

        x_1 = 3
        point_1 = (x_1, position_function(x_1))
        coords_1 = self.coords_to_point(point_1[0], point_1[1])
        plotted_point_1 = Dot(self.coords_to_point(3, point_1[1]))
        dash_line_1 = DashedLine(self.coords_to_point(3, 0), plotted_point_1)
        self.play(ShowCreation(dash_line_1))
        self.play(ShowCreation(plotted_point_1))
        self.wait(10)

        # Create label for the slope
        variation_label = TexMobject(r"{\Delta s", "\over", r"\Delta t", "}").move_to(np.array([2.5, 3, 0]))
        variation_label[0].set_color(BLUE)
        variation_label[2].set_color(YELLOW)

        variation_label_ctd = TexMobject("=", r"{s(t+h)-s(t)", "\over", r"h}").next_to(variation_label, RIGHT)
        variation_label_ctd[1].set_color(BLUE)
        variation_label_ctd[3].set_color(YELLOW)

        self.play(ShowCreation(variation_label))
        self.play(ShowCreation(variation_label_ctd))
        self.wait(15)

        # Sensitivity table (for h)
        h_label_table = TexMobject(r"h").move_to(np.array([5, 1.5, 0]))
        variation_label_table = TexMobject(r"{\Delta s", "\over", r"\Delta t", "}").next_to(h_label_table, RIGHT,
                                                                                            buff=MED_LARGE_BUFF)
        variation_label_table[0].set_color(BLUE)
        variation_label_table[2].set_color(YELLOW)

        horizontal_split = Line(h_label_table.get_center() + np.array([-0.5, -0.75, 0]),
                                variation_label_table.get_center() + np.array([1, -0.75, 0]))
        vertical_split = Line(horizontal_split.get_center() + np.array([-0.25, 1.25, 0]),
                              horizontal_split.get_center() + np.array([-0.25, -5, 0]))

        self.play(ShowCreation(h_label_table))
        self.play(ShowCreation(variation_label_table))
        self.play(ShowCreation(horizontal_split), ShowCreation(vertical_split))
        self.wait(10)


        # Plot the secant lines.
        initial_h = 1
        hs = [initial_h, initial_h / 4, initial_h / 8, initial_h / 32, initial_h / 128]
        hs_rounded = [1, 0.25, 0.125, 0.031, 0.008]
        first_h, first_deviation_ratio = h_label_table, variation_label_table
        previous_h = h_label_table
        previous_variation = variation_label_table
        for i, (h, h_rounded) in enumerate(zip(hs, hs_rounded)):

            if i == 0:
                the_buffer = 1.5*MED_LARGE_BUFF
            else:
                the_buffer = 0.50*MED_LARGE_BUFF

            # Populate the table of hs and slopes.
            table_h_value = TexMobject("{}".format(str(h_rounded))).next_to(previous_h, DOWN, buff=the_buffer).scale(0.75)

            calculated_slope = round_number((position_function(3 + h_rounded) - position_function(3))/h_rounded, digit_param=4)
            table_image = TexMobject("{}".format(str(calculated_slope))).next_to(table_h_value, RIGHT, buff=2*SMALL_BUFF).align_to(first_deviation_ratio, LEFT).scale(0.75)
            #table_image = TexMobject("{}".format(str(calculated_slope))).align_to(first_deviation_ratio, LEFT).scale(0.7)
            self.play(ShowCreation(table_h_value), ShowCreation(table_image))
            previous_h = table_h_value
            previous_variation = table_image


            # Plot the second point and compute tangent graph.
            x_2 = x_1 + h
            point_2 = (x_2, position_function(x_2))
            coords_2 = self.coords_to_point(point_2[0], point_2[1])
            plotted_point_2 = Dot(coords_2)
            dash_line_2 = DashedLine(self.coords_to_point(point_2[0], 0), plotted_point_2)
            slope, intercept = get_linear_function_params(point_1, point_2)
            intermediate_coords = self.coords_to_point(point_2[0], point_1[1])
            y_variation = Line(coords_2, intermediate_coords).set_color(BLUE)
            x_variation = Line(coords_1, intermediate_coords).set_color(YELLOW)
            tangentLine = self.get_graph(lambda x: slope*x + intercept, color=RED, x_min=0, x_max=10)
            scale_value = 0.6

            # Plot labels to illustrate delta y and delta x.
            ds = TexMobject(r"\Delta s").set_color(BLUE).scale(scale_value)
            dt = TexMobject(r"\Delta t").set_color(YELLOW).scale(scale_value)
            ds.next_to(y_variation, RIGHT)
            dt.next_to(x_variation, DOWN)
            scale_value = scale_value / 2

            if h == 1:
                self.play(ShowCreation(plotted_point_2), ShowCreation(dash_line_2))
                self.play(ShowCreation(tangentLine))
                self.play(ShowCreation(x_variation))
                self.play(ShowCreation(y_variation))


                self.wait(5)
                self.play(ShowCreation(ds))
                self.play(ShowCreation(dt))
                self.wait(10)

                self.play(FadeOut(ds))
                self.play(FadeOut(dt))
            else:
                self.play(ReplacementTransform(old_dash_line, dash_line_2), ReplacementTransform(old_plotted_dot, plotted_point_2),
                          ReplacementTransform(old_x_variation, x_variation), ReplacementTransform(old_y_variation, y_variation),
                          ReplacementTransform(old_ds, ds), ReplacementTransform(old_dt, dt))
                self.play(ReplacementTransform(old_tangent_line, tangentLine))


            old_ds, old_dt = ds, dt
            old_dash_line = dash_line_2
            old_tangent_line = tangentLine
            old_plotted_dot = plotted_point_2
            old_x_variation = x_variation
            old_y_variation = y_variation

        self.wait(15)




class vitesse_moyenne(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Vitesse moyenne", width=4.5, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        color_map = {
            r"3": YELLOW,
            r"4": YELLOW,
            r"0.68": BLUE,
            r"0.61": BLUE,
        }

        vertical = Line([-2, 2.5, 0], [-2, -4, 0])
        horizontal = Line([-2, -0.5, 0], [7, -0.5, 0])

        # Vitesse moyenne / calcul
        vitesse_moyenne = TextMobject("vitesse moyenne").move_to(np.array([-4.75, 2, 0])).scale(0.85)
        vitesse_moyenne_unites = TextMobject("(km/secs.)").next_to(vitesse_moyenne, DOWN, buff=SMALL_BUFF).scale(0.85)
        turned_arrow_1 = TexMobject(r"\Rightarrow").rotate(-PI/2).next_to(vitesse_moyenne_unites, DOWN)
        vitesse_moyenne_eq_1 = TextMobject(r"$\frac{\text{distance parcourue (km)}}{\text{temps écoulé (sec.)}}$").next_to(turned_arrow_1, DOWN).scale(0.95)
        turned_arrow_2 = TexMobject(r"\Rightarrow").rotate(-PI/2).next_to(vitesse_moyenne_eq_1, DOWN)
        #vitesse_moyenne_eq_2 = TexMobject(r"\frac{(0.68-0.61) \text{(km)}}{(4-3) \text{(secs.)}}$", tex_to_color_map=color_map).next_to(turned_arrow_2, DOWN).scale(0.95)
        vitesse_moyenne_eq_2 = TexMobject(r"{(0.68-0.61) \text{(km)}", "\over", r"{(4-3) \text{(sec.)}}", tex_to_color_map=color_map).next_to(turned_arrow_2, DOWN).scale(0.95)
        #vitesse_moyenne_eq_2 = TexMobject(r"{\text{Aire du cercle}", "\over", r"\text{Aire du carré}}", r"=")
        vitesse_moyenne_eq_3 = TexMobject(r"= 0.07\text{ km/sec.}").next_to(turned_arrow_2, DOWN).scale(0.95)
        vitesse_moyenne_eq_3.next_to(vitesse_moyenne_eq_2, DOWN).align_to(vitesse_moyenne_eq_2, LEFT)

        # Visualisations
        path = r"C:/Users/Utilisateur/Desktop/CEGEP/Ahunstic-Hiver2021/video/images/"
        image_name_1, image_name_2 = "car_t_3_0", "car_t_4_0"
        voiture_1 = ImageMobject("{}{}.PNG".format(path, image_name_1)).scale(1.15)
        voiture_1.next_to(np.array([0, 0.75, 0]))
        voiture_2 = ImageMobject("{}{}.PNG".format(path, image_name_2)).scale(1.15)
        voiture_2.next_to(voiture_1, DOWN, buff=MED_LARGE_BUFF)



        self.play(Write(title))
        self.wait()
        self.play(ShowCreation(vertical), ShowCreation(horizontal))
        self.play(ShowCreation(voiture_1), ShowCreation(voiture_2))
        self.wait()
        self.play(ShowCreation(vitesse_moyenne), ShowCreation(vitesse_moyenne_unites))
        self.play(ShowCreation(turned_arrow_1))
        self.wait(5)
        self.play(ShowCreation(vitesse_moyenne_eq_1))
        self.play(ShowCreation(turned_arrow_2))
        self.wait(5)
        self.play(ShowCreation(vitesse_moyenne_eq_2))
        self.play(ShowCreation(vitesse_moyenne_eq_3))
        self.wait(5)
        #self.play(Write(indice))
        self.wait(20)



class mandat(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Mandat", width=2.5, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        statement = TextMobject2(r"Déterminer la vitesse de la voiture à ", r"$t=3$", " secondes.")
        statement[1].set_color(YELLOW)
        statement.next_to(title, DOWN, buff=LARGE_BUFF)

        path = r"C:/Users/Utilisateur/Desktop/CEGEP/Ahunstic-Hiver2021/video/images/"
        image_name = "voiture"
        initial_voiture = ImageMobject("{}{}.PNG".format(path, image_name)).scale(0.75)
        initial_voiture.next_to(statement, DOWN, buff=0.5*LARGE_BUFF)

        def distance_function(time):
            return 1/(1+math.exp(1-time)) - 1/(1+math.exp(1))

        def round_number(number):
            return round(number, 2 - int(math.floor(math.log10(number))) - 1)


        old_time_text = TextMobject(r"$t={}$ sec.".format(str(3))).set_color(YELLOW)
        old_dist_text = TextMobject(r"$s({})={}$ km".format(str(3), str(round_number(distance_function(3))))).set_color(BLUE)
        old_time_text.next_to(initial_voiture, DOWN, buff=4.75 * SMALL_BUFF)
        old_dist_text.next_to(old_time_text, DOWN).align_to(old_time_text, LEFT)

        indice = TextMobject2(r"Indice: Étudiez la vitesse moyenne autour de $3$ secondes.").scale(1)
        indice.next_to(initial_voiture, DOWN, buff=2.5 * LARGE_BUFF).align_to(statement, LEFT)

        self.play(Write(title))
        self.wait()
        self.play(FadeIn(initial_voiture), Write(old_time_text), Write(old_dist_text))
        self.wait()
        self.play(Write(statement))
        self.wait(5)
        self.play(Write(indice))
        self.play()
        self.wait(10)



class MES(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Mise en situation", width=5, height=0.7, scale=0.75)
        title.move_to(np.array([0, 3.25, 0]))

        point_A, point_B = Dot().move_to(np.array([-5, -1, 0])), Dot().move_to(np.array([5, -1, 0]))
        name_A, name_B = TexMobject(r"A").next_to(point_A, LEFT), TexMobject(r"B").next_to(point_B, RIGHT)
        line = Line(start=point_A.get_center(), end=point_B.get_center())

        path = r"C:/Users/Utilisateur/Desktop/CEGEP/Ahunstic-Hiver2021/video/images/"
        image_name = "voiture"
        initial_voiture = ImageMobject("{}{}.PNG".format(path, image_name)).scale(0.5)
        old_location = point_A.get_center() + np.array([-0.6, 0.75, 0])
        initial_voiture.move_to(old_location)

        description = TextMobject2("Une voiture roule devant vous. Vous modélisez sa position en fonction du temps sous la fonction ",  r"$s(t)$",
                                   r" où la position est en kilomètres et le temps en secondes.").scale(0.7)
        description[1].set_color(BLUE)
        description.move_to(title.get_center() + np.array([-0.5, -2, 0]))

        self.play(Write(title))
        self.play(Write(description))
        self.wait(3)
        self.play(ShowCreation(point_A), ShowCreation(name_A), ShowCreation(point_B), ShowCreation(name_B))
        self.play(ShowCreation(line))
        self.play(ShowCreation(initial_voiture))

        def distance_function(time):
            return 1/(1+math.exp(1-time)) - 1/(1+math.exp(1))

        def round_number(number):
            return round(number, 2 - int(math.floor(math.log10(number))) - 1)


        time_gap = 0.5
        raw_times = [i*time_gap for i in range(1,21)]
        raw_distances = [distance_function(i*time_gap) for i in range(1,21)]

        times = [round_number(raw_time) for raw_time in raw_times]
        distances = [round_number(raw_distance) for raw_distance in raw_distances]

        old_time_text = TextMobject(r"$t={}$ sec.".format(str(0))).set_color(YELLOW)
        old_dist_text = TextMobject(r"$s({})={}$ km".format(str(0), str(0))).set_color(BLUE)
        old_time_text.next_to(initial_voiture, DOWN, buff=4.75 * SMALL_BUFF)
        old_dist_text.next_to(old_time_text, DOWN).align_to(old_time_text, LEFT)
        self.play(ShowCreation(old_time_text), ShowCreation(old_dist_text))
        self.wait(5)

        for i, (time, distance) in enumerate(zip(times, distances)):
            new_location = old_location + np.array([0.5, 0, 0])
            initial_voiture.move_to(new_location)
            new_time_text = TextMobject(r"$t={}$ sec.".format(time)).set_color(YELLOW)
            new_dist_text = TextMobject(r"$s({})={}$ km".format(time, distance)).set_color(BLUE)
            new_time_text.next_to(initial_voiture, DOWN, buff=4.75*SMALL_BUFF)
            new_dist_text.next_to(new_time_text, DOWN).align_to(new_time_text, LEFT)

            self.play(ShowCreationThenDestruction(initial_voiture), run_time=0.1)
            if i != 0:
                self.play(ReplacementTransform(old_time_text, new_time_text),
                          ReplacementTransform(old_dist_text, new_dist_text), run_time=0.1)

            old_location = new_location
            old_time_text, old_dist_text = new_time_text, new_dist_text

        self.wait(5)
        fonction = TexMobject(r"s(t)=\frac{1}{1+\mathrm{e}^{1-t}} - \frac{1}{1+\mathrm{e}}").set_color(BLUE)
        fonction.move_to((DR + DL)/2 - np.array([0,2,0]))
        boxed_fonction = SurroundingRectangle(fonction).set_color(WHITE)


        self.play(ShowCreation(fonction))
        self.play(WiggleOutThenIn(boxed_fonction))
        self.wait(5)


class IntroCEGEP(Scene):
    CONFIG = {
        "x_start": 3,
        "x_end": 7,
        "axes_config": {
            "center_point": [-1.5,-3,0],
            "x_axis_config": {
                "unit_size": 0.35,
                "x_min": 0,
                "x_max": 10,
                "include_numbers": True
            },
            "y_axis_config": {
                "unit_size": 0.4,
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
        title = BoxedTitle(text="La dérivée en un point", width=6, height=0.7, scale=0.75)
        title.move_to(np.array([0, 3.25, 0]))

        my_name = TextMobject2(r"Louis-Marc Mercier").scale(0.75)
        my_name.next_to(title, DOWN, buff=0.7 * LARGE_BUFF)

        college_name = TextMobject2(r"Collège", r"\textbf{Ahuntsic}").scale(0.75)
        college_name.next_to(my_name, DOWN, buff=0.7 * LARGE_BUFF)
        college_name[1][0].set_color("#E5070D")

        department_name = TextMobject2(r"Département de mathématiques").scale(0.7)
        department_name.next_to(college_name, DOWN, buff=SMALL_BUFF)

        # Displaying everything
        self.play(FadeIn(title))
        self.play(FadeIn(my_name))
        self.play(FadeIn(college_name), FadeIn(department_name))
        #self.play(FadeIn(trailer_subtitle_2))

        # Plot
        axes = self.get_axes()
        func = self.get_graph(self.func,**self.func_config)
        dot_start = self.get_dot_from_x_coord(self.x_start)
        dot_end = self.get_dot_from_x_coord(self.x_end)
        line = VMobject()
        line.add_updater(self.get_line_updater(dot_start,dot_end))
        #self.add(axes,func,dot_start,dot_end,line)
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
        #self.wait(3)

        self.move_dot(dot_end, self.x_end, self.x_start + 0.0001, run_time=2)
        line.clear_updaters()
        self.remove(dot_end)
        line.add_updater(self.get_derivative_updater(dot_start))
        self.add(line)
        self.wait()
        self.move_dot(dot_start, self.x_start, 8, run_time=3, rate_func=there_and_back)
        self.wait()



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