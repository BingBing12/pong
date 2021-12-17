from turtle import Turtle
import time
import random

STEP = 7


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        direction = [45, 135]
        self.setheading(random.choice(direction))
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_speed = 0.05

    def move(self):
        self.forward(STEP)
        time.sleep(self.move_speed)

    def collision(self):
        angle = -self.heading()
        self.setheading(angle)

    def pad_collision(self):
        angle = -self.heading() + 180
        self.setheading(angle)
        #self.forward(2*STEP)  # slight acceleration to avoid getting caught in wall boundary condition glitch
        self.move_speed *= 0.8
