import turtle as t
import random

t.speed(0)
t.color('red')

def drawStar(size):
    for i in range(5):
        t.fd(size)
        t.rt(144)

t.begin_fill()
drawStar(200)
t.end_fill()




 

