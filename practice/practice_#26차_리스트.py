#다음의 리스트 중 '20'을 출력할 방법
'''
ps = ["hello", 3.0, 5, [10, 20]]
ps[3][2] #첫번째 대괄호는 전체 리스트 위치, 두 번째 대괄호는 리스트 속 리스트 위치
'''
#리스트 속에 원하는 새가 있으면 'ok' 없으면 'zzz'를 출력
'''
birds = ['vulture', 'eagle', 'swallow', 'duck', 'sparrow']
count = 0
for i in birds:
    if i == 'sparrow':
        print('ok')
    else i != 'sparrow':
        count += 1
        if count == len(birds):
            print('zzz')

'''
'''
birds = ['vulture', 'eagle', 'swallow', 'duck', 'sparrow']
if 'sparrow' in birds:
    print('ok')
else:
    print('zzz')
'''
'''
#배선생님 실습 예시 2
birds = ['vulture', 'eagle', 'swallow', 'duck', 'sparrow']
if birds.count('sparrow'):
    print('ok')
else:
    print('zzz')
'''

'''
cities = ['Seoul', 'Busan', 'Jeju', 'Sejong', 'Suwon']
for i in cities:
    print('%s a is a city.' %i)

'''
'''
#배선생님 실습 예시 1
cities = ['Seoul', 'Busan', 'Jeju', 'Sejong', 'Suwon']
for i in range(len(cities)):
    print('%s a is a city.' %cities[i])
'''
#출력
Seoul a is a city.
Busan a is a city.
Jeju a is a city.
Sejong a is a city.
Suwon a is a city.

'''
for i in range(len(cities)):
    print('%10s a is a city.' %cities[i])
'''
#출력
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
'''

birds = ['vulture', 'eagle', 'swallow', 'duck', 'sparrow']
you = input('Enter a bird: ')

if you in birds:
    print('\'%s\' is a bird' %you.capitalize())
else:
    print('\'%s\' is NOT a bird' %you.capitalize())

#이스케이프 문자와 포맷 스트링에 대해서 알아두기
#로케일이 뭘까?

lotto = list(range(1,46))
Lot_Num = {1, 12, 23, 34, 44, 45}
You_Num = {1, 12, 23, 34, 44, 45}

#구구단
for i in range(1,10):
    print("9 x %d = %2d" %(i, 9*i))
for i in range(1,10):
    print("9 x %f = %3f" %(i, 9*i))
for i in range(1,10):
    print("9 x %f = %3.0f" %(i, 9*i))
for i in range(1,10):
    print("9 x %f = %3.0f" %(i, 9*i))
