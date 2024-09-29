from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 25
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def win(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

    def reset(self):
        self.goto(STARTING_POSITION)