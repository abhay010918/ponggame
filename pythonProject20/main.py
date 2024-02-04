from turtle import Screen
from paddle import Paddle
from boll import Boll
from scoreboard import Scoreboard
import time

r_paddle = Paddle((340, 0))
l_paddle = Paddle((-340, 0))
boll = Boll()
scoreboard = Scoreboard()

screen = Screen()
screen.screensize(800, 600)
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "z")

game_is_on = True
while game_is_on:
    time.sleep(boll.move_speed)
    screen.update()
    boll.move()

    # Detect collision with boll
    if boll.ycor() > 280 or boll.ycor() < -280:
        boll.bounce_Y()

    # Detect collision with paddles
    if (
        (boll.distance(r_paddle) < 50 and boll.xcor() > 310) or
        (boll.distance(l_paddle) < 50 and boll.xcor() < -310)
    ):
        boll.bounce_X()

    # Detect right paddle missed
    if boll.xcor() > 380:
        boll.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    # Detect left paddle missed
    if boll.xcor() < -380:
        boll.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()

screen.exitonclick()
