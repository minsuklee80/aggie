>>> #길이가 50인 임의의 문자열 만들기
>>> import random
>>> import string
>>> help(string)
Help on module string:

NAME
    string - A collection of string constants. #정수의 콜렉션

DESCRIPTION #기술
    Public module variables:

    whitespace -- a string containing all ASCII whitespace
	#모든 ASCII 공백이 포함 된 문자열
    ascii_lowercase -- a string containing all ASCII lowercase letters
	#모든 ASCII 소문자를 포함하는 문자열
    ascii_uppercase -- a string containing all ASCII uppercase letters
	#모든 ASCII 대문자를 포함하는 문자열
    ascii_letters -- a string containing all ASCII letters
	#모든 ASCII 문자가 포함 된 문자열
    digits -- a string containing all ASCII decimal digits
	#모든 ASCII 10 진수를 포함하는 문자열
    hexdigits -- a string containing all ASCII hexadecimal digits
	#모든 ASCII 16 진수가 포함 된 문자열
    octdigits -- a string containing all ASCII octal digits
	#모든 ASCII 8 진수를 포함하는 문자열
    punctuation -- a string containing all ASCII punctuation characters
	#모든 ASCII 구두점 문자를 포함하는 문자열
    printable -- a string containing all ASCII characters considered printable
	#인쇄 가능한 것으로 간주되는 모든 ASCII 문자가 포함 된 문자열

DATA
    __all__ = ['ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'cap...
    ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    hexdigits = '0123456789abcdefABCDEF'
    octdigits = '01234567'
    printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU...
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    whitespace = ' \t\n\r\x0b\x0c'

	
>>> dir(string)
['Formatter', 'Template', '_ChainMap', '_TemplateMetaclass', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_re', '_string', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']
>>> a=string.ascii_letters
>>> a
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> random.choice(a)
'd'
>>> random.choice(a)
'p'
>>> random.choice(a)
'p'
>>> for i in range(50):
	a+=random.choice(a)
>>> a
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZBmFKKAAAyewFBFutDvkJhlltonBvuFaBlydAuaBgAFQVdmvtmm'
>>> len(a)
102

>>> a=""
>>> for i in range(50):
	a+=random.choice(a)

Traceback (most recent call last):
  File "C:\Users\user\AppData\Local\Programs\Python\Python35-32\lib\random.py", line 253, in choice
    i = self._randbelow(len(seq))
  File "C:\Users\user\AppData\Local\Programs\Python\Python35-32\lib\random.py", line 230, in _randbelow
    r = getrandbits(k)          # 0 <= r < 2**k
ValueError: number of bits must be greater than zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#18>", line 2, in <module>
    a+=random.choice(a)
  File "C:\Users\user\AppData\Local\Programs\Python\Python35-32\lib\random.py", line 255, in choice
    raise IndexError('Cannot choose from an empty sequence')
IndexError: Cannot choose from an empty sequence
>>> for i in range(50):
	a+=random.choice(string.ascii_letters)

>>> a
'ROMUdklOHcvfiDieAAaePxnShjswrzSBpoivjOIUrZLZjFVnqg'
>>> len(a)
50
