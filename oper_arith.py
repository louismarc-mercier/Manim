from manimlib.imports import *
from manim_utils.slide_template import BoxedTitle, GenChannelLogo, YoutubeLogo
from MyAnim.RevisionSecondaire.id_rem_french import MeasureDistance
import pandas as pd
import numpy as np

# 1. intro       (X)
# 2.             (X)
# 3.   (X)
# 4.       (X)
# 5.              (X)
# 6.  ( )
# 9.       ()


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

        trailer_subtitle = TextMobject(r"\sc{\textbf{Notions de base - Opérations arithmétiques}}")
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

        statement_1 = TextMobject2(r" - Être en mesure d'effectuer des opérations arithmétiques (e.g. addition, multiplication, etc.).").scale(0.7)
        statement_1.next_to(title, DOWN, buff=LARGE_BUFF)

        statement_2 = TextMobject2(r" - Être en mesure d'importer une librairie de Python.").scale(0.7)
        statement_2.next_to(statement_1, DOWN, buff=MED_SMALL_BUFF).align_to(statement_1, LEFT)

        self.play(FadeIn(image))
        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement_1))
        self.wait(5)
        self.play(Write(statement_2))
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
        line_euclide = TextMobject(r"\sc{Comment est-ce qu'on additionne}", r"\sc{deux nombres?}").scale(0.7).set_color([PINK])
        line_euclide[0].next_to(3 * UP + 0 * RIGHT)
        line_euclide[1].next_to(line_euclide[0], DOWN)
        # line_e[1].next_to(2 * UP + 7 * LEFT)



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

        exemple_1 = TextMobject(">>", ' print("2+2") ').next_to(np.array([-7,0,0]))
        exemple_1[0].set_color(PURPLE)
        aide_exemple_1 = TextMobject("2+2").next_to(exemple_1, DOWN, buff=0.25 * LARGE_BUFF).align_to(exemple_1,
                                                                                                           LEFT)

        exemple_2 = TextMobject(">>", ' print("2" + "2") ').next_to(aide_exemple_1, DOWN).align_to(aide_exemple_1, LEFT)
        exemple_2[0].set_color(PURPLE)
        aide_exemple_2 = TextMobject("22").next_to(exemple_2, DOWN, buff=0.25 * LARGE_BUFF).align_to(exemple_2,
                                                                                                      LEFT)
        self.play(FadeIn(exemple_1))
        self.wait(3)
        self.play(FadeIn(aide_exemple_1))
        self.wait(3)
        self.play(FadeIn(exemple_2))
        self.wait(3)
        self.play(FadeIn(aide_exemple_2))
        self.wait(5)

        solution = TextMobject("La solution est d'utiliser des nombres.").to_corner(DL)
        self.play(FadeIn(solution))
        self.wait(5)


def get_sets_symbols():
    addition = TextMobject(r"$+$")
    soustraction = TextMobject(r"$-$")
    multiplication = TextMobject(r"*")
    division = TextMobject(r"/")
    exposant = TextMobject(r"**")
    empty = TextMobject(r"$\mathbb{R}$").set_color(BLACK)
    return [addition, soustraction, multiplication, division, exposant, empty]

def get_descriptions():
    addition = TextMobject(r"Addition")
    soustraction = TextMobject(r"Soustraction")
    multiplication = TextMobject(r"Multiplication")
    division = TextMobject(r"Division")
    exposant = TextMobject(r"Exposant")
    return [addition, soustraction, multiplication, division, exposant]

def get_examples():
    addition = TextMobject(r"$3+5$")
    soustraction = TextMobject(r"$3-5$")
    multiplication = TextMobject(r"3*5")
    division = TextMobject(r"3/5")
    exposant = TextMobject(r"5**3")
    return [addition, soustraction, multiplication, division, exposant]


