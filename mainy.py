from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score import score_board
import time

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My snake Game")
snake=Snake()
score=score_board()
screen.listen()

food=Food()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game= True

while(game):
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()<-280 or snake.head.ycor() >280:
        game=False
        score.game_over()
      
    for segment in snake.segment[1::]:
        if snake.head.distance(segment)<10:
            game=False
            score.game_over()

screen.exitonclick()