#函数改变参数值的说明
#如果参数是可变对象（列表，字典） 在函数中引用修改原对象时，原参数值会被改变 如list.append()
#如果是不可变对象（整数，字符串）在函数中引用修改原对象时，原参数值不会被改变
a=[1,2,3,4,5]
b=5
def test(b,a):
      a.append(6)
      b=6
test(b,a)
print(a,b)

#可变长度参数:元组,字典
def example(arg1, *args, kwarg1=None, **kwargs):#*后表示元组，**后表示字典
    print(f"arg1: {arg1}")
    print(f"args: {args}")
    print(f"kwarg1: {kwarg1}")
    print(f"kwargs: {kwargs}")

example(1, 2, 3, 4, kwarg1="test", a=5, b=6)

#关键字参数
def void(a,b,c=6):
	pass
#void(b=3,2,5) #会报错,先位置参数,再关键字参数,再默认参数

#lambda函数
#能够在一行内写的简单函数,简化使用功能
a=[1,2,4,6,5,3]
print(sorted(a,key=lambda a:a<4,reverse=True))

iterable=[1,2,3,4]
# sum()函数
sum(iterable,start =0)
'''
	•	iterable:一个可迭代对象(如列表、元组、字符串等),其中包含要求和的元素。
	•	start(可选):一个初始值,默认是 0,这个值会加到最终的求和结果中。如果传入了一个 start 值,那么求和时会从这个值开始。
'''

#random库
from random import *
seed()
random() #[0.0,1.0)
randint(1,5) #int[a,b]
randrange(1,6,2)#randrange(start,end,step) int
uniform(1,67) #[a,b] float




