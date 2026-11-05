import turtle
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.penup()
        self.pencolor("white")
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.goto(x=0, y=260)
        self.update_scoreboard()
        self.hideturtle()

    def increase_score(self):
        self.count += 1

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.count} High Score: {self.highscore}", False, "center", ("Arial", 20,"normal"))

    def reset(self):
        if self.count > self.highscore:
            self.highscore = self.count
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.count = 0
        self.update_scoreboard()

