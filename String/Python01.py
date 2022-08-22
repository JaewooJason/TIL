# 45의 String methods 사용법

# capitalized() 사용법
a = "python is Great and Super Super usefull"
a= a.capitalize()
print(a)
b = '13th of JULY'
print(b.capitalize())


"""
capitalize의 경우 첫번째 문자를 대문자로 변경하고 나머지 문자는 소문자로 자동으로 변경시킨다. 영어 문법에서 첫글자만 대문자로 만들어주것이라고 
생각하면 쉬울거 같다. 만약에 숫자가 제일 먼저 나오게 되면 숫자의 경우 대문자로 변경이 불가능하기 때문에 대문자로 변경되지 않고 문장에
대문자는 전부 소문자로 변경된다. 
"""
# casefold()사용법
txt = "Hello, And Welcome To My World!"
print(txt.casefold())

""" casefold()의 경우 모든 글자를 소문자로 변경시켜 버리는 함수이다. 위에서 보면 알 수 있다."""

# center(length, character)의 사용법
txt = "banana"
print(txt.center(20)) # 괄호안 첫번째에 숫자를 넣으면 그 숫자만큼의 공백을 만들고 중간에 변수에 지정된 문자열을 출력한다.
print(txt.center(20,'O')) # 이경우는 첫번째는 동일하게 length을 입력하고 두번째에는 문자열로 "O"를 넣어서 지정된 변수를 중간에두고 나머지는 지정한 캐릭터로 출력된다.

# count(value, start, end)의 사용법

txt = "I love apples, apple are my favorite fruit"
print(txt.count('apple'))

# 시작부분과 끝 부분을 지정해서 문자열을 찾을 수도 있다.

print(txt.count('apple', 10, 24))

# encode() 의 사용법

txt = "My name is Ståle"

x = txt.encode()
print(x)

# string.encode(encoding=encoding, errors=errors) 이런식으로 기본값에 정의되어 있지않는 에러를 처리할때는 이렇게 사용
# 사용법은 아래와 같다
txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

# endswitch()의 사용법

txt = "Hello, welcome to my world."

a = txt.endswith('.')
print("endswitch",a)

# string.endswith(value, start, end)
a = txt.endswith('my world.')
print(a)

a = txt.endswith('my world.', 5, 11) # 여기서는 지정한 시작지점과 끝지점을 범위로 잡기 때문에 False가 나오는것이다.
print(a)

# expandtabs()의 사용법

txt = "H\te\tl\tl\to" # 이렇게 된 경우 문자열 사이사이에 탭이 들어간 상태이다.
# 좀 더 보기 쉽게 밑에 있는것을 확인하면 된다.
print(txt) # default tab size is 8!
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(6))
print(txt.expandtabs(10))

# find()의 사용법
txt = "Hello, welcome to my world."
a = txt.find('welcome')
print(a)

# string.find(value, start, end)
print(txt.find('e', 5, 10)) # 위에서 했던 endswitch와 같이 위치를 지정해서 특정구간에서만 지정한 문자를 찾을 수 있다.

print(txt.find('q')) # -1로 결과값이 나온다.
# txt.index('q') # index의 경우 없는 문자의 경우 에러로 처리하지만 find의 경우는 -1로 나타냄으로써 에러로 처리하지 않는다.

# format()의 사용법

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

# string.format(value1, value2...)

# example

txt1= "My name is {frame}, I'm {age}".format(frame = 'Jason', age = 28)
txt2= "My name is {0}, I'm {1}".format('Jason',28)
txt3 = "My name is {}, I'm {}".format('Jason', 28)

print(txt1)
print(txt2)
print(txt3)

# 다양한 기호를 이용한 format()메서드 이용

txt = "We have {:<8} chickens." # 이렇게 사용하면 오른쪽에 공백을 넣은 숫자 만큼 넣어줍니다.
print(txt.format(49))

txt = "We have {:>8} chickens." # 이렇게 사용하면 왼쪽에 공백을 넣은 숫자 만큼 넣어줍니다.
print(txt.format(49))

txt = "We have {:^8} chickens." # 이번에는 공백의 중간에 글자를 넣어줍니다.
print(txt.format(49))

'''
glossary - iterable 용어는 이렇게 번역하는 편이 좋을 것 같습니다.

iterable: 자신의 멤버를 한 번에 리턴할 수 있는 객체입니다. list, str, tuple, dict 등이 여기에 속합니다.
'''

