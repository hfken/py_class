class Temperature:
    def __init__(self,c,f):
        self.c=c
        self.f=f
    def tof(self):
        return "{:.2f}".format(self.c*1.8+32)
    def toc(self):
        return '{:.2f}'.format((self.f-32)/1.8)
n=eval(input())
to=Temperature(n[0],n[1])
print(f'摄氏{n[0]:.2f}度->华氏{to.tof()}度,华氏{n[1]:.2f}度->摄氏{to.toc()}度')