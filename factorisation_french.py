from manimlib.imports import *


# 0. Thumbnail
# 1. Menu
# 2. Distributivite
# 3. DistributiviteSuite
# 4. DistributiviteSuitePk
# 5. Commutativite

# 6. Symetrie # TO REMOVE

# 7. DefFactorisation
# 8. MiseEvidenceSimple
# 9. PourquoiMES
# 10. MiseEvidenceDouble
# 12. Recette
# 13. RecetteExemple
# 14. FactoExoSup
# 15. Conclusion

color_map = {
    r"{a}": BLUE,
    r"{b}": YELLOW,
}

class Thumbnail(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        path = r"C:/Users/Utilisateur/Desktop/CEGEP/MANIM/manim-recent/media/images/"
        image_peinture = ImageMobject(path + "drake_factorisation")
        image_peinture.scale(4)
        #image_peinture.to_edge(DOWN)

        line_expand = TextMobject("$ab+ac$").set_color(BLACK).scale(2)
        line_expand.next_to(5.5*LEFT + 3.45*UP)

        line_factor = TextMobject(r"$a(b+c)$").set_color(BLACK).scale(1.9)
        line_factor.next_to(2*RIGHT + 3.45*UP)

        self.play(FadeIn(image_peinture))
        self.play(Write(line_expand), Write(line_factor))
        self.wait(5)


class Menu(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\sc Menu}", color=PURPLE).to_corner(UL).scale(1.5)

        l = NumberedList(
            *"""1) Révision des axiomes, 2) Mise en évidence simple, 3) Mise en évidence doubleeee""".split(","), dot_color=BLUE
        )

        #l = NumberedList(*["Révision des axiomes", "Riemann Hypothesis", "P vs NP Problem"], dot_color=BLUE)
        l.scale(1)
        l.shift(0.5 * DOWN + 3*LEFT)
        self.play(FadeInFromDown(title))
        self.play(Write(l))
        self.wait()

        #self.play(l.fade_all_but, 3)
        self.wait(15)


class Distributivite(Scene):
    def construct(self):

        def set_color(equation_term, color):
            return equation_term.set_color(color)

        def get_arrow(eq_term_1, eq_term_2, color, BUFFER=0.25):
            pointer = CurvedArrow(start_point=eq_term_1.get_center() - np.array([0, BUFFER, 0]),
                              end_point=eq_term_2.get_center() - np.array([0, BUFFER, 0]),
                              color=color)
            return pointer


        title = TextMobject(r"\underline{\sc Distributivité}", color=PURPLE).to_corner(UL).scale(1.25)

        context = TextMobject(r"Pour $a,b$ et $c\in\mathbb{R}$:")
        context.scale(1)
        context.move_to(5* LEFT + 2*UP)
        #context.set_color(YELLOW)
        set_color(context, YELLOW)

        #distributivite = TextMobject(r"$a(b+c)=ab+ac$")
        distributivite = TextMobject(r"$a$", r"$($", r"$b$", r" $+$ ", r"$c$", r"$)$", r" $=$ ",
                                     r"$ab$", r" $+$ ", r"$ac$")
        distributivite.scale(1)
        distributivite.move_to(0 * LEFT + 1 * UP)
        distributivite.set_color(WHITE)
        ab_arrow = get_arrow(distributivite[0], distributivite[2], color=PINK)
        ac_arrow = get_arrow(distributivite[0], distributivite[4], color=PURPLE)


        titre_exemple = TextMobject(r"\underline{\sc Exemples}", color=PURPLE)
        titre_exemple.move_to(5.75 * LEFT + 1 * DOWN)
        exemple_1 = TextMobject(r"$10(5+7)=10\times 5 + 10\times 7$")
        exemple_1.scale(1)
        exemple_1.move_to(4 * LEFT + 2 * DOWN)
        exemple_1.set_color(WHITE)

        exemple_2 = TextMobject(r"$10x(5x+7)=50x^{2} + 70x$")
        exemple_2.scale(1)
        exemple_2.move_to(4.2 * LEFT + 3 * DOWN)
        exemple_2.set_color(WHITE)

        self.play(Write(title))
        self.wait(5)
        self.play(Write(context))
        self.wait(5)
        self.play(Write(distributivite))
        self.wait(5)
        self.add(ab_arrow)
        distributivite[7].set_color(PINK)
        self.wait(5)
        self.add(ac_arrow)
        distributivite[9].set_color(PURPLE)
        self.wait(10)
        self.play(Write(titre_exemple))
        self.play(Write(exemple_1))
        self.wait(10)
        self.play(Write(exemple_2))
        self.wait(10)

        #self.play(l.fade_all_but, 3)
        self.wait(15)


class DistributiviteSuite(Scene):
    def construct(self):
        def set_color(equation_term, color):
            return equation_term.set_color(color)

        def get_arrow(eq_term_1, eq_term_2, color, BUFFER=0.25):
            pointer = CurvedArrow(start_point=eq_term_1.get_center() - np.array([0, BUFFER, 0]),
                              end_point=eq_term_2.get_center() - np.array([0, BUFFER, 0]),
                              color=color)
            return pointer


        title = TextMobject(r"\underline{\sc Distributivité (suite)}", color=PURPLE).to_corner(UL).scale(1.25)
        title.move_to(3.5 * LEFT + 3 * UP)

        context = TextMobject(r"Pour $a,b,c$ et $d\in\mathbb{R}$:")
        context.scale(1)
        context.move_to(4.75* LEFT + 2*UP)
        #context.set_color(YELLOW)

        # (a+b)(c+d)=ac+ad+bc+bd
        distributivite = TextMobject(r"$($", r"$a$", r" $+$ ", r"$b$", r")", r"$($", r"$c$", r" $+$ ", r"$d$", r"$)$", r" $=$ ", # LHS
                                    r"$ac$", r" $+$ ", r"$ad$", r" $+$ ", r"$bc$", r" $+$ ", r"$bd$")      # RHS
        distributivite.scale(1)
        distributivite.move_to(0 * LEFT + 1 * UP)
        distributivite.set_color(WHITE)

        ac_arrow = get_arrow(distributivite[1], distributivite[6], color=PINK)
        ad_arrow = get_arrow(distributivite[1], distributivite[8], color=PURPLE)
        bc_arrow = get_arrow(distributivite[3], distributivite[6], color=GOLD)
        bd_arrow = get_arrow(distributivite[3], distributivite[8], color=ORANGE)

        titre_exemple = TextMobject(r"\underline{\sc Exemple}", color=PURPLE)
        titre_exemple.move_to(5.75 * LEFT + 1 * DOWN)
        exemple_1 = TextMobject(r"$(x+1)(x+2)=x^{2}+2x+x+2=x^{2}+3x+2$")
        exemple_1.scale(1)
        exemple_1.move_to(1 * LEFT + 2 * DOWN)
        exemple_1.set_color(WHITE)

        self.play(Write(title))
        self.wait(5)
        self.play(Write(context))
        self.wait(5)
        self.play(Write(distributivite))
        self.wait(5)

        # Display distributivity (a*c)
        self.play(FadeIn(ac_arrow))
        set_color(distributivite[11], PINK)
        self.wait(3)
        self.play(FadeOut(ac_arrow))
        self.wait(3)

        # Display distributivity (b*c)
        self.play(FadeIn(ad_arrow))
        set_color(distributivite[13], PURPLE)
        self.wait(3)
        self.play(FadeOut(ad_arrow))
        self.wait(3)

        # Display distributivity (b*d)
        self.play(FadeIn(bc_arrow))
        set_color(distributivite[15], GOLD)
        self.wait(3)
        self.play(FadeOut(bc_arrow))
        self.wait(3)

        # Display distributivity (a*d)
        self.play(FadeIn(bd_arrow))
        set_color(distributivite[17], ORANGE)
        self.wait(3)
        self.play(FadeOut(bd_arrow))
        self.wait(3)

        self.wait(10)
        self.play(Write(titre_exemple))
        self.play(Write(exemple_1))
        self.wait(10)

        #self.play(l.fade_all_but, 3)
        self.wait(15)


class DistributiviteSuitePk(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\sc Preuve:}", color=PURPLE).to_corner(UL).scale(1.25)
        title.move_to(5 * LEFT + 3 * UP)

        eq_1 = TextMobject(r"$(a+b)(c+d)$")
        eq_1.scale(1)
        eq_1.move_to(3.6*LEFT + 1*UP)

        substitution = TextMobject(r"(Posons ", r"$e=(c+d)$", r")")
        substitution[1].set_color(GREEN)
        substitution.scale(0.8)
        substitution.move_to(5 * RIGHT + 1 * UP)

        substitution_2 = TextMobject(r"(Par distributivité)")
        substitution_2.scale(0.8)
        substitution_2.move_to(5 * RIGHT + 0 * UP)

        substitution_3 = TextMobject(r"(Par distributivité)")
        substitution_3.scale(0.8)
        substitution_3.move_to(5 * RIGHT + 1 * DOWN)

        eq_2 = TextMobject(r"$=$ ", r"$($", r"$a$", r" $+$ ", r"$b$", r"$)$", r"$e$")
        eq_2[6].set_color(GREEN)
        eq_2.scale(1)
        eq_2.move_to(0.85 * LEFT + 1 * UP)

        eq_3 = TextMobject(r"$=$ ", r"$a$", r"$e$", r" $+$ ", r"$b$", r"$e$")
        eq_3[2].set_color(GREEN)
        eq_3[5].set_color(GREEN)
        eq_3.scale(1)
        eq_3.move_to(1 * LEFT + 0 * UP)

        eq_4 = TextMobject(r"$=$ ", r"$a$", r"$(c+d)$", r" $+$ ", r"$b$", r"$(c+d)$")
        eq_4[2].set_color(GREEN)
        eq_4[5].set_color(GREEN)
        eq_4.scale(1)
        eq_4.move_to(0.25 * RIGHT + 1 * DOWN)

        substitution_4 = TextMobject(r"(Par distributivité)")
        substitution_4.scale(0.8)
        substitution_4.move_to(5 * RIGHT + 2 * DOWN)

        eq_5 = TextMobject(r"$=$ ", r"$ac$", r" $+$ ", r"$ad$", r" $+$ ", r"$bc$", r" $+$ ", r"$bd$")
        #eq_5[6].set_color(GREEN)
        eq_5.scale(1)
        eq_5.move_to(0.25 * RIGHT + 2 * DOWN)

        square = Square(side_length=0.25, fill_color=GOLD, fill_opacity=1, color=ORANGE)
        square.move_to(5 * RIGHT + 3 * DOWN)


        self.play(Write(title))
        self.play(Write(eq_1))
        self.wait(5)
        self.play(Write(substitution))
        self.wait(5)
        self.play(Write(eq_2))
        self.play(Write(substitution_2))
        self.wait(5)
        self.play(Write(eq_3))
        self.wait(5)
        self.play(Write(eq_4))
        self.play(Write(substitution_3))
        self.wait(5)
        self.play(Write(substitution_4))
        self.play(Write(eq_5))
        self.play(Write(square))
        self.wait(15)


class Commutativite(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\sc Commutativité de la multiplication}", color=PURPLE).to_corner(UL).scale(1.25)
        title.move_to(1 * LEFT + 3 * UP)

        context = TextMobject(r"Pour $a$ et $b\in\mathbb{R}$:")
        context.scale(1)
        context.move_to(5* LEFT + 2*UP)
        context.set_color(YELLOW)

        distributivite = TextMobject(r"$ab=ba$")
        distributivite.scale(1)
        distributivite.move_to(0 * LEFT + 1 * UP)
        distributivite.set_color(WHITE)


        titre_exemple = TextMobject(r"\underline{\sc Exemples}", color=PURPLE)
        titre_exemple.move_to(5.75 * LEFT + 1 * DOWN)
        exemple_1 = TextMobject(r"$10\times 5=5\times 10$")
        exemple_1.scale(1)
        exemple_1.move_to(5 * LEFT + 2 * DOWN)
        exemple_1.set_color(WHITE)

        exemple_2 = TextMobject(r"$-2xy+yx=-2xy+xy=-xy$")
        exemple_2.scale(1)
        exemple_2.move_to(3.5 * LEFT + 3 * DOWN)
        exemple_2.set_color(WHITE)

        self.play(Write(title))
        self.play(Write(context))
        self.play(Write(distributivite))
        self.wait(10)
        self.play(Write(titre_exemple))
        self.play(Write(exemple_1))
        self.wait(10)
        self.play(Write(exemple_2))
        self.wait(10)

        #self.play(l.fade_all_but, 3)
        self.wait(15)


class Symetrie(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\sc Symétrie}", color=PURPLE).to_corner(UL).scale(1.25)

        context = TextMobject(r"Pour $a,b\in\mathbb{R}$:")
        context.scale(1)
        context.move_to(5* LEFT + 2*UP)
        context.set_color(YELLOW)

        distributivite = TextMobject(r"$a=b \Leftrightarrow b=a$")
        distributivite.scale(1)
        distributivite.move_to(0 * LEFT + 1 * UP)
        distributivite.set_color(WHITE)


        self.play(Write(title))
        self.play(Write(context))
        self.wait(2)
        self.play(Write(distributivite))
        self.wait(15)


class DefFactorisation(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\sc Définir la factorisation}", color=PURPLE).to_corner(UL).scale(1.25)
        title.move_to(3 * LEFT + 3 * UP)

        definition = TextMobject2(r"La factorisation consiste à écrire une", r" expression algébrique", r" sous la forme d'un ",
                                  r"produit de facteurs", r".")
        definition[1].set_color(GOLD)
        definition[3].set_color(BLUE)
        definition.scale(0.7)
        definition.move_to(1* LEFT + 2*UP)
        #definition.set_color(YELLOW)

        titre_exemple = TextMobject(r"\underline{\sc Exemple}", color=PURPLE)
        titre_exemple.move_to(5.75 * LEFT + 0.5 * UP)
        distributivite = TextMobject(r"$a(b+c)$", r" $=$ ", r"$ab+ac$")
        distributivite[0].set_color(BLUE)
        distributivite[2].set_color(GOLD)
        distributivite.scale(1)
        distributivite.move_to(0 * LEFT + 1 * DOWN)
        #distributivite.set_color(WHITE)

        sup_text = TextMobject("Développer") #.set_color(BLUE)
        sup_arrow = TextMobject("$\Rightarrow$") #.set_color(BLUE)
        sup_arrow.move_to(0.1 * RIGHT + 0.5 * DOWN)
        sup_text.move_to(0.1 * RIGHT + 0 * DOWN)

        down_text = TextMobject("Factoriser") #.set_color(GOLD)
        down_arrow = TextMobject("$\Leftarrow$") #.set_color(GOLD)
        down_arrow.move_to(0 * RIGHT + 1.5 * DOWN)
        down_text.move_to(0 * RIGHT + 2 * DOWN)

        self.play(Write(title))
        self.wait(3)
        self.play(Write(definition))
        self.wait(5)
        self.play(Write(titre_exemple))
        self.play(Write(distributivite))
        self.wait(10)
        self.play(Write(sup_arrow))
        self.wait(5)
        self.play(Write(sup_text))
        self.wait(10)
        self.play(Write(down_arrow))
        self.wait(5)
        self.play(Write(down_text))
        self.wait(10)

        # Pause to think about it.
        circ = Arc(start_angle=PI / 2, angle=-2 * PI, radius=0.35).to_corner(DL)
        timers = [TexMobject(str(i)).move_to(circ) for i in range(5, -1, -1)]
        pause = TextMobject("Quel axiome utilise t'on pour obtenir développer une expression?").next_to(circ, RIGHT)
        pause.scale(0.8)
        self.play(ShowCreation(circ), Write(pause))
        self.play(Write(timers[0]), run_time=0.5)
        for i in range(5):
            self.play(ReplacementTransform(timers[i], timers[i + 1]), run_time=0.5)
            self.wait(0.5)
        self.play(FadeOut(pause), FadeOut(timers[-1]), FadeOut(circ), run_time=2)

        answer = TextMobject("Réponse: La distributivité.").to_corner(DL)
        self.play(Write(answer))
        self.wait(10)
        self.play(FadeOut(answer))

        #circ = Arc(start_angle=PI / 2, angle=-2 * PI, radius=0.35).to_corner(DL)
        #timers = [TexMobject(str(i)).move_to(circ) for i in range(5, -1, -1)]
        #pause = TextMobject("Quelle est l'opération pour factoriser une expression?").next_to(circ, RIGHT)
        #self.play(ShowCreation(circ), Write(pause))
        #self.play(Write(timers[0]), run_time=0.5)
        #for i in range(5):
        ##    self.play(ReplacementTransform(timers[i], timers[i + 1]), run_time=0.5)
        #    self.wait(0.5)
        #self.play(FadeOut(pause), FadeOut(timers[-1]), FadeOut(circ), run_time=2)


class MiseEvidenceSimple(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\sc Mise en évidence simple}", color=PURPLE).to_corner(UL).scale(1.25)
        title.move_to(1 * LEFT + 3 * UP)

        context = TextMobject(r"La mise en évidence simple est un procédé qui permet de décomposer un polynôme en deux "
                              r"facteurs, l'un étant un monôme et l'autre un polynôme.")
        context.scale(0.7)
        context.move_to(0* LEFT + 2*UP)
        context.set_color(YELLOW)


        titre_exemple = TextMobject(r"\underline{\sc Exemples}", color=PURPLE)
        titre_exemple.move_to(5.75 * LEFT + 1 * DOWN)
        exemple_1 = TextMobject(r"$ab+ac=a(b+c)$")
        exemple_1.scale(1)
        exemple_1.move_to(5 * LEFT + 2 * DOWN)
        exemple_1.set_color(WHITE)

        exemple_2 = TextMobject(r"$-2x^{2}+yx=x(-2+y)$")
        exemple_2.scale(1)
        exemple_2.move_to(4.5 * LEFT + 3 * DOWN)
        exemple_2.set_color(WHITE)

        self.play(Write(title))
        self.wait(3)
        self.play(Write(context))
        self.wait(5)
        #self.play(Write(distributivite))
        self.wait(10)
        self.play(Write(titre_exemple))
        self.play(Write(exemple_1))
        self.wait(10)
        self.play(Write(exemple_2))
        self.wait(10)

        #self.play(l.fade_all_but, 3)
        self.wait(15)


class PourquoiMES(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\sc Explication: Mise en évidence simple}", color=PURPLE).to_corner(UL).scale(1.25)
        title.move_to(0 * LEFT + 3 * UP)

        context = TextMobject(r"La mise en évidence simple est possible par l'axiome de distributivité.")
        context.scale(0.85)
        context.move_to(0* LEFT + 2*UP)
        context.set_color(YELLOW)

        distributivite = TextMobject(r"$a(b+c)=ab+ac$")
        distributivite.scale(1)
        distributivite.move_to(2 * LEFT + 1 * UP)
        distributivite.set_color(WHITE)

        texte_distributivite = TextMobject(r"(Par distributivité)")
        texte_distributivite.scale(1)
        texte_distributivite.move_to(4 * RIGHT + 1 * UP)
        texte_distributivite.set_color(WHITE)

        mes = TextMobject(r"$ab+ac=a(b+c)$")
        mes.scale(1)
        mes.move_to(2 * LEFT + 1 * DOWN)
        mes.set_color(WHITE)

        texte_mes = TextMobject(r"(Par symétrie)")
        texte_mes.scale(1)
        texte_mes.move_to(4 * RIGHT + 1 * DOWN)
        texte_mes.set_color(WHITE)

        self.play(Write(title))
        self.play(Write(context))
        self.play(Write(distributivite))
        self.wait(5)
        self.play(Write(texte_distributivite))
        self.wait(5)
        self.play(Write(mes))
        self.play(Write(texte_mes))
        #self.play(l.fade_all_but, 3)
        self.wait(10)



class MiseEvidenceDouble(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\sc Mise en évidence double}", color=PURPLE).to_corner(UL).scale(1.25)
        title.move_to(3 * LEFT + 3 * UP)

        context = TextMobject(r"Pour $a,b,c$ et $d\in\mathbb{R}$:")
        context.scale(1)
        context.move_to(4.75* LEFT + 2*UP)

        distributivite = TextMobject(r"$ac + ad + bc + bd = (a+b)(c+d)$")
        distributivite.scale(1)
        distributivite.move_to(0 * LEFT + 1 * UP)
        distributivite.set_color(WHITE)


        titre_exemple = TextMobject(r"\underline{\sc Idée}", color=PURPLE)
        titre_exemple.move_to(6.25 * LEFT + 1 * DOWN)
        exemple_1 = TextMobject(r"L'idée de la mise en évidence double est d'effectuer une séquence de deux mises en évidence.")
        exemple_1.scale(0.85)
        exemple_1.move_to(0 * LEFT + 2 * DOWN)
        exemple_1.set_color(WHITE)

        self.play(Write(title))
        self.play(Write(context))
        self.play(Write(distributivite))
        self.wait(10)
        self.play(Write(titre_exemple))
        self.play(Write(exemple_1))
        self.wait(15)


class Recette(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\sc Recette de la mise en évidence double}", color=GOLD).to_corner(UL)
        definition = TextMobject(r"""\RedBox[label=exsecond]{}{
                                     \begin{enumerate}
                                     \item Regrouper les termes ayant des facteurs communs.
                                     \item Effectuer une mise en évidence simple pour chaque groupe.
                                     \item Effectuer une deuxième mise en évidence avec le terme commun. 
                                     \end{enumerate}
                                    }      
                                """
                                 )
        definition.scale(0.7)

        self.play(Write(title))
        self.wait(10)
        self.play(FadeIn(definition))
        self.wait(45)
        self.play(FadeOut(definition))
        self.play(FadeOut(title))


class RecetteExemple(Scene):
    def construct(self):
        title = TextMobject(r"\underline{\sc Exemple:}", color=PURPLE).to_corner(UL).scale(1.25)
        title.move_to(5 * LEFT + 3 * UP)

        eq_1 = TextMobject(r"$x^{2}$", r" $+$ ", r"$4x$", r" $+$ ", r"$4$ ")
        eq_1[2].set_color(YELLOW)
        eq_1.scale(1)
        eq_1.move_to(3.6*LEFT + 1*UP)

        substitution_2 = TextMobject(r"(Étape 1)")
        substitution_2.scale(0.8)
        substitution_2.move_to(5 * RIGHT + 0 * UP)

        substitution_3 = TextMobject(r"(Étape 2)")
        substitution_3.scale(0.8)
        substitution_3.move_to(5 * RIGHT + 1 * DOWN)

        eq_2 = TextMobject(r" $=$ ", r"$x^{2}$", r" $+$ ", r"$2x$", r" $+$ ", r"$2x$", r" $+$ ", r"$4$")
        eq_2[3].set_color(YELLOW)
        eq_2[5].set_color(YELLOW)
        eq_2.scale(1)
        eq_2.move_to(0.25 * RIGHT + 1 * UP)

        eq_3 = TextMobject(r" $=$ ", r"$($", r"$x^{2}$", r" $+$ ", r"$2x$", r"$)$",
                           r" $+$ ", r"$($", r"$2x$", r" $+$ ", r"$4$", r"$)$")
        eq_3[1].set_color(RED)
        eq_3[5].set_color(RED)
        eq_3[7].set_color(BLUE)
        eq_3[11].set_color(BLUE)
        eq_3.scale(1)
        eq_3.move_to(0.6 * RIGHT + 0 * UP)

        eq_4 = TextMobject(r"$=$ ", r"$x$", r"$(x+2)$", r" $+$ ", r"$2$", r"$(x+2)$")
        eq_4[1].set_color(RED)
        eq_4[4].set_color(BLUE)
        eq_4.scale(1)
        eq_4.move_to(0.4 * RIGHT + 1 * DOWN)

        substitution_4 = TextMobject(r"(Étape 3)")
        substitution_4.scale(0.8)
        substitution_4.move_to(5 * RIGHT + 2 * DOWN)

        eq_5 = TextMobject(r"$=$ ", r"$(x+2)$", r"$($", r"$x$", r" $+$ ", r"$2$", r"$)$")
        eq_5[1].set_color(GREEN)
        eq_5[3].set_color(RED)
        eq_5[5].set_color(BLUE)
        eq_5.scale(1)
        eq_5.move_to(0.15 * LEFT + 2 * DOWN)

        #square = Square(side_length=0.25, fill_color=GOLD, fill_opacity=1, color=ORANGE)
        #square.move_to(5 * RIGHT + 3 * DOWN)


        self.play(Write(title))
        self.play(Write(eq_1))
        self.wait(5)
        self.play(Write(eq_2))
        self.play(Write(substitution_2))
        self.wait(5)
        self.play(Write(eq_3))
        self.wait(5)
        self.play(Write(eq_4))
        self.play(Write(substitution_3))
        self.wait(5)
        eq_4[2].set_color(GREEN)
        eq_4[5].set_color(GREEN)
        self.wait(5)
        self.play(Write(eq_5))
        self.play(Write(substitution_4))
        #self.play(Write(square))
        self.wait(15)


class FactoExoSup(Scene):
    CONFIG = {
        "square_scale": 1,
        "squares_colors": [WHITE, YELLOW]
    }
    # TO-DO :
    # Time limit. Find the answers.
    # Put the solution on both sides.
    def construct(self):
        title = TextMobject(r"\underline{\sc Exercices supplémentaires}").to_corner(UL).set_color(PURPLE).scale(1.15)
        exos = TextMobject(r" Factoriser les expressions suivantes avec la mise en évidence double:",
        r"""
        \begin{enumerate}
        \item $ac-bc+a-b$,
        \item $12x-y^{3}+3xy^{2}-4y$.
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
        timers = [TexMobject(str(i)).move_to(circ) for i in range(5, -1, -1)]
        pause = TextMobject("Faites pause et trouvez les solutions.").next_to(circ, RIGHT)
        self.play(ShowCreation(circ), Write(pause))
        self.play(Write(timers[0]), run_time=0.5)
        for i in range(5):
            self.play(ReplacementTransform(timers[i], timers[i + 1]), run_time=0.5)
            self.wait(0.5)
        self.play(FadeOut(pause), FadeOut(timers[-1]), FadeOut(circ), run_time=2)

        answer = TextMobject("Solutions (respectivement): $(a-b)(c+1)$, $(y^{2}+4)(3x-y)$").to_corner(DL)
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
        title = TextMobject(r"\underline{\sc Conclusion}", color=WHITE).to_corner(UL).set_color(PURPLE)

        compl_rules_str = [
            "",
            "Factoriser avec la mise en évidence simple ou double.",
            "Comprendre le lien entre la mise en évidence et la distributivité.",
        ]

        def choose_color(i):
            color = BLUE if i<=2 else YELLOW
            return color

        rules = [TextMobject("{}) {}".format(i, rule), color=choose_color(i)) for i, rule in enumerate(compl_rules_str)]
        rules = [rule.scale(0.65) for rule in rules]

        for (i, rule) in enumerate(rules):
            if i != 0:
                rule.next_to(rules[0].get_center() - rule.get_center() + np.array([-6, -0.7 * i, 0]))
        rules = VGroup(*rules)
        rules.to_corner(LEFT + UP)

        self.play(Write(title))
        self.wait(10)
        self.play(Write(rules[1]))
        self.wait(5)
        self.play(Write(rules[2]))
        self.wait(10)


class Credits(Scene):
    def wplay(self, *args, wait=1, run_time=1, rate_func=smooth):
        self.play(*args, run_time=run_time, rate_func=rate_func)
        if wait != 0:
            self.wait(wait)

    def construct(self):
        credits = TextMobject("Crédits").set_color(YELLOW).scale(1.7)
        thanks = TextMobject("Merci pour votre visionnement!!").set_color(ORANGE).scale(1.7)

        instructor = TexMobject(r"\text{Enseignant}", r"\text{Louis-Marc Mercier}")
        viewer = TexMobject(r"\text{Spectateur}", r"\text{Vous}")
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


class NumberedList(BulletedList):
    CONFIG = {
        "dot_scale_factor": 1,
        "num_color": BLUE,
    }

    def __init__(self, *items, **kwargs):
        line_separated_items = [s + "\\\\" for s in items]
        TextMobject.__init__(self, *line_separated_items, **kwargs)
        #for num, part in enumerate(self):
            #dot = TextMobject(f"{num+1}) ", color=self.dot_color).scale(
            #    self.dot_scale_factor)
            #dot.next_to(part[0], LEFT, MED_SMALL_BUFF)
            #part.add_to_back(dot)
        #self.arrange(
        #    DOWN,
        #    aligned_edge=LEFT,
        #    buff=self.buff
        #)
