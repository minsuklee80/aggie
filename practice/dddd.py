import random
lotto = set(range(1,46))
lotto_num1 = set(random.sample(range(1,46), 6))
print("이번 로또에 선택된 번호는 %s입니다." %lotto_num1)
lotto_num2 = set(random.sample((lotto - lotto_num1), 1))
print("이번 로또에 선택된 보너스 번호는 %s 입니다." %lotto_num2)
lotto_num_a = len(lotto_num1 & lotto_mynum1)
