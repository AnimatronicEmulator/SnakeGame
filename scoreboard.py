from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 17, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(255, 255, 255)
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.write(f"Final Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(0, 0)
        self.color(255, 0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -20)
        self.write("Click anywhere on screen to exit", align=ALIGNMENT, font=FONT)