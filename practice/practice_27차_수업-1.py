Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #2017년 4월 24일 월요일 1:30~
>>> help("return")
The "return" statement

>>> def greet():
	'''greets all of you.'''
	print("Hello!")
	print("Nice to meet you.")

>>> greet()
Hello!
Nice to meet you.
>>> Nice to meet you.
SyntaxError: invalid syntax
>>> greet
<function greet at 0x03BC0FA8>
>>> greet() #커튼콜
Hello!
Nice to meet you.
>>> greet
<function greet at 0x03BC0FA8>
>>> #함수명만 쓰면 함수의 위치가 나온다
>>> turtle
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    turtle
NameError: name 'turtle' is not defined
>>> #()는 커튼콜
>>> import turtle
>>> turtle
<module 'turtle' from 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python35-32\\lib\\turtle.py'>
>>> #함수명만 쓰면 함수의 위치가 나온다
>>> help(greet)
Help on function greet in module __main__:

greet()
    greets all of you.

>>> def greet(name):
	'''greets all of you.'''
	print("Hello!")
	print("Nice to meet you.")

>>> def greet(name):    #인수가 있는 함수
	'''greets all of you.'''
	print("Hello! " + name)

>>> greet(lee min suk)
SyntaxError: invalid syntax
>>> greet("lms")
Hello! lms
>>> def greet(name):    #인수가 있는 함수
	'''greets all of you.'''
	print("Hello! %s" %name)

>>> greet
<function greet at 0x03BD7B70>
>>> greet()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    greet()
TypeError: greet() missing 1 required positional argument: 'name'
>>> greet(10)
Hello! 10
>>> implicit explicit
SyntaxError: invalid syntax
>>>
>>> def d(x,y):
	return x+y

>>> d(51,25)
76
>>> def d(x,y):
	print(x+y)

>>> d(50,25)
75
>>> def n(x,y):
	if y == 0:
		print("no")
	else:
		return x/y

>>> n(3,1)
3.0
>>> n(3,0)
no
>>> def n(x,y):
	if y == 0:
		print("no")
	else:
		return int(x/y)

>>> greet("Bill")
Hello! Bill
>>> name
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> greet
<function greet at 0x03BD7B70>
>>> greet.name
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    greet.name
AttributeError: 'function' object has no attribute 'name'
>>> a = 'abcde'
>>> greet(name='Tom')
Hello! Tom
>>> help(greet)
Help on function greet in module __main__:

greet(name)
    greets all of you.

>>> #함수속 변수는 함수에서만 사용 가능한 지역 변수이다.
>>> d
<function d at 0x03BD7AE0>
>>> n
<function n at 0x03BD7E88>
>>> a
'abcde'
>>> b
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> d
<function d at 0x03BD7AE0>
>>>
