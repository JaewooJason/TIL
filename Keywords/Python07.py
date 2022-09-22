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
assert x == 'goodbye'
# but if it is not True, then you can see the error

assert x == "good morning","x should be 'hello'"


