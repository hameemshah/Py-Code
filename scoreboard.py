from turtle import Turtle
ALIGN = "center"
FONT = "Courier"


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
            self.write(f"Score : {self.score}", align=ALIGN, font=(FONT, 24, "normal"))
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=(FONT, 24, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()