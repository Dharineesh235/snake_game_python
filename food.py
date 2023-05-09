import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color('yellow')
        self.refresh()

    # method to give random position for food
    def refresh(self):
        random_pos = random.randint(-280, 280)
        self.goto(random_pos, random_pos)
