from numpy import random
from turtle import Turtle

class Ball:
    def __init__(self):
        self.ball = Turtle(shape = 'circle', visible=False)
        self.time = 0.1
        self.position = (0,0)
        self.ball.penup()

    def get_random_position(self):
        position = random.randint(-14, 15, 2) * 20
        position = tuple(position)
        return position

    def make_ball(self):
        self.ball.hideturtle()
        self.position = self.get_random_position()
        self.ball.goto(self.position)
        self.ball.showturtle()
        return self.position


