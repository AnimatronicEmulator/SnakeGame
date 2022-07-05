from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(255, 0, 255)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.setx(random.uniform(-280, 280))
        self.sety(random.uniform(-280, 280))
