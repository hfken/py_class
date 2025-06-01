'''
字符串
'''
#用\0表示字符串结束

#'sep'.join([string1],[string2]) 将字符串连接
print(','.join(['string','hello']))
#join也能连接迭代器中的字符元素
x=[1,2,3,4]
x=list(map(str,x))#将每个元素转成字符
print(','.join(x))#1,2,3,4  可以用于输出要求结尾不带 , 的题目


#string.split('sep',maxsplit) 将字符串分割
#string.rsplit('sep',maxsplit) 从右侧开始分割
a='hello,my name is XXX,Today'
b=a.split(',',1)#返回一个列表
print(b) #返回一个列表
b=a.rsplit(',',1)#从右侧开始分割
print(b[0])
print(a.split(',',1))

#字符串成员判断 string in string
print('he' in a) #True

#字符与数字的转换
print(ord('a')) #97
print(chr(65)) #A

#居中函数
print('hell'.center(13,'0')) #0000hello00000 左少右多
print('{:0^14}'.format('hello'))
#计算字符串长度 len()
x=len(a)
print(x)

#字符串计数
x=a.count('h')
print(x)

#全部转成大写
x=a.upper()
print(x)

#替换制定字符
x=x.replace('H','h')
print(x)
x=x.replace('n','N') #不会报错
print(x)

#字符串切片
ans='abcdefghijk'
print(ans[-1:-4:-1]) #kji