from manimlib.imports import *
from manim_utils.slide_template import BoxedTitle, GenChannelLogo, YoutubeLogo
from MyAnim.RevisionSecondaire.id_rem_french import MeasureDistance
import pandas as pd
import numpy as np

# 1. Thumbnail
# 2. Plan
# 3. Exemple1Intro
# 4. Exemple2Intro
# 5. MiseEnGarde
# 5. Formalisme
# 6. Formalisme2
# 7. Caracteristique
# 8. Pratique
# 9. Exercices

# https://youtu.be/7M_v13KS3xc

# Code: https://colab.research.google.com/drive/1-pCwp5ACjhwpLyS3oPuhWRMpmw5-aRyy?usp=sharing

class Thumbnail(Scene):
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



class Me_description(Scene):
    def construct(self):

        # Channel logo and name (UP LEFT CORNER)
        path = r"C:/Users/Utilisateur/Desktop/CEGEP/Cours_maison/"
        image = ImageMobject(path + "very_light_phoenix").to_corner(UL)
        image.to_corner(DL)
        image.scale(1)

        youtube_logo = YoutubeLogo().scale(0.4)
        youtube_logo.next_to(image, RIGHT)

        channel_name = TextMobject(r"Louis-Math")
        channel_name.next_to(image, DOWN, buff=0.1*SMALL_BUFF)
        channel_name.scale(0.75)
        channel_name.set_color_by_gradient(RED, ORANGE, GOLD, ORANGE, RED)


        # Graph image (DOWN RIGHT CORNER)
        path2 = r"C:/Users/Utilisateur/Desktop/CEGEP/Cours_maison/toastersman_videos/Revision_precalcul/TrailerCalculus/"
        portrait = ImageMobject(path2 + "portrait_final_3")
        portrait.next_to(np.array([3.75, -1, 0]))
        portrait.scale(2.9)

        # My name
        name_title = TextMobject(r"\sc{\textbf{- Mon nom est Louis-Marc Mercier.}}")
        name_title.set_color_by_gradient("#d9c78c", "#fffec4", "#fdf7b4","#e8e0a0","#d9bf87","#ae8963")
        name_title.move_to(np.array([-3, 2.75, 0]))
        name_title.scale(0.75)

        # My studies
        trailer_subtitle = TextMobject(r"\sc{- B.Sc. mathématiques}").scale(0.75)
        trailer_subtitle_ctd = TextMobject(r"\sc{- M.Sc.A mathématiques appliquées}").scale(0.75)
        trailer_subtitle.set_color_by_gradient("#d9c78c", "#fffec4", "#fdf7b4","#e8e0a0","#d9bf87","#ae8963")
        trailer_subtitle_ctd.set_color_by_gradient("#d9c78c", "#fffec4", "#fdf7b4","#e8e0a0","#d9bf87","#ae8963")
        trailer_subtitle.next_to(name_title, DOWN, buff=LARGE_BUFF).align_to(name_title, LEFT)
        trailer_subtitle_ctd.next_to(trailer_subtitle, DOWN).align_to(trailer_subtitle, LEFT)


        # Work
        work_subtitle = TextMobject(r"\sc{- Recherche en intelligence artificielle}").scale(0.75)
        work_subtitle.set_color_by_gradient("#d9c78c", "#fffec4", "#fdf7b4", "#e8e0a0", "#d9bf87", "#ae8963")
        work_subtitle.next_to(trailer_subtitle_ctd, DOWN, buff=LARGE_BUFF).align_to(trailer_subtitle_ctd, LEFT)
        work_subtitle_ctd = TextMobject(r"\sc{- Créateur de contenu sur Youtube}").scale(0.75)
        work_subtitle_ctd.set_color_by_gradient("#d9c78c", "#fffec4", "#fdf7b4", "#e8e0a0", "#d9bf87", "#ae8963")
        work_subtitle_ctd.next_to(work_subtitle, DOWN).align_to(work_subtitle, LEFT)

        # Displaying everything
        #self.play(FadeIn(image))
        #self.play(FadeIn(channel_name))
        self.play(FadeIn(portrait))
        self.wait()
        self.play(FadeIn(name_title))
        self.wait(5)
        self.play(FadeIn(trailer_subtitle))
        self.play(FadeIn(trailer_subtitle_ctd))
        self.wait(7)
        self.play(FadeIn(work_subtitle))
        self.play(FadeIn(work_subtitle_ctd))
        self.wait(7)
        self.play(ShowCreation(image), ShowCreation(channel_name))
        self.play(ShowCreation(youtube_logo))
        self.wait(5)


class Thumbnail(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        path = r"C:/Users/Utilisateur/Desktop/CEGEP/"
        python_img_path = r"C:/Users/Utilisateur/Desktop/CEGEP/Cours_maison/toastersman_videos/presentations/brebeuf/"
        philactere_name, coeur_bleu, python_img_name = "philactere_noire", "coeur_bleu", "python_symbol_clean"
        philactere = ImageMobject("{}{}.PNG".format(path, philactere_name)).scale(2.5).move_to(np.array([0,1.5,0]))
        coeur = ImageMobject("{}{}.PNG".format(path, coeur_bleu)).move_to(np.array([0,1.75,0]))
        python_img_name = ImageMobject("{}{}.PNG".format(python_img_path, python_img_name)).scale(2.5).move_to(np.array([0, 1.5, 0]))
        coeur.scale(1.15)

        line2 = TextMobject("$\mathbb{P}$")
        line3 = TextMobject("$\mathbb{P}$").scale(8).set_color(PINK).to_corner(DR)
        python_img_name.scale(0.5).next_to(np.array([-5.2, -2, 0]))
        line2.scale(8).to_corner(DR).set_color("#D4AF37")
        self.play(ShowCreation(python_img_name))
        self.play(Write(line2))
        self.wait(3)
        self.play(ShowCreation(philactere))
        self.play(WiggleOutThenIn(coeur))
        self.play(Transform(line2, line3))
        self.wait(5)




class motivation(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Motivation", width=3.5, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        statement = TextMobject2(r"La programmation est \textbf{importante} dans les sciences pures.").scale(0.8)
        statement.next_to(title, DOWN, buff=LARGE_BUFF)

        formula_general = TextMobject(r"- informatique,").align_to(statement, LEFT)
        formula_canon = TextMobject(r"- mathématiques,").next_to(formula_general, DOWN).align_to(formula_general, LEFT)
        formula_facto = TextMobject(r"- ingénierie.").next_to(formula_canon, DOWN).align_to(formula_canon, LEFT)

        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement))
        self.wait(5)
        self.play(Write(formula_general))
        self.wait(5)
        self.play(Write(formula_canon))
        self.wait(5)
        self.play(Write(formula_facto))
        self.wait(10)



