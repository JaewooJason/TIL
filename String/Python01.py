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



