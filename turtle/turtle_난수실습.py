import turtle as t
import random

def setTurtlePos(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

t.speed(0)

for i in range(20):
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    radius = random.randint(10, 100)    #radius는 반지름
    setTurtlePos(x,y)
    t.circle(radius)
