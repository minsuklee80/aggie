>>> #길이가 50인 임의의 문자열 만들기
>>> import random
>>> import string
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
