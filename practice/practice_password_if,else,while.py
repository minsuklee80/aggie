thePass = "1234"
newPass = input("암호: ")


#if thePass == newPass:
#    print("반가워요!")
#else:
#    print("다시 입력해주세요~ ")
#    newPass = input("암호: ")
#    if thePass == newPass:
#        print("반가워요!")
#    else:
#        print("다시 입력해주세요~ ")



#newPass를 thePass와 비교문
thePass = "1234"
newPass = input("암호: ")
ErrorPass = 0

while newPass != thePass:
    ErrorPass = ErrorPass+1
    newPass = input("다시 입력해주세요~ ")
    if ErrorPass == 5:
        break
    print(ErrorPass, "번 틀렸네요.")
        
    
  
#print(ErrorPass, "번 틀렸네요.")
print("반가워요!")









