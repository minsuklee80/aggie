def vo(string):
    string = string.lower()
    v = 'aeiou'
    vc = 0
    for x in string:
        if x in v:
            vc += 1
    return vc
