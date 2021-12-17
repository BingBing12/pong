from turtle import Screen
from paddle import Paddle
from ball import Ball


p1 = Paddle((-380, 0))
p2 = Paddle((370, 0))


screen = Screen()
screen.tracer(0)
ball = Ball()
screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.listen()
screen.onkey(p1.go_up, "w")
screen.onkey(p1.go_down, "s")
screen.onkey(p2.go_up, "Up")
screen.onkey(p2.go_down, "Down")

game_on = True
ball.setheading(20)
while game_on:
    screen.update()
    if ball.distance(p1) < 22 or ball.distance(p2) < 22:
        ball.pad_collision()
    if ball.ycor() > 285 or ball.ycor() < -280:
        ball.collision()
    ball.move()

screen.exitonclick()
