from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        title = Text("Pythagorean Theorem", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        triangle = Polygon(
            [0, 0, 0],  
            [3, 0, 0],  
            [3, 4, 0], 
            color=BLUE
        )
        triangle_label = MathTex("a^2 + b^2 = c^2").next_to(triangle, UP)

        self.play(Create(triangle))
        self.play(Write(triangle_label))
        self.wait(2)
