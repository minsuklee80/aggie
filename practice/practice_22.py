




========= RESTART: D:/다프수업_백업용/20170322_수업실습.py =========
Traceback (most recent call last):
  File "D:/다프수업_백업용/20170322_수업실습.py", line 2, in <module>
    for x in gange(1,11):
NameError: name 'gange' is not defined
>>>
========= RESTART: D:/다프수업_백업용/20170322_수업실습.py =========
[4, 16, 36, 64, 100]
>>> import random
>>> help(random.choice)
Help on method choice in module random:

choice(seq) method of random.Random instance
    Choose a random element from a non-empty sequence.

>>> random.choice('123')
'1'
>>> random.choice('123')
'3'
>>> random.randint(0,2)
2
>>> list(random.randint(1,10))
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    list(random.randint(1,10))
TypeError: 'int' object is not iterable
>>> list[random.randint(1,10)]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    list[random.randint(1,10)]
TypeError: 'type' object is not subscriptable
>>> a = []
>>> a.append(random.randint(1,10))
>>> a
[1]
>>> list(range(1,10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> random.randint(1,10)
8

Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

>>> import rnadom
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    import rnadom
ImportError: No module named 'rnadom'
>>> import random
>>> gbb = ["가위", "바위", "보"]
>>> youwin = ['13', '21', '32']
>>> you = input
>>>
>>> ord('a')
97
>>> ord('z')
122
>>> if ort('a') <= t <= ord('z'):
	print(t)

Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    if ort('a') <= t <= ord('z'):
NameError: name 'ort' is not defined
>>> a = ''
>>> if ort('a') <= a <= ord('z'):
	print(a)

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    if ort('a') <= a <= ord('z'):
NameError: name 'ort' is not defined
>>>
>>> random.string(len(50))
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    random.string(len(50))
AttributeError: module 'random' has no attribute 'string'
>>>
========= RESTART: D:/다프수업_백업용/20170322_수업실습.py =========
원래 문자열: aBc
Traceback (most recent call last):
  File "D:/다프수업_백업용/20170322_수업실습.py", line 70, in <module>
    lower+=1
TypeError: Can't convert 'int' object to str implicitly
>>>
========= RESTART: D:/다프수업_백업용/20170322_수업실습.py =========
원래 문자열: aBc
Traceback (most recent call last):
  File "D:/다프수업_백업용/20170322_수업실습.py", line 70, in <module>
    lower+=1
TypeError: Can't convert 'int' object to str implicitly
>>>
========= RESTART: D:/다프수업_백업용/20170322_수업실습.py =========
원래 문자열: aBc
Traceback (most recent call last):
  File "D:/다프수업_백업용/20170322_수업실습.py", line 69, in <module>
    lower+=1
TypeError: Can't convert 'int' object to str implicitly
>>>
========= RESTART: D:/다프수업_백업용/20170322_수업실습.py =========
원래 문자열: aBc
대문자: B
소문자: ac
>>> dir(string)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    dir(string)
NameError: name 'string' is not defined
>>> dir(random.string)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    dir(random.string)
NameError: name 'random' is not defined
>>> help(list.extend)
Help on method_descriptor:

extend(...)
    L.extend(iterable) -> None -- extend list by appending elements from the iterable

>>>
