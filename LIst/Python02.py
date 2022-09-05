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

