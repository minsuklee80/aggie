import time

j=987654321
for i in range(9,0,-1):
    time.sleep(0.03)
    print(j)
    j -= i*10**(i-1)
