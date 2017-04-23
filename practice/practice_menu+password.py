thePass = "1234"
passErrorCount = 0
choice = input("메뉴를 선택해 주세요.\n로그인(1), 암호 변경(2), 종료(q): ")

while (choice.lower() != "1") and (choice.lower() != "1") and (choice.lower() != "1"):
    ErrorCount += 1
    if ErrorCount < 5:
        choice = input("메뉴를 다시 선택해 주세요.\n로그인(1), 암호 변경(2), 종료(q): ")




        if passErrorCount < 3:
            newPass = input("암호를 다시 눌러주세요: ")
        else:
            break
    if thePass == newPass:
        print("반가워요!")
    else:
        thePass = input("암호를 변경해 주세요: ")

#로그인하기
if choice == "1":
    print("반가워요!")

#암호 변경하기
if choice == "2":
    print("암호를 변경해 주세요.")

#종료하기
if choice.lower() == "q":
    print("프로그램을 종료합니다.")
