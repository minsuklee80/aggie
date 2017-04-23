>>> import turtle as t
>>> t.circle(50)            #50크기의 원 그리기
>>> t.undo()
>>> t.circle(50, 90)        #원을 1/4만큼 그림
>>> t.undo()
>>> t.circle(50, steps=4)   #steps는 각의 개수
>>> t.undo()
>>> t.circle(50, 180)       #원을 1/2만큼 그림
>>> t.circle(50, 180, steps=4)  #원을 1/2만큼, 각이 4개인 원을 그림
>>> t.undo()
>>> t.circle(50,180)
>>> t.rt(180)
>>> t.circle(50,180)
>>> t.rt(180)
>>> t.circle(50,180)
>>> t.ht()
>>> t.reset()
>>> t.pen up(-50)
SyntaxError: invalid syntax
>>> t.pu(50)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    t.pu(50)
TypeError: pu() takes 0 positional arguments but 1 was given
>>> t.pu()
>>> t.rt(90)
>>> t.fd(50)
>>> t.pd()
>>> t.lt(90)
>>>
========= RESTART: D:/다프수업_백업용/20170215_실습-1.py =========
>>>
========= RESTART: D:/다프수업_백업용/20170215_실습-1.py =========
Traceback (most recent call last):
  File "D:/다프수업_백업용/20170215_실습-1.py", line 7, in <module>
    t.hd()
AttributeError: module 'turtle' has no attribute 'hd'
>>>
========= RESTART: D:/다프수업_백업용/20170215_실습-1.py =========
>>>
========= RESTART: D:/다프수업_백업용/20170215_실습-1.py =========
>>> help(t.circle)
Help on function circle in module turtle:

circle(radius, extent=None, steps=None)
    Draw a circle with given radius.

    Arguments:
    radius -- a number
    extent (optional) -- a number
    steps (optional) -- an integer

    Draw a circle with given radius. The center is radius units left
    of the turtle; extent - an angle - determines which part of the
    circle is drawn. If extent is not given, draw the entire circle.
    If extent is not a full circle, one endpoint of the arc is the
    current pen position. Draw the arc in counterclockwise direction
    if radius is positive, otherwise in clockwise direction. Finally
    the direction of the turtle is changed by the amount of extent.

    As the circle is approximated by an inscribed regular polygon,
    steps determines the number of steps to use. If not given,
    it will be calculated automatically. Maybe used to draw regular
    polygons.

    call: circle(radius)                  # full circle
    --or: circle(radius, extent)          # arc
    --or: circle(radius, extent, steps)
    --or: circle(radius, steps=6)         # 6-sided polygon

    Example:
    >>> circle(50)
    >>> circle(120, 180)  # semicircle

>>> t.reset()
>>> t.circle(-50)
>>> t.undo()
>>> t.circle(50, 360)
>>> t.circle(50, -360)
>>> t.reset()
>>> t.circle(50, 180)
>>> t.circle(50,-180)
>>> t.reset()
>>> t.circle(50, 180)
>>> t.circle(-50, 180)
>>> t.reset()
>>> t.pu(-50)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    t.pu(-50)
TypeError: pu() takes 0 positional arguments but 1 was given
>>> t.pu()
>>> t.rt(90)
>>> t.fd(50)
>>> t.pd()
>>> t.circle(50, 360)
>>> t.circle(-50, 360)
>>> t.circle(50, 360)
>>> t.reset()
>>> t.circle(50,540)
>>> t.reset
<function reset at 0x042E66A8>
>>> t.reset()
>>> t.circle(50, 180)
>>> t.circle(-50, 180)
>>> t.reset()
>>> t.circle(50, 180)
t.
>>> t.circle(50, -180)
>>> t.reset()
>>> t.circle(50, 180)
>>> t.circle(-50, 180)
>>> t.circle(50, 180)
>>> t.circle(50, 180)
>>> t.circle(-50, 180)
>>> t.circle(50, 180)
>>> t.ht()
