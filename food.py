from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.food_eaten = 3
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.respawn()

    def respawn(self):
        self.food_eaten += 1
        if self.food_eaten > 25:
            self.food_eaten = 0
        if self.food_eaten / 5 <= 1:
            self.color("white")
        elif self.food_eaten / 10 <= 1:
            self.color("blue")
        elif self.food_eaten / 15 <= 1:
            self.color("red")
        elif self.food_eaten / 20 <= 1:
            self.color("yellow")
        elif self.food_eaten / 25 <= 1:
            self.color("pink")

        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)
