#random库函数
from random import *

#种子，只要种子不变，每次运行相同位置函数生成的随机数不变；默认为当前系统时间
seed(10)
print(random()) #随机小数[0,1)
print(random())

#随机整数 [a,b]
#randint(a,b)
x=randint(1,4)

#随机整数带步长 [a,b) 间隔 c
#randrange(a,b,c)
y=randrange(1,10,2)

#随机小数[a,b]
#uniform(a,b)
z=uniform(1,10)

#随机选取可迭代数据中的元素
#choice(seq)
a=[1,2,3,4,5]
b=choice(a)
print(b)

#随机打乱list中的顺序，随机排列
#shuffle(list),没有返回值，直接对列表进行操作
shuffle(a)
print(a)

#随机选取k个元素，返回这k个元素构成的列表
#sample(seq,k) 若k>seq的长度，则会报错
k=sample(a,3)
print(k)