# 백준을 사용하면서 가장 많이 사용한 것이 input이다. 입력받는 것에 따라 변수가 계속 달라지게 된다.
username = input('please enter your name')
print('Username is ' + username)

age = int(input()) # 이렇게 다양하게 사용할 수 있다.


# formating 보통 모맷팅은 변수나 받아온 값을 자동으로 입력시켜주기 위해서 사용한다. 굳이 사용자 직접입력할 필요가 없음

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

txt = "The price is {:.2f} dollars"

# 이런식으로 하나만이 아님 다양하게 만들 수 있음
price = 1000
itemno = int(input())
count = int(input())

print(txt.format(price, itemno, count))



quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))