tnum = '\0일이삼사오육칠팔구'
number = int(input("숫자를 입력하세요(두 자리까지만): "))
if number < 10:
    print(tnum[number])
else:
    print(tnum[int(number/10)]+'십'+' '+tnum[int(number%10)])
