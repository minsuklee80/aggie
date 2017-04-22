#함수 실습하기 - 사람은 도구를 사용할 줄 안다.
import turtle as t          #turtle 라이브러리를 가져온다.

def drawSide(side, angle):  #함수를 정의한다. 인수는 side와 angle이다.
    t.fd(side)              #인수 side만큼 선을 긋는다.
    t.lt(angle)             #인수 angle만큼 왼쪽으로 회전한다.

#drawSide 함수의 첫 번째 인수(side)에 100을, 두 번째 인수(angle)에 90을 전달한다.
drawSide(100, 90)   #100짜리 선을 긋고, 왼쪽으로 90도 회전
drawSide(100, 90)   #100짜리 선을 긋고, 왼쪽으로 90도 회전
drawSide(100, 90)   #100짜리 선을 긋고, 왼쪽으로 90도 회전
drawSide(100, 90)   #100짜리 선을 긋고, 왼쪽으로 90도 회전

#함수에 사용된 side와 angle은 함수를 실행할 때만 사용되는 지역 변수이다.



'''
#다각형 만들기_1 함수
def m_side(side, angleNom):
    t.fd(side)
    t.lt(360/angleNom)

#다각형 그리기 위치
def move_turtle(posX, posY):
    t.penup()
    t.goto(posX, posY)
    t.pendown()

#다각형 그리기 + 위치
def m_polygon(length, angleNom, posX, posY):
    move_turtle(posX, posY)
    for i in range(angleNom):
        m_side(length, angleNom)

m_polygon(100, 8, -50, -100)
m_polygon(100, 6, -50, -100)
m_polygon(100, 5, -50, -100)
m_polygon(100, 4, -50, -100)
m_polygon(100, 3, -50, -100)
'''
