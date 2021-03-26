#添加一些注释1
class Person:
    name = "default"
    age = 0
    gender = 'male'
    weight = 0.00
    def __init__(self,name,age,gender,weight):
        self.name=name
        self.age=age
        self.gender=gender
        self.weight=weight
    def fun1(self):
        print(f"我的姓名是：{self.name},性别：{self.gender},年龄：{self.age}岁,体重：{self.weight}KG")

    @classmethod
    def fun2(cls):
        print(f"我的姓名是：{cls.name},性别：{cls.gender},年龄：{cls.age}岁,体重：{cls.weight}KG")

person1 =Person('lq',18,'女',44.5)
person1.fun1()
print(person1.name)
print(Person.name)
Person.name = '1'
person1.name = '2'
print(person1.name)
print(Person.name)
#类方法不能直接访问Person.fun1()会报错,需要给类方法添加一个装饰器@classmethod，才可以直接用类名访问类方法而与具体的实例无关
Person.fun2()