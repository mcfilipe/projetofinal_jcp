import turtle
import random

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
colors = ["red", "blue", "green", "yellow", "purple", "orange", "white"]

for _ in range(100):
    t.color(random.choice(colors))
    t.forward(random.randint(50, 200))
    t.right(random.randint(30, 180))

turtle.done()
