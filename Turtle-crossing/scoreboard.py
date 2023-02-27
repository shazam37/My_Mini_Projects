from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'LEVEL: {self.score}', align='left', font = FONT)

    def increase_level(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(f'GAME OVER!', align='center', font=FONT)


