from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()

    def updated(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def score_player_one(self):
        self.speed("fastest")
        self.goto(-100, 260)
        self.updated()

    def score_player_two(self):
        self.speed("fastest")
        self.goto(100, 260)
        self.updated()

    def increase(self):
        self.score += 1
        self.clear()
        self.updated()

    def win_player_one(self):
        self.goto(0, 0)
        self.write(f"Player one wins, score {self.score}", align="center", font=("Arial", 24, "normal"))

    def win_player_two(self):
        self.goto(0, 0)
        self.write(f"Player two wins, score {self.score}", align="center", font=("Arial", 24, "normal"))
