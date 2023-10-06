from turtle import Turtle
COLORS = ["white", "blue", "red", "yellow"]
class Snake:

    def __init__(self):
        self.body = []
        self.move_distance = 20
        self.segment_num = 0
        # start going right, then can go up, left, down
        self.directions = [True, False, False, False]
        # now spawn snake
        self.spawn_snake()
        self.head = self.body[0]

    def spawn_snake(self):
        for i in range(3):
            self.add_segment()

    def extend(self):
        self.add_segment()

    def add_segment(self):
        self.segment_num += 1
        snake_square = Turtle(shape="square")
        snake_square.penup()
        if len(self.body) >= 3:  # fixes bug where player sees new snake_square at (0,0); must occur after snake spawns or else game over will occur
            snake_square.goto(self.body[-1].position())
        snake_square.speed("fastest")

        if self.segment_num > 25:
            self.segment_num = 0

        if self.segment_num / 5 <= 1:
            snake_square.color("white")
        elif self.segment_num / 10 <= 1:
            snake_square.color("blue")
        elif self.segment_num / 15 <= 1:
            snake_square.color("red")
        elif self.segment_num / 20 <= 1:
            snake_square.color("yellow")
        elif self.segment_num / 25 <= 1:
            snake_square.color("pink")
        print(self.segment_num)
        self.body.append(snake_square)

    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        self.body[0].forward(self.move_distance)

    def right(self):
        if self.directions[2] == False:
            self.body[0].setheading(0)
            self.directions = [True, False, False, False]

    def left(self):
        if self.directions[0] == False:
            self.body[0].setheading(180)
            self.directions = [False, False, True, False]

    def down(self):
        if self.directions[1] == False:
            self.body[0].setheading(270)
            self.directions = [False, False, False, True]

    def up(self):
        if self.directions[3] == False:
            self.body[0].setheading(90)
            self.directions = [False, True, False, False]