class Prerequis(Scene):
    CONFIG = {
        "x_start": 2,
        "x_end": 1,
        "axes_config": {
            "center_point": [3, -1.75, 0],
            "x_axis_config": {
                "unit_size": 0.6,
                "x_min": 0,
                "x_max": 4,
                "include_numbers": True
            },
            "y_axis_config": {
                "unit_size": 0.6,
                "label_direction": UP,
                "x_min": -2,
                "x_max": 5,
                "include_numbers": True
            },
        },
        "func": lambda x: (x-1)*(x-2),
        "func_config": {
            "color": PINK,
            "x_min": -0.5,
            "x_max": 3.5,
        },
        "dot_radius": 0.1,
        "line_config": {}
    }
    def construct(self):

        vertical = Line([-2,3,0], [-2,-4,0])
        horizontal = Line([-7,3,0], [7,3,0])

        # Source: https://github.com/vivek3141/videos/blob/master/maxwell.py
        color_map = {
            r"x_{1}": YELLOW,
            r"x_{2}": "#D4AF37",
        }

        color_map_2 = {
            r"A": PINK,
            r"R": YELLOW,
        }

        statement = TextMobject2(r"Vous devez maîtriser les éléments suivants:").scale(0.8)
        statement.next_to(horizontal, UP, buff=SMALL_BUFF).align_to(horizontal, LEFT)

        #function_latex = TexMobject(r"f(x)=(x-1)(x-2)", tex_to_color_map=color_map_2).align_to(statement, LEFT).scale(0.8)
        #function_latex.next_to(statement, RIGHT)

        algebraic_box = BoxedTitle(text="Mathématiques", width=3.5, height=0.7, scale=0.7, box_color="#D4AF37")
        algebraic_box.move_to(np.array([-4.5, 2.5, 0]))
        visual_box = BoxedTitle(text="Python", width=2, height=0.7, scale=0.7, box_color="#D4AF37")
        visual_box.move_to(np.array([2, 2.5, 0]))

        area_circle_title = TextMobject("- Aire du cercle,").next_to(np.array([-7, 1, 0])).scale(1)

        #cercle = Circle(fill_opacity=0.5, color=PINK).next_to(area_circle_title, DOWN)
        #center_cercle = Dot().next_to(cercle, 0)
        #radius = Line(start=center_cercle.get_center(), end=center_cercle.get_center() - np.array([0 , 1, 0])).set_color(YELLOW)
        #area_circle_formula = TexMobject("A=\pi R^{2}", tex_to_color_map=color_map_2).next_to(cercle, DOWN)
        #circle_formula = TexMobject("x^{2}+y^{2}= R^{2}", tex_to_color_map=color_map_2).next_to(cercle, DOWN)
        #circle_formula.next_to(area_circle_formula, DOWN).align_to(area_circle_formula, LEFT)

        aire_carre_statement = TextMobject("- Aire du carré,").scale(1)
        aire_carre_statement.next_to(area_circle_title, DOWN).align_to(area_circle_title, LEFT)

        equation_cercle = TextMobject("- Équation du cercle,").scale(1)
        equation_cercle.next_to(aire_carre_statement, DOWN).align_to(aire_carre_statement, LEFT)

        probabilites_title = TextMobject("- Bonus: ", "probabilités", ".").scale(1)
        probabilites_title[1].set_color(YELLOW)
        probabilites_title.next_to(equation_cercle, DOWN).align_to(equation_cercle, LEFT)

        import_skill = TextMobject(r"- Importer des librairies; ")
        import_skill.next_to(area_circle_title, RIGHT, buff=2*LARGE_BUFF)

        fonction_skill = TextMobject(r"- Créer des fonctions; ")
        fonction_skill.next_to(import_skill, DOWN).align_to(import_skill, LEFT)

        types_skill = TextMobject(r"- Connaître les types de variables; ")
        types_skill.next_to(fonction_skill, DOWN).align_to(fonction_skill, LEFT)

        boucle_skill = TextMobject(r"- Créer une boucle \textbf{for}. ")
        boucle_skill.next_to(types_skill, DOWN).align_to(types_skill, LEFT)

        path_python_logo = r"C:/Users/Utilisateur/Desktop/CEGEP/Cours_maison/toastersman_videos/presentations/brebeuf/"
        python_logo_name = "python_symbol_clean"
        python_logo = ImageMobject("{}{}.PNG".format(path_python_logo, python_logo_name)).scale(1.5).next_to(visual_box, RIGHT, buff=MED_LARGE_BUFF).scale(0.3)
        python_logo.next_to(np.array([5.75, 2.25, 0]))


        self.play(Write(statement))
        #self.play(Write(function_latex))
        self.wait(5)
        self.play(Write(horizontal))
        self.wait(5)
        self.play(Write(vertical))
        self.wait(5)
        self.play(ShowCreation(algebraic_box))
        self.play(Write(area_circle_title))

        #self.play(ShowCreation(cercle), ShowCreation(center_cercle))
        #self.play(ShowCreation(area_circle_formula), ShowCreation(radius))
        #self.play(ShowCreation(circle_formula))

        self.play(ShowCreation(aire_carre_statement))
        self.play(ShowCreation(equation_cercle))
        self.play(ShowCreation(probabilites_title))
        self.wait(10)
        self.play(ShowCreation(visual_box))
        self.play(WiggleOutThenIn(python_logo))
        self.play(ShowCreation(import_skill))
        self.wait()
        self.play(ShowCreation(fonction_skill))
        self.wait()
        self.play(ShowCreation(types_skill))
        self.wait()
        self.play(ShowCreation(boucle_skill))
        self.wait(10)


