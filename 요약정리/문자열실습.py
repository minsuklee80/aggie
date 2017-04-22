#이스케이프(escape) 문자
#\(역슬래쉬)를 붙여 원래의 의미를 벗어나는 문자

\n      개행(줄바꿈)
\v      수직 탭
\t      수평 탭
\r      캐리지 리턴
\f      폼 피드
\a      벨소리
\b      백스페이스
\000    널(Null)
\\      문자 '\'
\'      단일 인용부호(')
\"      이중 인용부호(")

>>> a = 'abc \n def'
>>> print(a)
abc
 def
>>> a = 'abc \v def'
>>> print(a)
abc  def
>>> a = 'abc \t def'
>>> print(a)
abc 	 def
>>> a = 'abc \r def'
>>> print(a)
abc
 def
>>> a = 'abc \f def'
>>> print(a)
abc  def
>>> a = 'abc \a def'
>>> print(a)
abc  def
>>> a = 'abc \b def'
>>> print(a)
abc  def
>>> a = 'abc \000 def'
>>> print(a)
abc

print("Hi,\vHellow")
print("Hi,\tHellow")
print("Hi,\aHellow")
print("Hi,\bHellow")

#대소문자 변경
.lower()        #모두 소문자
.upper()        #모두 대문자
.capitalize()   #문장 첫 글자만 대문자
.title()        #단어 첫 글자만 대문자

>>> a = 'abc DEF'
>>> a.lower()
'abc def'
>>> a.upper()
'ABC DEF'
>>> a.capitalize()
'Abc def'
>>> a.title()
'Abc Def'



#문자열 다루기
>>> name = 'Lee min suk'
>>> name
'Lee min suk'
>>> print(name)
Lee min suk
>>> len(name)	         #len은 요소의 길이를 공백 포함해서 나타냄
11
>>> print(len(name))
11
>>> name[0]
'L'
>>> name[10]            #리스트 넘버는 '0'부터 시작하니까 마지막 번호는 '10'
'k'
>>> name[len(name)-1]   #요소의 길이가 '11'니까 리스트 넘버 '10'이 출력
'k'
>>> name[-1]
'k'
>>> name[-1]*len(name)  #10번째 글자 11개를 출력
'kkkkkkkkkkk'
>>>



#포맷 문자(%)
>>> mypens = 100
>>> youpens = 90
>>> print('I have', mypens, 'pens.')
I have 100 pens.
>>> print("I have "+str(mypens)+" pens.")
I have 100 pens.
>>> print("I have",str(mypens),"pens.")
I have 100 pens.
>>> print("I have %d pens." %mypens)
I have 100 pens.
>>> print("I have %s pens." %str(mypens))
I have 100 pens.
>>> print("I have %d pens and you have %d pens" %(mypens, youpens))
I have 100 pens and you have 90 pens

>>> x = 100
>>> print("x: %d" %x)   #int
x: 100
>>> print("x: %s" %x)   #str
x: 100
>>> print("x: %c" %x)   #???
x: d
>>> print("x: %f" %x)   #부동소수점?
x: 100.000000
>>> print("x: %o" %x)   #???
x: 144
>>> print("x: %x" %x)   #???
x: 64
