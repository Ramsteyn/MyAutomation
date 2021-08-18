from A import parent
from B import child
from ThirdLevel import T



class C(child,parent,T):
    def div(self,a,b):
        print(a/b)