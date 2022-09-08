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

# pop()의 사용법
fruits = ['apple', 'banana','cherry']
fruits.pop(1) # pop의 경우 ()의 저장된 숫자 자리를 사라지게 하는 메서드이다.
print(fruits)

fruits =['banana', 'cherry', 'orange']
x = fruits.pop(2) # 변수에 담아서 프린트하게 되면 그 자리에서 pop으로 사라진 친구가 보이게 된다.
print(x)

# remove()의 사용법
fruits = ['apple', 'banana', 'cherry']
fruits.remove('banana') # pop의 경우 포지션을 적었다면, remove의 경우 직접적인 리스트 안에 있는것을 적어서 삭제하는것이다.
print(fruits)

# reverse()의 사용법
fruits = ['apple', 'banana', 'cherry']
fruits.reverse() # 변수에 담아서 사용하지 말고 메서드를 적용시키고 알아서 적용이 된다. 그 후 print()로 확인하면 리스트 안에 원소가 반대로 되어 있다.
print(fruits)

# sort()의 사용법

cars = ['Ford', 'BMW', 'Volvo']
cars.sort() # ABCD 순서대로 자동으로 정렬해준다.
print(cars)

cars = ['Ford', 'BMW', 'Volvo', 'Benz']
cars.sort(reverse=True) # 이렇게 하면 reverse = True로 하게되면 반대로 정렬하여 나오게 된다.
print(cars)

def myFunc(e):
    return len(e)
cars = ['Ford', 'BMW', 'Volvo', 'Benz','VW']
cars.sort(key=myFunc) # Key를 사용하여 정렬하게 하는법 따로 함수를 정의하여서 사용하였다.
print(cars)

def myYear(e):
    return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=myYear) # 키를 사용해서 다양하게 정렬을 할 수 있겠다.
print(cars)

def myfunc(e):
    return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myfunc) # 두가지를 모두 사용하여서 정렬도 가능하다.
print(cars)







