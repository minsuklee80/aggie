import turtle as t

#그리고 싶은 다각형 묻기
angleNom = input("어떤 다각형을 그릴 지 다음 괄호에서 골라주세요(3/4/5/6/8). ")
angleNom = int(angleNom)

length = 100
posX = -50
posY = -75

#다각형 그리기
def m_side(length, angleNom):
    angleNom = angleNom + 3
    t.fd(length)
    t.left(360/angleNom)
    
#다각형 위치
def move_turtle(posX, posY):
    t.penup()
    t.goto(posX, posY)
    t.pendown()
  
#다각형 그리기 + 위치
def m_polygon(length, angleNom, posX, posY):
    move_turtle(posX, posY)
    for i in range(angleNom):
        m_side(length, angleNom)
    print("메인의 angleNom: ", angleNom)

m_polygon(length, angleNom, posX, posY)













