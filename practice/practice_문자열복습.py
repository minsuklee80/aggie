>>> name = "lee min suk"
>>> name
'lee min suk'
>>> print(name)
lee min suk
>>> len(name)
11
>>> print(len(name))
11
>>> name.upper()
'LEE MIN SUK'
>>> print(name.upper())
LEE MIN SUK
>>>
>>> name
'lee min suk'
>>> name[0]
'l'
>>> name[10]
'k'
>>> name[len(name)-1]
'k'
>>> name[-1]
'k'
>>> name[-1] * len(name)
'kkkkkkkkkkk'
>>>
>>> mypens = 100
>>> urpens = 90
>>> print("I have", mypens, "pens.")
I have 100 pens.
>>>
>>> print("I have "+str(pens), " pens.")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print("I have "+str(pens), " pens.")
NameError: name 'pens' is not defined
>>> print("I have "+str(pens)+" pens.")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print("I have "+str(pens)+" pens.")
NameError: name 'pens' is not defined
>>> print("I have "+str(mypens)+" pens.")
I have 100 pens.
>>> print("I have %d pens." %mypens)
I have 100 pens.
>>> print("I have %s pens." %str(mypens))
I have 100 pens.
>>> print("I have %s pens." %mypens)
I have 100 pens.
>>> print("I have %d pens and you have %d pens" %(mypens, urpens))
I have 100 pens and you have 90 pens
>>>
print("I have "+str(pens), " pens.")
Traceback (most recent call last):
  File "<pyshell#32>", line 2, in <module>
    print("I have "+str(pens), " pens.")
NameError: name 'pens' is not defined
>>> x = 100
>>> print("x: %d" %x)
x: 100
>>> print("x: %s" %x)
x: 100
>>> print("x: %c" %x)
x: d
>>> print("x: %f" %x)
x: 100.000000
>>> print("x: %o" %x)
x: 144
>>> print("x: %x" %x)
x: 64
>>> name.count(a)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    name.count(a)
NameError: name 'a' is not defined
>>> name.count(e)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    name.count(e)
NameError: name 'e' is not defined
>>> name = "lee min suk"
>>> name.count(e)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    name.count(e)
NameError: name 'e' is not defined
>>> name.count("a")
0
>>> name.coun("e")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    name.coun("e")
AttributeError: 'str' object has no attribute 'coun'
>>> name.count("e")
2
>>> name.find("s")
8
>>> name.find("e")
1
>>> name.find("z)

SyntaxError: EOL while scanning string literal
>>> name.find("z")
-1
>>> name.find("o")
-1
>>> name.index("o")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    name.index("o")
ValueError: substring not found
>>> name.replace(" ", "_")
'lee_min_suk'
>>> name.split()
['lee', 'min', 'suk']
>>> name[0]
'l'
>>> na = name.split()
>>> na[0]
'lee'
>>> na[0][0]
'l'
>>>

>>> na[0] = "yoon"
>>> na
['yoon', 'min', 'suk']
>>> name.split(a)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    name.split(a)
NameError: name 'a' is not defined
>>> name.split(m)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    name.split(m)
NameError: name 'm' is not defined
>>> name.split("m")
['lee ', 'in suk']
>>> null = notting
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    null = notting
NameError: name 'notting' is not defined
>>>

>>>
>>> name
'lee min suk'
>>>
========== RESTART: D:/다프수업/20170125_문자열실습-2.py ==========
Traceback (most recent call last):
  File "D:/다프수업/20170125_문자열실습-2.py", line 3, in <module>
    print("이름: %d" %name)
TypeError: %d format: a number is required, not str
>>>
========== RESTART: D:/다프수업/20170125_문자열실습-2.py ==========
이름: lee min suk
e: 2개
i: 1개
u: 1개
>>>
========== RESTART: D:/다프수업/20170125_문자열실습-2.py ==========
이름: lee min suk
e: 2개
i: 1개
u: 1개
>>> name[0]
'l'
>>>
========== RESTART: D:/다프수업/20170125_문자열실습-2.py ==========
이름: lee min suk
e: 2개
i: 1개
u: 1개
모음은 모두: 4개
>>>
========== RESTART: D:/다프수업/20170125_문자열실습-2.py ==========
이름: lee min suk
e: 2개
i: 1개
u: 1개
========== RESTART: D:/다프수업/20170125_문자열실습-2.py ==========
이름: lee min suk
e: 2개
i: 1개
u: 1개
이름에 없는 알파벳은: abcdefghijklmnopqrstuvwxyz 이네요.
>>>
