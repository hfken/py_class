'''
字典
dict1={'name':x,'age':'number'}
键必须为数字，字符串或元组等不可变对象，且互不相同，值可以是任何类型的元素
'''
#字典的相关函数
#len()可以求所有可迭代对象的长度
dict1={'name':'may','age':'13'}
print(len(dict1))

#.keys()    以列表返回字典的键 是迭代器
#.values()   以列表返回字典的值 是迭代器
#.items()   返回键值的二元组 是迭代器
dict1.keys()
dict1.values()
dict1.items()

#对于添加和修改，有则修改，无则添加
dict1['name']='Jack'

#排序
print(sorted(dict1.items(),reverse=True))

#快速更新表中元素
ainfo={'name':'peter','age':18}
binfo={'name':'Jack','age':20,'gender':'male'}
ainfo.update(binfo)# ainfo={}
print(ainfo)
