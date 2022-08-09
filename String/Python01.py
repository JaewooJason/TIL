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
print(a)

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
