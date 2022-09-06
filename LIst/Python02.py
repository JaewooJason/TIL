# append()의 사용법

fruits = ['apple', 'banana', 'pear'] # append()는 리스트의 마지막에 추가하는 리스트 메서드이다.
fruits.append('orange')
print(fruits)

a = ['apple', 'banana', 'cherry']
b = ['volvo', 'BMW', 'Benz']
a.append(b) # 이런식으로 리스트에 리스트를 어펜드를 하는것이 가능하지만 리스트안에 리스트가 담기는것이므로 사용에 주의해야한다.
print(a)

# clear()의 사용법

fruits = ['apple', 'orange', 'banana', 'kiwi']
print(fruits.clear()) # 이렇게 클리어를 사용하게 되면 리스트안에 있는 요소들을 전부 삭제 시켜준다.

# copy()의 사용법
fruits = ['apple', 'orange', 'banana', 'kiwi']
a = fruits.copy() # 이렇게 copy를 사용하는것은 원본에 영향을 주지 않고 카피하여 사용하기 위해서 이다.
print(a)

# count()의 사용법

fruits = ['apple', 'orange', 'banana', 'kiwi']
x = fruits.count('apple')
print(x)

point= [1,2,3,3,4,5,4,5,6,6,6,9]
y = point.count(6)
print(y)

# extend()의 사용법

fruits = ['apple', 'orange', 'banana']
car = ['Volvo', 'Hyundai', 'Kia']
print(car)
fruits.extend(car)
print(fruits)

fruit = ['apple','kiwi', 'mandarin']
points = (1,2,3,4)

fruit.extend(points)
print(fruit) # list 와 tuple 을 합칠 수 있다.

# index()의 사용법
fruits = ['apple','banana','orange']
x = fruits.index('banana')
print(x)

fruits = [4, 55, 64, 32, 16, 32]
fruits.index(32) # 첫번째 만나는 수를 리턴해준다.

# insert()의 사용법
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1,'orange') # 원하는곳에 집어 넣어준다.
print(fruits)




