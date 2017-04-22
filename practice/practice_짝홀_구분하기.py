
#짝홀구분
#x(1~10)의 제곱을 리턴한다.
>>> [x*x for x in range(1,11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#x의 제곱을 리턴 후 2로 나눠
#나머지가 1이면 false 0이면 true이고, 
#true만 출력한다.
>>> [x*x for x in range(1,11) if not(x*x%2)]
[4, 16, 36, 64, 100]


>>>listA = []
>>>for x in range(1,11):
       if not(x*x%2):
           listA.append(x*x)
>>>print(listA)
[4, 16, 36, 64, 100]
#위의 코드 b와 같은 값을 출력한다.





#random 모듈 설명
>>> help(random.choice)
Help on method choice in module random:

choice(seq) method of random.Random instance
    Choose a random element from a non-empty sequence.
#choice 메소드는 늘어서 데이터(문자열)를 사용함


>>> help(random.randint)
Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points. #설명 틀림
#randint 메소드는 정수 사용


#tip.
>>> random.randint(1,10)
10
#random.randint(1,10)는 1에서 10 중에서 랜덤으로 숫자 선택

>>> list(range(1,10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#list(range(10))은 0에서 9까지 리스트를 출력
'''



#데이터의 형식을 어떻게 정의하느냐에 따라 코드의 알고리즘이 달라진다.




o_string = "aBc"
upper = ''
lower = ''

print("원래 문자열: %s" %o_string)

for i in o_string:
    if ord('A') <= ord(i) <= ord('Z'):
        upper+=i
    if ord('a') <= ord(i) <= ord('z'):
        lower+=i

print("대문자: %s" %upper)
print("소문자: %s" %lower)
