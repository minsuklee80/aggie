import random

a = input("로또 번호 6개 입력하세요(예:1,2,3,4,5,6): ")
a1 = a.split(',')
print("구입 번호: %s" %a1)
print("당첨 번호: %s" %random.sample(range(1,46), 6))
