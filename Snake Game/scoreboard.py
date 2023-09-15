from turtle import Turtle
ALIGN = "center"
FONT = "Courier"


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('../../../data.txt', 'r') as file:
            contents = file.read()
            self.high_score = int(contents)
        self.pu()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align=ALIGN, font=(FONT, 24, "normal"))
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('../../../data.txt', "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
    
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()