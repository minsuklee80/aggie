
>>> #연산자 실습하기
>>> a = 10
>>> b = 3
>>>
>>> #산술 연산자
>>> print("a ** b =", a**b)
a ** b = 1000
>>> print("a / b =", a/b)
a / b = 3.3333333333333335
>>> print("a // b =", a//b)
a // b = 3
>>> print("a % b =", a%b)
a % b = 1
>>>
>>> 
>>> #논리 연산자 & 관계 연산자
>>> print("(a==10) and (b==3):", (a==10) and (b==3))
(a==10) and (b==3): True
>>> print("(a!=10) or (b>=3):", (a!=10) or (b>=3))
(a!=10) or (b>=3): True
>>> print("not((a==10) and (b==3)):", not((a==10) and (b==3)))
not((a==10) and (b==3)): False
>>>
>>> #print는 함수이다. 따옴표("")안에 있는 내용은 그대로 출력하고 연산자가 있는 건 연산 후 출력한다.
>>>

>>> a
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> side
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    side
NameError: name 'side' is not defined
>>> print(side)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(side)
NameError: name 'side' is not defined
>>>
===================== RESTART: Shell =====================
>>> side
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    side
NameError: name 'side' is not defined
>>>
======= RESTART: D:\다프수업\20161130_turtle라이브러리실습.py =======
>>> side
100
>>>
===== RESTART: D:\다프수업\20161130_turtle라이브러리실습-함수.py =====
>>> side
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    side
NameError: name 'side' is not defined
>>>
======== RESTART: D:/다프수업/20161130_마인크래프트함수실습.py ========
플레이어의 현재 x 좌표: 10
플레이어의 현재 y 좌표: 80
플레이어의 현재 z 좌표: 68
>>>
======= RESTART: D:/다프수업/20161130_for,while반복문.py =======
0
2
4
6
8
for 루프가 끝난 i의 값:  8
0
2
4
6
8
while 루프가 끝난 i의 값:  10
>>>
======= RESTART: D:/다프수업/20161130_for,while반복문.py =======
0
2
4
6
8
for 루프가 끝난 i의 값:  8
0
2
4
6
8
10
while 루프가 끝난 i의 값:  12
>>> a = 10
>>> b = input("Enter the number: ")
Enter the number:
>>> print(b)

>>> b = input("Enter the number: ")
Enter the number: 10
>>> b = 10
>>> b
10
>>> b = int(b)
>>> b
10
>>> b = input("넌 몇살이니? ")
넌 몇살이니?
>>> b
''
>>> input("넌 몇살이니? ")
넌 몇살이니? 10
'10'
>>> number = input("3+5=")
3+5=8
>>> number
'8'
>>> number
'8'
>>> number = int(number)
>>> number
8
>>> number == 8
True
>>>
