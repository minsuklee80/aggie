#이름:
#길이:
#대문자로:
#마지막글자:
#마지막 글자를 이름의 길이만큼 반복하면:
#이름 세로쓰기:

name = "Lee min suk"
print("이름: %s" %name)
print("길이: %d" %len(name))
print("대문자로: %s" %name.upper())
print("마지막 글자: %s" %name[-1])
print("마지막 글자를 이름의 길이만큼 반복하면: %s" %(name[-1]*len(name)))
for i in name:
	print(i)
