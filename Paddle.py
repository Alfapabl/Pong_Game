from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=2.5, stretch_len=0.5)
        self.move_y = 5


    def padle_one(self):
        self.speed("fastest")
        self.setx(-380)

    def padle_two(self):
        self.speed("fastest")
        self.setx(380)

    def up(self):
        if(self.ycor() < 260):
            self.sety(self.ycor()+35)

    def down(self):
        if (self.ycor() > -260):
            self.sety(self.ycor()-35)

















