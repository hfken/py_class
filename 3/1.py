class Father():
    def __init__(self,name,hobby):
        self.name=name
        self.hobby=hobby
    def like(self):
        print(self.name+self.hobby)
class son(Father):
    def __init__(self,name,hobby,skill):
        super().__init__(name, hobby)
        self.skill=skill
    def like(self):
        print(','.join([self.name,self.hobby,self.skill]))
n=eval(input())
zhangsan=son(n[0],n[1],n[2])
zhangsan.like()
        

