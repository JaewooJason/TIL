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

# print(Myclass)
# del을 이용해서 변수 삭제
x = 'hello'
del x
# print(x)

# elif 사용법
for i in range(-5,5):
    if i>0 :
        print("Yes")
    elif i == 0:
        print('Whatever')
    else:
        print('No')
# else if 를 합친거라고 생각하면 된다.

# else 사용법
x = 2
if x > 3 :
    print('Yes')
else:
    print('No')

# 혹은 try except 문에도 사용 가능하다.

x = 5

try:
    x > 10
except:
    print('Something went wrong')
else:
    print('The "try" code was excuted without raising any errors')

# except 사용법
try:
    x > 3
except:
    print("something went wrong")


x = 'hello'
try :
    x > 3
except NameError:
    print('You have a variable that is not defined.')
except TypeError:
    print("You are comparing value of different type")

try :
    x = 1/10
except NameError:
    print("You have a variable that is not defined.")
except TypeError:
    print("You are comparing values of different type")
except:
    print("something else went wrong")

x = 1

try :
    x >10
except NameError:
    print("You have a variable that is not defined.")
except TypeError:
    print("You are comparing values of different type")
else:
    print("The 'Try' code was excuted without raising any errors")

# Fasle 의 사용법
print(5 > 6)
print( 4 in [1,2,3])
print('hello' is 'goodbye')
print(5==6)
print(5==6 or 6==7)
print(5==6 and 6==7)
print('Hello' is not 'Hello')
print(3 not in [1,2,3])

# finally 의 사용법

try:
    x > 3
except:
    print('Something went wrong!')
else:
    print('Nothing went wrong')
finally:
    print('The try..... except block is finished')
# finally is useful to close the object and clean up resources

# for 의 사용법

for i in range(1,9):
    print(i)

for i in ['apple','banana','cherry']:
    print(i)
# or

fruits = ['apple','banana','cherry']
for i in fruits:
    print(i)

from datetime import time
x = time(hour=15)
print(x)

# global 의 사용법
def myFunction():
    global x
    x = 'hello'
myFunction()
# global은 함수안에 있는 지역변수 함수밖에서도 사용하게 하는 키워드이다.
# global을 사용하게 되면 디버깅에도 편리하며 함수밖에서 써도 되지만 함수 안에서 사용함으로써 좀 더 쉽게 정의 할 수 있다.
print(x)

# if 의 사용법

x = 5
if x > 3:
    print('Yes')
# else를 같이 사용하는 경우

x = 5
if x > 3:
    print('Yes')
else:
    print('No')

# import 의 사용법
import datetime

x = datetime.datetime.now()
print(x)


# in 키워드 사용법

fruits = ["apple",'banana','cherry']
if 'banana' in fruits:
    print('Yes')
# 위에 경우 처럼 if 문에 사용하는 방법도 존재하고
for i in fruits:
    print(i)
# 위에 방법 처럼 for으로 사용하는 방법도 있습니다.

# is 의 사용법
x = ['apple', 'banana','cherry']
y = x
print(x is y)

x = ['apple', 'banana','cherry']
y = ['apple', 'banana','cherry']

print(x is y)

# lambda 의 사용
x = lambda x : x + 10
print(x(5))

x = lambda a,b,c : a + b + c
print(x(4,5,6))

# None 의 사용법

x = None

print(x)

if x :
    print('Do you think None is True?')
elif x is False:
    print('Do you think None is False?')
else:
    print('None is not True and False. None is just None')

# nonlocal 의 사용법

def myFunc1():
    x = 'Jason'
    def myFunc2():
        nonlocal x # nonlocal을 사용하면 내부변수가 아닌 광역 변수로 바뀌게 되는것이다.
        x = 'Hello'
    myFunc2()
    return x
print(myFunc1())
# 아래와 비교하면 좀 더 쉽게 이해가 가능하다.
def myFunc3():
    x = 'Jason'
    def myFunc4():
        x = 'Hello'
    myFunc4()
    return x
print(myFunc3())

# not 의 사용법

x = False
print(not x)

# or 의 사용법
x = (7>5 or 6>5)
print(x)

# if문 안에서도 많이 사용된다.
if 7 >5 or 6>5:
    print('At least one of the statements are True')
else:
    print('None of the statement are True')

# pass 의 사용법
# 보통 pass 는 함수를 설정하거나 클라스를 설정하기전에 정확하지 않은 상황에서 열려있는 함수나 클라스를 넘길 때 사용

def myFunc():
    pass

class myClass():
    pass

a = 22
b = 400
if a < b:
    pass
# raise 사용법
# 상황에 따라 에러를 발생시키는 용도

x =-1

if 0 >x:
    raise Exception('Sorry, there is no number below Zero')

x= 'hello'

if not type(x) is int:
    raise TypeError('Only integers are allowed')

# how to use returen keyword

# The return keyword is that exit a function and return the sum

def myFunc1():
    return 3+3

print(myFunc1())

def myFunc2():
    return 6+2
    print('Hello, World')
print(myFunc2())

# True 의 사용법
# True는 불리언으로 비교하여서 결과를 True or False 로 나타낸다.
print(7>6)
print(5==5)
print(3<7)
print('hello' is not 'goodbye')

# try 의 사용법
# try and except 는 세트라고 생각하면 된다. 예외처리의 세트

try:
    x >3
except:
    print('Something went wrong')
# or below

try:
    x > 5
except:
    Exception('Something went wrong')

# while 의 사용법
# while 또한 loop 를 만들어 주는 함수이다.

x = 0
while x < 9:
    print(x)
    x = x +1
# while 구문을 쓸때 continue and break를 많이 사용한다.
