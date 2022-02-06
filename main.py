# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from turtle import Turtle, Screen
from player import Player
import time, ball

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
tim = Turtle()
tim.goto(x=0, y=250)
tim.setheading(270)
tim.color("white")
tim.pensize(width=5)
tim.hideturtle()

while tim.ycor() > -270:
    tim.forward(10)
    tim.penup()
    tim.forward(15)
    tim.pendown()

playerOne = Player("player one")
playerTwo = Player("player two")
screen.onkey(fun=playerOne.moveDown, key="Down")
screen.onkey(fun=playerOne.moveUp, key="Up")
screen.onkey(fun=playerTwo.moveUpNegative, key="W")
screen.onkey(fun=playerTwo.moveDownNegative, key="X")
screen.listen()
game_is_on = True
ball = ball.Ball()
ball.penup()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    #playerOne.move()
    ball.move()
    ball.checkPaddleCollision(rightSidePlayer=playerOne, leftSidePlayer=playerTwo)
    ball.checkFloorCollision()
    ball.checkRoofCollision()
    ball.checkWallCollision()



screen.exitonclick()