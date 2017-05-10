import random

lotto_mynum = []                                #내 번호가 담길 곳
tap = '-----------------------------------'     #구분선

for i in range(1,7):
    mynum = int(input("%d번째 번호 입력: " %i))
    while mynum > 45:                           #45보다 큰 번호 오류 표시
        print("로또는 45까지만 있습니다.")
        mynum = int(input("%d번째 번호 입력: " %i))
    lotto_mynum.append(mynum)
while len(set(lotto_mynum)) < 6:                #중복되는 번호가 있을 경우 번호 추가하기
    mynum = int(input("번호를 하나 더 입력: "))
    lotto_mynum.append(mynum)

print("%s\n구입 번호: %s" %(tap, list(set(lotto_mynum))))

lotto = set(range(1,46))                        #로또 전체 번호
num1 = set(random.sample(range(1,46), 6))       #로또 1등 번호
num2 = set(random.sample((lotto - num1), 1))    #로또 2등 추가 번호

print("당첨 번호: %s" %(list(num1)))
print("추가 번호: %s" %(list(num2)))

if len(num1 & set(lotto_mynum)) == 0:           #1등 번호와 내 번호 비교
    print("일치 번호: 없음")
else:
    print("일치 번호: %s" %list(num1 & set(lotto_mynum)))

if len(num1 & set(lotto_mynum)) == 6:
    print("%s\n1등" %tap)
elif len(num1 & set(lotto_mynum)) == 5 and len(num2 & set(lotto_mynum)) == 1:
    print("%s\n2등" %tap)
elif len(num1 & set(lotto_mynum)) == 5:
    print("%s\n3등" %tap)
elif len(num1 & set(lotto_mynum)) == 4:
    print("%s\n4등" %tap)
else:
    print("%s\n꽝!" %tap)




