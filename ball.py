from turtle import Turtle
import time
import random

STEP = 3


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        direction = [random.randint(-45, 45), random.randint(135, 225)]
        self.setheading(random.choice(direction))
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        self.forward(STEP)
        time.sleep(0.001)

    def collision(self):
        angle = -self.heading()
        self.setheading(angle)

    def pad_collision(self):
        angle = -self.heading() + 180
        self.setheading(angle)
        self.forward(2*STEP)  # slight acceleration to avoid getting caught in wall boundary condition glitch
