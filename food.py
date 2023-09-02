from turtle import Turtle
import random
SHAPE_SIZE = 0.5


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=SHAPE_SIZE,stretch_len=SHAPE_SIZE)
        self.refresh()

    def refresh(self):
        x_distance=random.randint(-280,280)
        y_distance=random.randint(-280,280)
        self.goto(x_distance,y_distance)

