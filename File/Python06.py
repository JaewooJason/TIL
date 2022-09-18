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








