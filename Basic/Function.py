# 파이썬에 Function에 대한 이해
# function 은 block of code라고 이해하면 쉽다. 하나의 덩어리에 많은 것들을 할 수 있도록 나만의 함수를 만드는 것이라 생각하자.
# function을 만들때에는 def를 사용해서 만들게 된다.

def myFunc():
    print('Hello, it is my first function')

myFunc() # 이런식으로 호출하게 되면 자연스럽게 내가 정의한 function이 나오게 된다. 각자의 회사에는 회사만의 function을 만들어 사용한다.

def myFunction(fname):
    print(fname + ' Refsnes')

myFunction('Emil')
myFunction('Tobias')
myFunction('Linus')
# 위에서 사용한것처럼 함수안에 정의 한것을 저런식으로 활용을 해도 되는것이다.

def familyName(fname,lname):
    print(fname + ' ' + lname)
familyName('Emil', 'Refsnes') # 주의 해야하점은 만약 두개를 인력해야하면 두개를 꼭 넣어줘야한다. 넣지 않으면 에러이다.

# 만약에 내가 몇개를 넣어야할지를 모를때는 밑에 있는 예시를 보면된다.
def myFunc(*kids):
    print('The youngest child is '+ kids[2])
myFunc('Emil', 'Tobias','Linus') # 이러한 방식으로 해도 된다.

def myFunc(child3, child2, child1):
    print("The youngest child is " + child3)
myFunc(child1= 'Emil', child2='Tobias', child3='Linus') # 이런식으로 키 밸류 방식으로 만들어 된다.

def myFunc(**kid):
    print('His last name is ' + kid['lname'])
myFunc(fname = 'Tobias', lname='Refsnes')
# 위의 방식은 키워드가 몇개가 들어갈지 모를때 사용하면 된다.






