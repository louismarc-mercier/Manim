from big_ol_pile_of_manim_imports import *


class FirstProperty(Scene):
    def construct(self):
        text=TexMobject(
            "\\frac{d(f+g)}{dx}(x_{0})=",       #0
            "\\frac{df}{dx}(x_{0})",        #1
            "+",                            #2
            "\\frac{dg}{dx}(x_{0})"         #3
        )
        self.play(Write(text))
        brace1 = Brace(text[1], UP, buff = SMALL_BUFF)
        brace2 = Brace(text[3], UP, buff = SMALL_BUFF)
        t1 = brace1.get_text("$f'(x_{0})$")
        t2 = brace2.get_text("$g'(x_{0})$")
        self.play(
            GrowFromCenter(brace1),
            FadeIn(t1),
            )
        self.wait()
        self.play(
        	ReplacementTransform(brace1, brace2),
        	ReplacementTransform(t1, t2)
        	)
        self.wait()

        # Remove the showed property.
        objects = [t2, brace2, text]
        for object in objects:
            self.play(FadeOut(object))


class SecondProperty(Scene):
    def construct(self):
        text=TexMobject(
            "\\frac{d(fg)}{dx}(x_{0})=",       #0
            "f(x_{0})\\frac{dg}{dx}(x_{0})",        #1
            "+",                            #2
            "g(x_{0})\\frac{df}{dx}(x_{0})"         #3
        )
        self.play(Write(text))
        brace1 = Brace(text[1], UP, buff = SMALL_BUFF)
        brace2 = Brace(text[3], UP, buff = SMALL_BUFF)
        t1 = brace1.get_text("$f(x_{0})g'(x_{0})$")
        t2 = brace2.get_text("$g(x_{0})f'(x_{0})$")
        self.play(
            GrowFromCenter(brace1),
            FadeIn(t1),
            )
        self.wait()
        self.play(
        	ReplacementTransform(brace1, brace2),
        	ReplacementTransform(t1, t2)
        	)
        self.wait()

        # Remove the showed property.
        objects = [t2, brace2, text]
        for object in objects:
            self.play(FadeOut(object))


class ThirdProperty(Scene):
    def construct(self):
        text=TexMobject(
            "\\frac{d(f\mathbin{/}g)}{dx}(x_{0})=",       #0
            "\\frac{f'(x_{0})g(x_{0})-f(x_{0})g'(x_{0})}{g^{2}(x_{0})}",      #1
        )
        self.play(Write(text))
        self.wait()

        # Remove the showed property.
        self.play(FadeOut(text))


class FourthProperty(Scene):
    def construct(self):

        text=TexMobject(
            "\\frac{d(h \circ f)}{dx}(x_{0})=",       #0
            "\\frac{dh}{dx}(f(x_{0}))\\frac{df}{dx}(x_{0})",      #1
        )
        self.play(Write(text))
        brace = Brace(text[1], UP, buff = SMALL_BUFF)
        t = brace.get_text("$h'(f(x_{0}))f'(x_{0})$")
        self.play(
            GrowFromCenter(brace),
            FadeIn(t),
            )
        self.wait()

        # Remove the showed property.
        objects = [t, brace, text]
        for object in objects:
            self.play(FadeOut(object))


class DerivativeProperties(Scene):

    def construct(self):
        # Generate the title
        Title = TextMobject(r"\textbf{Th\'eor\`eme}: Si $f,g:(a,b)\rightarrow\mathbb{R}$ sont d\'erivables en $x_{0}\in(a,b)$, alors")
        Title.scale(0.75)
        Title.move_to(np.array([-1,3,0]))

        captions = [r"1. $f+g$ est d\'erivable en $x_{0}$ et:",
                    r"2. $fg$ est d\'erivable en $x_{0}$ et:",
                    r"3. Si $g(x_{0})\neq 0 $, $f\mathbin{/}g$ est d\'erivable en $x_{0}$ et:",
                    r"4. Si $f((a,b))\subseteq (c,d)$ et si $h:(c,d)\rightarrow \mathbb{R}$ est d\'erivable en $f(x_{0})$ alors, $h\circ f$ est d\'erivable en $x_{0}$ et"
                    ]
        captions_position = [np.array([-4,2.1,0]), np.array([-4.2, 2.1, 0]), np.array([-3, 2.1, 0]), np.array([-2, 2.1, 0])]
        captions_properties = [TextMobject(caption) for caption in captions]
        [caption_property.scale(0.7) for caption_property in captions_properties]
        [caption_property.move_to(caption_position) for caption_property, caption_position in zip(captions_properties, captions_position)]
        captions_properties[-1].scale(0.75)

        # Display title
        self.play(Write(Title))

        properties_classes = [FirstProperty, SecondProperty, ThirdProperty, FourthProperty]
        for i, caption_property in enumerate(captions_properties):
            self.play(Write(caption_property))
            properties_classes[i].construct(self)

            # Make the first property dissapears
            self.play(FadeOut(caption_property))
            self.wait(2)




