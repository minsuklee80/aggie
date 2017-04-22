import time
j=0
for i in range(10):
    time.sleep(0.03)
    j += 10**i
    print(j)
