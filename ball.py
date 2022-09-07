from turtle import Turtle, Screen
import time

SCREEN = Screen()


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # ball is moving in a y-axis positive direction. when it hits the top or bottom wall,
        # the heading of the ball heads in the exact opposite direction along the y-axis
        # the x-axis direction does not change
        # therefore, simply multiply the y-move (direction) by -1 to reverse the ball's course
        self.y_move *= -1

    def bounce_x(self):
        # bounces the ball in the opposite direction along the x-axis off of each paddle
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        SCREEN.update()
        time.sleep(1)
        self.move_speed = 0.1
        self.bounce_x()
