import turtle 
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    ball.move()
    time.sleep(ball.move_speed)
    screen.update()
    
    #Detect colloison with walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    
    #Detect colloison with paddle
    if ball.xcor() > 320 and r_paddle.distance(ball) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
    
    #Detect missed ball
    if ball.xcor() > 380:
        ball.reset()
        score.l_point()
        
    if ball.xcor() < -380:
        ball.reset()
        score.r_point()

screen.exitonclick( )
