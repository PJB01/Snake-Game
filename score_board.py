from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 260)
        self.cur_score = 0
        self.color("white")
        self.hideturtle()
        self.write(f"score: {self.cur_score} ", align='center', font=('courier', 16, 'bold'))


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=('courier', 24, 'bold'))


    def update_score(self):
        self.cur_score = self.cur_score + 1
        cur_score = self.cur_score + 1
        self.clear()
        self.write(f"score: {self.cur_score} ", align='center', font=('courier', 16, 'bold'))
        return self.cur_score
