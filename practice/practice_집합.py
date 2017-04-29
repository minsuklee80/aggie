>>> b={3,1,2,2}
>>> b
{1, 2, 3}
>>> b={5,4,6,4,5,2,8,}
>>> len(b)
5
>>> b
{8, 2, 4, 5, 6}
>>> b
{8, 2, 4, 5, 6}
>>> b.pop
<built-in method pop of set object at 0x03728558>
>>> b.union
<built-in method union of set object at 0x03728558>
>>> b
{8, 2, 4, 5, 6}
>>> a=[3,2,1]
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.count()
TypeError: count() takes exactly one argument (0 given)
>>>
>>> type(a)
<class 'list'>
>>> type(b)
<class 'set'>
>>> 10 in a
False
>>> a in 1
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a in 1
TypeError: argument of type 'int' is not iterable
>>> for i in ['a', 'b']:
	print(i)

a
b
>>> for i in ['a', 'b']:
	print(i)


a
b
>>> a="abc"
>>> type(a)
<class 'str'>
>>> import string
>>> dir(string)
['Formatter', 'Template', '_ChainMap', '_TemplateMetaclass', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_re', '_string', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']
>>> string.digits
'0123456789'
>>> a=string.digits
>>> print(a)
0123456789
>>> a=[]
>>> b=()
>>> c=""
>>> type(a)
<class 'list'>
>>> type(b)
<class 'tuple'>
>>> type(c)
<class 'str'>
>>> d={}
>>> type(d)
<class 'dict'>
>>> a='abc'
>>> type(a)
<class 'str'>
>>> a=list(a)
>>> list(a)
['a', 'b', 'c']
>>> a="abc"
>>> list(a)
['a', 'b', 'c']
>>> tuple(a)
('a', 'b', 'c')
>>> set(a)
{'b', 'c', 'a'}
>>> set()
set()
>>> type(a)
<class 'str'>
>>> a=list(a)
>>> a=tuple()
>>> a=tuple(a)
>>>
>>> a
()
>>> a
()
>>> a="abc"
>>> a=list(a)
>>> a
['a', 'b', 'c']
>>> a=tuple(a)
>>> a
('a', 'b', 'c')
>>> a=set(a)
>>> a
{'b', 'c', 'a'}
>>> a=set()
>>> a
set()
>>> type(a)
<class 'set'>
>>> a=[]
>>> a
[]
>>> a={0}
>>> a
{0}
>>> a={'1':11, '2':22}
>>> a['1']
11
>>> a={1:11, 2:22}
>>> a
{1: 11, 2: 22}
>>> a[2]
22
>>> #딕셔너리는 키와 값을 가지고 있다.
>>> #딕셔너리의 키로 값을 불러온다.
>>> a={1,2,3}
>>> a
{1, 2, 3}
>>> for i in a:
	print(i)

1
2
3
>>> #딕셔너리가 발전한 것이 클래스,
>>> #클래스가 발전한 것이 객체,
>>>
>>>
>>> #프로토콜...
>>>
