from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=500,height=500)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
snake = Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
segments =[]
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detection  of food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() > 250 or snake.head.xcor() <-250 or snake.head.ycor() > 250 or snake.head.ycor() < -250:
        game_is_on =False
        scoreboard.game_over()
    #dection with tail
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment) <10:
            game_is_on=False
            scoreboard.game_over()



screen.exitonclick()

