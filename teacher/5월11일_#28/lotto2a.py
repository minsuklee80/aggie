lotto = [1, 2, 3, 4, 5, 6]
lotto.sort()
you = [int(x) for x in input("번호 6개 입력(예: 1,2,3,4,5,6): ").split(",")]
you.sort()
result = {3:'5등', 4:'4등', 5:'3등', 6:'1등'}
win = [x for x in you if x in lotto]

print("당첨 번호: %s" %lotto)
print("구입 번호: %s" %you)

if win == []:
    print("일치하는 번호가 없습니다!")
else:
    print("일치 번호: %s" %win)

if len(win) >= 3:
    print("%s" %result[len(win)])
else:
    print("아우~ 아까워라!")
