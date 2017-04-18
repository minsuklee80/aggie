Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: C:/Users/user/Desktop/20170418_26차_.py ==============
Enter a bird: ll
%s is NOT a bird.
>>> #집합은 자연수의 집합
>>> #집합은 중복도 없고 순서도 없다. 그래서 인덱스가 없다.
>>> 
============== RESTART: C:/Users/user/Desktop/20170418_26차_.py ==============
Enter a bird: duck
sparrow is a bird.
>>> 
============== RESTART: C:/Users/user/Desktop/20170418_26차_.py ==============
Enter a bird: duck
duck is NOT a bird.
>>> 
============== RESTART: C:/Users/user/Desktop/20170418_26차_.py ==============
ok
>>> 
============== RESTART: C:/Users/user/Desktop/20170418_26차_.py ==============
zzz
>>> 
============== RESTART: C:/Users/user/Desktop/20170418_26차_.py ==============
Traceback (most recent call last):
  File "C:/Users/user/Desktop/20170418_26차_.py", line 27, in <module>
    if birds.count('sparrow') == 1:
NameError: name 'birds' is not defined
>>> 
============== RESTART: C:/Users/user/Desktop/20170418_26차_.py ==============
ok
>>> 
============== RESTART: C:/Users/user/Desktop/20170418_26차_.py ==============
>>> 
============== RESTART: C:/Users/user/Desktop/20170418_26차_.py ==============
zzz
>>> 
============== RESTART: C:/Users/user/Desktop/20170418_26차_.py ==============
ok
>>> 
============== RESTART: C:/Users/user/Desktop/20170418_26차_.py ==============
Traceback (most recent call last):
  File "C:/Users/user/Desktop/20170418_26차_.py", line 40, in <module>
    for i in range(len(cities)):
NameError: name 'cities' is not defined
>>> 
============== RESTART: C:/Users/user/Desktop/20170418_26차_.py ==============
Seoul a is a city.
Busan a is a city.
Jeju a is a city.
Sejong a is a city.
Suwon a is a city.
>>> 
============== RESTART: C:/Users/user/Desktop/20170418_26차_.py ==============
Seoul a is a city.
Busan a is a city.
Jeju a is a city.
Sejong a is a city.
Suwon a is a city.
     Seoul a is a city.
     Busan a is a city.
      Jeju a is a city.
    Sejong a is a city.
     Suwon a is a city.
>>> 
============== RESTART: C:/Users/user/Desktop/20170418_26차_.py ==============
Seoul a is a city.
Busan a is a city.
Jeju a is a city.
Sejong a is a city.
Suwon a is a city.
     Seoul a is a city.
     Busan a is a city.
      Jeju a is a city.
    Sejong a is a city.
     Suwon a is a city.
>>> 
>>> 
>>> input()
input()
'input()'
>>> 
============== RESTART: C:/Users/user/Desktop/20170418_26차_.py ==============
Enter a bird: dog
zzz
>>> 
============== RESTART: C:/Users/user/Desktop/20170418_26차_.py ==============
Enter a bird: dog
'dog' is NOT a bird
>>> 
============== RESTART: C:/Users/user/Desktop/20170418_26차_.py ==============
Enter a bird: sparrow
'sparrow' is a bird
>>> 
============== RESTART: C:/Users/user/Desktop/20170418_26차_.py ==============
Enter a bird: cat
"cat" is NOT a bird
>>> 
============== RESTART: C:/Users/user/Desktop/20170418_26차_.py ==============
Enter a bird: dog
""dog"" is NOT a bird
>>> 
============== RESTART: C:/Users/user/Desktop/20170418_26차_.py ==============
Enter a bird: dog
"dog" is NOT a bird
>>> a = "Hello"
>>> a = 'Hello'
>>> a
'Hello'
>>> a
'Hello'
>>> a = "i\'m a boy"
>>> a
"i'm a boy"
>>> a = 'apple'
>>> a
'apple'
>>> print(a)
apple
>>> a = "i\'m a boy"
>>> print(a)
i'm a boy
>>> 
============== RESTART: C:/Users/user/Desktop/20170418_26차_.py ==============
Enter a bird: dog
"Dog" is NOT a bird
>>> lotto = range(1. 46)
SyntaxError: invalid syntax
>>> lotto = list(range(1,46)
KeyboardInterrupt
>>> lotto = list.range(1,46)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    lotto = list.range(1,46)
AttributeError: type object 'list' has no attribute 'range'
>>> lotto = list(range(1,46))
>>> lotto
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
>>> win_1 = [1, 12, 23, 34, 44, 45]
>>> 
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
>>> for i in range(1,10)
SyntaxError: invalid syntax
>>> for i in range(1,10):
	print("9 x %d = %d" %(i, 9*i))

9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
>>> for i in range(1,10):
	print("9 x %d = %2d" %(i, 9*i))

9 x 1 =  9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
>>> for i in range(1,10):
	print("9 x %f = %3f" %(i, 9*i))

9 x 1.000000 = 9.000000
9 x 2.000000 = 18.000000
9 x 3.000000 = 27.000000
9 x 4.000000 = 36.000000
9 x 5.000000 = 45.000000
9 x 6.000000 = 54.000000
9 x 7.000000 = 63.000000
9 x 8.000000 = 72.000000
9 x 9.000000 = 81.000000
>>> for i in range(1,10):
	print("9 x %f = %3.0f" %(i, 9*i))

9 x 1.000000 =   9
9 x 2.000000 =  18
9 x 3.000000 =  27
9 x 4.000000 =  36
9 x 5.000000 =  45
9 x 6.000000 =  54
9 x 7.000000 =  63
9 x 8.000000 =  72
9 x 9.000000 =  81
>>> for i in range(1,10):
	print("9 x %f = %3.0f" %(i, 9*i))

	
9 x 1.000000 =   9
9 x 2.000000 =  18
9 x 3.000000 =  27
9 x 4.000000 =  36
9 x 5.000000 =  45
9 x 6.000000 =  54
9 x 7.000000 =  63
9 x 8.000000 =  72
9 x 9.000000 =  81
>>> st = '영일이삼사오육칠팔구'
>>> 