# isalnum() 의 사용법
txt = "Company12"
print(txt.isalnum())
''' isalnum()은 문자열 안에 a-z and 0-9의 숫자가 들어 있을 경우 True로 리턴되는 메서드이다. 만약 스페이스는 특수기호가 
포함되어 있을 시 False로 리턴된다.'''


# isalpha()의 사용법

txt = "CompanyX"
print(txt.isalpha())
''' isalpha()의 경우는 a-z만 있을때 True로 리턴되는 메서드이다. 숫자가 포함되어 있어도 False로 리턴된다.'''

# isascii()의 사용법
txt = "Company123"
print(txt.isascii())
''' 파이썬에 내장되어 있는 아스키코드가 있다면 True로 리턴해주는 메서드이다.'''

# isdecimal() 의 사용법
txt = "\u0033" #unicode for 3
print(txt.isdecimal()) # 문자열안에 유니코드를 체크하는것이다. 하지만 문자가 아닌 숫자만 True로 리턴한다.

# isdisit() 의 사용법
txt = "50800"
print(txt.isdigit()) # 문자열 안에 숫자가 포함이 되어 있으면 True를 리턴해주는 메서드이다. SW 에서 기본 파이썬으로 나옴
# isdigit()의 경우 제곱도 True로 리턴해준다.
print('*'*10)
txt = '0.225'
print(txt.isdigit())#숫자가 아닌 .이나 -의 경우에는 숫자가 아니기 때문에 False 리턴이 된다.


# isidentifier()의 사용법
txt= 'Demo'
print(txt.isidentifier()) # isidentifierd()의 경우 언어(a-z), 숫자(0-9) 그리고 (_) 이렇게가 포함이 되어 있으면 True로 리턴

# 하지만 변수를 지정할때 처럼 시작이 숫자이거나 띄워쓰기가 포함되면 False 이다.
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print('*'*50)
print(c.isidentifier())
print(d.isidentifier())

# islower() 의 사용법

txt = "hello world!"
print(txt.islower())

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())



# isnumeric() 의 사용법

txt = "565543"
print(txt.isnumeric()) # 글자안에 정수가 포함이 되어 있으면 True 리턴이 된다.

a = "\u0030" #unicode for 0 유니코드도 가능하다
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1" # 음수의 경우 되지 않는다
e = "1.5" # float 의 경우에도 False 로 리턴이 된다. isdigit()의 경우에도 같은 상황이다. .이나 -의 포함은 숫자가 아니기 때문에 False 이다.

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())

# isprintable()의 사용법

txt = "Hello! Are you #1?"
print(txt.isprintable()) # 프린트가 가능한 모든 문자가 포함이 되어 있으면 True 로 리턴

txt = "Hello!\nAre you #1?"
print(txt)
print(txt.isprintable()) # txt안에 단순히 문자만 포함이 되어 있는것이 아닌 줄 바꿈의 하는 /n이 포함이 되어 있어 False 이다.

# isspace()의 사용법

txt= '       '
print(txt.isspace()) #스페이스만 포함되어 경우에만 True로 리턴이 되는 메서드이다.

txt = '      s       '
print(txt.isspace()) # 이렇게 하나만 문자가 포함이 되어 있으면 False로 리턴이 된다.


# istitle()의 사용법

txt = "Hello, And Welcome To My World!"
print(txt.istitle())
# 변수안에 있는 첫번째 문자가 대문자이고 소문자와 대문자가 섞여있으면 True리턴이 되는 메서드이다.

a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(b.istitle())
# isupper() 의 사용법

txt = "THIS IS NOW!"
print(txt.isupper()) # 이렇게 모든 문자가 대문자 일때 True로 리턴이 된다.

a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print(a.isupper())
print(b.isupper())
print(c.isupper())

myTuple = ("John", "Peter", "Vicky")
x = '#'.join(myTuple) # 이렇게 튜플안에 들어 있는 단어들을 '' 안에 설정한 문자 대로 나누게 한다.
print(x)
myList = ['John', 'Jason', 'Kiki'] # 리스트도 가능하고 딕셔너리도 가능하다.
y = ' # '.join(myList)
print(y)

myDict = {"name": "John", "country": "Norway"} # 대신 딕셔너리는 키값 사이에 들어가게 된다.
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)




