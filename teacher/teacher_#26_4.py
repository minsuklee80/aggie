birds = ['vulture', 'eagle', 'swallow', 'duck', 'sparrow']

# 사용자에게 단어를 입력받고 그 단어가 birds에 있는지 없는지
ub = input("Enter a bird: ")

if ub in birds:
    print("%s is a bird." %ub)
else:
    print("%s is NOT a bird." %ub)

# 혹시?
# print('OK')
