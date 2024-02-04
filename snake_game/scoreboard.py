from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scores=0
        with open("/Users/HP/Desktop/python/snake_game/data.txt",mode="r") as file:
            self.high_score=int(file.read())
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()
    def update_scoreboard(self):
        self.clear()
        self.write(f"ScoreBoard: {self.scores}   HighScore: {self.high_score}",align="center",font=("Arial",15,"normal"))
    def is_game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=("Arial",25,"normal"))
    def increase_score(self):
        self.scores+=1
        self.clear()
        self.update_scoreboard()
    def reset(self):
        if self.scores>self.high_score:
            self.high_score=self.scores
            with open("/Users/HP/Desktop/python/snake_game/data.txt",mode="w") as file:
                file.write(f"{self.high_score}")
        self.scores=0
        self.update_scoreboard()
