#구구단 중 7단 출력하기
'''
for x in range(1,10):
    print("7 x %d = %2d" %(x,7*x))  #포맷문자열 %s는 문자열, %d는 정수(10진수)
                                    #포맷문자열에서 '%'과 'd'사이의 숫자는 출력 열 수다

for x in range(1,10):
    print("7 x", x, "=", 7*x)       #포맷문자열을 사용하지 않았을 때

'''
#포맷문자열 실습
'''
print("%3.1f" %12.345)              #'%f'부동소수점(Floating point) 출력
int(12.567)                         #출력은 뒤 소수점 뒤 모두를 버리고 '12'가 나온다
'''
#int는 정수만 받을 수 있다.
#flowe는 부동소수점도 받을 수 있다.
'''
a = '123456789'
for i in range(1,11):
    b=a[:11-i]

'''
