MA = lambda x,y:(x>y)*x+(x<y)*y
MI = lambda x,y:(x>y)*y+(x<y)*x
a =10
b=20
print(MA(a,b))
print(MI(a,b))