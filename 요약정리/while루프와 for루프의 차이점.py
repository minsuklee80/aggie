#for와 while 실습하기 - 1
>>> for i in range(0,10,2):
	print(i)

0
2
4
6
8
>>>
>>>
>>>
>>> i
8
>>>
>>> i = 0
>>> while i < 10:
	print(i)
	i = i + 2

0
2
4
6
8
>>> i
10



#for와 while 실습 설명
#for 루프에서는 변수값을 초기화할 필요가 없다.
for i in range(0,10,2): #시작 0, 종료 10-1, 간격 2
    print(i)

print("for 루프가 끝난 i의 값: ", i) #for 루프 바깥이다.


#while 루프에서 사용하는 조건문의 변수값은 초기화가 필요하다
i = 0           #조건문 변수 초기화
while i < 10:   #i가 10보다 작은 동안
    print(i)
    i = i + 2   #순서상 다음 i를 지정하기위해

print("while 루프가 끝난 i의 값: ", i) #while 루프 바깥이다.
