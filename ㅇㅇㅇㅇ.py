'''
ps = ["hello", 3.0, 5, [10, 20]]
ps[3][2]
'''
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
#배선생님 실습 예시 1
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

for i in range(len(cities)):
    print('%10s a is a city.' %cities[i])
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
    
