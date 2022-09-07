from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.listen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("GT's Pong Game")
# if turn off the screen tracer, then paddle will be created in the background and will not show up
# must create a while loop to update the screen once the paddle is created and moves to location
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# W and S keys are used to move Left Paddle, Up and Down arrow keys are used to move Right Paddle
screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# must use this screen update method if screen tracer has been turned off ->
# when paddle moves, screen is updated and the paddle appears in correct location
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when right paddle misses the ball -> reset ball -> add score left player
    if ball.xcor() > 400:
        ball.reset()
        scoreboard.clear()
        scoreboard.l_point()

    # detect when left paddle misses the ball -> reset ball -> add score right player
    if ball.xcor() < -400:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
