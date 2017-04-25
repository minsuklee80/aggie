>>> def greet():
	'''greets all of you.''' #docstring
	print("Hello!")
	print("Nice to meet you.")

>>> greet
<function greet at 0x02DA96A8>  #greet 함수의 메모리 위치
>>> help(greet)
Help on function greet in module __main__:

greet()
    greets all of you.    #메모리에 저장된 함수의 설명(docstring)을 볼 수 있다.
>>> greet()               #함수의 괄호는 '커튼콜'에 해당한다.
Hello!
Nice to meet you.
>>> def greet(name):      #인수가 있는 함수
	'''greets all of you.'''
	print("Hello! " + name)

>>> greet("minsuk")
Hello! minsuk
>>> def greet(name):    #인수가 있는 함수
	'''greets all of you.'''
	print("Hello! %s" + %name)
>>> greet("minsuk")
Hello! minsuk
>>>greet(name='Tom')
Hello! Tom

>>> def d(x,y): #더하기
	return x+y

>>> d(5,2)
7
>>> def b(x,y): #빼기
	return x-y

>>> b(5,2)
3
>>> def g(x,y): #곱하기
	return x*y

>>> g(5,2)
10
>>> def n(x,y): #나누기
	return x/y

>>> n(5,2)
2.5
>>> help(d)
Help on function d in module __main__:

d(x, y)

>>> help(b)
Help on function b in module __main__:

b(x, y)

>>> help(g)
Help on function g in module __main__:

g(x, y)

>>> help(n)
Help on function n in module __main__:

n(x, y)

#아이들을 새로 열면 함수에 대한 설명은 나오지 않는다.
#함수가 저장된 곳은 가상 메모리?
