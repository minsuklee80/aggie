thePass = "1234"
newPass = input("암호: ")
ErrorPass = 0

while thePass != newPass:
    ErrorPass = ErrorPass+1
    newPass = input("다시 입력해주세요~ ")

print(ErrorPass, "번 틀렸네요.")
print("반가워요!")
