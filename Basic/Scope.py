'''파이썬에서 말하는 스콥은 변수가 어디에서 정의 되었냐를 생각하면 되는것이다. 만약 변수가 클라스 혹은 펑션에서 정의가 되었다면
그것은 local scope 즉 그 클라스 안에서 정의된 변수인것이다. 만약 평균적으로 우리가 사용하는곳에서 사용된것이라면 그것을
Global scope이라고 부른다. '''

# local scope - 함수안에서만 사용가능한 변수
def local():
    x =300
    print(x)
local()

# 그리고 펑션안에서 정의된 function은 funtion안의 function에서도 사용 가능하다.

def inner_local():
    x = 500
    def inner_fun():
        print(x)
    inner_fun()
inner_local()

# 다음은 global scope이다.
x = 600

def glo_func():
    print(x)
glo_func()
print(x)

def glob():
    global x
    x=300
glob()
print(x)

x = 300
def myfunc():
  global x
  x = 200

myfunc()

print(x)

