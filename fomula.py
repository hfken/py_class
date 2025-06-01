#运算符的使用
#'//'向下取整 7//2=3 -7//2=-4
#'%'取余，结果符号与除数相同 5%2=1 5%-2=-1 -5%2=1

#逻辑运算符
#短路返回左操作数，不短路返回右操作数
from decimal import * 
a=(1,2,3)
b=a
b is a  #True

#表达式总体上为从左到右算
#算数运算>关系运算>逻辑运算

#保留小数=
number=3.1456
round(number,2) # round(value,需要保留的位数)，返回的是一个浮点数

#用decimal函数更加精确的四舍五入
from decimal import Decimal, ROUND_HALF_UP
number = Decimal('32.125')
rounded_number = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
print(rounded_number)  # 输出 32.13

print('{:.2f}'.format(number))# fotmat函数返回的是一个字符串

#运算符的左右结合性
#右结合性 举例：**,赋值运算符：+= 三元条件运算符
3**2**3 #3**(2**3)

#格式化
print('%.4d'%57.65) #前面填充四个空格,d代表整数 57
print('%.2f'%Decimal(32.125))
print('{:.2f}'.format(Decimal(32.125)*100))
print(round(Decimal(32.125),2))

#import
import math #需要用.来调用
from math import * #不需要.调用直接用函数名
print(abs(-1123))

#cmath函数可以返回 复数解,可以开负数根
import cmath
z=-4
print(cmath.sqrt(z))

#map()函数,将指定函数作用于给定可迭代对象的每个元素,并返回map对象,用于批量处理数据
'''
	•	列表(List)
	•	元组(Tuple)
	•	字符串(String)
	•	字典(Dictionary)
	•	集合(Set)
	•	文件对象(File)
	•	range() 对象
	•	生成器(Generator)
	•	enumerate() 的返回值
	•	zip() 的返回值
'''
b=[1,2,3,4,5,6]
print(list(map(lambda x:x+1,b)))

#filter()函数
#过滤可迭对象中不符合条件的元素
#filter(function,iteration) function的返回值为bool
a=[1,2,3,4,5,6]
a=list(filter(lambda i:i>5,a))
print(a)
