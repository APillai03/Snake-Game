from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(-20,270)
        self.color('white')
    def updater(self):
        self.clear()
        self.score +=1
        self.writer()
    def writer(self):
        self.write(f'Score: {self.score}',font=("Arial",16,"italic"))
    def gameover(self):
        self.clear()
        self.goto(-130,80)
        self.color('red')
        self.write(f'GAME OVER\n Your Score: {self.score}',font=("Arial",32,"italic"))

