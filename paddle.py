from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)
        self.up()
        self.down()

    def go_up(self):
        self.penup()
        if self.ycor() < 245:
            new_y = self.ycor() + 25
            self.goto(self.xcor(), new_y)

    def go_down(self):
        self.penup()
        if self.ycor() > -240:
            new_y = self.ycor() - 25
            self.goto(self.xcor(), new_y)

