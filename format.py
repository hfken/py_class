'''
format函数的用法
'''
#保留小数位
a=1.455
b='hello'
print('{:.2f}'.format(a))
print('{:2.2f}'.format(a)) #2:最小字符串长度为两个字符
print('{:x^10s}'.format('hello'))
print('{:.1e}'.format(3120000))
print('{}'.format('hello'.upper()))
print('{:x<10s}'.format('hello'))

#插入字符串的值
print('{1} and {0}'.format(a,b))

#format
a='{:d^12s}'.format('fuclo')
print(a)
print(format(8,'x<4d')) #左填充 8xxx
print(format('hello','x^10s')) #居中字符串 若剩下的空格为奇数,则左少右多 str.center(5,'x')左少右多
print(format(100000,',')) #100,000 
print(format(0.45,'.2%')) #45.00%
print(format(60000000,'.3E')) #6.000e+07 科学计数法
#转换进制
print('{0:d} {0:b} {0:o} {0:0x}'.format(10))


#fstring
print(f'my name is {0.123:.2f}')
print(f"{'hello'.upper()}")


