#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Employee:
    """所有员工的基类"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name  # self相当于this
        self.salary = salary
        Employee.empCount += 1  # 直接在类名后面.，就是静态变量，empCount

    @staticmethod  # 用注解的形式标明是静态方法
    def displayCount():
        print "Total Employee %d" % Employee.empCount

    def sayHello(self, times=1):
        print ("Hello My name is %s" % self.name) * times


def displayEmployee(self):
    print "Name : ", self.name, ", Salary: ", self.salary


emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
Employee.displayCount()
emp2.displayCount()
print "Total Employee %d " % Employee.empCount # 也可以直接访问
emp1.sayHello(times=2)
emp2.sayHello()


emp1.age = 7  # 添加一个 'age' 属性
print emp1.age, hasattr(emp1, 'age')  #查看是否有age属性
emp1.age = 8  # 修改 'age' 属性
print emp1.age, hasattr(emp1, 'age')
print getattr(emp1, 'age')  # 获取age属性
# del emp1.age  # 删除 'age' 属性
# print emp1.age
hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。

setattr(emp1, 'age', 18) # 添加或设置属性 'age' 值为 18
print getattr(emp1, 'age')    # 返回 'age' 属性的值
delattr(emp1, 'age')    # 删除属性 'age'

print "Employee.__doc__:", Employee.__doc__  # """所有员工的基类"""
print "Employee.__name__:", Employee.__name__  # Employee
print "Employee.__module__:", Employee.__module__  # __main__
print "Employee.__bases__:", Employee.__bases__  # ()
print "Employee.__dict__:", Employee.__dict__  # 相当于序列化对象，形成一个字典的数据


class Parent:  # 定义父类
    parentAttr = 100

    def __init__(self):
        print "调用父类构造函数"

    def parentMethod(self):
        print '调用父类方法'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性 :", Parent.parentAttr


class Child(Parent):  # 定义子类，括号里面代表继承自Parent
    def __init__(self):
        print "调用子类构造方法"

    def childMethod(self):
        print '调用子类方法 child method'


c = Child()  # 实例化子类   # 调用子类构造方法，不会调用父类的构造函数
c.childMethod()  # 调用子类的方法
c.parentMethod()  # 调用父类方法
c.setAttr(200)  # 再次调用父类的方法
c.getAttr()  # 再次调用父类的方法


print issubclass(Child, Parent)
print isinstance(c, Child)
print isinstance(c, Parent)


class JustCounter:
    __secretCount = 0  # 两个下划线开头私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount


counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
print counter.__secretCount  # 报错，实例不能访问私有变量
