'''
由逗号分隔的元素，同时没有重复的元素
集合用{}表示
'''

a=(1,1,2,3)
s3=set('ababd')
s1=set(a)
print(s1,s3,sep='\n')  #结果无序{'b','a','d'}/{'a','b','d'}
list1=list(s3) #转换为列表

print(list1)
s2={1,2,3}
print(type(s2)) #<class 'set'>

x=frozenset() #不可变集合，元素不可改变，更改

'''相关函数和方法'''
#add()
s1.add('春')
print(s1)

#discard() 删除指定元素
s1.discard(2)
print(s1)

#copy() 复制一份集合 浅拷贝
s3=s1.copy()
s3.discard(1)
print(s1)

#deepcopy() 深拷贝
import copy
s2=copy.deepcopy(s1)
s1.discard(1)
print(s1)
print(s2)

#集合的特殊去除  可记为  A=A-B
# difference_update()函数
s5={1,2,3}
s6={2,3,5}
s5.difference_update(s6)#保留在s5但不在s6中的元素，直接修改原集合
s5={1,2,3}
s6={2,3,5}
s7=s5.difference(s6)#保留在s5但不在s6中的元素，但返回一个新的集合



#clear() 清空
s1.clear()