def get_operators():
    parenthesis = TextMobject(r"()")
    exponant = TextMobject(r"**")
    multiplication_division = TextMobject(r"*, /")
    addition_substraction = TextMobject(r"+, -")
    empty = TextMobject(r"$\mathbb{R}$").set_color(BLACK)
    return [parenthesis, exponant, multiplication_division, addition_substraction, empty]

def get_operators_descriptions():
    parenthesis = TextMobject(r"Parenthèses")
    exponant = TextMobject(r"Exposant")
    multiplication_division = TextMobject(r"Multiplication, division")
    addition_substraction = TextMobject(r"Addition, soustraction")
    return [parenthesis, exponant, multiplication_division, addition_substraction]

def get_operators_examples():
    parenthesis = TextMobject(r"$(2+3)+5$")
    exponant = TextMobject(r"1+5**2")
    multiplication_division = TextMobject(r"1+5*2")
    addition_substraction = TextMobject(r"$3-5$")
    return [parenthesis, exponant, multiplication_division, addition_substraction]


class PrioriteOperations(Scene):
    def wplay(self, *args, wait=1, run_time=1, rate_func=smooth):
        self.play(*args, run_time=run_time, rate_func=rate_func)
        if wait != 0:
            self.wait(wait)

    def construct(self):
        horiz = Line([-FRAME_X_RADIUS + MED_LARGE_BUFF, 2.75, 0],
                     [FRAME_X_RADIUS - MED_LARGE_BUFF, 2.75, 0])

        headers = TexMobject(r"\textbf{Opérateur}", r"\textbf{Description}", r"\textbf{Exemple}").next_to(horiz, UP)
        headers[0].set_x(horiz.get_start()[0] + headers[0].get_width() / 2 + MED_LARGE_BUFF)
        vert_1 = Line([headers[0].get_right()[0] + MED_LARGE_BUFF, FRAME_Y_RADIUS - MED_LARGE_BUFF, 0],
                    [headers[0].get_right()[0] + MED_LARGE_BUFF, -FRAME_Y_RADIUS + MED_LARGE_BUFF, 0])
        vert_2 = Line([headers[1].get_right()[0] + MED_LARGE_BUFF, FRAME_Y_RADIUS - MED_LARGE_BUFF, 0],
                      [headers[1].get_right()[0] + MED_LARGE_BUFF, -FRAME_Y_RADIUS + MED_LARGE_BUFF, 0])
        remaining_space = horiz.get_right()[0] - vert_1.get_x()
        spacing = remaining_space / 4

        headers[0].set_color(PINK)
        headers[1].set_x(vert_1.get_x() + headers[1].get_width() / 2 + spacing / 2).set_color(YELLOW)
        headers[2].set_x(headers[1].get_x() + 2 * spacing)
        headers[2].set_color(BLUE)

        sets_symbols = VGroup(*get_operators()).arrange(DOWN,buff=0.45).next_to(horiz, DOWN).set_x(headers[0].get_x())

        rows = VGroup(*[horiz.copy().set_stroke(width=1)
                      .set_y((sets_symbols[i].get_y() + sets_symbols[i + 1].get_y()) / 2) for i in range(4)])

        descriptions = VGroup(*get_operators_descriptions()).arrange(DOWN, buff=0.45) \
            .next_to(horiz, DOWN).set_x(headers[1].get_x())#.set_color(YELLOW)

        examples = VGroup(*get_operators_examples()).arrange(DOWN, buff=0.45) \
            .next_to(horiz, DOWN).set_x(headers[2].get_x())

        # Channel logo and name (UP LEFT CORNER)
        logo_path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/videos/logoCTM/images/"
        image = ImageMobject(logo_path + "CTM_boite")
        image.scale(0.7).to_corner(DR)
        self.play(FadeIn(image))

        self.play(ShowCreation(horiz), ShowCreation(vert_1), ShowCreation(vert_2))
        self.play(Write(headers[0]), Write(headers[1]), Write(headers[2]))
        self.wait(5)
        for set_symbol, description, example, row in zip(sets_symbols[0:-1], descriptions, examples, rows):
            self.play(ShowCreation(set_symbol))
            self.wait(3)
            self.play(ShowCreation(description))
            self.wait(6)
            self.play(ShowCreation(example))
            self.wait(3)
            self.play(ShowCreation(row))
        self.wait(8)


