# Set의 메서드 Set은 순서와 중복을 허용하지 않는다. 그러므로 유니크한 값을 쉽게 알 수 있는 것이다.

# add()의 사용법
fruits = {"apple", "banana", "cherry"}
fruits.add('orange') # 다른 리스트나 튜플의 add처럼 똑같이 추가된다.
print(fruits)

fruits = {"apple", "banana", "cherry"}
fruits.add('apple') # 하지만 셋을 특성상 중복을 허용하지 않고 순서가 없기에 같은 요소를 또 추가할 수는 없다.
print(fruits)

# clear()의 사용법

fruits = {"apple", "banana", "cherry"}
fruits.clear() # 셋 안에 있는 요소들을 전부 클리어하는 메서드 입니다.
print(fruits)

# copy()의 사용법

fruits = {"apple", "banana", "cherry"}
x = fruits.copy() # 여기에서도 원본은 건드리지 않고 사용하기 위해서 copy를 사용한다.
print(x)

# difference()의 사용법
x = {'apple', 'banana','cherry'}
y = {'apple', 'microsoft', 'google'}

z = x.difference(y) # difference()의 경우 다른 점을 리턴해준다. 즉 x안에 있는 요소 중 y에 있다면 그 요소를 제외하고 보여준다.
print(z)

w = y.difference(x)
print(w)

# difference_update() 의 사용법
x = {'apple', 'banana','cherry'}
y = {'apple', 'microsoft', 'google'}

z = x.difference_update(y) # difference_update의 경우 다른점을 원본에서 삭제해버린다.
print(x)

# discard() 의 사용법

fruits = {"apple", "banana", "cherry"}
fruits.discard('apple')

print(fruits) # 특정한 요소를 삭제하여 준다. remove의 경우 요소가 없을때 에러를 발생시키는 경우를 올려 discard를 사용한다.






