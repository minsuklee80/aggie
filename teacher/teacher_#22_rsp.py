import random

gbb = ["가위", "바위", "보"]

you = int(input("결정하셩. 가위(1), 바위(2), 보(3): ")) - 1
py = gbb.index(random.choice(gbb))

if you == py:
    print("너 %s? 나도 %s인데.\n우린 일심도체!" %(gbb[you], gbb[py]))
elif ((you==0) and (py==2)) or (you == py+1):
    print("너 %s야? 난 %s.\n헉! 내가 젖소." %(gbb[you], gbb[py]))
else:
    print("넌 %s네. 우하하 난 %s인데.\n메롱!" %(gbb[you], gbb[py]))