class LesOperations(Scene):
    def wplay(self, *args, wait=1, run_time=1, rate_func=smooth):
        self.play(*args, run_time=run_time, rate_func=rate_func)
        if wait != 0:
            self.wait(wait)

    def construct(self):
        horiz = Line([-FRAME_X_RADIUS + MED_LARGE_BUFF, 2.75, 0],
                     [FRAME_X_RADIUS - MED_LARGE_BUFF, 2.75, 0])

        headers = TexMobject(r"\textbf{Opérateur}", r"\textbf{Description}", r"\textbf{Exemple}").next_to(horiz, UP)
        headers[0].set_x(horiz.get_start()[0] + headers[0].get_width() / 2 + MED_LARGE_BUFF)
        vert_1 = Line([headers[0].get_right()[0] + MED_LARGE_BUFF, FRAME_Y_RADIUS - MED_LARGE_BUFF, 0],
                    [headers[0].get_right()[0] + MED_LARGE_BUFF, -FRAME_Y_RADIUS + MED_LARGE_BUFF, 0])
        vert_2 = Line([headers[1].get_right()[0] + MED_LARGE_BUFF, FRAME_Y_RADIUS - MED_LARGE_BUFF, 0],
                      [headers[1].get_right()[0] + MED_LARGE_BUFF, -FRAME_Y_RADIUS + MED_LARGE_BUFF, 0])
        remaining_space = horiz.get_right()[0] - vert_1.get_x()
        spacing = remaining_space / 4

        headers[0].set_color(PINK)
        headers[1].set_x(vert_1.get_x() + headers[1].get_width() / 2 + spacing / 2).set_color(YELLOW)
        headers[2].set_x(headers[1].get_x() + 2 * spacing)
        headers[2].set_color(BLUE)

        sets_symbols = VGroup(*get_sets_symbols()).arrange(DOWN,buff=0.55).next_to(horiz, DOWN).set_x(headers[0].get_x())

        rows = VGroup(*[horiz.copy().set_stroke(width=1)
                      .set_y((sets_symbols[i].get_y() + sets_symbols[i + 1].get_y()) / 2) for i in range(5)])

        descriptions = VGroup(*get_descriptions()).arrange(DOWN, buff=0.45) \
            .next_to(horiz, DOWN).set_x(headers[1].get_x())#.set_color(YELLOW)

        examples = VGroup(*get_examples()).arrange(DOWN, buff=0.4) \
            .next_to(horiz, DOWN).set_x(headers[2].get_x())

        # Channel logo and name (UP LEFT CORNER)
        logo_path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/videos/logoCTM/images/"
        image = ImageMobject(logo_path + "CTM_boite")
        image.scale(0.7).to_corner(DR)
        self.play(FadeIn(image))

        self.play(ShowCreation(horiz), ShowCreation(vert_1), ShowCreation(vert_2))
        self.play(Write(headers[0]), Write(headers[1]), Write(headers[2]))
        for set_symbol, description, example, row in zip(sets_symbols[0:-1], descriptions, examples, rows):
            self.play(ShowCreation(set_symbol))
            self.wait(3)
            self.play(ShowCreation(description))
            self.wait(6)
            self.play(ShowCreation(example))
            self.wait(3)
            self.play(ShowCreation(row))
        self.wait(8)


