#!/usr/bin/env python3

import turtle
from random import randint

X_LOW, X_HIGH = -300, 300
Y_LOW, Y_HIGH = -300, 300

class Runner:
    def __init__(self, color="red", shape="turtle", speed=10):
        self.x = randint(X_LOW, X_HIGH)
        self.y = randint(Y_LOW, Y_HIGH)
        self.speed = speed
        self.turtle = t = turtle.Turtle()
        t.color(color)
        t.shape(shape)
        t.penup()
        t.setpos(self.x, self.y)
        t.pendown()

    def step(self):
        "Do one step"
        t = self.turtle
        speed = self.speed
        t.left(randint(-10, +10))
        t.forward(speed)
        if t.xcor() < X_LOW or t.xcor() > X_HIGH or \
           t.ycor() < Y_LOW or t.ycor() > Y_HIGH:
                t.left(180)
                t.forward(1.5*speed)
        self.x, self.y = t.xcor(), t.ycor()

def run_demo():
    "Run demo"
    speedy = Runner()
    for i in range(1000):
        speedy.step()
    turtle.exitonclick()

if __name__ == '__main__':
    run_demo()
