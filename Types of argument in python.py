# Required argument
def sum(a,n):
    c=a+n
    print(c)
sum(10,20)

# Keyword arguments
def dif(a,b):
    c=a+b
    print(a)
    print(b)
    print(c)
dif(b=200,a=100)

# Default arguments

def t(a,b=10,d=50):
    c=a+b+d
    print(c)
t(500,20,30)

