'''
2017년 4월 24일 제27차

what matters most in life?
유튜브에서 검색해보세용

차정인 기자의 T타임 소프트웨어 토크 콘서트에서 나온 명문장
코딩의 핵심은 생각(과정)의 구조화가 우선되어야 한다. 손(코딩)은 나중에...
========================================================================
대부분의 언어는 변수 타입(variable type)을 미리 정해야(선언) 한다.
하지만 python은 변수 타입을 미리 정하지 않아도 되는 것이 가장 큰 특징이다.
타입 오류가 있을 경우 연산 할 때 에러가 난다.
(ex. 'abc'+1 문자열과 정수는 연산이 되지 않는다.)
========================================================================
함수의 특징은 재사용성, 디버깅, 모듈성, 확장성(고무줄처럼 유연하게 커졌다 작아지는)이다.
(마인크래프트 도서 참고)
함수 사용의 목적은 각자의 역할을 분업하기 위함이다.
함수는 주연, 조연, 액스트라 등의 배역과 같다.
========================================================================
namespace ===> 함수를 지칭하는 단어
========================================================================
따옴표 세 개 주석 (''' abc ''')
docstring ===> 함수 역할의 설명과 함수 속 변수의 설명을 작성한 문장
========================================================================
파이썬은 묵시적(implicit)이고, 대부분의 언어는 명시적(explicit)이다.
========================================================================
클래스는 프랜차이즈의 본점에 해당하고 인스턴스는 지점에 해당한다.
instanciation ===> 인스턴스를 생성
(대체로 '인스턴스화'라고 번역 되어지지만 '인스턴스 생성'이 더 적합한 번역이다. )
override => 인스턴스 된 것이 그 상황에 맞게 변경되는 것을 말한다.
클래스에 포함된 함수는 '메서드'라고 한다.

'''
def greet():    #함수 정의하기
	'''greets all of you.'''
	print("Hello!")
	print("Nice to meet you.")


def greet(name):    #인수가 있는 함수
	'''greets all of you.'''
	print("Hello! " + name)

return
