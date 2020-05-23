from big_ol_pile_of_manim_imports import *

class PythagoreanProof(Scene):
    CONFIG = {
        "square_scale": 2,
        "squares_colors": [WHITE, YELLOW]
    }
    def construct(self):
        CONFIG = {
            "square_scale": 2,
            "squares_colors": [WHITE, YELLOW]
        }

        # Define two squares (one yellow and one white, opacity allows to fill color in figure).
        left_square, right_square = Square(), Square()

        # Put the two squares next to another.
        VGroup(left_square, right_square)\
                .scale(self.square_scale)\
                .arrange_submobjects(RIGHT,buff=2)


        # LEFT SQUARE SETTINGS

        ## Configure dots to draw triangles inside left square.
        dots = [left_square.point_from_proportion(i * 1/4 + 1/16) for i in range(4)]     # Segment lines of square.
        dots_corners = [left_square.point_from_proportion(i * 1/4) for i in range(4)]    # In corners of square.

        ## Configure the triangles inside the left square.
        triangles = VGroup(*[Polygon(dots[i], dots_corners[i], dots[i - 1],
                stroke_width=2.5, fill_opacity=0.25, color=YELLOW) for i in range(4)])

        ## Configure the inside left square which has its own color.
        left_inside_square = VGroup(Polygon(dots[0], dots[1], dots[2], dots[3], stroke_width=2.5,
                                       fill_opacity=0.5, color=ORANGE))

        # RIGHT SQUARE SETTINGS
        ## Configure dots to draw triangles inside right square.
        dots2 = [right_square.point_from_proportion(i * 1 / 4 + j * 1 / 16) for i, j in zip(range(4), [1, 3, 3, 1])]
        dots_corners2 = [right_square.point_from_proportion(i * 1 / 4) for i in range(4)]
        middle = np.array([dots2[0][0], dots2[1][1], 0])


        def get_color(i):
            if i == 0 or i == 2:
                return "ORANGE"
            elif i == 1:
                return "BLUE"
            else:
                return "PURPLE"


        # Generate the rectangles and squares in which to place the triangles.
        all_rectangles = VGroup(*[Polygon(dots_corners2[i], dots2[i], middle, dots2[i - 1],
                fill_opacity=0.7, color=get_color(i)) for i in range(4)])
        rectangles = all_rectangles[0::2]   # Rectangles: rectangles of the triangles
        squares = all_rectangles[1::2]  # Big and small squares

        # Get a subset of the dots of the rectangle (interpolation created more points) ?
        total_points = 3
        rect_dot = [[rectangles[i].points[total_points * j] for j in range(4)] for i in range(2)]

        triangles2 = VGroup(*[
            Polygon(
                rect[i + 1],
                rect[i],
                rect[i - 1],
                fill_opacity=0.7
            )
            for rect in rect_dot
            for i in [0, 2]
        ])


        # Generate the title
        Title = TextMobject(r"\underline{Th\'eor\`eme de Pythagore}")
        Title.to_edge(UP + LEFT)

        # Latex formula (located at the bottom of screen).
        theorem = TexMobject("c^2", "=", "a^2", "+", "b^2").to_edge(DOWN)
        theorem[0].set_color(ORANGE)
        theorem[2].set_color(BLUE)
        theorem[4].set_color(PINK)

        # Create tex formula expressions to the new locations (in the Figure (for visualization))
        parts_theorem = VGroup(
            TexMobject("c^2").move_to(left_square),
            TexMobject("a^2").move_to(squares[0]),
            TexMobject("b^2").move_to(squares[1])
        )


        # Display title
        self.play(Write(Title))

        # Draw borders of the squares and fill them (if opacity is defined).
        self.play(*list(map(DrawBorderThenFill, [left_square, triangles.copy(), right_square])))

        # Move the triangles from the left square to the right square.
        self.play(*[ApplyMethod(triangles[i].move_to, triangles2[i].get_center()) for i in range(len(triangles))])

        # Rotate the triangles by 180 degrees.
        self.play(Rotate(triangles[1], -PI / 2), Rotate(triangles[2], PI / 2))

        # Display the left square, the small right squares and the expressions of the theorem (in small squares).
        self.play(ShowCreation(left_inside_square), ShowCreation(squares), Write(parts_theorem))

        # Replace the elements of the bottom formula by the colored one associated to the figure.
        self.play(*[ReplacementTransform(t_.copy()[:], r_, run_time=4)
                for t_, r_ in zip(parts_theorem, [theorem[0], theorem[2], theorem[4]])],
            Write(theorem[1]), Write(theorem[-2])
        )

        self.wait(3)