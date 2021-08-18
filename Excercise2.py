n1=input("Enter the number 1")
n2=input("Enter the number 2")
n3=input("Enter the number 3")

n1=int(n1)
n2=int(n2)
n3=int(n3)

if(n1<n2 and n3<n2):
    print ("The number is Greater of all " +str(n2))
elif(n2<n1 and n3<n1):
    print ("The number is Greater of all " +str(n1))
elif(n2==n1 or n2==n3):
    print("Numbers are equal")
else:
    print ("The number is Greater of all " +str(n3))

if(n1>n2 and n3>n2):
    print ("The number is Smaller of all " +str(n2))
elif(n2>n1 and n3>n1):
    print ("The number is smaller of all " +str(n1))
elif(n2==n1 or n2==n3):
    print("Numbers are equal")
else:
    print ("The number is smaller of all " +str(n3))
