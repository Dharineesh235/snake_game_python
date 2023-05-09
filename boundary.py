from turtle import Turtle


class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor('red')
        self.goto(290, -290)
        self.width(5)
        self.pendown()
        self.goto(290, 290)
        self.goto(-290, 290)
        self.goto(-290, -290)
        self.goto(290, -290)