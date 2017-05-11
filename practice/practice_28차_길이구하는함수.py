def LEN(string):
    '''길이 구하는 함수
    calculates the length of the string'''
    count = 0
    for x in string:
        count += 1
    return count

'''
>>> LEN("abcdefg")
7
'''

'''
함수 만드는 법
def = 함수 정의
LEN = 함수이름
string = 파라미터(함수 속에서 통용되는 변수)

idle = caller
함수'LEN' = callee
'abcdefg' = 아규먼트(인자)
===========================================
>>> help(LEN)
Help on function LEN in module __main__:

LEN(string)
    길이 구하는 함수
    calculates the length of the string

#'LEN'함수 실행 후 help로 docstring 확인 가능.
'''
