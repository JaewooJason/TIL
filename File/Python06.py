# 제일 기본적으로 알아야 하는 것들이다. 파일을 열고 닫지 못한다면 어떤 파일을 불러들여서 사용하고 할 수 있겠나

# close()의 사용법

f = open("demofile.txt", "r")
print(f.read()) # close()는 열려있는 파일을 닫아준다.
f.close()

# fileno()의 사용법

f = open('demofile.txt', 'r')
print(f.fileno()) # 파일의 넘버를 리턴해준다.

# flush()의 사용법
f.open('mywife.txt', 'a')
f.write("Now the file has one more line")
f.flush()
f.write("... and another one!")

# issatty()의 사용법
f.open('demofile.txt','r')
print(f.isatty()) # 만약 파일 터미널과 연결되어 있다면 True로 리턴해준다. 아니라면 False

# read() 의 사용법
f.open('demofile.txt', 'r')
print(f.read())

# 만약에 숫자를 ()안에 넣으면 넣은 숫자만큼의 바이트로 리턴해준다. -1은 원본사이즈로 리턴 디폴트 값이다.

f.open('demofile.txt','r')
print(f.read(33))

# readable()의 사용법
f.open('demofile.txt','r')
print(f.readable()) # file을 읽을 수 있는지 없는지 True or False로 나타내준다.

# readline()의 사용법
f.open('demofile.txt','r')
print(f.readline()) # 파일에서 한줄씩 읽어오는 메서드이다.

f.open('demofile.txt', 'r')
print(f.readline())
print(f.readline()) # 이렇게 하면 첫 번째 줄이 들어오고 다음으로 두 번째 줄이 들어온다.

f.open('demofile.txt', 'r')
print(f.readline(5)) # 첫 번째 줄에서 5바이트까지의 데이터를 가져온다.

# readlines()의 사용법
f.open('demofile.txt','r')
print(f.readlines())

f.open('demofile.txt','r')
print(f.readlines(33)) # 33byte 보다 높은 친구를 리턴한다.

# seek()의 사용법
f.open('demofile.txt', 'r')
f.seek(4)
print(f.readline()) # file의 포지션을 바꿔주는 메서드

# seekable()의 사용법
f = open('demofile.txt','r')
print(f.seekable()) # seek을 사용 할 수 있는지 없는지를 True or False로 알려줌

# tell()의 사용법
f = open('demofile.txt','r')
print(f.tell()) # 현재의 위치를 알려준다

f = open('demofile.txt','r')
print(f.readline())
print(f.tell()) # 위에 줄을 읽고 난 뒤에 다음부터 리턴해준다.

# truncate()의 사용법

f = open('demofile.txt', 'a') # 'a'의 의미는 appending
f.truncate(20) # 여기서 지정한 바이트의 크기만큼만 리턴해준다.
# 리턴된 결과값: 123456789101234567890
f.close()
# 위에서 열고 truncate 쓰고 close 닫은것
f = open('demofile.txt','r')
print(f.read())

# writable()의 사용법
f = open('demofile.txt', ' r')
print(f.writable()) # 파일에 글을 쓸 수 있는지에 대한 확인 여부를 판단해주는 메서드

# write()의 사용법
f = open('demofile.txt', 'a')
f.write('Thank you so much. See you soon')
f.close()
#  이런식으로 문자를 파일안에 입력할 수 있다.
f = open('demofile.txt', 'r')
print(f.read())

# /n 을 사용 할 수 있다.
f = open('demofile.txt', 'a')
f.write('/nSee you soonnnnn')
f.close()

f = open('demofile.txt','r')
print(f.read())

# writelines()의 사용법
f = open('demofile.txt', 'a')
f.writelines(['See you soon', 'Thank you so muchhhh'])
f.close()
# list 형식으로도 파일안에 문자를 넣을 수 있다.
f = open('demofile','r')
print(f.read)

# /n is also possible

f = open('demofile.txt','a')
f.writelines(['/nSeee you soon', '/Thank you so muchhh'])
f.close()

f = open('demofile.txt','r')
print(f.read())











