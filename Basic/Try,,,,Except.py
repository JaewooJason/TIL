# 기본적으로 try,,, except 에 대해서 잘 해야지만 프로젝트를 하거난 하는것에서도 좋다

try:
    print(x)
except:
    print('An exception occured')
# 간단하게 사용하는 try구문


try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# 아래에서 파일을 열때에도 사용한다.

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")