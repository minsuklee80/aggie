def v(string):
    vowels = 'aeiou'
    numV = 0
    string = string.lower()
    for x in string:
        if x in vowels:
            numV += 1
    return numV

print("Hello, Bill. I love Windows.에서 모음의 개수: %d" \
%v("Hello, Bill. I love Windows."))
