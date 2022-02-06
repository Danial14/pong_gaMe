from turtle import Turtle
import random
Direction = ["Left", "Right"]
x_axis_start = ""
class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.color("white")
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)

    def checkPaddleCollision(self, rightSidePlayer, leftSidePlayer):
        global x_axis_start
        direction = random.choice(Direction)
        if self.distance(rightSidePlayer) <= 35:
            self.__changeBallPosition(direction=direction, player="right")

        elif self.distance(leftSidePlayer) <= 35:
            self.__changeBallPosition(direction=direction, player="left")

    def __changeBallPosition(self, direction, player):
        if player == "right":
            self.goto(self.xcor() - 2, self.ycor())
            self.changeX_axis_start("positive")
            self.__turn(direction=direction)

        elif player == "left":
            self.goto(self.xcor() + 2, self.ycor())
            self.changeX_axis_start("negative")
            self.__turn(direction=direction)

    def checkWallCollision(self):

        if self.xcor() >= 280:
            self.changeX_axis_start("positive")
            self.goto(x=0, y=0)
        elif self.xcor() <= -280:
            self.changeX_axis_start("negative")
            self.goto(x=0, y=0)


    def changeX_axis_start(self, start):
        global x_axis_start
        x_axis_start = start

    def generateAngle(self):
        global x_axis_start
        if x_axis_start == "positive":
            self.setheading(0)
        elif x_axis_start == "negative":
            self.setheading(180)
        return random.randint(95, 180)

    def generateAngleForRoofandFloorCollision(self):
        return random.randint(20, 85)

    def __turn(self, direction):
        if direction == "Left":
            self.left(self.generateAngle())
        elif direction == "Right":
            self.right(self.generateAngle())

    def checkRoofCollision(self):
        if self.ycor() >= 270:
            if x_axis_start == "negative":
                self.setheading(0)
                self.right(self.generateAngleForRoofandFloorCollision())

            else:
                self.setheading(180)
                self.left(self.generateAngleForRoofandFloorCollision())

    def checkFloorCollision(self):
        if self.ycor() <= -270:
            if x_axis_start == "negative":
                self.setheading(0)
                self.left(self.generateAngleForRoofandFloorCollision())

            else:
                self.setheading(180)
                self.right(self.generateAngleForRoofandFloorCollision())

    def move(self):
        self.forward(20)