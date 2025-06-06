class Dog():
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def out(self):
        print(self.name,self.color)
n=eval(input())
dog=Dog(n[0],n[1])
dog.out()
