>>> a = ["gawi", "bawi", "bo"]
>>> len(a)
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
>>> for i in a:
	print(i)

gawi
bawi
bo
