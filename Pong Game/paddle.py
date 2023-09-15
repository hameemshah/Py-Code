import turtle 
turtle.mode(mode='logo')

class Paddle(turtle.Turtle):
    
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.shapesize(1, 5)
        self.pu()
        self.goto(pos)

    def up(self):
            self.fd(80)

    def down(self):
            self.bk(80)
        

