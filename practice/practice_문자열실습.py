Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = "abc DEF"
>>> a
'abc DEF'
>>> a.upper()
'ABC DEF'
>>> a.lower()
'abc def'
>>> a.capitalize()
'Abc def'
>>> a.title()
'Abc Def'
>>> a
'abc DEF'
>>> a = a.lower()
>>> a
'abc def'
>>> a = 1
>>> a = a + 1
>>> a += 1
>>> a
3
>>> iterative development
SyntaxError: invalid syntax
>>> iterative development
SyntaxError: invalid syntax
>>> iterative loop / recursive loop
SyntaxError: invalid syntax
>>> a = ["gawi", "bawi", "bo"]
>>> a
['gawi', 'bawi', 'bo']
>>> a[0]
'gawi'
>>> a[1]
'bawi'
>>> a[2]
'bo'
>>> a[3]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a[3]
IndexError: list index out of range
>>> a[-1]
'bo'
>>> gbb = [gawi, bawi, bo]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    gbb = [gawi, bawi, bo]
NameError: name 'gawi' is not defined
>>> for i in a:
	print(i)

gawi
bawi
bo
>>> weekdays = ["mon", "tue", "wed", "thu"]
>>> len(weekdays)
4
>>> for i in weekdays:
	print(i)

mon
tue
wed
thu
>>> getpass.getpass(" ")
