from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        self.tail = self.body[1:]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)

    def add_square(self, position):
        new_square = Turtle("square")
        new_square.color(255, 255, 255)
        new_square.penup()
        new_square.goto(position)
        if len(self.body) > 0:
            new_square.setheading(self.body[-1].heading())
        self.body.append(new_square)

    def extend(self):
        self.add_square(self.body[-1].position())

    def move(self):
        for square_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[square_num - 1].xcor()
            new_y = self.body[square_num - 1].ycor()
            self.body[square_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def north(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def west(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def south(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def east(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
