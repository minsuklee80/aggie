import random

gbb = {'1':'가위', '2':'바위', '3':'보'}
youwin = ['13', '21', '32']

you = input("결정하셩. 가위(1), 바위(2), 보(3): ")
py = random.choice('123')

if you==py:
    print("너 %s? 나돈데.\n우린 일심도체!" %gbb[you])
elif you+py in youwin:
    print("너 %s야? 난 %s.\n헉! 내가 젖소." %(gbb[you], gbb[py]))
else:
    print("넌 %s네. 우하하 난 %s인데.\n메롱!" %(gbb[you], gbb[py]))
