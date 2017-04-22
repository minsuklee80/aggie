import turtle as t

t.speed(0)
t.color('red')
t.begin_fill()
for i in range(108):
    # t.pensize(i)
    t.circle(i*2)
    t.lt(10)
t.end_fill()
