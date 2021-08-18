class A():
    def __init__(self):
        print("This is constructor")
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

def sum(a,b):
    c=a+b
    return c