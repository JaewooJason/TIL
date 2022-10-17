# 클래스 사용하는 방법에 대한 것들

class myClass:
    x = 5
p1 = myClass
print(p1.x)

class person:
    def __init__(self, age, name):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})" # __str__ 사용한 경우 와 없는 경우 비교


p1 = person(36,"John")

print(p1.name)
print(p1.age)
print(p1)
