from manimlib.imports import *
from manim_utils.slide_template import Warning, BoxedTitle, GenChannelLogo, YoutubeLogo

# 1. ThumbnailFrench
# 2. Plan
# 3. Exemple1Intro
# 4. Exemple2Intro
# 5. MiseEnGarde
# 5. Formalisme
# 6. Formalisme2
# 7. Caracteristique
# 8. Pratique
# 9. Exercices



class ThumbnailFrench(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        line_e = TextMobject(r"\sc{On se}", r"\sc{ressemble!}").scale(2.25).shift(2.25 * UP + 4 * LEFT).set_color([PINK,YELLOW])
        line_e[0].next_to(3 * UP + 7 * LEFT)
        line_e[1].next_to(2 * UP + 7 * LEFT)
        line_pi = TextMobject(r"{\sc J'étais comme}", r"{\sc toi avant!}").scale(1.9).set_color([YELLOW,PINK])
        line_pi[0].next_to(3 * UP + 0 * LEFT)
        line_pi[1].next_to(2 * UP + 0 * LEFT)

        line2 = TextMobject("$x$", r"$\mapsto$", r"$f(x)$")
        line2[0].scale(10).next_to(2.4 * DOWN + 6 * LEFT).set_color([PINK,YELLOW])
        line2[1].scale(6).next_to(line2[0], RIGHT, buff=2*MED_LARGE_BUFF)
        line2[2].scale(6).next_to(2.1 * DOWN + 1.1 * RIGHT).set_color([YELLOW,PINK])
        self.play(FadeIn(line2))
        self.wait(2)
        self.play(FadeIn(line_e))
        self.wait(2)
        self.play(FadeIn(line_pi))
        self.wait(5)

def get_checkmark(word, buff_size=MED_SMALL_BUFF):
    checkmark = TexMobject("\\checkmark")
    checkmark.set_color(GREEN)
    checkmark.scale(1.25)
    checkmark.next_to(word, RIGHT, buff=buff_size)
    return checkmark


class Plan(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Plan", width=4, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        compl_rules_str = [
            "",
            "Familier avec les ensembles.",
            "Interactions plus dynamiques.",
            "Lier les éléments des ensembles.",
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

        checkmark = get_checkmark(rules[1])

        self.play(Write(title))
        self.wait(5)
        self.play(Write(rules[1]))
        self.play(ShowCreation(checkmark))
        self.wait(5)
        self.play(Write(rules[2]))
        self.wait(5)
        self.play(Write(rules[3]))
        self.wait(7)


class Exemple1Intro(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Exemples", width=3, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        # Get labels (names and values)
        names = ["Astérix", "Obélix", "$\dots$", "Panoramix"]
        numbers = ["$5$", "$12$", "$\dots$", "$20$"]
        colors = [RED, BLUE, WHITE, GREEN]
        mapping_arrow = TextMobject(r"$\mapsto$").rotate(-PI/2)

        # Get images
        path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/images/asterix_dossier/"
        asterix_img = ImageMobject(path + "MonAsterix2")
        obelix_img = ImageMobject(path + "MonObelix2")
        black_img = ImageMobject(path + "black_image")
        panoramix_img = ImageMobject(path + "MonPanoramix")
        images = [asterix_img, obelix_img, black_img, panoramix_img]

        new_images, new_names, new_numbers = [], [], []
        for i, (image, name, number, color) in enumerate(zip(images, names, numbers, colors)):
            if i==0:
                new_name = TextMobject(name, color=color).next_to(np.array([-6,0,0]))
                new_image = image.next_to(new_name, UP)
                new_number = TextMobject(number, color=color).next_to(new_name, DOWN, buff=2*LARGE_BUFF)
                new_names.append(new_name)
                new_images.append(new_image)
                new_numbers.append(new_number)
            if i!=0:
                new_name = TextMobject(name, color=color).next_to(new_name, RIGHT, buff=2*LARGE_BUFF)
                new_image = image.next_to(new_name, UP)
                new_number = TextMobject(number, color=color).next_to(new_name, DOWN, buff=2*LARGE_BUFF)
                new_names.append(new_name)
                new_images.append(new_image)
                new_numbers.append(new_number)


        # Change images locations


        self.play(Write(title))
        self.wait(5)

        # Display names.
        for i, (new_image, new_name) in enumerate(zip(new_images, new_names)):
            self.play(ShowCreation(new_name))
            self.play(FadeIn(new_image))
        self.wait(5)

        # Display mapping arrows.
        for i, new_name in enumerate(new_names):
            if i!=2:
                new_mapping_arrow = mapping_arrow.copy().next_to(new_name, DOWN, buff=0.7*LARGE_BUFF).scale(2)
                self.play(ShowCreation(new_mapping_arrow))

        self.wait(5)

        # Display numbers
        for new_number in new_numbers:
            self.play(ShowCreation(new_number))

        self.wait(10)


class Exemple2Intro(GraphScene):
    """
    Quadratic function on interval [-10, 10]
    """
    CONFIG = {
        "y_max" : 100,
        "y_min" : 0,
        "x_max" : 10,
        "x_min" : -10,
        "y_axis_label": "$f(x)$",
        "y_tick_frequency" : 5,
        "x_tick_frequency" : 0.5,
        "axes_color" : BLUE,
        "y_labeled_nums": range(0,100,10),
        "x_labeled_nums": list(np.arange(-10, 10, 2)),
        "x_label_decimal":0,
        "y_label_decimal":0,
        "graph_origin": np.array((0, -3.25, 0))
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : x**2,
                                    color = GREEN,
                                    x_min = self.x_min,
                                    x_max = self.x_max
                                    )
        #graph.y_axis_label = TextMobject(r"$f(x)$")

        graph_lab = self.get_graph_label(graph, label="x^2")
        self.play(ShowCreation(graph), ShowCreation(graph_lab), run_time = 2)
        self.wait(5)
        mapping = TextMobject(r"$x$ ", r"$\mapsto$", r" $x^{2}$").next_to(graph_lab, DOWN, buff=LARGE_BUFF).align_to(graph_lab, LEFT)
        mapping[2].set_color(GREEN)
        self.play(ShowCreation(mapping))
        self.wait(10)


class Cancel(VGroup):
    CONFIG = {
        "line_kwargs": {"color":RED},
        "buff_text": None,
        "buff_line": 0.7,
    }
    def __init__(self,text,texmob=None,**kwargs):
        digest_config(self,kwargs)
        VGroup.__init__(self,**kwargs)

        pre_coord_dl = text.get_corner(DL)
        pre_coord_ur = text.get_corner(UR)
        reference_line = Line(pre_coord_dl,pre_coord_ur)
        reference_unit_vector = reference_line.get_unit_vector()
        coord_dl = text.get_corner(DL) - text.get_center() - reference_unit_vector*self.buff_line
        coord_ur = text.get_corner(UR) - text.get_center() + reference_unit_vector*self.buff_line
        if texmob == None:
            line = Line(coord_dl,coord_ur,**self.line_kwargs)
            self.add(line)
        else:
            arrow = Arrow(coord_dl,coord_ur,**self.line_kwargs)
            unit_vector = arrow.get_unit_vector()
            if self.buff_text == None:
                self.buff_text = get_norm((texmob.get_center()-texmob.get_critical_point(unit_vector))/2)*2
            texmob.move_to(arrow.get_end()+unit_vector*self.buff_text)
            self.add(arrow,texmob)


class MiseEnGarde(Scene):
    def construct(self):
        title = BoxedTitle(text="Mise en garde", width=4, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))
        warning = Warning().next_to(title, LEFT).scale(0.45)
        warning_2 = Warning().next_to(title, RIGHT).scale(0.45)

        formula_1 = TexMobject("y=\sqrt{x}", height=1).next_to(title, DOWN, buff=LARGE_BUFF)
        cancel_formula_1 = Cancel(formula_1).next_to(formula_1, 0)

        formula_2 = TexMobject("f(x)=\sqrt{x}", height=1).next_to(formula_1, DOWN, buff=LARGE_BUFF).align_to(formula_1, RIGHT)
        checkmark = get_checkmark(formula_2, buff_size=LARGE_BUFF)

        self.play(ShowCreation(title))
        self.wait(2)
        self.play(DrawBorderThenFill(warning), DrawBorderThenFill(warning_2))
        self.play(ShowCreation(formula_1))
        self.wait(10)
        self.play(ShowCreation(cancel_formula_1))
        self.play(ShowCreation(formula_2))
        self.wait(10)
        self.play(ShowCreation(checkmark))
        self.wait(5)

        # Pause to think about it.
        circ = Arc(start_angle=PI / 2, angle=-2 * PI, radius=0.35).to_corner(DL)
        timers = [TexMobject(str(i)).move_to(circ) for i in range(5, -1, -1)]
        pause = TextMobject("Et pour $x<0$ ?").next_to(circ, RIGHT)
        self.play(ShowCreation(circ), Write(pause))
        self.play(Write(timers[0]), run_time=0.5)
        for i in range(5):
            self.play(ReplacementTransform(timers[i], timers[i + 1]), run_time=0.5)
            self.wait(0.5)
        self.play(FadeOut(pause), FadeOut(timers[-1]), FadeOut(circ), run_time=2)

        answer = TextMobject("Réponse: La fonction n'est pas définie!").to_corner(DL)
        self.play(Write(answer))
        self.wait(15)


class Formalisme(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Formalisme", width=3, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        statement = TextMobject2(r"$\textit{``$f$ est une fonction de $A$ à $B$''}$", " est exprimé symboliquement par:").scale(0.8)
        statement[0].set_color(BLUE)
        statement.next_to(title, DOWN, buff=LARGE_BUFF)

        formulas = TextMobject(r"$f:A\rightarrow B\quad$", "ou", r"$\quad A\xrightarrow[]{f}B$")
        formulas[0].set_color(BLUE)
        formulas[2].set_color(BLUE)
        formulas.next_to(statement, DOWN, buff=LARGE_BUFF)

        raw_dom_et_codom = [r"$\bullet$ $A$ correspond au domaine de la fonction (i.e. $dom(f)$).",
                            r"$\bullet$ $B$ correspond à l'image de la fonction (i.e. $ima(f)$)."]
        dom_et_codom = [TextMobject(elem).scale(0.75) for elem in raw_dom_et_codom]
        dom_et_codom[0].next_to(formulas, DOWN, buff=1.5*LARGE_BUFF).align_to(statement, LEFT)
        dom_et_codom[1].next_to(dom_et_codom[0], DOWN, buff=MED_LARGE_BUFF).align_to(dom_et_codom[0], LEFT)


        self.play(Write(title))
        self.wait(7)
        self.play(Write(statement))
        self.wait(8)
        self.play(Write(formulas))
        self.wait(10)
        self.play(Write(dom_et_codom[0]))
        self.wait(10)
        self.play(Write(dom_et_codom[1]))
        self.wait(20)


class Formalisme2(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Formalisme (suite)", width=4.5, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        statement = TextMobject2(r"$\textit{``$f$ transforme $x$ en $f(x)$''}$", " est exprimé symboliquement par:").scale(0.8)
        statement[0].set_color(BLUE)
        statement.next_to(title, DOWN, buff=LARGE_BUFF)

        formulas = TextMobject(r"$x\mapsto f(x)\quad$", "ou", r"$\quad x\xmapsto[]{f}f(x)$")
        formulas[0].set_color(BLUE)
        formulas[2].set_color(BLUE)
        formulas.next_to(statement, DOWN, buff=LARGE_BUFF)

        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement))
        self.wait(8)
        self.play(Write(formulas))
        self.wait(20)



class Caracteristique(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Caractéristique", width=5, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        statement = TextMobject2(r"La valeur de $f(x)$ est définie $\underline{\textbf{uniquement}}$ pour tout élément $x$ du domaine.").scale(0.7)
        statement[0].set_color(BLUE)
        statement.next_to(title, DOWN, buff=LARGE_BUFF)

        contre_exemple_nom = TextMobject2(r"Contre-exemples:").scale(0.7).next_to(statement, DOWN, buff=2*LARGE_BUFF).align_to(statement, LEFT)
        cercle = Circle().next_to(contre_exemple_nom, RIGHT, buff=1.5*LARGE_BUFF).set_color(RED)
        contre_exemple_cercle = TextMobject2(r"Cercle $\Big($e.g. $y=\pm\sqrt{5-x^{2}}\Big)$").scale(0.7)
        contre_exemple_cercle.next_to(cercle, DOWN)

        ellipse = Ellipse(width=4, height=2).next_to(cercle, RIGHT, buff=2 * LARGE_BUFF).set_color(ORANGE)
        contre_exemple_ellipse = TextMobject2(r"Ellipse $\bigg($e.g. $y=\pm\sqrt{9-\frac{9x^{2}}{25}}\bigg)$").scale(0.7)
        contre_exemple_ellipse.next_to(contre_exemple_cercle, RIGHT, buff=1.25*MED_LARGE_BUFF)


        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement))
        self.wait(15)
        self.play(Write(contre_exemple_nom), ShowCreation(cercle))
        self.play(Write(contre_exemple_cercle))
        self.wait(10)
        self.play(ShowCreation(ellipse))
        self.play(Write(contre_exemple_ellipse))
        self.wait(10)


class VieillePratique(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Exemple", width=5, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        statement = TextMobject2(r"Soit la fonction $f:\mathbb{R}_{+}\rightarrow\mathbb{R}_{+}$ définie par $f(x)=\sqrt{x}$.").scale(0.7)
        statement.next_to(title, DOWN, buff=LARGE_BUFF)

        raw_dom_et_codom = [r"$\bullet$ $\mathbb{R}_{+}$ correspond au domaine de la fonction (i.e. $dom(f)$).",
                            r"$\bullet$ $\mathbb{R}_{+}$ correspond à l'image de la fonction (i.e. $ima(f)$)."]
        dom_et_codom = [TextMobject(elem).scale(0.75) for elem in raw_dom_et_codom]
        dom_et_codom[0].next_to(statement, DOWN, buff=1.5 * LARGE_BUFF).align_to(statement, LEFT)
        dom_et_codom[1].next_to(dom_et_codom[0], DOWN, buff=MED_LARGE_BUFF).align_to(dom_et_codom[0], LEFT)


        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement))
        self.wait(15)
        self.play(Write(dom_et_codom[0]))
        self.play(Write(dom_et_codom[1]))
        self.wait(10)


