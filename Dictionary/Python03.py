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

