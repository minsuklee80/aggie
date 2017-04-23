Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ta = (10, 100, 19, 100)
>>> ta
(10, 100, 19, 100)
>>> ta.count(100)
2
>>> ta.index
<built-in method index of tuple object at 0x0411F8A0>
>>> ta.index()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    ta.index()
TypeError: index() takes at least 1 argument (0 given)
>>> help(ta.index)
Help on built-in function index:

index(...) method of builtins.tuple instance
    T.index(value, [start, [stop]]) -> integer -- return first index of value.
    Raises ValueError if the value is not present.

>>> ta.index(1)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ta.index(1)
ValueError: tuple.index(x): x not in tuple
>>> ta.index(100)
1
>>> a = (4, 5)
>>> ta + a
(10, 100, 19, 100, 4, 5)
>>> ta.sort()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    ta.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a = [1,2]
>>> b = [3,4,a,[5,6]]
>>> b
[3, 4, [1, 2], [5, 6]]
>>> len(b)
4
>>> 
