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

print(fruits) # 특정한 요소를 삭제하여 준다. remove의 경우 요소가 없을때 에러를 발생시키는 경우를 높혀 discard를 사용한다.

# intertsection()의 사용법

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y) # difference()의 반대이다. 두개이상의 셋에서 같은것이 있으면 리턴시켜준다.
print(z)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
w = x.intersection(y,z) # 이러한 경우 3개를 모두 비교하여 같은 요소를 리턴해준다.
print(w)

# intersection_update()의 사용법
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y) # intersection_update()의 경우 두개의 셋에 모두 포함되어 있는
# 요소만 남기고 삭제 시켜준다.
print(x)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y,z)# 3개 이상의 셋일때도 똑같다.
print(x)

# isdisjoint()의 사용법

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z= x.isdisjoint(y) # x 셋 안에 y 셋의 요소가 없을 경우 True로 리턴한다.

print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

w = x.isdisjoint(y)
print(w)

# issubset()의 사용법
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y) # 만약 x의 요소가 모두 y에 있다면 True를 리턴해주는 메서드이다.
print(z)

x = {"a", "b", "c"}
y = {"f", "e", "d", "b", "a"}
w = x.issubset(y)
# 만약 포함되어 있지 않는 것이 있을때에는 False를 리턴해준다.
print(w)

# issuperset()의 사용법
x = {"f", "e", "d", "c", "b", "a"}
y = {"a",'b','c'}
z = x.issuperset(y)
# issuperset의 경우 issubset이랑 개념이 반대라고 생각하면 된다. y에 있는 요소들이 x에 있을경우 True로 리턴하는 메서드이다.
print(z)

x = {"f", "e", "d", "c", "a"}
y = {"a",'b','c'}
w = x.issuperset(y)
# 만약에 하나라도 빠진다면 False를 리턴한다.
print(w)

# pop()의 사용법
fruits = {"apple", "banana", "cherry"}
fruits.pop()
# 셋안에 랜덤의 요소를 삭제해주는 메서드이다.
print(fruits)

fruits = {"apple", "banana", "cherry"}
x = fruits.pop()
# 변수에 담게 되면 사라진 요소를 보여준다.
print(fruits)
print(x)

# remove()의 사용법
fruits = {"apple", "banana", "cherry"}
fruits.remove('apple')
print(fruits)
# 특정한 요소를 지정해서 삭제 시켜주는 메서드이다. 대신 요소가 완전히 삭제됨으로 discard 에러발생할 확률이 높다.

# symmetric_difference()의 사용법
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
# 이 메서드의 경우 두개의 셋을 비교하고 같은걸은 비교하고 두개의 셋에 포함되어 있는 요소만 제거하고 나머지요소를 합친다.
print(z)

# symmetric_difference_update()의 사용법
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
# 이 메서드의 경우 위에서 본 것과 달리 원본에 영향을 준다고 생각하면 된다. 그러므로 사용할때 주의해야함
# 이메서드는 셋들을 비교하고 다른 부분을 찾을때 사용하면 된다.
print(x)


# union()의 사용법

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
# 공통으로 들어가 있는 부분은 셋의 특성상 하나만 들어가기 때문에 하나로 줄이고 나머지는 한곳에 전부 모인다.
print(z)

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
w = x.union(y,z)
# 유니크한 값을 찾을때 사용하면 된다.
print(w)

# update()의 사용법

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y) # 중복된 값을 제외하고 나머지를 전부 한곳에 담아준다.
print(x)





