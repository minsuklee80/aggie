#int()은 문자열을 정수로 변환.
>>> int("1492")
1492
>>> int("1492")+520
2012
>>> int(1.414)  #부동 소수점을 정수로 변환하고, 소수점 이하는 모두 버린다.
1
>>> int(2.999999)
2
>>> int(-2.999999)
-2

#문자열을 정수로 변환할 뿐 부동 소수점은 오류가 난다.
>>> int("1.414")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    int("1.414")
ValueError: invalid literal for int() with base 10: '1.414'

#float()은 문자열을 부동 소수점으로 변환.
>>> float("1.414")
1.414
>>> float("1.414")*1.414
1.9993959999999997
>>> float(1.414*1.414)
1.9993959999999997
