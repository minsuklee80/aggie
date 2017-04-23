import getpass
thePW = "1234"
passwordErrorCount = 0

choice = input("메뉴를 선택하세요. 로그인(1), 비밀번호 변경(2), 종료(q): ")
menu = choice.lower()

while (menu != "1") and (menu != "2") and (menu != "q"):
    choice = input("메뉴를 다시 선택하세요(1,2,q): ")
    menu = choice.lower()

#로그인하기
if choice == "1":
    newPW = getpass.getpass("비밀번호를 입력하세요: ")
    if thePW != newPW:
        print("로그인 되었습니다.")
    else:
        print("바이러스에 감염되었습니다.")

