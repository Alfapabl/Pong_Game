import time
from turtle import Screen
from Paddle import Paddle
from ScoreBoard import Score
from Ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

'#Padles'
padle = Paddle()
padle_pc = Paddle()
padle.padle_one()
padle_pc.padle_two()
'#Scores'
score_one = Score()
score_two = Score()
score_one.score_player_one()
score_two.score_player_two()
'#Ball'
ball = Ball()
'#Movement'
screen.listen()
screen.onkey(padle.up, "Up")
screen.onkey(padle.down, "Down")
screen.onkey(padle_pc.up, "w")
screen.onkey(padle_pc.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_movement()
    '#wall colision'
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    '#score update'
    if ball.xcor() > 400:
        score_two.increase()
        ball.refresh()

    if ball.xcor() < -400:
        score_one.increase()
        ball.refresh()
    '#Paddle colision'
    if ball.distance(padle_pc) < 20 or ball.distance(padle) < 20:
        ball.bounce_padle()
    if score_one.score == 5:
        score_one.win_player_one()
        game_is_on = False
    if score_two.score ==5:
        score_two.win_player_two()
        game_is_on = False

screen.exitonclick()