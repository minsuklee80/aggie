lotto = [1, 2, 3, 4, 5, 6]
lotto.sort()
you = [10, 12, 23, 3, 6, 40]
you.sort()
count = 0
win = []

print("당첨 번호: %s" %lotto)
print("구입 번호: %s" %you)

for x in you:
    if x in lotto:
        count += 1
        win.append(x)

if win == []:
    print("일치하는 번호가 없습니다!")
else:
    print("일치 번호: %s" %win)
    if count == 3:
        print("5등")
    elif count == 4:
        print("4등")
    elif count == 5:
        print("3등")
    elif count == 6:
        print("1등")
    else:
        print("아우~ 아까워라!")
