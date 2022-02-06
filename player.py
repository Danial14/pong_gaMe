from turtle import Turtle
X_POSITIVE_AXIS = 270
X_NEGATIVE_AXIS = -270
Y_AXIS = 0
class Player(Turtle):
    def __init__(self, playerNaMe):
        super().__init__()
        self.playerNaMe = playerNaMe
        self.playerScore = 0
        self.__playerSetup()

    def __playerSetup(self):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        if self.playerNaMe == "player one":
            self.goto(x=X_POSITIVE_AXIS, y=Y_AXIS)

        elif self.playerNaMe == "player two":
            self.goto(x=X_NEGATIVE_AXIS, y=Y_AXIS)

    def moveUp(self):
        y_axis = self.ycor()
        if y_axis < 240:
            new_y = y_axis + 20
            self.goto(x=X_POSITIVE_AXIS, y=new_y)

    def moveDown(self):
        y_axis = self.ycor()
        if y_axis > -240:
            new_y = self.ycor() - 20
            self.goto(x=X_POSITIVE_AXIS, y=new_y)

    def moveUpNegative(self):
        y_axis = self.ycor()
        if y_axis < 240:
            new_y = self.ycor() + 20
            self.goto(x=X_NEGATIVE_AXIS, y=new_y)

    def moveDownNegative(self):
        y_axis = self.ycor()
        if y_axis > -240:
            new_y = self.ycor() - 20
            self.goto(x=X_NEGATIVE_AXIS, y=new_y)
