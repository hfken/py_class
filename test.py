import copy
a=[1,23,5,10,[10,4]]
b=copy.copy(a)
print(id(a[4]),id(b[4]))#相同
b[4].append(5)
b.append(12)
print(a)
print(b)