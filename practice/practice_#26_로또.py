>>> #집합은 자연수의 집합
>>> #집합은 중복도 없고 순서도 없다. 그래서 인덱스가 없다.

>>> lotto = list(range(1,46))
>>> lotto
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
>>> win_1 = [1, 12, 23, 34, 44, 45]
>>> Lot_Num = {1, 12, 23, 34, 44, 45}
>>> lot_Num.sort()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    lot_Num.sort()
NameError: name 'lot_Num' is not defined
>>> for i in Lot:
	print(i, i+1, sep='Hello')

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    for i in Lot:
NameError: name 'Lot' is not defined
>>> for i in Lot_Num:
	print(i, i+1, sep='Hello')

1Hello2
34Hello35
12Hello13
44Hello45
45Hello46
23Hello24
