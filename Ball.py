from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("slowest")
        self.penup()
        self.color("white")
        self.shape("circle")
        self.move_x = 15
        self.move_y = 15
        self.move_speed = 0.1

    def refresh(self):
        self.goto(0, 0)
        self.move_speed = 0.1

    def ball_movement(self):
        new_y = self.ycor() + self.move_y
        new_x = self.xcor() + self.move_x
        self.goto(new_x, new_y)

    def bounce(self):
        self.move_y *= -1

    def bounce_padle(self):
        self.move_x *= -1
        self.move_speed *= 0.9
