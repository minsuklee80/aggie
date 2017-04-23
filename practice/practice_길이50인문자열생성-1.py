import random
import string

fifty = ''
# 임의의 문자열 생성
for i in range(50):
    fifty += random.choice(string.ascii_letters)

print('생성된 문자열: %s' %fifty)
print('이 문자열의 길이: ', len(fifty))
