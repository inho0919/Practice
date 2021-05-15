line = input()
lists = list()

lists = line.split(' ')

a = lists[0]
b = lists[1]
c = lists[2]

a = int(a)
b = int(b)
c = int(c)

if (a + b <= c) or (b + c <= a) or (a+c <= b):
  print("삼각형아님")
else:
  if(a*a + b*b == c*c) or (a*a + c*c == b*b) or (a*a == b*b + c*c):
    if (a == b) or (a == c) or (b == c):
      if(a == b == c):
        print("정삼각형")
      else:
        print("이등변삼각형")
    else:
      print("직각삼각형")
  else:
    if (a == b) or (a == c) or (b == c):
      if(a == b == c):
        print("정삼각형")
      else:
        print('이등변삼각형')
    else:
      print('삼각형')
