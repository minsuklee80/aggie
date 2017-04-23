import time

for i in range(1,11):
    time.sleep(0.5)
    print('%s%s' %(' '*(10-i), 'o'*(2*i-1)))
