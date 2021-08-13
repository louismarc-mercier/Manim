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

        trailer_subtitle = TextMobject(r"\sc{\textbf{Notions de base - Boucle \textit{for}}}")
        trailer_subtitle.set_color(WHITE)
        trailer_subtitle.next_to(trailer_title, DOWN, buff=0.2*LARGE_BUFF).align_to(trailer_title, LEFT)
        trailer_subtitle.scale(1)
        image.next_to(trailer_subtitle.get_center() + np.array([-4,-2,0]))

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
        line_euclide = TextMobject(r"\sc{Comment exécuter des instructions}", r"\sc{un certain nombre de fois?}").scale(0.7).set_color([PINK])
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
        self.wait(5)

        solution = TextMobject(r"Une solution est d'utiliser la boucle \textit{for}.").next_to(euclide_img, LEFT, buff=1.5*LARGE_BUFF)
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

        statement_1 = TextMobject2(r" - Être en mesure d'utiliser la boucle \textit{for} pour résoudre des problèmes.").scale(0.7)
        statement_1.next_to(np.array([-6,1,0]))

        self.play(FadeIn(image))
        self.play(Write(title))
        self.wait(3)
        self.play(Write(statement_1))
        self.wait(5)


class introFor(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text=r"Boucle \textit{for}", width=4.5, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        statement = TextMobject2(r"La boucle \textit{for} est dites bornée, car le code est exécuté un nombre de fois déterminé. L'entête de la boucle se termine par un double point "
                                 r"suivie d’un bloc indenté d'instructions qui constitue le corps de la boucle. Une itération de la boucle consiste en l'exécution du corps de la boucle.").scale(0.7)
        statement.next_to(title, DOWN, buff=0.5*LARGE_BUFF)

        schema_path = r"C:/Users/Utilisateur/Desktop/CEGEP/Maisonneuve-Ete2021/CodeTesMaths/videos/boucle_for/"
        schema = ImageMobject(schema_path + "schema_for_colors").next_to(statement, DOWN, buff=1.5*LARGE_BUFF).scale(2.25)

        self.play(Write(title))
        self.wait(7)
        self.play(Write(statement))
        self.wait(20)
        self.play(FadeIn(schema))
        self.wait(30)


class variantes(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text=r"Boucle \textit{for} (suite)", width=5.5, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        statement = TextMobject2(r"Il existe plusieurs façons de parcourir des valeurs sur lesquelles on va itérer. Voici des alternatives:").scale(0.7)
        statement.next_to(title, DOWN, buff=0.5*LARGE_BUFF)

        elem_1 = TextMobject(r"$\bullet$ range(10) $\leftrightsquigarrow (0,1,2,3,4,5,6,7, 8, 9)$").next_to(statement, DOWN, buff=LARGE_BUFF).align_to(statement, LEFT)
        elem_2 = TextMobject(r"$\bullet$ range(1, 10) $\leftrightsquigarrow (1,2,3,4,5,6,7, 8, 9)$ ").next_to(elem_1, DOWN).align_to(elem_1, LEFT)
        elem_3 = TextMobject(r"$\bullet$ range(1, 10, 2) $\leftrightsquigarrow (1,3,5,7,9)$").next_to(elem_2, DOWN).align_to(elem_2, LEFT)
        elem_4 = TextMobject(r"$\bullet$ range(5, -5, -1) $\leftrightsquigarrow (5,4,3,2,1,0,-1,-2,-3,-4)$").next_to(elem_3, DOWN).align_to(
            elem_3, LEFT)
        #schema_path = r"C:/Users/Utilisateur/Desktop/CEGEP/Maisonneuve-Ete2021/CodeTesMaths/videos/boucle_for/"
        #schema = ImageMobject(schema_path + "schema_for_colors").next_to(statement, DOWN, buff=1.5*LARGE_BUFF).scale(2.25)

        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement))
        self.wait(5)
        self.play(Write(elem_1))
        self.wait(13)
        self.play(Write(elem_2))
        self.wait(10)
        self.play(Write(elem_3))
        self.wait(10)
        self.play(Write(elem_4))
        self.wait(15)
        #self.play(FadeIn(schema))
        #self.wait(15)