class test(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Test", width=1.25, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        # Channel logo and name (UP LEFT CORNER)
        logo_path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/videos/logoCTM/images/"
        image = ImageMobject(logo_path + "CTM_boite")
        image.scale(0.7).to_corner(DR)

        statement = TextMobject2(r"Qu'est-ce qui arrivera après avoir exécuté chacune des lignes de code suivantes?").scale(0.80)
        statement.next_to(title, DOWN, buff=LARGE_BUFF)

        #exemples_titre = TextMobject2(r"\underline{Exemples}:").scale(0.85).next_to(statement, DOWN, buff=LARGE_BUFF).align_to(statement, LEFT)



        exemple_1 = TextMobject('>>', ' print(5/3) ').next_to(statement, DOWN, buff=1.5*LARGE_BUFF).align_to(statement, LEFT)
        exemple_1[0].set_color(PURPLE)
        aide_exemple_1 = TextMobject("1.6666").next_to(exemple_1, DOWN, buff=0.25 * LARGE_BUFF).align_to(exemple_1,
                                                                                                           LEFT)

        exemple_2 = TextMobject('>>',  ' print(1/0) ').next_to(aide_exemple_1, DOWN, buff=0.25 * LARGE_BUFF).align_to(aide_exemple_1, LEFT)
        aide_exemple_2 = TextMobject("ZeroDivisionError: division by zero").next_to(exemple_2, DOWN, buff=0.25 * LARGE_BUFF).align_to(exemple_2, LEFT)
        aide_exemple_2.set_color(RED)

        self.play(FadeIn(image))
        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement))
        self.wait(5)
        self.play(Write(exemple_1))
        self.play(Write(exemple_2))
        self.wait(5)
        # Pause to think about it.
        circ = Arc(start_angle=PI / 2, angle=-2 * PI, radius=0.35).to_corner(DL)
        timers = [TexMobject(str(i)).move_to(circ) for i in range(5, -1, -1)]
        pause = TextMobject("Faites pause et trouvez la solution.").next_to(circ, RIGHT)
        self.play(ShowCreation(circ), Write(pause))
        self.play(Write(timers[0]), run_time=0.5)
        for i in range(5):
            self.play(ReplacementTransform(timers[i], timers[i + 1]), run_time=0.5)
            self.wait(0.5)
        self.play(FadeOut(pause), FadeOut(timers[-1]), FadeOut(circ), run_time=2)

        self.play(Write(aide_exemple_1))
        self.wait(5)
        self.play(Write(aide_exemple_2))
        self.wait(5)



class introLib(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Librairies de Python", width=5, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        # Channel logo and name (UP LEFT CORNER)
        logo_path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/videos/logoCTM/images/"
        image = ImageMobject(logo_path + "CTM_boite")
        image.scale(0.7).to_corner(DR)

        # Put box with equivalence
        equivalence_box = BoxedTitle(text=r"$\sqrt{9}\leadsto\text{math.sqrt(9)}$", width=4, height=0.7, scale=0.7, box_color=BLUE, CAPS_LOCKED=False)
        equivalence_box.next_to(image, LEFT, buff=1.5)

        statement = TextMobject2(r"Une librairie (i.e. \textit{python module} en anglais) est un fichier contenant un ensemble de fonctions que vous pouvez utiliser dans votre code.").scale(0.7)
        statement.next_to(title, DOWN, buff=LARGE_BUFF)

        exemples_titre = TextMobject2(r"\underline{Exemple - Racine carrée (librairie \textit{math})}:").scale(0.85).next_to(statement, DOWN, buff=LARGE_BUFF).align_to(statement, LEFT).set_color(BLUE)

        exemple_1 = TextMobject(">>", " import ", "math").next_to(exemples_titre, DOWN, buff=0.5*LARGE_BUFF).align_to(exemples_titre, LEFT)
        exemple_1[0].set_color(PURPLE)
        exemple_1[1].set_color(PINK)
        #exemple_1 = TextMobject(">>", " import ").next_to(exemples_titre, DOWN, buff=0.5 * LARGE_BUFF).align_to(
        #    exemples_titre, LEFT)
        exemple_1_suite = TextMobject(">>", " print(math.sqrt(9))").next_to(exemple_1, DOWN, buff=0.25*LARGE_BUFF).align_to(exemple_1, LEFT)
        exemple_1_fin = TextMobject("3").next_to(exemple_1_suite, DOWN, buff=0.25*LARGE_BUFF).align_to(exemple_1_suite, LEFT)


        # Méthode 2
        #exemple_2 = TextMobject(">>", " from ", "math ", "import ", "sqrt","   \# Méthode 2").next_to(exemple_1, DOWN, buff=0.5*LARGE_BUFF).align_to(exemple_1, LEFT)
        #exemple_2[0].set_color(PURPLE)
        #exemple_2[2].set_color(PINK)
        #exemple_2[4].set_color(PINK)
        #exemple_2[5].set_color(GREEN)
        #aide_exemple_2 = TextMobject("Bonjour à tous ! ").next_to(exemple_2, DOWN, buff=0.25*LARGE_BUFF).align_to(exemple_2, LEFT)


        self.play(FadeIn(image))
        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement))
        self.wait(5)
        self.play(Write(exemples_titre))
        self.wait(5)
        self.play(Write(exemple_1))
        self.wait(5)
        self.play(Write(exemple_1_suite))
        self.wait(5)
        self.play(Write(exemple_1_fin))
        self.play(WiggleOutThenIn(equivalence_box))
        self.wait(15)


