class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")

# 继承 Animal 类
class Cat(Animal):
    def __init__(self, name, species="Cat"):
        super().__init__(species)  # 调用父类的构造函数
        self.name = name

    def make_sound(self):
        print(f"{self.name} says Meow!")

my_cat = Cat("Whiskers")
my_cat.make_sound()  # Whiskers says Meow!

#类的输入与传参
class test():
    def __init__(self):
        self.x=int(input())
    def show(self):
        print(self.x)
a=test()
a.show()