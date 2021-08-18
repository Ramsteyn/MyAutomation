# InHeriting the Class A to B
from B import childClass
obj=childClass()
obj.childclassMethod()
obj.parentClassMethod()
# Duplicate method in class will always execute in the child class
obj.sum(30,50)

