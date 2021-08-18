class A():
    # Function with no arguments and return values
    def f(self):
        print("Hello world")
    # Function with arguments and no return values
    def sum(self,a,b):
        c=a+b
        print(c)
    # Function with both arguments and return value
    def product(self,a,b):
        c=a*b
        return c
obj=A()
obj.f()
obj.sum(10,30)
x=obj.product(10,30)
print(x)