from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.p1_score = 0
        self.p2_score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"{self.p1_score} : {self.p2_score}", align="center")

    def end_game(self):
        self.goto(0, 0)
        if self.p1_score == self.p2_score:
            self.write("DRAW", align="center")
        elif self.p1_score > self.p2_score:
            self.write("LEFT WINS", align="center")
        else:
            self.write("RIGHT WINS", align="center")