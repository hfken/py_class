'''
列表
各个元素其中可为任意类型
'''
#类型转换
list1=list('abc') #转换为['a','b','c']

#列表删除指定索引值元素
list1.pop(1)
#如果参数为空，则会把最后一个元素移除，并返回它

list1.append(5)
print(list1)

#在列表尾部增添一个可迭代对象
list1.extend([1,2,3])

#排序
list2=[1,2,3,5,4,6]
print(sorted(list2,reverse=True))

#插入元素
index=5
value=10
list1.insert(index,value)
#如果index超出列表范围则插入到末尾

#翻转
print(list(reversed(list2))) #reversed函数返回的是地址 要用list转换
x=list2
x.reverse() #.reverse是一种操作方式，直接修改x的顺序
print(x)

list2=list2[::-1] #或者用这种方法

#用解析法创建列表
list2=[i for i in range(1,6) if i%5==0]
print(list2)



#列表删除指定的值或元素
list1.remove('a') #若删除的元素不存在,则会报错

#列表增添一个值到列表尾部