Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> abc = open('C:/Users/user/AppData/Local/Programs/Python/Python35-32/exfiletxt
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> abc = open('ex.txt', 'r')
>>> abc.read()
'Hello\nHi\nHow are you?byeLee min-suk'
>>> def v(string):
    vowels = 'aeiou'
    numV = 0
    string = string.lower()
    for x in string:
        if x in vowels:
            numV += 1
    return numV

>>> v(abc)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    v(abc)
  File "<pyshell#4>", line 4, in v
    string = string.lower()
AttributeError: '_io.TextIOWrapper' object has no attribute 'lower'
>>> abc.seek(0)
0
>>> v(abc.read())
13
>>> abc.seek(0)
0
>>> print(v(abc.read()))
13
>>> 
===================== RESTART: Shell =====================
>>> abc = open('D:/aggie/teacher/5월23일_#30', 'r')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    abc = open('D:/aggie/teacher/5월23일_#30', 'r')
PermissionError: [Errno 13] Permission denied: 'D:/aggie/teacher/5월23일_#30'
>>> abc = open('D:/aggie/teacher/5월23일_#30/exfile2', 'r')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    abc = open('D:/aggie/teacher/5월23일_#30/exfile2', 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'D:/aggie/teacher/5월23일_#30/exfile2'
>>> abc = open('D:/aggie/teacher/5월23일_#30/exfile2.txt', 'r')
>>> v(abc.read())
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    v(abc.read())
NameError: name 'v' is not defined
>>> abc.seek(0)
0
>>> print(v(abc.read()))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(v(abc.read()))
NameError: name 'v' is not defined
>>> def v(string):
    vowels = 'aeiou'
    numV = 0
    string = string.lower()
    for x in string:
        if x in vowels:
            numV += 1
    return numV

>>> print(v(abc.read()))
95
>>> v(abc.read())
0
>>> abc.seek(0)
0
>>> v(abc.read())
95
>>> help(abc.seek())
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    help(abc.seek())
TypeError: seek() takes at least 1 argument (0 given)
>>> abc.seek(0)
0
>>> a = v(abc.read())
>>> print("exfile2.txt 파일의 모음 개수는 %s 입니다." %a)
exfile2.txt 파일의 모음 개수는 95 입니다.
>>> 
>>> 
>>> 
>>> #파일 경로는 백슬래시(\)가 아닌 슬래시(/)를 사용해야 합니다.
>>> import string
>>> 
