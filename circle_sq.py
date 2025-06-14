from manim import *
class CircleSquare(Scene):
    def construct(self):
        circle = Circle(radius=1, color=YELLOW)
        square = Square(side_length=2, color=BLUE)
        self.play(Create(circle))
        self.wait(1)
        self.play(Transform(circle, square))
        self.wait(1)
        self.play(FadeOut(circle))