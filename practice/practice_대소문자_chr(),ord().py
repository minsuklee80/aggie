>>> chr(65)
'A'
>>> chr(65+32)
'a'
>>> ord("A")
65
>>> ord("a")
97
>>> a = "abcdefgh"
>>> a[0]
'a'
>>> a[1]
'b'
>>> a[-1]
'h'
>>> ord(a[-1])
104
>>> a = "abcdeFGH"
>>> a
'abcdeFGH'
>>> a[-1]
'H'
>>> for i in range(8):
	print(a[i])

a
b
c
d
e
F
G
H
>>> for i in a:
	print(a[i])

Traceback (most recent call last):
  File "<pyshell#23>", line 2, in <module>
    print(a[i])
TypeError: string indices must be integers
>>> for i in a:
	print(i)

a
b
c
d
e
F
G
H
>>> range(8)
range(0, 8)
>>> range(1, 10, 1)
range(1, 10)
>>> list(range(1, 10, 2))
[1, 3, 5, 7, 9]


>>> a = ''
>>> for i in range(26):
	a = a + chr(97+i)

>>> a
'abcdefghijklmnopqrstuvwxyz'

>>> a = ''
>>> a
>>> ''
>>> for i in range(26):
	a += chr(ord("A")+i)
>>> print(a)
ABCDEFGHIJKLMNOPQRSTUVWXYZ
>>> ord("a")
97
>>> ord("z")
122
>>> ord("A")
65
>>> ord("Z")
90
>>>
========= RESTART: D:/다프수업_백업용/20170201_실습-2.py =========
영문자 한 글자를 써주세요: D
대문자네!
>>>
========= RESTART: D:/다프수업_백업용/20170201_실습-2.py =========
영문자 한 글자를 써주세요: z
>>>
>>>
>>>
>>>
========= RESTART: D:/다프수업_백업용/20170201_실습-2.py =========
영문자 한 글자를 써주세요: s
소문자네!
>>>
========= RESTART: D:/다프수업_백업용/20170201_실습-2.py =========
영문자 한 글자를 써주세요: D
대문자네!
>>>
========= RESTART: D:/다프수업_백업용/20170201_실습-2.py =========
영문자 한 글자를 써주세요: d
소문자네!
>>>
========= RESTART: D:/다프수업_백업용/20170201_실습-2.py =========
영문자 한 글자를 써주세요: D
대문자네!
>>>
========= RESTART: D:/다프수업_백업용/20170201_실습-2.py =========
영문자 한 글자를 써주세요: a
>>>
========= RESTART: D:/다프수업_백업용/20170201_실습-2.py =========
영문자 한 글자를 써주세요: a
소문자네!
>>>
========= RESTART: D:/다프수업_백업용/20170201_실습-2.py =========
영문자 한 글자를 써주세요: A
대문자네!


>>> chr(65)
'A'
>>> 0x16
22
>>> 0xa
10
>>> ord("A")
65
>>> a = ord("A")
>>> a
65
>>> print("'A': %x" %a)
'A': 41
>>> print("'A': %o" %a)
'A': 101
>>> print("'J': %o" %ord("J"))
'J': 112
>>> ord("J")
74
>>> print("'J': %d" %ord("J"))
'J': 74
>>> print("'J': %s" %ord("J"))
'J': 74
>>> print("'J': %x" %ord("J"))
'J': 4a
>>> Ox4a
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    Ox4a
NameError: name 'Ox4a' is not defined
>>>
>>>
>>> max(10, 20, 30)
30
>>> min(10, -10, 1000)
-10
>>> a = (10,20,30,-10)
>>> a
(10, 20, 30, -10)
>>> max(a)
30
>>> min(a)
-10
>>> a = "Hi, Hello, Bye"
>>> max(a)
'y'
>>> min(a)
' '
>>>
