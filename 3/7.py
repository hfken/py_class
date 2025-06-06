id=input()
if len(id)!=18:
    print('这是一个错误的身份证号码')
    quit()
idn=list(map(int,id))
list1=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
listx=[i*j for i,j in zip(idn,list1)]
x=(12-sum(listx)%11)%11
if x==int(id[-1]) or (x==10 and id[-1]=='X'):
    print('这是一个正确的身份证号码')
else:
    print('这是一个错误的身份证号码')
