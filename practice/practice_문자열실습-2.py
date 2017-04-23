name = "lee min suk"

print("이름: %s" %name)
print("e: %d개" %name.count("e"))
print("i: %d개" %name.count("i"))
print("u: %d개" %name.count("u"))

#vowels = ""

#vowels = "eiu"
#numVowels = 0
#for i in range(3):
#    numVowels += name.count(vowels[i])
#print("모음은 모두: %d개" %numVowels)


noletters = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(alphabet)):
    if name.find(alphabet[i]) == -1:
        noletters += alphabet[i]

print("이름에 없는 알파벳은: %s 이네요." %alphabet)




