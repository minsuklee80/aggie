o_string = "aBCdeFgHiJkLmnOpqRsTuVwXyZ"
upper = ''
lower = ''

print("원래 문자열: %s" %o_string)

for i in o_string:
    if (ord('A') <= ord(i) <= ord('Z')):
        upper+=i
    if (ord('a') <= ord(i) <= ord('z')):
        lower+=i

print("대문자 문자열: %s" %upper)
print("소문자 문자열: %s" %lower)
