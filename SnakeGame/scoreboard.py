from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 12, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 12, "normal"))





