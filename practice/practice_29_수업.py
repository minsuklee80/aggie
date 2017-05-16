Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 3
>>> b = 3
>>> a == b
True
>>> a is b
True
>>> a = 7000
>>> b = 7000
>>> a == b
True
>>> a is b
False
>>> #'=='는 변수가 가진 값만 비교
>>> #'is'는 변수의 값과 메모리 위치까지 비교해서
>>> #'=='는 변수가 가진 값만 비교해서 같으면 'True'
>>> #'is'는 변수의 값과 메모리 위치까지 비교해서 같아야 'True'가 나온다.
>>> a,b,c = 1,2,3
>>> a
1
>>> b
2
>>> c
3
>>> a,b,c = 1,2
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a,b,c = 1,2
ValueError: not enough values to unpack (expected 3, got 2)
>>> #단체로 여행 갔는데 사람은 세 명인데 캐리어가 두 개밖에 없어서 오류가 난 것임.
>>> 1,2
(1, 2)
>>> a = 1,2,3,4,5,6
>>> a
(1, 2, 3, 4, 5, 6)
>>> (a,b,c) = (1,2,3)
>>> a
1
>>> b
2
>>> c
3
>>> (a,b,c) = [1,2,3]
>>> a
1
>>> b
2
>>> c
3
>>> type(a)
<class 'int'>
>>> a = 1,2,3
>>> type(a)
<class 'tuple'>
>>> a = [1,2,3]
>>> type(a)
<class 'list'>
>>> a = ''
>>> type(a)
<class 'str'>
>>> (a,b,c) = ('1','2','3')
>>> a
'1'
>>> b
'2'
>>> c
'3'
>>> (a,b,c) = ([1,2,3],[4,5,6],[7,8,9])
>>> a
[1, 2, 3]
>>> b
[4, 5, 6]
>>> c
[7, 8, 9]
>>> 
===================== RESTART: Shell =====================
>>> a
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> initialize
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    initialize
NameError: name 'initialize' is not defined
>>> a,b,c = 1,2,3
>>> a
1
>>> b
2
>>> c
3
>>> type(a)
<class 'int'>
>>> 1,2,3
(1, 2, 3)
>>> type(1,2,3)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    type(1,2,3)
TypeError: type() argument 1 must be str, not int
>>> a = b = 1
>>> a
1
>>> b
1
>>> a = b = 7000
>>> a == b
True
>>> a is b
True
>>> a = {1,2,3}
>>> b = {1,2,3}
>>> a == b
True
>>> a is b
False
>>> id(a)
61508464
>>> id(b)
61508224
>>> a = b = {1,2,3}
>>> for x in a:
	print(x)

1
2
3
>>> a = {1000, 1002, 3001}
>>> for x in a:
	print(x)

1000
3001
1002
>>> for x in a:
	print(x)

1000
3001
1002
>>> for x in a:
	print(x)

1000
3001
1002
>>> a
{1000, 3001, 1002}
>>> import random
>>> a = input("Enter: ")
Enter: 1 2 3 4 5
>>> a
'1 2 3 4 5'
>>> a.split(' ')
['1', '2', '3', '4', '5']
>>> a = a.split(' ')
>>> for x in range(len(a)):
	a[x] = int(a[x])

>>> 
>>> a
[1, 2, 3, 4, 5]
>>> a = input("Enter: ")
Enter: 25 65 40 22 12 6
>>> for x in input("???: ").split(" "):
	print(int(x))

???: 15 25 66 85 6 
15
25
66
85
6
Traceback (most recent call last):
  File "<pyshell#92>", line 2, in <module>
    print(int(x))
ValueError: invalid literal for int() with base 10: ''
>>> for x in input("???: ").split(" "):
	int(x)

???: 45 225 35 631 15
45
225
35
631
15
>>> for x in input("???: ").split(" "):
	print(x)

???: 52 58 66 89 74 8
52
58
66
89
74
8
>>> x
'8'
>>> type(x)
<class 'str'>
>>> for x in input("Enter: ").split(" "):
	a[x] = int(a[x])

Enter: 52 55 68 48 
Traceback (most recent call last):
  File "<pyshell#101>", line 2, in <module>
    a[x] = int(a[x])
TypeError: string indices must be integers
>>> a = for x in input("Enter: ").split(" "):
	a[x] = int(a[x])
	
SyntaxError: invalid syntax
>>> 
>>> for x in a = input("Enter: ").split(" "):
	a[x] = int(a[x])
	
SyntaxError: invalid syntax
>>> for x in input("Enter: ").split(" "):
	a[x] = int(a[x])

Enter: 12 25 33 56 883
Traceback (most recent call last):
  File "<pyshell#106>", line 2, in <module>
    a[x] = int(a[x])
TypeError: string indices must be integers
>>> a = []
>>> for x in input("Enter: ").split(" "):
	a.append(x)

Enter: 12 58 66 
>>> a
['12', '58', '66', '']
>>> 
