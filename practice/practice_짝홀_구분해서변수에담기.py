# 홀수, 짝수 판단, 새 리스트 생성

numbers = [9, 56, 75, 31, 18, 19, 3, 4, 6, 7, 8, 2, 13, 56, 79, 23, 44, 56, 67, 87, 88]
even = []
odd = []

for i in numbers:
    if (i%2) == 0:
        even.append(i)
    else:
        odd.append(i)
        
print("odd numbers: ", odd)
print("even numbers: ", even)



    