class solution_probs(Scene):

    def construct(self):
        # Source: https://github.com/vivek3141/videos/blob/master/maxwell.py

        color_map = {
            r"R": YELLOW
        }



        title = BoxedTitle(text="Approche mathématique", width=5.5, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        calcul_proba = TexMobject("p", "=", r"{\text{Aire du cercle}", "\over", r"\text{Aire du carré}}", r"=")
        calcul_proba.next_to(np.array([-6, 0, 0]))
        horizontal = Line([-1, 0, 0], [1, 0, 0])
        horizontal.next_to(calcul_proba, RIGHT)

        calcul_proba_ctd = TexMobject("=", r"{\pi R^{2}", "\over", r"(2R)^{2}}", r"=", r"{\pi", "\over", r"4}", tex_to_color_map = color_map)
        calcul_proba_ctd.next_to(horizontal, RIGHT)

        cercle = Circle(radius=0.5, fill_opacity=0.5, color=WHITE).next_to(horizontal, UP)
        center_cercle = Dot().next_to(cercle, 0)
        radius = Line(start=center_cercle.get_center(), end=center_cercle.get_center() - np.array([0 , 0.5, 0])).set_color(YELLOW)
        square = Square(side_length=1, fill_opacity=0.5, color=PURPLE).next_to(horizontal, DOWN)

        self.play(ShowCreation(title))
        self.wait(5)
        self.play(ShowCreation(calcul_proba))
        self.wait(5)
        self.play(ShowCreation(horizontal))
        self.wait(5)
        self.play(ShowCreation(cercle))
        self.play(ShowCreation(center_cercle), ShowCreation(radius))
        self.play(ShowCreation(square))
        self.wait(5)
        self.play(ShowCreation(calcul_proba_ctd))
        self.wait(10)



class revision_aire(Scene):

    def construct(self):

        # Source: https://github.com/vivek3141/videos/blob/master/maxwell.py
        color_map = {
            r"A": PURPLE,
            r"c": BLUE,
        }

        color_map_2 = {
            r"A": GRAY,
            r"R": YELLOW,
        }

        #title = BoxedTitle(text="Révision Aire", width=3.5, height=0.7, scale=0.7)
        #title.move_to(np.array([0, 3.25, 0]))

        algebraic_box = BoxedTitle(text="Aire du cercle", width=3.5, height=0.7, scale=0.7, box_color="#D4AF37")
        algebraic_box.move_to(np.array([-3.5, 2.5, 0]))
        visual_box = BoxedTitle(text="Aire du carré", width=3.5, height=0.7, scale=0.7, box_color="#D4AF37")
        visual_box.move_to(np.array([2, 2.5, 0]))

        cercle = Circle(radius=1, fill_opacity=0.5, color=WHITE).next_to(algebraic_box, DOWN, buff=MED_LARGE_BUFF)
        center_cercle = Dot().next_to(cercle, 0)
        radius = Line(start=center_cercle.get_center(), end=center_cercle.get_center() - np.array([0, 1, 0])).set_color(YELLOW)
        area_circle_formula = TexMobject("A=\pi R^{2}", tex_to_color_map=color_map_2).next_to(cercle, DOWN)
        label_r = TexMobject("R").next_to(radius, RIGHT, buff=0.5 * SMALL_BUFF).set_color(YELLOW)

        square = Square(radius=1, fill_opacity=0.5, color=PURPLE).next_to(visual_box, DOWN, buff=MED_LARGE_BUFF)
        area_square_formula = TexMobject("A=c^{2}", tex_to_color_map=color_map).next_to(square, DOWN)

        mesure_1 = Arrow(np.array([0.35,0,0]) + (square.get_corner(DR) + square.get_corner(UR))/2,
                         np.array([0.35,0,0]) + square.get_corner(DR) + np.array([0,-0.25,0]))
        mesure_2 = Arrow(np.array([0.35,0,0]) + (square.get_corner(DR) + square.get_corner(UR))/2,
                         np.array([0.35,0,0]) + square.get_corner(UR) + np.array([0,0.25,0]))
        label_c = TexMobject("c", tex_to_color_map=color_map_2).next_to((square.get_corner(DR) + square.get_corner(UR))/2).set_color(BLUE)

        self.play(ShowCreation(algebraic_box))
        self.play(Write(cercle))
        self.play(Write(center_cercle), Write(radius))
        self.play(ShowCreation(label_r))
        self.play(Write(area_circle_formula))
        self.wait(15)
        self.play(ShowCreation(visual_box))
        self.play(Write(square))
        self.play(Write(area_square_formula))
        self.play(ShowCreation(mesure_1), ShowCreation(mesure_2))
        self.play(ShowCreation(label_c))
        self.wait(15)



class cercle_disque(Scene):
    def construct(self):
        # Source: https://github.com/vivek3141/videos/blob/master/maxwell.py
        color_map = {
            r"A": PURPLE,
            r"c": BLUE,
        }

        color_map_2 = {
            r"A": GRAY,
            r"R": YELLOW,
        }

        algebraic_box = BoxedTitle(text="Aire du cercle", width=3.5, height=0.7, scale=0.7, box_color="#D4AF37")
        algebraic_box.move_to(np.array([-3.5, 2.5, 0]))
        visual_box = BoxedTitle(text="Aire du carré", width=3.5, height=0.7, scale=0.7, box_color="#D4AF37")
        visual_box.move_to(np.array([2, 2.5, 0]))

        cercle = Circle(radius=1, fill_opacity=0.5, color=WHITE).next_to(algebraic_box, DOWN, buff=MED_LARGE_BUFF)
        center_cercle = Dot().next_to(cercle, 0)
        radius = Line(start=center_cercle.get_center(), end=center_cercle.get_center() - np.array([0, 1, 0])).set_color(YELLOW)
        area_circle_formula = TexMobject("A=\pi R^{2}", tex_to_color_map=color_map_2).next_to(cercle, DOWN)
        label_r = TexMobject("R").next_to(radius, RIGHT, buff=0.5 * SMALL_BUFF).set_color(YELLOW)

        square = Square(radius=1, fill_opacity=0.5, color=PURPLE).next_to(visual_box, DOWN, buff=MED_LARGE_BUFF)
        area_square_formula = TexMobject("A=c^{2}", tex_to_color_map=color_map).next_to(square, DOWN)

        mesure_1 = Arrow(np.array([0.35,0,0]) + (square.get_corner(DR) + square.get_corner(UR))/2,
                         np.array([0.35,0,0]) + square.get_corner(DR) + np.array([0,-0.25,0]))
        mesure_2 = Arrow(np.array([0.35,0,0]) + (square.get_corner(DR) + square.get_corner(UR))/2,
                         np.array([0.35,0,0]) + square.get_corner(UR) + np.array([0,0.25,0]))
        label_c = TexMobject("c", tex_to_color_map=color_map_2).next_to((square.get_corner(DR) + square.get_corner(UR))/2).set_color(BLUE)

        self.play(ShowCreation(algebraic_box))
        self.play(Write(cercle))
        self.play(Write(center_cercle), Write(radius))
        self.play(ShowCreation(label_r))
        self.play(Write(area_circle_formula))
        self.wait(15)
        self.play(ShowCreation(visual_box))
        self.play(Write(square))
        self.play(Write(area_square_formula))
        self.play(ShowCreation(mesure_1), ShowCreation(mesure_2))
        self.play(ShowCreation(label_c))
        self.wait(15)


class UpdateFunctionWithDt2(Scene):
    def construct(self):
        color_map = {
            r"R": YELLOW
        }

        self.t_offset = 0
        orbit = Circle(color=BLUE).scale(2.5)
        center_circle = Dot().next_to(orbit, 0)
        center_circle_label = TexMobject("(0, 0)").next_to(center_circle, UP)

        planet = Dot()
        planet_label = TexMobject("(x, y)").next_to(planet, DOWN, buff=LARGE_BUFF)
        planet.move_to(orbit.point_from_proportion(0))
        #planet_label.move_to(orbit.point_from_proportion(0))

        def update_planet(mob, dt):
            rate = dt*0.05
            mob.move_to(orbit.point_from_proportion((self.t_offset + rate) % 1))
            self.t_offset += rate

        equation = TexMobject(r"x^{2}+y^{2} = R^{2}", tex_to_color_map=color_map)
        equation.to_corner(UR)

        planet.add_updater(update_planet)
        planet_label.add_updater(update_planet)
        self.play(ShowCreation(equation))
        self.wait(15)
        self.add(orbit, planet, planet_label, center_circle, center_circle_label)
        self.wait(10.5)
        planet.clear_updaters()
        planet_label.clear_updaters()
        self.wait()


class CercleDef(Scene):
    def construct(self):
        color_map = {
            r"R": YELLOW
        }

        circle = Circle(radius=3).set_color(BLUE)
        center_circle = Dot().next_to(circle, 0)
        center_circle_label = TexMobject("(0, 0)").next_to(center_circle, UP)

        base_line = Line(ORIGIN, RIGHT * 3, color=YELLOW)
        side_1 = Line(ORIGIN, RIGHT * 3, color=YELLOW)
        sides = VGroup(side_1)

        def triangle_update(mob):
            side_1 = mob
            new_side_1 = Line(ORIGIN, circle.points[-1], color=YELLOW)
            side_1.become(new_side_1)

        equation = TexMobject(r"x^{2}+y^{2} = R^{2}", tex_to_color_map=color_map)
        equation.to_corner(UR)
        sides.add_updater(triangle_update)
        self.play(ShowCreation(equation, run_time=3))
        self.wait(10)
        self.add(base_line, sides)
        self.play(ShowCreation(center_circle), ShowCreation(center_circle_label))
        self.wait(10)
        self.play(ShowCreation(circle, run_time=3))
        self.wait(20)


class disque(Scene):

    def construct(self):
        # Source: https://github.com/vivek3141/videos/blob/master/maxwell.py
        color_map = {
            r"R": YELLOW
        }

        cercle = Circle(radius=2, fill_opacity=0.5, color=WHITE)
        center_cercle = Dot().next_to(cercle, 0)
        radius = Line(start=center_cercle.get_center(), end=center_cercle.get_center() - np.array([0, 2, 0])).set_color(YELLOW)
        label_r = TexMobject("R").next_to(radius, RIGHT, buff=0.5 * SMALL_BUFF).set_color(YELLOW)
        equation = TexMobject(r"x^{2}+y^{2} \leq R^{2}", tex_to_color_map=color_map)
        equation.to_corner(UR)

        self.play(Write(cercle))
        self.play(Write(center_cercle), Write(radius))
        self.play(ShowCreation(label_r))
        self.play(Write(equation))
        self.wait(15)


class probleme(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Problème", width=3.5, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        square_box = Square(side_length=4, fill_opacity=0.5, color=PURPLE)
        question = TextMobject(r"Quelle est la probabilité de toucher la cible sachant que le tir est \textbf{aléatoire}, entre dans le cadre et que le rayon de la cible est de 0.5 mètre?").scale(0.85)
        question.next_to(square_box, DOWN, buff=MED_LARGE_BUFF)

        # Colors (from exterior to center): WHITE, BLACK, BLUE, RED, YELLOW

        # Center
        #circle_2 = Circle(radius=0.35, fill_opacity=0.95).set_color(YELLOW)
        #circle_1_5 = Circle(radius=0.25, fill_opacity=0).set_color(BLACK)
        #circle_2.next_to(square_box, 0)

        # White cercles
        circle_white_2 = Circle(radius=2, fill_opacity=0.95).set_color(WHITE)
        circle_white_1_5 = Circle(radius=1.8, fill_opacity=0).set_color(BLACK)

        # Black cercles
        circle_black_2 = Circle(radius=1.6, fill_opacity=0.95).set_color(BLACK)
        circle_black_1_5 = Circle(radius=1.4, fill_opacity=0).set_color(WHITE)

        # Blue cercles
        circle_blue_2 = Circle(radius=1.2, fill_opacity=0.95).set_color(BLUE)
        circle_blue_1_5 = Circle(radius=1.0, fill_opacity=0).set_color(BLACK)

        # Red cercles
        circle_red_2 = Circle(radius=0.8, fill_opacity=0.95).set_color("#CE1A19")
        circle_red_1_5 = Circle(radius=0.6, fill_opacity=0).set_color(BLACK)

        # Yellow cercles
        circle_yellow_2 = Circle(radius=0.4, fill_opacity=0.95).set_color(YELLOW)
        circle_yellow_1_5 = Circle(radius=0.2, fill_opacity=0).set_color(BLACK)

        # Arrow
        path = r"C:/Users/Utilisateur/Desktop/CEGEP/Cours_maison/toastersman_videos/presentations/brebeuf/"
        fleche_img_name = "fleche"
        fleche_img = ImageMobject("{}{}.PNG".format(path, fleche_img_name)).scale(1.5).next_to(square_box, RIGHT, buff=MED_LARGE_BUFF)


        #self.play(Write(title))
        self.wait(5)
        self.play(ShowCreation(fleche_img))
        self.play(ShowCreation(square_box))
        self.wait(5)
        self.play(ShowCreation(circle_white_2))
        self.play(ShowCreation(circle_white_1_5))
        self.play(ShowCreation(circle_black_2))
        self.play(ShowCreation(circle_black_1_5))
        self.play(ShowCreation(circle_blue_2))
        self.play(ShowCreation(circle_blue_1_5))
        self.play(ShowCreation(circle_red_2))
        self.play(ShowCreation(circle_red_1_5))
        self.play(ShowCreation(circle_yellow_2))
        self.play(ShowCreation(circle_yellow_1_5))
        self.wait(10)
        self.play(FadeIn(question))
        self.wait(10)
        self.play(FadeOut(question))


class idee_simulation(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        #title = BoxedTitle(text="Simulations de tirs", width=5, height=0.7, scale=0.7)
        #title.move_to(np.array([0, 3.25, 0]))

        color_map = {
            r"s": GREEN,
            r"e": RED
        }

        square_box = Square(side_length=4, fill_opacity=0.5, color=PURPLE)
        circle_white_2 = Circle(radius=2, fill_opacity=0.95).set_color(WHITE)

        statement = TextMobject(r"Simulons $n\in\mathbb{N}$ tirs!")
        statement.next_to(square_box, DOWN, buff=MED_LARGE_BUFF)

        equation = TexMobject("p", "=", r"{\#\text{succès}", "\over", r"\#\text{succès}", r"+", r"\#\text{échecs}}").scale(1)
        equation[2].set_color(GREEN)
        equation[4].set_color(GREEN)
        equation[6].set_color(RED)
        equation.to_corner(UL)

        equation_2 = TexMobject("=", r"{s", "\over", r"s", r"+", r"e}").scale(1)
        equation_2[1].set_color(GREEN)
        equation_2[3].set_color(GREEN)
        equation_2[5].set_color(RED)
        equation_2.next_to(equation, DOWN).align_to(equation[1], LEFT)

        path = r"C:/Users/Utilisateur/Desktop/CEGEP/Brebeuf_presentation/"
        tirs = pd.read_csv(r"{}simulations.csv".format(path))
        tirs_ = tirs.values

        # Arrow
        path = r"C:/Users/Utilisateur/Desktop/CEGEP/Cours_maison/toastersman_videos/presentations/brebeuf/"
        fleche_img_name = "fleche"
        fleche_img = ImageMobject("{}{}.PNG".format(path, fleche_img_name)).scale(1.5).next_to(square_box, RIGHT, buff=MED_LARGE_BUFF)

        self.play(WiggleOutThenIn(fleche_img))
        self.play(ShowCreation(square_box))
        self.play(ShowCreation(circle_white_2))
        self.wait(15)
        self.play(ShowCreation(equation))
        self.play(ShowCreation(equation_2))
        self.wait(25)
        self.play(ShowCreation(statement))

        tirs_colores = []
        number_success, total = 0, 0
        for i, tir in enumerate(tirs_):
            # Display the arrow mark
            color, success = predicate_color(tir[0], tir[1], 0.5)
            x_shift, y_shift = np.array([tir[0] * 4, 0, 0]), np.array([0, tir[1] * 4, 0])
            tir = Dot(radius=0.075).next_to(circle_white_2.get_center() + x_shift + y_shift, 0).set_color(color)
            self.play(ShowCreation(tir), run_time=0.2)

            # Get the proportion and calculate it
            total += 1
            number_success += success
            proportion = round(number_success/total, 2 - int(math.floor(math.log10(abs(number_success / total)))) - 1)
            if i == 0:
                equation_3 = TexMobject("=", "{}".format(proportion)).scale(1)
                equation_3.next_to(equation_2, DOWN).align_to(equation_2, LEFT)
                n_value = TexMobject("n", "=", "{}".format(i + 1)).scale(1)
                n_value.next_to(equation_3, DOWN,  buff=LARGE_BUFF).align_to(equation, LEFT)
                self.play(ShowCreation(equation_3), run_time=0.1)
                self.play(ShowCreation(n_value), run_time=0.1)
            else:
                equation_3 = TexMobject("=", "{}".format(proportion)).scale(1)
                equation_3.next_to(equation_2, DOWN).align_to(equation_2, LEFT)
                n_value = TexMobject("n", "=", "{}".format(i + 1)).scale(1)
                n_value.next_to(equation_3, DOWN, buff=LARGE_BUFF).align_to(equation, LEFT)
                self.play(ReplacementTransform(old_equation_3, equation_3), run_time=0.1)
                self.play(ReplacementTransform(old_n_value, n_value), run_time=0.1)
            old_equation_3 = equation_3
            old_n_value = n_value
            tirs_colores.append(tir)
        self.wait(25)


def predicate_color(x, y, r):
    value = x**2 + y**2
    color = (RED, 0) if value>r**2 else (GREEN, 1)
    return color


class plots(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Analyse de $p$", width=3.5, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        # Plot
        path = r"C:/Users/Utilisateur/Desktop/CEGEP/Brebeuf_presentation/plots/reverse/"
        names = [r"{}_epreuves".format(int(i*1000)) for i in range(1,11)]
        experiment_curve = ImageMobject("{}{}.PNG".format(path, names[0])).scale(2.5)

        p_label = TexMobject("p").next_to(np.array([-3.15, 2.25, 0]))
        n_label = TexMobject("n").next_to(np.array([3, -1.85, 0]))

        # Question
        question = TextMobject(r"Qu'est-ce que vous constatez?").scale(0.85)
        question.next_to(experiment_curve, DOWN, buff=MED_LARGE_BUFF)

        self.play(Write(title))
        self.wait(5)
        for i, name in enumerate(names):
            if i == 0:
                image = ImageMobject("{}{}.PNG".format(path, name)).scale(2.5)
                self.play(ShowCreation(image))
                self.play(ShowCreation(p_label), ShowCreation(n_label))
                old_image = image
                old_p_label, old_n_label = p_label, n_label
            else:
                image = ImageMobject("{}{}.PNG".format(path, name)).scale(2.5)
                p_label = TexMobject("p").next_to(np.array([-3.15, 2.25, 0]))
                n_label = TexMobject("n").next_to(np.array([3, -1.85, 0]))
                self.play(ReplacementTransform(old_image, image))
                self.play(ReplacementTransform(old_p_label, p_label), ReplacementTransform(old_n_label, n_label))
                old_image = image
                old_p_label, old_n_label = p_label, n_label
        self.play(FadeIn(question))
        probability = TexMobject(r"{\pi", "\over", r"4}").next_to(np.array([2.6, -1.3, 0])).set_color(BLUE).scale(0.7)
        self.wait(10)
        self.play(ShowCreation(probability))
        self.wait(15)


class pile_ou_face(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Simulations: pile ou face?", width=5.5, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        statement = TextMobject2(r"Pour $i\in\{1,2,\dots,n_{\star}\}$:").scale(0.9)
        statement.next_to(np.array([-7, 2.5, 0]))

       # etape_0 = TextMobject(r"0) Lancer un dard.").align_to(statement, LEFT)
        etape_1 = TextMobject(r"1) Faire pile ou face.").next_to(statement, DOWN, buff=MED_LARGE_BUFF).align_to(statement, LEFT)
        etape_2 = TextMobject(r"2) Est-ce que le résultat est face?").next_to(etape_1, DOWN).align_to(etape_1, LEFT)
        etape_3 = TextMobject(r"3) Ajuster le nombre de pile ou de face.").next_to(etape_2, DOWN).align_to(etape_2, LEFT)
        etape_4 = TextMobject(r"4) Incrémenter le nombre total ($i\leftarrow i+1$).").next_to(etape_3, DOWN).align_to(etape_3, LEFT)
        etape_5 = TextMobject(r"5) Recommencer à l'étape $1$ (sauf si $i=n_{\star}$).").next_to(etape_4, DOWN).align_to(etape_4, LEFT)

        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement))
        self.wait(15)
        self.play(Write(etape_1))
        self.wait(10)
        self.play(Write(etape_2))
        self.wait(10)
        self.play(Write(etape_3))
        self.wait(10)
        self.play(Write(etape_4))
        self.wait(10)
        self.play(Write(etape_5))
        self.wait(20)


class mathematisation(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Mathématisation", width=4, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))


        statement = TextMobject2(r"Pour $i\in\{1,2,\dots,n_{\star}\}$:").scale(0.9)
        statement.next_to(np.array([-7, 2.5, 0]))

       # etape_0 = TextMobject(r"0) Lancer un dard.").align_to(statement, LEFT)
        etape_1 = TextMobject(r"1) Générer $\mathbf{x}_{i}=(x_{i},y_{i})$ où $x_{i},y_{i}\sim U[-0.5,0.5]$.").next_to(statement, DOWN, buff=LARGE_BUFF).align_to(statement, LEFT)
        etape_2 = TextMobject(r"2) Est-ce que $x_{i}^{2} + y_{i}^{2}\leq R^{2}$?").next_to(etape_1, DOWN).align_to(etape_1, LEFT)
        etape_3 = TextMobject(r"3) ", r"$s\leftarrow s+\mathds{1}_{\{x_{i}^{2} + y_{i}^{2}\leq R^{2}\}}$ et").next_to(etape_2, DOWN).align_to(etape_2, LEFT)
        etape_3_5 = TextMobject(r"$e\leftarrow e + \Big(1-\mathds{1}_{\{x_{i}^{2} + y_{i}^{2}\leq R^{2}\}}\Big)$").next_to(etape_3, DOWN).align_to(etape_3[1], LEFT)
        etape_4 = TextMobject(r"4) $n\leftarrow n+1$.").next_to(etape_3_5, DOWN).align_to(etape_3, LEFT)
        etape_5 = TextMobject(r"5) Recommencer à l'étape $1$ (i.e. $i\leftarrow i+1$) (sauf si $i=n_{\star}$).").next_to(etape_4, DOWN).align_to(etape_4, LEFT)

        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement))
        self.wait(15)
        self.play(Write(etape_1))
        self.wait(10)
        self.play(Write(etape_2))
        self.wait(10)
        self.play(Write(etape_3))
        self.play(Write(etape_3_5))
        self.wait(10)
        self.play(Write(etape_4))
        self.wait(10)
        self.play(Write(etape_5))
        self.wait(20)


class simul_rand_var(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        #title = BoxedTitle(text="Simulations de tirs", width=5, height=0.7, scale=0.7)
        #title.move_to(np.array([0, 3.25, 0]))

        color_map = {
            r"s": GREEN,
            r"e": RED
        }

        square_box = Square(side_length=4, fill_opacity=0.5, color=PURPLE)
        circle_white_2 = Circle(radius=2, fill_opacity=0.95).set_color(WHITE)

        center_point = Dot().next_to(circle_white_2, 0).set_color(BLACK)
        center_label = TexMobject("(0,0)").next_to(center_point, DOWN).set_color(BLACK)

        horizontal_line = Line((square_box.get_corner(DL) + square_box.get_corner(UL))/2,
                               (square_box.get_corner(DR) + square_box.get_corner(UR))/2).set_color(BLUE)

        vertical_line = Line((square_box.get_corner(UR) + square_box.get_corner(UL))/2,
                               (square_box.get_corner(DR) + square_box.get_corner(DL))/2).set_color(ORANGE)

        # Right side measure
        mesure_1 = Arrow(np.array([0.35, 0, 0]) + (square_box.get_corner(DR) + square_box.get_corner(UR)) / 2,
                         np.array([0.35, 0, 0]) + square_box.get_corner(DR) + np.array([0, -0.25, 0]))
        mesure_2 = Arrow(np.array([0.35, 0, 0]) + (square_box.get_corner(DR) + square_box.get_corner(UR)) / 2,
                         np.array([0.35, 0, 0]) + square_box.get_corner(UR) + np.array([0, 0.25, 0]))
        label_right_side = TexMobject("1").next_to((square_box.get_corner(DR) + square_box.get_corner(UR)) / 2)

        # Top measure
        mesure_3 = Arrow(np.array([0, 0.35, 0]) + (square_box.get_corner(UR) + square_box.get_corner(UL)) / 2,
                         square_box.get_corner(UR) + np.array([0.25, 0.35, 0]))
        mesure_4 = Arrow(np.array([0, 0.35, 0]) + (square_box.get_corner(UR) + square_box.get_corner(UL)) / 2,
                         square_box.get_corner(UL) + np.array([-0.25, 0.35, 0]))
        label_top_side = TexMobject("1").next_to(mesure_3.get_start() + np.array([-0.6, 0, 0]))

        path = r"C:/Users/Utilisateur/Desktop/CEGEP/Brebeuf_presentation/"
        tirs = pd.read_csv(r"{}simulations.csv".format(path))
        tirs_ = tirs.values

        # Generer la composante horizontale
        random_x = TexMobject(r"\bullet x_{i}\sim U[-0.5,0.5]").set_color(BLUE)
        random_x.next_to(mesure_4, LEFT, buff=1*LARGE_BUFF)
        random_x_value = Dot().next_to(center_point.get_center() + np.array([4*tirs_[0, 0], 0, 0])).set_color(GREEN)

        # Generer la composante verticale
        random_y = TexMobject(r"\bullet y_{i}\sim U[-0.5,0.5]").set_color(ORANGE)
        random_y.next_to(random_x, DOWN)
        random_y_value = Dot().next_to(center_point.get_center() + np.array([-0.325, 4*tirs_[0, 1], 0])).set_color(RED)

        #print("Red dot position: {}".format(center_point.get_center() + np.array([0, tirs_[0, 1], 0])))

        label = TextMobject("Considérons le $i$-ième lancer :").next_to(random_x, UP, buff=0.75*LARGE_BUFF).align_to(random_x, LEFT)
        label_ctd = TextMobject("On obtient :").next_to(random_y, DOWN, buff=0.75 * LARGE_BUFF).align_to(random_y, LEFT)

        random_x_value_label = TexMobject(r"x_{i}=0.049").set_color(GREEN).next_to(label_ctd, DOWN, buff=MED_LARGE_BUFF).align_to(label_ctd, LEFT)
        random_y_value_label = TexMobject(r"y_{i}=0.271").set_color(RED).next_to(random_x_value_label, DOWN).align_to(random_x_value_label, LEFT)
        random_xy_value_label = TexMobject(r"(x_{i},y_{i})=(0.049,0.271)").set_color(GRAY).next_to(square_box, DOWN, buff=LARGE_BUFF)

        boxed_answer = SurroundingRectangle(random_xy_value_label).set_color(YELLOW)

        # Create dashed lines.
        new_point = Dot().next_to(random_y_value, RIGHT).align_to(random_x_value, LEFT).set_color(GRAY)
        dashed_line_1 = DashedLine(random_y_value.get_center(), new_point.get_center()).set_color(BLACK)
        dashed_line_2 = DashedLine(random_x_value.get_center(), new_point.get_center()).set_color(BLACK)

        self.play(ShowCreation(square_box))
        self.play(ShowCreation(mesure_1), ShowCreation(mesure_2), ShowCreation(label_right_side))
        self.play(ShowCreation(mesure_3), ShowCreation(mesure_4), ShowCreation(label_top_side))
        self.play(ShowCreation(circle_white_2))
        self.play(ShowCreation(center_point), ShowCreation(center_label))
        self.wait(15)
        self.play(ShowCreation(label))
        self.wait(10)
        self.play(ShowCreation(random_x))
        self.wait(10)
        self.play(ShowCreation(horizontal_line))
        self.wait(10)
        self.play(ShowCreation(label_ctd))
        self.wait(5)
        self.play(ShowCreation(random_x_value_label))
        self.wait(5)
        self.play(ShowCreation(random_x_value))
        self.wait(15)
        self.play(ShowCreation(random_y))
        self.wait(10)
        self.play(ShowCreation(vertical_line))
        self.wait(10)
        self.play(ShowCreation(random_y_value_label))
        self.wait(5)
        self.play(ShowCreation(random_y_value))
        self.wait(10)
        self.play(ShowCreation(dashed_line_1), ShowCreation(dashed_line_2))
        self.play(ShowCreation(new_point))
        self.play(ShowCreation(random_xy_value_label))
        self.wait(5)
        self.play(WiggleOutThenIn(boxed_answer))
        self.wait(20)


class point_disque(Scene):

    def construct(self):
        # Source: https://github.com/vivek3141/videos/blob/master/maxwell.py
        color_map = {
            r"1": YELLOW
        }
        random_xy_value_label = TexMobject(r"(x_{i},y_{i})=(0.049,0.271)").set_color(GRAY).to_corner(UL)
        cercle = Circle(radius=2, fill_opacity=1, color=WHITE)
        center_cercle = Dot().next_to(cercle, 0).set_color(BLACK)
        random_dot = Dot().next_to(center_cercle, 0.3*RIGHT + 1.8*UP).set_color(GRAY)
        center_cercle_label = TexMobject(r"(0,0)").set_color(BLACK).next_to(center_cercle, DOWN)
        radius = Line(start=center_cercle.get_center(), end=center_cercle.get_center() + np.array([0, 2, 0])).set_color(YELLOW)
        label_r = TexMobject("1").next_to(radius, LEFT, buff=0.5 * SMALL_BUFF).set_color(YELLOW)
        equation = TexMobject(r"x^{2}+y^{2} \leq 1^{2}", tex_to_color_map=color_map)
        equation.to_corner(UR)

        equation_2 = TexMobject(r"0.049^{2}+0.271^{2}= 0.073441\leq 1^{2}")
        equation_2.next_to(random_xy_value_label, DOWN).align_to(random_xy_value_label, LEFT)
        checkmark = TexMobject("\\checkmark").next_to(equation_2).set_color(GREEN)

        self.play(Write(cercle))
        self.play(Write(center_cercle), Write(radius), Write(center_cercle_label))
        self.play(ShowCreation(label_r))
        self.play(ShowCreation(random_dot))
        self.play(Write(equation))
        self.wait(10)
        self.play(ShowCreation(random_xy_value_label))
        self.wait(10)
        self.play(ShowCreation(equation_2))
        self.wait(7)
        self.play(ShowCreation(checkmark))
        self.wait(15)


class mise_a_jour(Scene):

    def construct(self):
        # Source: https://github.com/vivek3141/videos/blob/master/maxwell.py

        title = BoxedTitle(text="Mise à jour des paramètres", width=6, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        #system0 = TexMobject(r"""S(\mathbf{x})=\systeme{1\text{ si }\quad x^{2}+y^{2}<R^{2}, 0\quad\text{ sinon}}""")
        #system0.move_to(np.array([-1, 2, 0]))
        #system0 = TexMobject(r"""S(\mathbf{x})=\systeme{1, 0}""")
        system0 = TexMobject(r"S(x,y)", r"=" r"""\systeme{1, 0}""")
        detail_1 = TextMobject(r" si $x^{2}+y^{2}<R^{2}$").next_to(np.array([1.33, 0.4, 0]))
        detail_2 = TextMobject(r" sinon").next_to(np.array([1.35, -0.3, 0]))

        system1 = TexMobject(r"=", r"\mathds{1}_{\{x^{2} + y^{2}< R^{2}\}}").next_to(system0, DOWN).\
            align_to(system0[1], LEFT)

        etape_3 = TexMobject(r"\bullet ", r"s", r"\leftarrow", r"s", r"+", r"\mathds{1}_{\{x_{i}^{2} + y_{i}^{2}< R^{2}\}}\text{ et}")
        etape_3[1].set_color(GREEN)
        etape_3[3].set_color(GREEN)
        etape_3_5 = TexMobject(r"e", r"\leftarrow", r"e", r"+", r"\Big(1-\mathds{1}_{\{x_{i}^{2} + y_{i}^{2}< R^{2}\}}\Big)").\
            next_to(etape_3, DOWN).align_to(etape_3[1], LEFT)
        etape_3_5[0].set_color(RED)
        etape_3_5[2].set_color(RED)
        etape_4 = TextMobject(r"$\bullet n\leftarrow n+1$.").next_to(etape_3_5, DOWN).align_to(etape_3, LEFT)

        self.play(Write(title))
        self.play(ShowCreation(system0), ShowCreation(detail_1),  ShowCreation(detail_2))
        self.play(ShowCreation(system1))
        self.wait(15)
        self.play(FadeOut(system0), FadeOut(detail_1),FadeOut(detail_2))
        self.play(FadeOut(system1))
        self.wait(5)
        self.play(ShowCreation(etape_3))
        self.wait(5)
        self.play(ShowCreation(etape_3_5))
        self.wait(5)
        self.play(ShowCreation(etape_4))
        self.wait(15)



class algorithme(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Modélisation", width=3.5, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        statement = TextMobject2(r"Pour $n\in\{1,2,\dots,n_{\star}\}$:").scale(0.9)
        statement.next_to(np.array([-7, 2.5, 0]))

       # etape_0 = TextMobject(r"0) Lancer un dard.").align_to(statement, LEFT)
        etape_1 = TextMobject(r"1) Lancer un dard.").next_to(statement, DOWN, buff=MED_LARGE_BUFF).align_to(statement, LEFT)
        etape_2 = TextMobject(r"2) Est-ce qu'il a atteint la cible?").next_to(etape_1, DOWN).align_to(etape_1, LEFT)
        etape_3 = TextMobject(r"3) Ajuster le nombre de succès.").next_to(etape_2, DOWN).align_to(etape_2, LEFT)
        etape_4 = TextMobject(r"4) Incrémenter le nombre d'épreuves ($n\leftarrow n+1$).").next_to(etape_3, DOWN).align_to(etape_3, LEFT)
        etape_5 = TextMobject(r"5) Recommencer à l'étape $1$ (sauf si $n=n_{\star}$).").next_to(etape_4, DOWN).align_to(etape_4, LEFT)

        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement))
        self.wait(15)
        self.play(Write(etape_1))
        self.wait(10)
        self.play(Write(etape_2))
        self.wait(10)
        self.play(Write(etape_3))
        self.wait(10)
        self.play(Write(etape_4))
        self.wait(10)
        self.play(Write(etape_5))
        self.wait(20)




class WriteCode(Scene):
    def construct(self):

        line1 = TextMobject("$>>>$ array = [ ]")
        line1.shift(LEFT * 3.5 + UP * 3.1)
        line1[:3].set_color(RED_A)

        line2 = TextMobject("$>>>$ for i in range(1, 6):")
        line2[:3].set_color(RED_A)
        line2[3:6].set_color(RED_E)
        line2[7:9].set_color(RED_E)
        line2[9:14].set_color(BLUE)
        line2.next_to(line1, DOWN).align_to(line1, LEFT)

        line3 = TextMobject("array.append(i)")
        line3[6:12].set_color(BLUE)
        line3.next_to(LEFT * 3.5 + UP * 1.7)

        # line3.shift(LEFT * 2.6 + UP * 2.3)
        #line3.shift(LEFT * 1.7 + UP * 1.6) # OLD

        line4 = TextMobject("$>>>$ array")
        line4[:3].set_color(RED_A)
        line4.next_to(line2[:len(line4)], DOWN * 3.5)
        line4.align_to(line2, LEFT)

        line5 = TextMobject("[1, 2, 3, 4, 5]")
        for i in range(1, len(line5), 2):
            line5[i].set_color(PURPLE_A)
        line5.move_to(UP * 0.25 + LEFT * 4)

        write_runtime = 1.5
        self.play(Write(line1, run_time=write_runtime))
        self.wait(10)
        self.play(Write(line2, run_time=write_runtime))
        self.wait(10)
        self.play(Write(line3, run_time=write_runtime))
        self.wait(10)
        self.play(Write(line4), run_time=write_runtime)
        self.wait(5)
        self.play(FadeIn(line5, run_time=0.5))

        prev_code_arrow = Arrow(RIGHT * 0.5 + UP * 3, 1.5 * LEFT + UP * 3)
        prev_code_arrow.set_color(GREEN)

        diagram = TextMobject("array")
        diagram.move_to(DOWN * 3 + LEFT * 5)
        line_draw1 = Line(DOWN * 1, DOWN * 1.5)
        line_draw1.next_to(diagram, RIGHT)
        line_draw2 = Line(line_draw1.get_end(), line_draw1.get_end() + RIGHT * 0.5)

        line_draw1_center = (line_draw1.get_start() + line_draw1.get_end()) / 2
        arrow_start = line_draw1_center
        diagram_arrow = Arrow(arrow_start, arrow_start + RIGHT * 2)

        diagram_runtime = 0.5

        self.play(ShowCreation(prev_code_arrow))
        self.play(FadeIn(diagram), FadeIn(line_draw1), FadeIn(line_draw2),
                  Write(diagram_arrow), run_time=diagram_runtime)

        line2_position_start, line2_position_end = RIGHT * 2.1 + UP * 2.3, RIGHT * 0.1 + UP * 2.3
        new_code_arrow = Arrow(line2_position_start, line2_position_end)
        new_code_arrow.set_color(GREEN)
        self.play(ReplacementTransform(prev_code_arrow, new_code_arrow), run_time=diagram_runtime)

        prev_code_arrow = new_code_arrow
        line3_position_start, line3_position_end = RIGHT * 2 + UP * 1.6, RIGHT * 0 + UP * 1.6
        new_code_arrow = Arrow(line3_position_start, line3_position_end)
        new_code_arrow.set_color(GREEN)
        self.play(ReplacementTransform(prev_code_arrow, new_code_arrow), run_time=diagram_runtime)
        prev_code_arrow = new_code_arrow

        line4_position_start, line4_position_end = LEFT * 0.9 + UP * 1.05, LEFT * 2.9 + UP * 1.05

        array = create_array(5, BLUE, diagram_arrow.get_end() + RIGHT, 1, 1.5)
        array_text = generate_chars_in_array(array, '1', PURPLE_A)
        for i in range(len(array)):
            new_code_arrow = Arrow(line2_position_start, line2_position_end)
            new_code_arrow.set_color(GREEN)
            self.play(GrowFromCenter(array[i]), FadeIn(array_text[i]),
                      ReplacementTransform(prev_code_arrow, new_code_arrow), run_time=diagram_runtime)
            prev_code_arrow = new_code_arrow
            if i == len(array) - 1:
                new_code_arrow = Arrow(line4_position_start, line4_position_end)
                new_code_arrow.set_color(GREEN)
                self.play(ReplacementTransform(prev_code_arrow, new_code_arrow), run_time=diagram_runtime)
            else:
                new_code_arrow = Arrow(line3_position_start, line3_position_end)
                new_code_arrow.set_color(GREEN)
                self.play(ReplacementTransform(prev_code_arrow, new_code_arrow), run_time=diagram_runtime)
            prev_code_arrow = new_code_arrow

        line6 = TextMobject("$>>>$ array[3]")
        line6.move_to(DOWN * 0.5 + LEFT * 3.8)
        line6[:3].set_color(RED_A)
        #line6[-2].set_color(PURPLE_A)
        self.play(Write(line6))

        line6_position_start, line6_position_end = DOWN * 0.5 + LEFT * 0.4, DOWN * 0.5 + LEFT * 2.4
        new_code_arrow = Arrow(line6_position_start, line6_position_end)
        new_code_arrow.set_color(GREEN)
        self.play(ReplacementTransform(prev_code_arrow, new_code_arrow))
        self.play(Indicate(array_text[3]), run_time=2)
        text_copy_4 = array_text[3].copy()
        text_copy_4.move_to(DOWN * 1 + LEFT * 5.2)
        self.play(TransformFromCopy(array_text[3], text_copy_4))

        text_copy_5 = array_text[4].copy()
        text_copy_5.move_to(DOWN * 1.8 + LEFT * 5.25)
        #self.play(FadeOut(array[4]))
        #self.play(ReplacementTransform(array_text[4], text_copy_5))
        self.wait(8.5)

        array_copy = create_array(4, BLUE, LEFT * 5, 1, 1.5)
        array_text_copy = generate_chars_in_array(array_copy, '1', PURPLE_A)
        old_and_new = zip(array[:5] + array_text, array_copy + array_text_copy)
        #array_anims = [ReplacementTransform(arr, arr_copy) for arr, arr_copy in old_and_new]
        #all_animations = [FadeOut(line1),
        #                  FadeOut(line2),
        #                  FadeOut(line3), FadeOut(line4),
        #                  FadeOut(line5), FadeOut(line6),
        #                  #FadeOut(line7),
        #                  FadeOut(diagram_arrow),
        #                  FadeOut(text_copy_4), FadeOut(text_copy_5),
        #                  FadeOut(diagram), FadeOut(line_draw1),
        #                  FadeOut(line_draw2), FadeOut(new_code_arrow)] + array_anims

        #self.play(*all_animations, run_time=3)
        self.wait(5)

        #pointer = Arrow(LEFT * 2.8 + UP * 2, LEFT * 2.8 + UP * 0.5)
        #declaration = TextMobject("Array")
        #declaration.move_to(LEFT * 2.8 + UP * 2)
        #self.play(FadeIn(pointer), Write(declaration))
        self.wait()


def create_computer_char(color=BLUE, scale=1, position=ORIGIN):
    outer_rectangle = Rectangle(height=2, width=3,
                                fill_color=color, fill_opacity=1, color=color)
    inner_rectangle = Rectangle(height=1.6, width=2.5,
                                fill_color=DARK_GRAY, fill_opacity=1, color=DARK_GRAY)
    extension = Rectangle(height=0.2, width=0.4,
                          fill_color=color, fill_opacity=1, color=color)
    extension.move_to(DOWN * (outer_rectangle.get_height() / 2 + extension.get_height() / 2))
    base = Rectangle(height=0.2, width=1,
                     fill_color=color, fill_opacity=1, color=color)
    base.move_to(extension.get_center() + DOWN * extension.get_height())

    computer = VGroup(outer_rectangle, extension, base)

    left_circle = Circle(radius=0.27, color=color)
    left_circle.shift(LEFT * 0.6 + UP * 0.3)
    inner_left = Circle(radius=0.08, color=color, fill_color=color, fill_opacity=1)
    inner_left.shift(LEFT * 0.52, UP * 0.22)

    right_circle = Circle(radius=0.27, color=color)
    inner_right = Circle(radius=0.08, color=color, fill_color=color, fill_opacity=1)
    inner_right.shift(RIGHT * 0.52, UP * 0.22)
    right_circle.shift(RIGHT * 0.6 + UP * 0.3)

    left_line = Line(DOWN * 0.3, DOWN * 0.5)
    right_line = Line(DOWN * 0.3, DOWN * 0.5)
    left_line.shift(LEFT * 0.5)
    right_line.shift(RIGHT * 0.5)
    bottom_line = Line(left_line.get_end(), right_line.get_end())
    left_line.set_color(color)
    right_line.set_color(color)
    bottom_line.set_color(color)

    smile = ArcBetweenPoints(left_line.get_start(), right_line.get_start())
    smile.set_color(color)

    left_eye_brow = ArcBetweenPoints(LEFT * 0.8 + UP * 0.6, LEFT * 0.4 + UP * 0.6, angle=-TAU / 4)
    left_eye_brow.set_color(color)
    right_eye_brow = left_eye_brow.copy()
    right_eye_brow.shift(RIGHT * 1.2)
    right_eye_brow.set_color(color)

    eyes_and_smile = VGroup(left_circle, inner_left, right_circle, inner_right,
                            smile, left_eye_brow, right_eye_brow)

    character = VGroup(computer, inner_rectangle, eyes_and_smile)
    character.scale(scale)
    character.move_to(position)
    return character


def create_array(num_rectangles, color, start_pos, height, width):
    initial_array = [Rectangle(height=height, width=width) for _ in range(num_rectangles)]
    for rect in initial_array:
        rect.set_color(color)
    initial_array[0].move_to(start_pos)
    for i in range(1, len(initial_array)):
        initial_array[i].next_to(initial_array[i - 1], RIGHT, buff=0)
    return initial_array


def generate_chars_in_array(array, start_char, color, scale=1):
    text_objects = []
    for rect in array:
        text = TextMobject(start_char)
        text.set_color(color)
        text.scale(scale)
        text.move_to(rect.get_center())
        text_objects.append(text)
        start_char = chr(ord(start_char) + 1)
    return text_objects


def create_confused_char(color=BLUE, scale=1, position=ORIGIN):
    outer_rectangle = Rectangle(height=2, width=3,
                                fill_color=color, fill_opacity=1, color=color)
    inner_rectangle = Rectangle(height=1.6, width=2.5,
                                fill_color=DARK_GRAY, fill_opacity=1, color=DARK_GRAY)
    extension = Rectangle(height=0.2, width=0.4,
                          fill_color=color, fill_opacity=1, color=color)
    extension.move_to(DOWN * (outer_rectangle.get_height() / 2 + extension.get_height() / 2))
    base = Rectangle(height=0.2, width=1,
                     fill_color=color, fill_opacity=1, color=color)
    base.move_to(extension.get_center() + DOWN * extension.get_height())

    computer = VGroup(outer_rectangle, extension, base)

    left_circle = Circle(radius=0.27, color=color)
    left_circle.shift(LEFT * 0.6 + UP * 0.3)
    inner_left = Circle(radius=0.08, color=color, fill_color=color, fill_opacity=1)
    inner_left.shift(LEFT * 0.52, UP * 0.22)

    right_circle = Circle(radius=0.27, color=color)
    inner_right = Circle(radius=0.08, color=color, fill_color=color, fill_opacity=1)
    inner_right.shift(RIGHT * 0.52, UP * 0.22)
    right_circle.shift(RIGHT * 0.6 + UP * 0.3)

    left_line = Line(DOWN * 0.3, DOWN * 0.5)
    right_line = Line(DOWN * 0.3, DOWN * 0.5)
    left_line.shift(LEFT * 0.5)
    right_line.shift(RIGHT * 0.5)
    bottom_line = Line(left_line.get_end(), right_line.get_end())
    left_line.set_color(color)
    right_line.set_color(color)
    bottom_line.set_color(color)

    smile = ArcBetweenPoints(left_line.get_start() + DOWN * 0.2, right_line.get_start(), angle=-TAU / 4)
    smile.set_color(color)

    left_eye_brow = ArcBetweenPoints(LEFT * 0.8 + UP * 0.7, LEFT * 0.4 + UP * 0.7, angle=-TAU / 4)
    left_eye_brow.set_color(color)
    right_eye_brow = ArcBetweenPoints(RIGHT * 0.8 + UP * 0.72, RIGHT * 0.4 + UP * 0.72, angle=-TAU / 4)

    right_eye_brow.set_color(color)

    eyes_and_smile = VGroup(left_circle, inner_left, right_circle, inner_right,
                            smile, left_eye_brow, right_eye_brow)

    character = VGroup(computer, inner_rectangle, eyes_and_smile)
    character.scale(scale)
    character.move_to(position)

    return character




class TitleBox(Scene):
    def construct(self):
        Title = BoxedTitle(text="Description", width=5, height=1, box_color="#D4AF37")
        Title.move_to(np.array([0, 3.25, 0]))

        channel_logo_1 = GenChannelLogo()
        channel_logo_1.next_to(np.array([-7, 3.25, 0]))

        channel_logo_2 = GenChannelLogo(image_name="mirror_very_light_phoenix")
        channel_logo_2.next_to(np.array([5, 3.25, 0]))

        # Displaying everything
        self.play(FadeIn(Title))
        self.play(FadeIn(channel_logo_1), FadeIn(channel_logo_2))
        self.wait(5)

