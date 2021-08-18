# Parent Class
class parent:
    def __init__(self):
        print("This is parent Class constructor")
    def sum(self,a,b):
        print(a+b)
obj=parent()
x=obj.sum(20,30)
