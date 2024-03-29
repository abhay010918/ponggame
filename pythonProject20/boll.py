from turtle import Turtle

class Boll(Turtle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_Y(self):
        self.y_move *= -1

    def bounce_X(self):
        self.x_move *= -1
        self.move_speed *= 0.9  # Fix the typo here

    def reset_position(self):  # Fix the typo here
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_X()
