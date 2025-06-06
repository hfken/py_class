id=input()
if len(id)!=18:
      print('这是一个错误的身份证号码')
      quit()
idn=list(map(int,id[:17]))
if id[-1]=='X':
  idn.append(10)
else:
  idn.append(int(id[-1]))
list1=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
listx=[i*j for i,j in zip(idn,list1)]
x=(12-sum(listx)%11)%11
if x==int(idn[-1]):
  print('这是一个正确的身份证号码')
else:
  print('这是一个错误的身份证号码')