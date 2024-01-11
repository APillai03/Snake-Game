import turtle
POSITION = [0,-20,-40]
DIS = 20
class Snake:
    def __init__(self):
        self.parts = []
        self.creator()
    
    def creator(self):
        for i in range(3):
            t1 = turtle.Turtle('circle')
            t1.color('white')
            t1.penup()
            t1.goto(POSITION[i],0)
            self.parts.append(t1)
    def extend(self):
        t1 = turtle.Turtle('circle')
        t1.color('white')
        t1.penup()
        t1.goto(self.parts[len(self.parts)-1].xcor(),self.parts[len(self.parts)-1].ycor())
        self.parts.append(t1)
    def move(self):
        for i in range(len(self.parts)-1,0,-1):
            x1 = self.parts[i-1].xcor()
            y1 = self.parts[i-1].ycor()
            self.parts[i].goto(x1,y1)
        self.parts[0].forward(DIS)
    def up(self):
        if not self.parts[0].heading() == 270:
            self.parts[0].setheading(90)
    def down(self):
        if not self.parts[0].heading() == 90:
            self.parts[0].setheading(270)
    def left(self):
        if not self.parts[0].heading() == 0:
            self.parts[0].setheading(180)
    def right(self):
        if not self.parts[0].heading() == 180:
            self.parts[0].setheading(0)
    def gameset(self):
        for part in self.parts:
            part.hideturtle()