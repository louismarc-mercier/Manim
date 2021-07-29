from manimlib.imports import *
from manim_utils.slide_template import BoxedTitle, GenChannelLogo, YoutubeLogo
from MyAnim.RevisionSecondaire.id_rem_french import MeasureDistance
import pandas as pd
import numpy as np


class CTM_blanc(Scene):
    CONFIG = {
        "camera_config":{"background_color": WHITE}
    }

    def construct(self):
        # Creating the logo
        screen_border = RoundedRectangle(height= 3.5, width= 3.5, fill_opacity=5).set_color(BLACK)
        inside_screen = Rectangle(height= 3.0, width= 3.0, fill_opacity=5).next_to(screen_border, 0, buff=0)
        inside_screen.set_fill()
        inside_screen.set_color(WHITE)
        text = TextMobject('>>', 'C', r'$\tau$', r'$M$').set_color("#0079C2")
        text.scale(1.25)
        text[0].scale(1)
        text[2].scale(1.5)
        #text[3].rotate(-PI/2)
        text.next_to(inside_screen, 0, buff=0)

        screen_support = Rectangle(height= 0.35, width= 0.75, fill_opacity=5).next_to(screen_border, DOWN, buff=0.25*SMALL_BUFF)
        screen_support.set_color(BLACK)

        screen_base = Rectangle(height= 0.25, width= 1.75, fill_opacity=5).next_to(screen_support, DOWN, buff=0.25*SMALL_BUFF)
        screen_base.set_color(BLACK)

        full_text = TextMobject("<", "Code", r"$+$",  "tes", r"$+$",  "maths", ">").next_to(screen_base, DOWN)
        full_text[0].set_color(BLACK)
        full_text[6].set_color(BLACK)
        full_text[3].set_color(BLACK)
        full_text[1].set_color("#0079C2")
        full_text[5].set_color("#0079C2")
        full_text[2].set_color("#D8D8D8")
        full_text[4].set_color("#D8D8D8")
        full_text.scale(1.5)


        self.play(DrawBorderThenFill(screen_border,  run_time=0.5), DrawBorderThenFill(inside_screen, run_time=0.5),
                  DrawBorderThenFill(screen_support, run_time=0.5), DrawBorderThenFill(screen_base, run_time=0.5))
        #self.play(DrawBorderThenFill(inside_screen, run_time=1))
        #self.play(DrawBorderThenFill(screen_support, run_time=1))
        #self.play(DrawBorderThenFill(screen_base, run_time=1))
        #self.wait(1)
        self.play(Write(text))
        self.wait(1)
        self.play(Write(full_text))
        self.wait(1)


class CTM_noir(Scene):
    CONFIG = {
        "camera_config":{"background_color": BLACK}
    }

    def construct(self):
        # Creating the logo
        screen_border = RoundedRectangle(height= 3.5, width= 3.5, fill_opacity=5).set_color(WHITE)
        inside_screen = Rectangle(height= 3.0, width= 3.0, fill_opacity=5).next_to(screen_border, 0, buff=0)
        inside_screen.set_fill()
        inside_screen.set_color(BLACK)
        text = TextMobject('>>', 'C', r'$T$', r'$M$').set_color("#0079C2")
        text.scale(1.25)
        text[0].set_color(WHITE).scale(1)
        #text[2].scale(1.5)
        #text[3].rotate(-PI/2)
        text.next_to(inside_screen, 0, buff=0)

        screen_support = Rectangle(height= 0.35, width= 0.75, fill_opacity=5).next_to(screen_border, DOWN, buff=0.25*SMALL_BUFF)
        screen_support.set_color(WHITE)

        screen_base = Rectangle(height= 0.25, width= 1.75, fill_opacity=5).next_to(screen_support, DOWN, buff=0.25*SMALL_BUFF)
        screen_base.set_color(WHITE)

        full_text = TextMobject("<", "Code", r"$+$",  "tes", r"$+$",  "maths", ">").next_to(screen_base, DOWN)
        full_text[0].set_color(WHITE)
        full_text[6].set_color(WHITE)
        full_text[3].set_color("#0079C2")
        full_text[1].set_color("#0079C2")
        full_text[5].set_color("#0079C2")
        full_text[2].set_color("#D8D8D8")
        full_text[4].set_color("#D8D8D8")
        full_text.scale(1.5)


        self.play(DrawBorderThenFill(screen_border,  run_time=0.5), DrawBorderThenFill(inside_screen, run_time=0.5),
                  DrawBorderThenFill(screen_support, run_time=0.5), DrawBorderThenFill(screen_base, run_time=0.5))
        #self.play(DrawBorderThenFill(inside_screen, run_time=1))
        #self.play(DrawBorderThenFill(screen_support, run_time=1))
        #self.play(DrawBorderThenFill(screen_base, run_time=1))
        #self.wait(1)
        self.play(Write(text))
        self.wait(0.5)
        self.play(Write(full_text))
        self.wait(1)