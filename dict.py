'''
字典
dict1={'name':x,'age':'number'}
键必须为数字，字符串或元组等不可变对象，且互不相同，值可以是任何类型的元素
'''
d={(1,2):1}#合法
#字典的相关函数
#len()可以求所有可迭代对象的长度
dict1={'name':'may','age':'13'}
print(len(dict1)) #2

#.keys()    以列表返回字典的键 是迭代器
#.values()   以列表返回字典的值 是迭代器
#.items()   返回键值的二元元组 是迭代器
dict1.keys()
dict1.values()
dict1.items()

#对于添加和修改，有则修改，无则添加
dict1['name']='Jack'

#排序
print(sorted(dict1.items(),reverse=True))#先按照key排，再按照value排

#快速更新表中元素
ainfo={'name':'peter','age':18}
binfo={'name':'Jack','age':20,'gender':'male'}
ainfo.update(binfo)# ainfo={}
print(ainfo)

#字典的排序
dict2={'a':1,'b':3,'c':5,'d':0}
print(sorted(dict2.items(),key=lambda x:x[1]))
