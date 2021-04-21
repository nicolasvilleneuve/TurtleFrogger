from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.pendown()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score : {self.score}', align='center', font=('Courier', 24))

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,200)
        self.write('Game Over', align='center', font=('Courier', 24))
        self.goto (0,150)
        self.write(f'Your score was {self.score}', align='center', font=('Courier', 24))

