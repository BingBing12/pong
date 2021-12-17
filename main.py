from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

p1 = Paddle((-380, 0))
p2 = Paddle((370, 0))


def stop():
    global game_on
    game_on = False
    score.end_game()


screen = Screen()
screen.tracer(0)
score = Score()
screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.listen()
screen.onkey(p1.go_up, "w")
screen.onkey(p1.go_down, "s")
screen.onkey(p2.go_up, "Up")
screen.onkey(p2.go_down, "Down")
screen.onkey(stop, "space")
game_on = True


def pong():
    while game_on:
        screen.update()
        if ball.distance(p1) < 22 or ball.distance(p2) < 22:
            ball.pad_collision()
        if ball.ycor() > 285 or ball.ycor() < -280:
            ball.collision()
        if ball.xcor() > 390:
            score.p1_score += 1
            score.write_score()
            break
        elif ball.xcor() < -390:
            score.p2_score += 1
            score.write_score()
            break
        else:
            ball.move()


while game_on:
    ball = Ball()
    pong()
    ball.reset()
screen.exitonclick()
