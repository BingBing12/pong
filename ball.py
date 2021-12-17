from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        self.forward(2)
        time.sleep(0.001)

    def collision(self):
        angle = -self.heading()
        self.setheading(angle)

    def pad_collision(self):
        angle = -self.heading() + 180
        self.setheading(angle)
        self.forward(4)  # slight acceleration to avoid getting caught in wall boundary condition glitch
