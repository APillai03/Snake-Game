from turtle import Screen,Turtle
from snake import Snake
import time
from food import Food
from score import Score

root = Screen()
root.bgcolor('black')
root.setup(height=600,width=600)
root.tracer(0)
snake = Snake()
root.listen()
try:
    with open('hs.txt', 'r') as file:
        high_score = int(file.read())
except FileNotFoundError:
    print("High score file not found. Creating a new file with a high score of 0.")
    with open('hs.txt', 'w') as file:
        file.write('0')
    high_score = 0




food = Food()
scorecard = Score()
root.onkey(snake.up,'Up')
root.onkey(snake.down,'Down')
root.onkey(snake.left,'Left')
root.onkey(snake.right,'Right')
game = True
t1= Turtle()
t1.hideturtle()
while game:
    root.update()
    time.sleep(0.1)
    snake.move()
    scorecard.writer()
    if snake.parts[0].distance(food)<20:
        snake.extend()
        food.reset()
        scorecard.updater()
    if snake.parts[0].xcor()>=300 or snake.parts[0].xcor()<=-300 or snake.parts[0].ycor()>=300 or snake.parts[0].ycor()<=-300:
        t1.clear()
        scorecard.gameover()
        game = False
        snake.gameset()
    for body in snake.parts:
        if(body==snake.parts[0]):
            pass
        elif(snake.parts[0].distance(body)<10):
            game =False
            
            snake.gameset()
            food.clear()
            t1.clear()
            scorecard.gameover()
    if(high_score<scorecard.score):
        high_score = scorecard.score
        t1.color('green')
        t1.penup()
        t1.goto(-30,250)
        t1.write('New High Score!', font=("Arial",12,'italic'))
        
with open('hs.txt', 'w') as file:
    file.write(str(high_score))

root.exitonclick()