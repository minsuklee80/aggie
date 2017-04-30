import random

lotto_mynum = []

for i in range(1,7):
    mynum = int(input("%d번째 로또 번호를 입력하세요: " %i))
    while mynum > 45:     #45보다 큰 번호는 오류를 표시
        print("로또는 45까지만 있습니다.")
        mynum = int(input("%d번째 로또 번호를 입력하세요: " %i))
    lotto_mynum.append(mynum)

if len(lotto_mynum) == 5:
    mynum = input("로또 번호를 하나 더 입력하세요: ")
    lotto_mynum.append(mynum)
    
print("당신이 선택한 번호는\n%d 입니다." %set(lotto_mynum))

lotto = set(range(1,46))                     #로또 전체 번호
num1 = set(random.sample(range(1,46), 6))    #로또 1등 번호
num2 = set(random.sample((lotto - num1), 1)) #로또 2등 보너스 번호
print("이번 로또 번호는 /n%d이고,\n보너스 번호는%d 입니다." %(num1, num2))

lotto_num1 = len(num1 & set(lotto_mynum))
lotto_num2 = num2 & set(lotto_mynum)

if lotto_num1 == 6:
    print("축하합니다. 1등에 당첨되었습니다.")
elif lotto_num1 == 5:
    if len(num2 & lotto_num2) == 1:
       print("축하합니다. 2등에 당첨되었습니다.")
    else:
        print("축하합니다. 3등에 당첨되었습니다.")   
elif lotto_num1 == 4:
    print("축하합니다. 4등에 당첨되었습니다./n")
else:
    print("꽝")


