# Dictionary 메서드 파악하기 딕션너리에서 사용가능한 메서드는 총 11개
# clear()의 사용법
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear() # 안에 저장되어 있는 친구를 전부 삭제한다.
print(car)

# copy()의 사용법
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.copy() # list에서 사용했던것 처럼 원본 데이터를 훼손하지 않고 복사하여 사용한다.
print(x)

# fromkey()의 사용법
# 는 dictionary 를 쉽게 만들기 위해서 사용하는 메서드이다.

x= ('key1','key2','key3') # 튜플로 해서도 가능하다
y = 0

thisdict = dict.fromkeys(x,y)
print(thisdict)

x1 = ['Ja0', 'Ja1', 'Ja2'] # 리스트도 가능하다.
x2= 1
expDict = dict.fromkeys(x1,x2)
print(expDict)

x = ('key1', 'key2', 'key3')
thisDict = dict.fromkeys(x) # 이렇게 아무것도 적지 않으면 None으로 해서 나오게 된다.
print(thisDict)

# get()의 사용법

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get('model') # get()을 사용해서 specific한 value값을 가지고 오게 된다.
print(x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

y = car.get('price', 15000)
print(y) # 만약에 아이템이 존재하지 않을 경우에도 이렇게 사용하면 된다.

# items()의 사용법
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x) # items()의 경우는 key & Value 두개의 정보가 모두 나오는것이다.

car = {
  'brand':'Ford',
  'model':'Mustang',
  'year':1964
}

x = car.items()
car["year"] = 2008 # x에 변수가 먼저 나왔더라도 업데이트된 새롭게 바뀐 내용으로 나오게 된다.
print(x)

# key()의 사용법

car = {
  'brand':'Benz',
  'model':'AMG',
  'year': 2021
}
x = car.keys() # list의 담긴 상태로 키 값을 리턴한다.
print(x)

car = {
  'Brand':'BMW',
  'Model':'M5',
  'year':'2021'
}

x = car.keys()

car['color'] = 'white' # key의 경우에도 똑같다. 변수에 담기고 난 뒤에 추가 되었어도 업데이트 되어서 나온다.
print(x)


# pop()의 사용법

car = {
  'brand':'Benz',
  'model':'AMG G-Class',
  'year': 2021
}
car.pop('model') # 이 경우에는 pop()으로 사라지게 한 후 car를 프린트하여서 없어진 요소를 확인하는것이다.
print(car)

car = {
  'Brand':'BMW',
  'Model':'M5',
  'year':'2021'
}
x = car.pop('Model') # 이런식으로 변수로 담게 된다면 없어진 요소를 확인하는것이다.
print(x)


# popitem()의 사용법

car = {
  'brand':'Benz',
  'model':'AMG G-Class',
  'year': 2021
}
car.popitem() # popitem()의 경우 마지막에 추가된 요소를 없애주는 메서드이다. 3.7버전이전에는 아무거나 랜덤하게 삭제하였다.
print(car)

car = {
  'brand':'Benz',
  'model':'AMG G-Class',
  'year': 2021
}
x = car.popitem() # popitem() 역시 변수에 담아서 그 변수를 프린트하게 되면 사라진 요소를 직접 확인가능하다.
print(x)


