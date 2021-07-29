from manimlib.imports import *


class BoxedTitle(Rectangle):
    CONFIG = {
        "bronze": "#da9f65",
        "silver": "#D3D3D3",
        "gold": "#D4AF37"
    }

    def __init__(self, width=5, height=1, text="Description", text_color=BLACK,
                 box_split_color=BLACK, box_split_opacity=0,
                 box_color=WHITE, box_opacity=1,
                epsilon=0.1, scale=None):

        # Draw title box.
        Rectangle.__init__(self, width=width, height=height, fill_opacity=box_opacity, color=box_color)

        inside_box = Rectangle(width=width - epsilon, height=height - epsilon, fill_opacity=box_split_opacity, color=box_split_color)
        inside_box.move_to(self)

        # Write text inside the title box.
        if len(text) > 0:
            box_description = TextMobject(r"\sc{\textbf{%s}}" % text).set_color(text_color)
            if scale is None:
                scale = 0.75*height
            box_description.scale(scale)
            box_description.move_to(inside_box)

        # Add the inside box and the title
        self.add(inside_box)

        if len(text) > 0:
            self.add(box_description)


class Warning(Triangle):
    CONFIG = {
        "bronze": "#da9f65",
        "silver": "#D3D3D3",
        "gold": "#D4AF37"
    }

    def __init__(self, symbol="!", fill_opacity=0.75, color=YELLOW):

        # Draw warning symbol box.
        Triangle.__init__(self, fill_opacity=fill_opacity, color=color)
        warning_content = TexMobject(symbol, color=BLACK).scale(2.5)
        warning_content.move_to(self)

        # Add the inside box and the title
        self.add(warning_content)


class Star(Triangle):
    CONFIG = {
        "bronze": "#da9f65",
        "silver": "#D3D3D3",
        "gold": "#D4AF37"
    }

    def __init__(self, symbol="!", fill_opacity=1, color=YELLOW):

        # Draw warning symbol box.
        Triangle.__init__(self, fill_opacity=fill_opacity, color=color)

        reverse_triangle = Triangle(fill_opacity=fill_opacity, color=color)
        reverse_triangle.rotate(-PI)
        reverse_triangle.next_to(self, DOWN, buff=-1)

        # Add the inside box and the title
        self.add(reverse_triangle)


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



class YoutubeSubscribeLogo(RoundedRectangle):
    CONFIG = {
        "bronze": "#da9f65",
        "silver": "#D3D3D3",
        "gold": "#D4AF37"
    }

    def __init__(self, message="Subscribe", fill_opacity=1, color="#ff0000"):

        # Draw warning symbol box.
        RoundedRectangle.__init__(self, width=3.5, height=2, corner_radius=0.6, fill_opacity=fill_opacity, color=color)
        play_symbol = Triangle(fill_opacity=1, color=WHITE).scale(0.7)
        play_symbol.rotate(-PI/2)
        play_symbol.move_to(self)

        # Subscribe text
        description = TextMobject(message, color=color)
        description.next_to(self, DOWN, buff=MED_LARGE_BUFF).scale(1.5)

        # Add the inside box and the title
        self.add(play_symbol)
        self.add(description)



class YoutubeLogo(RoundedRectangle):
    CONFIG = {
        "bronze": "#da9f65",
        "silver": "#D3D3D3",
        "gold": "#D4AF37"
    }

    def __init__(self, fill_opacity=1, color="#ff0000"):

        # Draw warning symbol box.
        RoundedRectangle.__init__(self, width=3, height=2, corner_radius=0.6, fill_opacity=fill_opacity, color=color)

        # Subscribe text
        description_1 = TextMobject(r"\textbf{You}", color="WHITE").scale(2)
        description_1.next_to(self, LEFT)

        description_2 = TextMobject(r"\textbf{Tube}", color="BLACK").scale(2)
        description_2.move_to(self)

        # Add the inside box and the title
        self.add(description_1)
        self.add(description_2)


class GenChannelLogo(ImageMobject):

    def __init__(self, path=r"C:/Users/Utilisateur/Desktop/CEGEP/Cours_maison/", image_name="very_light_phoenix",
                 image_scale=0.65, channel_name_scale=0.5):

        # Get image from repository.
        ImageMobject.__init__(self, path + image_name)
        self.scale(image_scale)

        # Put name under the logo
        channel_name = TextMobject(r"Louis-Math")
        channel_name.next_to(self.get_corner(DL)-np.array([0.6,0,0]))
        channel_name.scale(channel_name_scale)
        channel_name.set_color_by_gradient(RED, ORANGE, GOLD, ORANGE, RED)

        # Add the channel name under the logo
        self.add(channel_name)





class Test_0(Scene):
    def construct(self):
        # Generate title
        formula = r"Work = $\int_C \overrightarrow{\textbf{F}} \bullet \textbf{d}\overrightarrow{\textbf{r}}$"
        title = BoxedTitle(width=6, height=1.5, text=formula, box_color="#D4AF37")

        # Play title
        self.play(ShowCreation(title))
        self.wait()


class Test_1(Scene):
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


class Test_2(Scene):
    def construct(self):
        # Generate logo
        channel_logo = GenChannelLogo()

        # Play title
        self.play(ShowCreation(channel_logo))
        self.wait()

class Test_3(Scene):
    def construct(self):
        # Generate logo
        warning_logo = YoutubeSubscribeLogo()

        # Play title
        self.play(DrawBorderThenFill(warning_logo))
        self.wait()


class Test_4(Scene):
    def construct(self):
        # Generate logo
        warning_logo = YoutubeLogo()

        # Play title
        self.play(DrawBorderThenFill(warning_logo))
        self.wait()


class Test_5(Scene):
    def construct(self):
        # Generate logo
        star_logo = Star()

        # Play title
        self.play(DrawBorderThenFill(star_logo))
        self.wait()


class OldTemplate(Scene):
    def construct(self):
        title_box = Rectangle(width=5, height=1, fill_opacity=1, color=WHITE)
        title_box.next_to(np.array([-3,3,0]))

        inside_box = Polygon(title_box.get_corner(UL) + np.array([0.05, -0.05, 0]),
                           title_box.get_corner(UR) + np.array([-0.05, -0.05, 0]),
                           title_box.get_corner(DR) + np.array([-0.05, 0.05, 0]),
                           title_box.get_corner(DL) + np.array([0.05, 0.05, 0]), color=BLACK, fill_opacity=0)
        inside_box.move_to(title_box)

        inside_box_description = TextMobject(r"\sc{\textbf{Description}}", color=WHITE).move_to(inside_box).set_color(BLACK)
        inside_box_description.scale(1)

        # Trailer subtitle
        #left_rectangle = Rectangle(width=0.035, height=1.25, fill_opacity=1, color=ORANGE)
        #left_rectangle.to_corner(DL)

        # Put logo on the side
        path = r"C:/Users/Utilisateur/Desktop/CEGEP/Cours_maison/"
        image = ImageMobject(path + "very_light_phoenix").next_to(np.array([-7, 3.25, 0]))
        image.scale(0.65)

        channel_name = TextMobject(r"Louis-Math")
        channel_name.next_to(np.array([-6.85, 2.6, 0]))
        channel_name.scale(0.5)
        channel_name.set_color_by_gradient(RED, ORANGE, GOLD, ORANGE, RED)


        # Displaying everything
        self.play(FadeIn(title_box), FadeIn(inside_box), FadeIn(inside_box_description))
        self.play(FadeIn(image), FadeIn(channel_name))
        self.wait(5)