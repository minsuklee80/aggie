#구구단 출력하기
#한영:구구단(multiplication table)

multiplicationtable=0
multipli=int(input("구구단: "))
count=0
'''
for multipli in range(1, 10):
    for count in range(1, 10):
        multiplicationtable=multipli*count
        print(multiplicationtable)
'''
for count in range(1, 10):
    multiplicationtable=multipli*count
    print('%dx%d=%2d' %(multipli,count,multiplicationtable))

