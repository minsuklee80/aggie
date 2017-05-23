Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> abc = open('ex.txt', 'w')
>>> abc.write("Thank you.")
10
>>> abc.close()
>>> 
>>> #파일을 열었으면 반드시 닫아야 한다. (open, close)
>>> 
===================== RESTART: Shell =====================
>>> abc = open('ex.txt', 'w')
>>> abc.write("Hello")
5
>>> abc.close()
>>> 
>>> #같은 파일을 쓰기 위해 열면 기존 내용이 모두 삭제된 상태가 된다.
>>> 
>>> abc = open('ex.txt', 'r')
>>> texts = abc.read()
>>> print(texts)
Hello
>>> abc = open('ex.txt', 'r')
>>> texts = abc.read()
>>> print(texts)
Hello
Hi
How are you?
>>> texts = abc.readline()
>>> print(texts)

>>> abc.readline
<built-in method readline of _io.TextIOWrapper object at 0x03DA7D30>
>>> help(abc.readline)
Help on built-in function readline:

readline(size=-1, /) method of _io.TextIOWrapper instance
    Read until newline or EOF.
    
    Returns an empty string if EOF is hit immediately.

>>> #open했을 때 파일이 어느 곳에 생성되는 지 찾아볼 것
>>> #C:\Users\user\AppData\Local\Programs\Python\Python35-32
>>> #요기에 생겼다.
>>> texts = abc.readline()
>>> print(texts)

>>> texts = abc.read()
>>> print(texts)

>>> abc.close()
>>> abc = open('ex.txt', 'r')
>>> abc.write()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    abc.write()
TypeError: write() takes exactly one argument (0 given)
>>> #읽기용으로 파일을 열었기 때문에 쓸 수 없다.
>>> 
>>> abc.close()
>>> abc = open('ex.txt', 'a')
>>> abc.write("bye")
3
>>> abc.close()
>>> abc = open('ex.txt', 'a')
>>> abc.write("Lee min-suk")
11
>>> abc.read()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    abc.read()
io.UnsupportedOperation: not readable
>>> abc.close()
>>> abc = open('ex.txt', 'r')
>>> abc.read()
'Hello\nHi\nHow are you?byeLee min-suk'
>>> abc.read()
''
>>> abc.seek(0)
0
>>> abc.read()
'Hello\nHi\nHow are you?byeLee min-suk'
>>> 
