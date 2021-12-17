from turtle import Turtle, Screen
from paddle import Paddle

p1 = Paddle((-380, 0))
p2 = Paddle((380, 0))

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")


screen.onkey(p1.go_up, "w")
screen.onkey(p1.go_down, "s")
screen.onkey(p2.go_up, "Up")
screen.onkey(p2.go_down, "Down")
screen.listen()
screen.exitonclick()
