from turtle import Turtle
from turtle import Screen
from ball import Ball
import time

screen = Screen()
screen.setup(600,600)
screen.tracer(0)
speed_of_turtle = 1
score = 0
screen.title(f'Score: {score}')

def move():
    global ball, pos_of_ball, score

    xy = snake[0].pos()
    head = round(xy[0]), round((xy[1]))
    snake[0].forward(20)
    for part in snake:
        if abs(xy[0]) >= 300 or abs(xy[1]) >= 300:
            finish_game()
            return
        if part == snake[0]:
            continue
        x_y = part.pos()
        part.goto(xy)
        xy = x_y
    time.sleep(0.12)
    screen.update()
    if head == pos_of_ball:
        score += 1
        screen.title(f'Score: {score}')
        pos_of_ball = ball.make_ball()
        add_part(xy = xy)


def right():
    if snake[0].heading() != 180:
        snake[0].setheading(0)

def left():
    if snake[0].heading() != 0:
        snake[0].setheading(180)

def up():
    if snake[0].heading() != 270:
        snake[0].setheading(90)

def down():
    if snake[0].heading() != 90:
        snake[0].setheading(270)

def finish_game():
    screen.clear()

def add_part(xy):
    t = Turtle(shape='square', visible=False)
    t.speed(speed_of_turtle)
    t.penup()
    t.goto(xy)
    snake.append(t)
    t.showturtle()

def game():
    global ball, pos_of_ball
    ball = Ball()
    t = Turtle(shape='square')
    t.speed(speed_of_turtle)
    t.penup()
    snake.append(t)

    screen.listen()
    screen.onkey(right, 'Right')
    screen.onkey(left, 'Left')
    screen.onkey(up, 'Up')
    screen.onkey(down, 'Down')

    pos_of_ball = ball.make_ball()
    while True:
        move()


snake = []
game()