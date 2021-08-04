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

        trailer_subtitle = TextMobject(r"\sc{\textbf{Notions de base - Assignation de variables}}")
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
        line_euclide = TextMobject(r"\sc{Comment éviter de réércrire du}", r"\sc{code inutilement?}").scale(0.7).set_color([PINK])
        line_euclide[0].next_to(3 * UP + 0 * RIGHT)
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

        solution = TextMobject("La solution est d'utiliser des variables.").next_to(euclide_img, LEFT, buff=1.5*LARGE_BUFF)
        self.play(FadeIn(solution))
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

        statement_1 = TextMobject2(r" - Être en mesure de déclarer des variables de différents types (e.g. chaîne de caractères, nombre, etc.).").scale(0.7)
        statement_1.next_to(title, DOWN, buff=LARGE_BUFF)

        self.play(FadeIn(image))
        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement_1))
        self.wait(5)


class introVariable(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Les variables", width=4, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        # Channel logo and name (UP LEFT CORNER)
        logo_path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/videos/logoCTM/images/"
        image = ImageMobject(logo_path + "CTM_boite")
        image.scale(0.7).to_corner(DR)

        # Définition
        statement = TextMobject2(r"Les variables sont des conteneurs pour stocker des valeurs de données.").scale(0.7)
        statement.next_to(title, DOWN, buff=LARGE_BUFF)

        # Exemple
        exemples_titre = TextMobject2(r"\underline{Exemple}:").scale(0.85).next_to(statement, DOWN, buff=LARGE_BUFF).align_to(statement, LEFT)
        exemple_1 = TextMobject(">>", " a", " = " , "5").next_to(exemples_titre, DOWN, buff=0.5*LARGE_BUFF).align_to(exemples_titre, LEFT)
        exemple_1[0].set_color(PURPLE)
        exemple_1[1].set_color(PINK)
        exemple_1[3].set_color(BLUE)

        exemple_2 = TextMobject('>>', ' print(', "a", ")").next_to(exemple_1, DOWN, buff=0.25 * LARGE_BUFF).align_to(exemple_1, LEFT)
        exemple_2[0].set_color(PURPLE)
        exemple_2[2].set_color(PINK)
        exemple_2_result = TextMobject('5 ').next_to(exemple_2, DOWN, buff=0.25 * LARGE_BUFF).align_to(exemple_2, LEFT).set_color(BLUE)

        # Mémoire
        memory_box = Rectangle(width=1, height=1, fill_opacity=0, color=WHITE)
        memory_box.next_to(exemple_1, RIGHT, buff=5*LARGE_BUFF)
        title_memory_box = TextMobject("a").next_to(memory_box, UP).set_color(PINK).scale(0.9)
        value_memory_box = TextMobject("5").next_to(memory_box, 0).set_color(BLUE).scale(0.9)
        memory_cell_title = TextMobject("cellules de mémoire").next_to(memory_box, DOWN, buff=MED_SMALL_BUFF).scale(0.7)

        memory_box_2 = Rectangle(width=1, height=1, fill_opacity=0, color=WHITE).next_to(memory_box, LEFT, buff=0.05)
        memory_box_3 = Rectangle(width=1, height=1, fill_opacity=0, color=WHITE).next_to(memory_box, RIGHT, buff=0.05)

        self.play(FadeIn(image))
        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement))
        self.wait(7)
        self.play(Write(exemples_titre))
        self.play(FadeIn(memory_box), FadeIn(memory_box_2), FadeIn(memory_box_3))
        self.play(FadeIn(memory_cell_title))
        self.wait(7)
        self.play(Write(exemple_1))
        self.play(WiggleOutThenIn(title_memory_box), WiggleOutThenIn(value_memory_box))
        self.wait(7)
        self.play(Write(exemple_2))
        self.wait(4)
        self.play(WiggleOutThenIn(exemple_2_result))
        self.wait(10)


class reglesNomVariable(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Noms de variables - Partie 1", width=6.5, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        # Channel logo and name (UP LEFT CORNER)
        logo_path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/videos/logoCTM/images/"
        image = ImageMobject(logo_path + "CTM_boite")
        image.scale(0.7).to_corner(DR)

        statement = TextMobject2(r"Pour simplifier les choses, voici une liste de caractéristiques valides pour un nom de variable:").scale(0.7)
        statement.next_to(title, DOWN, buff=LARGE_BUFF)

        # Règles
        regle_1 = TextMobject2(r"- Elle peut contenir des chiffres (i.e. 0, 1, ..., 9) sauf en première position.").scale(0.7).set_color(GREEN)
        regle_1.next_to(statement, DOWN, buff=LARGE_BUFF).align_to(statement, LEFT)

        regle_2 = TextMobject2(r"- Elle peut contenir des lettres minuscules (i.e. a, b, ..., z).").scale(0.7).set_color(GREEN)
        regle_2.next_to(regle_1, DOWN, buff=MED_LARGE_BUFF).align_to(regle_1, LEFT)

        regle_3 = TextMobject2(r"- Elle peut contenir des lettres majuscules (i.e. A, B, ..., Z).").scale(0.7).set_color(GREEN)
        regle_3.next_to(regle_2, DOWN, buff=MED_LARGE_BUFF).align_to(regle_2, LEFT)

        regle_4 = TextMobject2(r"- Elle peut contenir des tirets bas (i.e. \_).").scale(0.7).set_color(GREEN)
        regle_4.next_to(regle_3, DOWN, buff=MED_LARGE_BUFF).align_to(regle_3, LEFT)

        self.play(FadeIn(image))
        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement))
        self.wait(5)
        self.play(Write(regle_1))
        self.wait(5)
        self.play(Write(regle_2))
        self.wait(3)
        self.play(Write(regle_3))
        self.wait(3)
        self.play(Write(regle_4))
        self.wait(10)


class interditsNomVariable(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Noms de variables - Partie 2", width=6.5, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        # Channel logo and name (UP LEFT CORNER)
        logo_path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/videos/logoCTM/images/"
        image = ImageMobject(logo_path + "CTM_boite")
        image.scale(0.7).to_corner(DR)

        statement = TextMobject2(r"Pour le nom d'une variable, " r"\textbf{vous ne devez pas}:").scale(0.7)
        statement.next_to(np.array([-7,2,0]))
        # la variable ne peut contenir que des 0-9, a-z, A-Z et des barres en bas.

        # Règles
        regle_1 = TextMobject2(r"- mettre un espace dans le nom de la variable,").scale(0.7).set_color(RED)
        regle_1.next_to(statement, DOWN, buff=LARGE_BUFF).align_to(statement, LEFT)

        regle_2 = TextMobject2(r"- mettre un chiffre en première position du nom,").scale(0.7).set_color(RED)
        regle_2.next_to(regle_1, DOWN, buff=MED_LARGE_BUFF).align_to(regle_1, LEFT)

        regle_3 = TextMobject2(r"- mettre de virgules, de points, d’accents ou d’opérateurs arithmétiques (e.g. +, - , / et *) de Python.").scale(0.7).set_color(RED)
        regle_3.next_to(regle_2, DOWN, buff=MED_LARGE_BUFF).align_to(regle_2, LEFT)

        self.play(FadeIn(image))
        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement))
        self.wait(5)
        self.play(Write(regle_1))
        self.wait(5)
        self.play(Write(regle_2))
        self.wait(3)
        self.play(Write(regle_3))
        self.wait(10)