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
print('%20s'%('nice',))
print('%-10s'%('holololo',)) # 이런식으로 %뒤에 숫자를 입력하면 입력한 숫자의 위치에서 문자가 출력된다.

# %d 는 숫자를 넣는 방법이다.
print('%d %d'%(10,20))

