from manimlib.imports import *
from manim_utils.slide_template import BoxedTitle, GenChannelLogo, YoutubeLogo
from MyAnim.RevisionSecondaire.id_rem_french import MeasureDistance


class bandeAnnonce(Scene):
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

        trailer_subtitle = TextMobject(r"\sc{\textbf{Notions de base - Fonction d'impression}}")
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


class Credits(Scene):
    def wplay(self, *args, wait=1, run_time=1, rate_func=smooth):
        self.play(*args, run_time=run_time, rate_func=rate_func)
        if wait != 0:
            self.wait(wait)

    def construct(self):
        credits = TextMobject("Crédits").set_color(YELLOW).scale(1.7)
        thanks = TextMobject("Merci d'avoir visionné le vidéo!!").set_color(ORANGE).scale(1.7)

        instructor = TexMobject(r"\text{Enseignant}", r"\text{Louis-Marc Mercier}")
        viewer = TexMobject(r"\text{Spectateur}", r"\text{You}")
        lines = [instructor, viewer]

        instructor[0].align_to([-0.5, 0, 0], RIGHT).shift(8 * DOWN)
        instructor[1].align_to([0.5, 0, 0], LEFT).shift(8 * DOWN)

        viewer[0].next_to(instructor, DOWN, buff=LARGE_BUFF).align_to(instructor[0], RIGHT)
        viewer[1].next_to(instructor, DOWN, buff=LARGE_BUFF).align_to(instructor[1], LEFT)

        credits.set_y(instructor.get_top()[1] + 2 * LARGE_BUFF)
        thanks.set_y(-14.5)

        def half_start(t):
            # this rate function is great for gradually starting into a `linear` rate
            # it goes from 0 to 0.5 in value, and from 0 to 1 in slope (speed)
            return 1 / 2 * t ** 2

        everything_no_thanks = VGroup(credits, *lines)

        self.play(VGroup(*everything_no_thanks, thanks).shift, UP, rate_func=half_start)
        self.play(VGroup(*everything_no_thanks, thanks).shift, 14 * UP, rate_func=linear, run_time=14)
        self.play(everything_no_thanks.shift, 3 * UP, rate_func=linear, run_time=3)
        self.remove(*everything_no_thanks)
        self.wait(3)

        # all done :)
        self.wplay(FadeOut(thanks))