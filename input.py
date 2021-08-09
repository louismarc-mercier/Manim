from manimlib.imports import *
from manim_utils.slide_template import BoxedTitle, GenChannelLogo, YoutubeLogo
from MyAnim.RevisionSecondaire.id_rem_french import MeasureDistance
import pandas as pd
import numpy as np


class intro(Scene):
    def construct(self):

        # Channel logo and name (UP LEFT CORNER)
        path = r"C:/Users/Utilisateur/Desktop/CEGEP/Cours_maison/"
        path_2 = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/videos/logoCTM/images/"
        image = ImageMobject(path_2 + "CTM_boite")
        image.scale(1.4)

        # Title and subtitle of the trailer (UP RIGHT CORNER)
        trailer_title = TextMobject("Code tes maths").set_color("#0079C2")

        trailer_title.next_to(np.array([-5.5,3.25,0]))
        trailer_title.scale(1.75)

        trailer_subtitle = TextMobject(r"\sc{\textbf{Notions de base - Fonction de saisie}}")
        trailer_subtitle.set_color(WHITE)
        trailer_subtitle.next_to(trailer_title, DOWN, buff=0.2*LARGE_BUFF).align_to(trailer_title, LEFT)
        trailer_subtitle.scale(1)
        image.next_to(trailer_subtitle.get_center() + np.array([-5,-2,0]))

        # Trailer subtitle
        left_rectangle = Rectangle(width=0.035, height=2, fill_opacity=1, color=PINK)
        left_rectangle.to_corner(DL)

        video_description = TextMobject(r"\sc{\textbf{Collège Maisonneuve}}").set_color(WHITE)
        departement = TextMobject(r"\sc{\textbf{Département de mathématiques}}").set_color(WHITE).scale(0.7)
        noms = TextMobject("Rosalie Bentz-Moffet, Melisande Fortin-Boisvert, Stéphanie Larocque et").scale(0.7)
        noms_suite = TextMobject("Louis-Marc Mercier").scale(0.7)
        video_description.next_to(left_rectangle.get_corner(UR) + np.array([0.05,-0.15,0]))
        departement.next_to(video_description, DOWN).align_to(video_description, LEFT)
        noms.next_to(departement, DOWN).align_to(departement, LEFT)
        noms_suite.next_to(noms, DOWN).align_to(noms, LEFT)
        video_description.scale(1)

        # Displaying everything
        self.play(FadeIn(trailer_title), FadeIn(trailer_subtitle))
        self.play(FadeIn(image))
        self.play(FadeIn(left_rectangle), FadeIn(video_description), FadeIn(departement), FadeIn(noms), FadeIn(noms_suite))
        self.wait(5)


class MES(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        # Get images
        path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/images/Euclide/"
        euclide_img = ImageMobject(path + "perfect_euclide").scale(2)
        what_guy = ImageMobject(path + "What_meme_miroir").scale(2)

        # Channel logo and name (UP LEFT CORNER)
        logo_path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/videos/logoCTM/images/"
        image = ImageMobject(logo_path + "CTM_boite")
        image.scale(0.7).to_corner(UL)

        # Quotes
        line_euclide = TextMobject(r"\sc{Comment est-ce qu'on peut interagir}", r"\sc{avec un utilisateur?}").scale(0.7).set_color([PINK])
        line_euclide[0].next_to(3 * UP + 1 * LEFT)
        line_euclide[1].next_to(line_euclide[0], DOWN)
        # line_e[1].next_to(2 * UP + 7 * LEFT)

        # Bubbles
        # Euclide
        right_rectangle = Rectangle(width=7, height=1.5, fill_opacity=0, color=PURPLE)
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

        # Place images
        euclide_img.next_to(np.array([3,-1,0]))
        euclide_name_tag = TextMobject(r"\sc{MOI}").scale(0.75).next_to(euclide_img, DOWN).set_color(PINK)


        self.play(FadeIn(image))
        self.play(FadeIn(euclide_img))
        self.play(Write(euclide_name_tag))
        self.wait(3)
        self.play(Write(line_euclide))
        self.play(ShowCreation(right_rectangle), ShowCreation(right_triangle))
        self.play(ShowCreation(right_black_line))
        self.wait(10)

        solution = TextMobject("La solution est d'utiliser la fonction de saisie de Python.").next_to(image, DOWN, buff=2*LARGE_BUFF).scale(0.7)
        solution.align_to(image, LEFT)
        self.play(Write(solution))
        self.wait(5)


class mandatVideo(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Mandat", width=3, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        # Channel logo and name (UP LEFT CORNER)
        logo_path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/videos/logoCTM/images/"
        image = ImageMobject(logo_path + "CTM_boite")
        image.scale(0.7).to_corner(DR)

        statement_1 = TextMobject2(r" - Être en mesure d'utiliser la fonction de saisie de Python.").scale(0.7)
        statement_1.next_to(np.array([-6,1.5,0]))

        statement_2 = TextMobject2(r" - Sous certaines conditions, être en mesure de changer le type d'une variable.").scale(0.7)
        statement_2.next_to(statement_1, DOWN, buff=LARGE_BUFF).align_to(statement_1, LEFT)

        self.play(FadeIn(image))
        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement_1))
        self.wait(3)
        self.play(Write(statement_2))
        self.wait(5)


class introInput(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Fonction de saisie", width=5, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        # Channel logo and name (UP LEFT CORNER)
        logo_path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/videos/logoCTM/images/"
        image = ImageMobject(logo_path + "CTM_boite")
        image.scale(0.7).to_corner(DR)

        statement = TextMobject2(r"La fonction de saisie (i.e. \textit{input} en anglais) permet de saisir une entrée de l'utilisateur sous la forme d'une chaîne de caractères.").scale(0.7)
        statement.next_to(title, DOWN, buff=LARGE_BUFF)

        exemples_titre = TextMobject2(r"\underline{Exemple}:").scale(0.85).next_to(statement, DOWN, buff=LARGE_BUFF).align_to(statement, LEFT).set_color(BLUE)

        exemple_1 = TextMobject(">>", " prenom = input('Quel est ton prénom?') ").next_to(exemples_titre, DOWN, buff=0.5*LARGE_BUFF).align_to(exemples_titre, LEFT)
        exemple_1[0].set_color(PURPLE)

        self.play(FadeIn(image))
        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement))
        self.wait(5)
        self.play(Write(exemples_titre))
        self.wait(5)
        self.play(Write(exemple_1))
        self.wait(10)


class variableType(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Variable - conversion du type", width=7, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        # Channel logo and name (UP LEFT CORNER)
        logo_path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/videos/logoCTM/images/"
        table_path = r"C:/Users/Utilisateur/Desktop/CEGEP/Maisonneuve-Ete2021/CodeTesMaths/videos/input/"
        image = ImageMobject(logo_path + "CTM_boite")
        image.scale(0.7).to_corner(DR)

        statement = TextMobject2(r"Une variable a un type (e.g. chaîne de caractère, entier, nombre, etc.). "
                                 r"Sous certaines conditions, on peut convertir d'un type à un autre à l'aide de certaines fonctions.").scale(0.7)
        statement.next_to(title, DOWN, buff=LARGE_BUFF)

        table_image = ImageMobject(table_path + "tab_inverser").next_to(np.array([-5,-1,0])).scale(1.25)

        self.play(FadeIn(image))
        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement))
        self.wait(10)
        self.play(FadeIn(table_image))
        self.wait(43)