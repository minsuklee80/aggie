a = int(input("어떤 곱셈을 할까? 숫자 하나 입력하셩: "))
b = int(input("어떤 곱셈을 할까? 다른 숫자도 입력하셩: "))
c = int(input("몇이라고 생각해? "))
if c == a * b:
    print("오케이. %d x %d = %d. 이거 맞아." %(a, b, c))
else:
    print("에휴~ %d x %d = %d. 이렇게 되는 건데. 넌 %d?" %(a, b, a*b, c))
