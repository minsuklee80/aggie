# 대출 상환금 계산

#사용자 입력
print("대출 상환금 계산")

loan = int(input("대출금(백만원 이상 만원 단위): "))
assert loan>=100
years=int(input("대출 기간(연 단위): "))
assert years>=1
yrate=float(input("연 이자율(% 단위): "))
assert 0<=yrate<=100

loan = loan*10000
months = years*12
mrate = yrate/12/100

# 상환금 계산
mpay = loan * mrate * ((1+mrate)**months) / ((1+mrate)**months-1)

# 월 상환금 출력
print("매월 상환금: %d원" %mpay)
