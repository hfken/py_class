import math
class MyMath():
    def __init__(self,r):
        self.r=r
    def c(self):
        return '{:.2f}'.format(2*math.pi*self.r,2)
    def s(self):
        return '{:.2f}'.format(math.pi*self.r*self.r,2)
    def bs(self):
        return '{:.2f}'.format(4*math.pi*self.r*self.r,2)
    def bv(self):
        return '{:.2f}'.format((4/3)*math.pi*self.r**3,2)
r=eval(input())
n=MyMath(r)
print(','.join([n.c(),n.s(),n.bs(),n.bv()]))