class importerConstante(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        title = BoxedTitle(text="Importer des constantes", width=5.25, height=0.7, scale=0.7)
        title.move_to(np.array([0, 3.25, 0]))

        # Channel logo and name (UP LEFT CORNER)
        logo_path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/videos/logoCTM/images/"
        image = ImageMobject(logo_path + "CTM_boite")
        image.scale(0.7).to_corner(DR)

        # Put box with equivalence
        equivalence_box = BoxedTitle(text=r"$\pi\leadsto\text{math.pi}$", width=3, height=0.7, scale=0.7,
                                     box_color=BLUE, CAPS_LOCKED=False)
        equivalence_box.next_to(image, LEFT, buff=1.5)

        statement = TextMobject2(r"On peut aussi importer des constantes mathématiques à partir de certaines librairies de Python.").scale(0.7)
        statement.next_to(title, DOWN, buff=LARGE_BUFF)

        exemples_titre = TextMobject2(r"\underline{Exemple - Importer $\pi$ (librairie \textit{math})}:").scale(0.85).next_to(statement, DOWN, buff=LARGE_BUFF).align_to(statement, LEFT).set_color(BLUE)

        exemple_1 = TextMobject(">>", " import ", "math").next_to(exemples_titre, DOWN, buff=0.5*LARGE_BUFF).align_to(exemples_titre, LEFT)
        exemple_1[0].set_color(PURPLE)
        exemple_1[1].set_color(PINK)
        #exemple_1 = TextMobject(">>", " import ").next_to(exemples_titre, DOWN, buff=0.5 * LARGE_BUFF).align_to(
        #    exemples_titre, LEFT)
        exemple_1_suite = TextMobject(">>", " print(math.pi)").next_to(exemple_1, DOWN, buff=0.25*LARGE_BUFF).align_to(exemple_1, LEFT)
        exemple_1_suite[0].set_color(PURPLE)
        exemple_1_fin = TextMobject("3.141592653589793").next_to(exemple_1_suite, DOWN, buff=0.25*LARGE_BUFF).align_to(exemple_1_suite, LEFT)


        # Méthode 2
        #exemple_2 = TextMobject(">>", " from ", "math ", "import ", "sqrt","   \# Méthode 2").next_to(exemple_1, DOWN, buff=0.5*LARGE_BUFF).align_to(exemple_1, LEFT)
        #exemple_2[0].set_color(PURPLE)
        #exemple_2[2].set_color(PINK)
        #exemple_2[4].set_color(PINK)
        #exemple_2[5].set_color(GREEN)
        #aide_exemple_2 = TextMobject("Bonjour à tous ! ").next_to(exemple_2, DOWN, buff=0.25*LARGE_BUFF).align_to(exemple_2, LEFT)


        self.play(FadeIn(image))
        self.play(Write(title))
        self.wait(5)
        self.play(Write(statement))
        self.wait(5)
        self.play(Write(exemples_titre))
        self.wait(5)
        self.play(Write(exemple_1))
        self.wait(5)
        self.play(Write(exemple_1_suite))
        self.wait(5)
        self.play(Write(exemple_1_fin))
        self.play(WiggleOutThenIn(equivalence_box))
        self.wait(15)





class credits(Scene):
    def wplay(self, *args, wait=1, run_time=1, rate_func=smooth):
        self.play(*args, run_time=run_time, rate_func=rate_func)
        if wait != 0:
            self.wait(wait)

    def construct(self):
        credits = TextMobject("Crédits").set_color(PINK).scale(1.7)
        thanks = TextMobject("Merci d'avoir visionné la vidéo!!").set_color("#0079C2").scale(1.7)

        instructor = TexMobject(r"\text{Enseignant}", r"\text{Louis-Marc Mercier}")
        conceptors = TexMobject(r"\text{Conception du contenu}", r"\text{Rosalie Bentz-Moffet}",  r"\text{Melisande Fortin-Boisvert}",
                                r"\text{Stéphanie Larocque}", r"\text{Louis-Marc Mercier}")

        director = TexMobject(r"\text{Direction du projet}", r"\text{Melisande Fortin-Boisvert}")
        animation_conceptor = TexMobject(r"\text{Conception d'animations}", r"\text{Louis-Marc Mercier}")


        lines = [instructor, conceptors, director, animation_conceptor]

        instructor[0].align_to([-0.5, 0, 0], RIGHT).shift(8 * DOWN)
        instructor[1].align_to([0.5, 0, 0], LEFT).shift(8 * DOWN)

        conceptors[0].next_to(instructor, DOWN, buff=LARGE_BUFF).align_to(instructor[0], RIGHT)
        conceptors[1].next_to(conceptors[0], RIGHT, buff=SMALL_BUFF).align_to(instructor[1], LEFT)
        conceptors[2].next_to(conceptors[1], DOWN, buff=SMALL_BUFF).align_to(conceptors[1], LEFT)
        conceptors[3].next_to(conceptors[2], DOWN, buff=SMALL_BUFF).align_to(conceptors[2], LEFT)
        conceptors[4].next_to(conceptors[3], DOWN, buff=SMALL_BUFF).align_to(conceptors[3], LEFT)

        director[0].next_to(conceptors, DOWN, buff=LARGE_BUFF).align_to(conceptors[0], RIGHT)
        director[1].next_to(conceptors, DOWN, buff=LARGE_BUFF).align_to(conceptors[1], LEFT)

        animation_conceptor[0].next_to(director, DOWN, buff=LARGE_BUFF).align_to(director[0], RIGHT)
        animation_conceptor[1].next_to(director, DOWN, buff=LARGE_BUFF).align_to(director[1], LEFT)

        credits.set_y(instructor.get_top()[1] + 2 * LARGE_BUFF)
        thanks.set_y(-15.5)

        def half_start(t):
            # this rate function is great for gradually starting into a `linear` rate
            # it goes from 0 to 0.5 in value, and from 0 to 1 in slope (speed)
            return 1 / 2 * t ** 2

        everything_no_thanks = VGroup(credits, *lines)

        self.play(VGroup(*everything_no_thanks, thanks).shift, UP, rate_func=half_start)
        self.play(VGroup(*everything_no_thanks, thanks).shift, 14 * UP, rate_func=linear, run_time=14)
        self.play(everything_no_thanks.shift, 3 * UP, rate_func=linear, run_time=3)
        self.remove(*everything_no_thanks)
        self.wait(1.5)

        # all done :)
        self.wplay(FadeOut(thanks))