class Pratique(GraphScene):
    """
    Quadratic function on interval [-10, 10]
    """
    CONFIG = {
        "y_max" : 5,
        "y_min" : 0,
        "x_max" : 11,
        "x_min" : 0,
        "y_axis_label": "$f(x)$",
        "y_tick_frequency" : 0.25,
        "x_tick_frequency" : 0.5,
        "axes_color" : BLUE,
        "y_labeled_nums": range(0,5,1),
        "x_labeled_nums": list(np.arange(0, 10, 2)),
        "x_label_decimal":0,
        "y_label_decimal":0,
        "graph_origin": np.array((1, -3.25, 0))
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : x**0.5,
                                    color = GREEN,
                                    x_min = self.x_min,
                                    x_max = self.x_max
                                    )
        #graph.y_axis_label = TextMobject(r"$f(x)$")

        graph_lab = self.get_graph_label(graph, label="\sqrt{x}")

        title = BoxedTitle(text="Exercice", width=5, height=0.7, scale=0.7)
        title.to_corner(UL)


        statement_1 = TextMobject2(r"Soit $f:\mathbb{R}_{+}\rightarrow\mathbb{R}_{+}$ définie par").scale(0.75)
        statement_1.next_to(np.array([-7,2,0]))

        statement_2 = TextMobject(r"$f(x)=\sqrt{x}$")
        statement_2.next_to(statement_1, DOWN, buff=LARGE_BUFF)

        raw_dom_et_codom = [r"$\bullet$ Quel est le domaine de $f$?", r"$\bullet$ Quelle est l'image de $f$?"]
        dom_et_codom = [TextMobject(elem).scale(0.75) for elem in raw_dom_et_codom]
        dom_et_codom[0].next_to(statement_2, DOWN, buff=2 * LARGE_BUFF).align_to(statement_1, LEFT)
        dom_et_codom[1].next_to(dom_et_codom[0], DOWN, buff=MED_LARGE_BUFF).align_to(dom_et_codom[0], LEFT)

        self.play(ShowCreation(title))
        self.wait(3)
        self.play(Write(statement_1), Write(statement_2))
        self.wait(10)
        self.play(ShowCreation(dom_et_codom[0]), ShowCreation(dom_et_codom[1]), run_time=2)
        self.wait(5)
        self.play(ShowCreation(graph), ShowCreation(graph_lab), run_time = 2)
        self.wait(5)
        self.wait(10)




class Derivative2(Scene):
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

        trailer_subtitle = TextMobject(r"\sc{\textbf{Les fonctions}}")
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
