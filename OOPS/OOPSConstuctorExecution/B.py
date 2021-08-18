# Second Parent Class
from A import parent

class child(parent):
    def __init__(self):
        print("This is another child class constructor")

    def sub(self,a,b):
        print(a-b)