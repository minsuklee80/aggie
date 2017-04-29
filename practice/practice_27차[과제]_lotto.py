import random
lotto_mynum = []

lotto = set(range(1,46))
lotto_num1 = set(random.sample(range(1,46), 6))
print("이번 로또 번호는 %s입니다." %lotto_num1)
lotto_num2 = set(random.sample((lotto - lotto_num1), 1))
print("이번 보너스 번호는 %s 입니다." %lotto_num2)

for i in range(1,7):
    mynum = int(input("%d번째 로또 번호를 입력하세요 " %i))
    while mynum > 45:
        print("로또는 45까지만 있습니다.")
        mynum = int(input("%d번째 로또 번호를 입력하세요 " %i))
    lotto_mynum.append(mynum)
    
print(input("당신이 선택한 번호는 %s 입니다. " %set(lotto_mynum)))
lotto_mynum1 = set(lotto_mynum)
lotto_num_a = len(lotto_num1 & lotto_mynum1)

if lotto_num_a == 6:
    print("1등")
elif lotto_num_a == 5:
    print("2등")

    

'''
lotto_num1과 비교
1등 6개가 같다. 상금 10어어어억
2등 5개가 같고, lotto_num2가 같다. 상금 1어어어억
3등 5개가 같다. 상금 1백만원
4등 4개가 같다. 상금 5,000원
'''
