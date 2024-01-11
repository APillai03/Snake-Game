from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('green')
        self.speed('fastest')
        self.penup()
        self.goto(random.randint(-280,280),random.randint(-280,280))
        self.reset()
    def reset(self):
        self.goto(random.randint(-280,280),random.randint(-280,280))
    def gameset(self):
        self.hideturtle()