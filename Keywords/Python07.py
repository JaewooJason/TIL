# 파이썬에서 가장 많이 사용되고 있는 것들을 공부

# and 의 사용법(Logical operator)
x= (5>3 and 5<10)
print(x) # 두 가지 모두 다 맞다면 True로 리턴한다. 아니라면 False
# and 는 if에서 사용하는 경우가 많다.
if 5>3 and 5<10:
    print('Both statements are True')
else:
    print('At least one of statements are False')

# as의 사용법
import calendar as c
print(c.month_name[1]) # as는 import 한 라이브러리의 약어를 만들어준다
# 밑에 있는 예시 처럼 자주 사용된다.
import numpy as np
import pandas as pd

# assert의 사용법
x = 'hello'
# assert는 디버깅할때 많이 사용된다.
assert x == 'hello'
# True 라면 아무일도 일어나지 않음
# assert x == 'goodbye'
# but if it is not True, then you can see the error

# assert x == "good morning","x should be 'hello'"

# break 의 사용법
# 보통 break는 while loop에서 가장 많이 사용한다. 밑에 있는 예시를 보면 좀 더 쉽게 이해가 갈 수 있다.
# or For loop에서도 많이 사용한다.
i = 1
while i < 9 :
    print(i)
    if i ==3:
        break
    i += 1

# class 의 사용법
# class 는 부모 클라스, 자식 클라스로 나뉘면서 자식 클라스는 부모의 클라스를 상속 받으면서 자신 만의 클라스를 가진다.
# class 안에는 def을 사용하여 만들 수 있다.
class Person():
    name = 'Jason'
    age = 29

p1 = Person()
print(p1.name)

# contiue 의 사용법
for i in range(9):
    if i == 3:
        continue
    print(i)


# 다르게 사용하는 방법
i = 0
while i <9:
    i += 1
    if i ==3:
        continue
    print(i)

# def 의 사용법
# def 는 funcion 을 만드는것이다. 영어로 define이라고 생각해주면 된다.
def my_function():
    print('When I used~')

my_function()

# del 의 사용법
# del을 이용해서 class 삭제
class Myclass:
    name = "Jason"
del Myclass

print(Myclass)
# del을 이용해서 변수 삭제
x = 'hello'
del x
print(x)




