# Seperator option
print('P','Y','T','H','O','N',sep='-')

print('J','A','S','O','N', sep='')

print('Jason ',' smart',sep='is')

# end option

print('Welcome',end=' ')
print('world')

# format 숫자를 직접입력하지 않고 변화하는 값에 대한것을 적용 할 수 있어 많이 사용된다. 동적인 데이터를 만들 수 있다.

print("Jason's age is {}, and his girlfriend name is {}".format(28,'Kiki'))
''' .format() 은 다양한 방법으로 문자나 숫자 등을 넣을 수 있다.'''
# %s 는 스트링을 넣는 방법이다.
print('%20s'%('nice',)) # 이런식으로 .format()을 사용하지 말고 %을 사용해서 처리 할 수 있다.
print('%-10s'%('holololo',)) # 이런식으로 %뒤에 숫자를 입력하면 입력한 숫자의 위치에서 문자가 출력된다.

# %d 는 숫자를 넣는 방법이다.
print('%d %d'%(10,20))

# format은 변수명을 줘서 사용도 가능하다.
year = 2022
month = 9
day = 1
print('오늘은 {}년 {}월 {}일 입니다.'.format(year,month,day))

intValue = 123
floatValue = 3.141592
strValue = 'Jason'
boolValue = True
print(intValue, type(intValue))
print(floatValue, type(floatValue))
print(strValue, type(strValue))
print(boolValue, type(boolValue))

print(str(intValue)+strValue) # 다른 형태끼리는 연산자를 사용할 수 없다. 하지만 형식을 앞에 처럼 바꾸면 가능
