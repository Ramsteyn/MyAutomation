from B import childClass
from A import parentClass
class Multi(childClass,parentClass):
    def mul(self,a,b):
        print(a*b)
        print("This is a Class D method")
