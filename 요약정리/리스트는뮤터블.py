>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
>>> help(math.pow)
Help on built-in function pow in module math:

pow(...)
    pow(x, y)

    Return x**y (x to the power of y).

>>> #내장된 도움말을 참조하는 게 가장 좋음
>>> math.pow(3, 4)
81.0
>>> la = [18, 10, 9]
>>> 50 in la
False
>>> 18 in la
True
>>> la.append(500)
>>> la
[18, 10, 9, 500]
>>> la.sort()
>>> la
[9, 10, 18, 500]
>>> la[-2] = la.index(18)
>>> la
[9, 10, 2, 500]
>>> la.reverse()
>>> la
[500, 2, 10, 9]
>>> la = [18, 10, 9]
>>> help(list.pop)
Help on method_descriptor:

pop(...)
    L.pop([index]) -> item -- remove and return item at index (default last).
    Raises IndexError if list is empty or index is out of range.

>>> la.pop()
9
>>> la
[18, 10]
>>> la = [18, 10, 9]
>>> la.remove(18)
>>> la
[10, 9]
>>> la = [18, 10, 9]
>>> la.append(500)
>>> la
[18, 10, 9, 500]
>>> la.sort()
>>> la
[9, 10, 18, 500]
>>> la.reverse()
>>> la
[500, 18, 10, 9]
>>> la[-2] = la.index(18)
>>> la
[500, 18, 1, 9]
>>> la.insert(2, 300)
>>> la
[500, 18, 300, 1, 9]
>>> a = [9, 8, 7, 3, 0]
>>> a.sort()
>>> a
[0, 3, 7, 8, 9]
>>> a.sort(reverse=True)
>>> a
[9, 8, 7, 3, 0]
>>> a
[9, 8, 7, 3, 0]
>>> a.reverse()
>>> a
[0, 3, 7, 8, 9]
>>> a = [9, 3, 8, 5, 0]
>>> a.sort()
>>> a
[0, 3, 5, 8, 9]
>>> a = [9, 3, 8, 5, 0]
>>> a
[9, 3, 8, 5, 0]
>>> a.sort(reverse=True)
>>> a
[9, 8, 5, 3, 0]
>>> la
[500, 18, 300, 1, 9]
>>> la.remove(18)
>>> la
[500, 300, 1, 9]
>>> la.insert(1, la.pop())
>>> la
[500, 9, 300, 1]
>>> print("Score you've got: %d" $la.pop(0))
SyntaxError: invalid syntax
>>> print("Score you've got: %d" %la.pop(0))
Score you've got: 500
>>> la
[9, 300, 1]
>>> la.sort()
>>> la
[1, 9, 300]
>>> bb = la.sort()
>>> bb
>>> bb
>>> bb
>>> bb = la.pop()
>>> bb
300
>>> help(list.sort)
Help on method_descriptor:

sort(...)
    L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*

>>> la
[1, 9]
>>> la.sort(key=1, reverse=True)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    la.sort(key=1, reverse=True)
TypeError: 'int' object is not callable
>>> a = "abc"
>>> b = ['a', 'b', 'c']
>>> b[0] = 'd'
>>> b
['d', 'b', 'c']
>>> a[0]
'a'
>>> a[1]
'b'
>>> a[0,1]
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a[0,1]
TypeError: string indices must be integers
>>>

>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>> girl = ['smart', ' good-looking', 'poor']
>>> boy = ['well-off]

SyntaxError: EOL while scanning string literal
>>> boy = ['well-off']
>>> girl.remove('poop')
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    girl.remove('poop')
ValueError: list.remove(x): x not in list
>>> girl.remove('pool)

SyntaxError: EOL while scanning string literal
>>> girl.remove('pool')
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    girl.remove('pool')
ValueError: list.remove(x): x not in list
>>> girl.remove('poor')
>>> babe = boy
>>> baby = boy
>>> baby += girl
>>> baby
['well-off', 'smart', ' good-looking']
>>> kid = baby
>>> kid.append('money talks')
>>> kid.append('bully')
>>> kid.insert(kid.index('money talks'), 'sympthy')
>>> teen = kid
>>> teen.pop(teen.index('bully'))
'bully'
>>> teen.pop(teen.index('money talks'))
'money talks'
>>> print("teen: %s\nThey lived happily ever after." %teen)
teen: ['well-off', 'smart', ' good-looking', 'sympthy']
They lived happily ever after.
>>> boy.clear()
>>> print("teen:", teen)
teen: []
>>> boy
[]
>>> teen
[]
>>>
