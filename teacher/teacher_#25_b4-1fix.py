j=0
k=0
for i in range(10):
    j += 10**i
    k += j
    if i==9:
        print(k-10)
        break
    print(k)
