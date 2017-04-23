st = '영일이삼사오육칠팔구'
tunit = '십'
strnum = input("숫자를 입력하세요(두 자리 숫자만): ")
print('%s%s %s' %(st[int(strnum[0])], tunit[0], st[int(strnum[1])]))
